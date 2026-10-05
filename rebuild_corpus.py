#!/usr/bin/env python3
"""
rebuild_corpus.py — Full rebuild of the msi-corpus public repo indexes.

Usage:
    python3 rebuild_corpus.py [--articles-dir PATH] [--columns-dir PATH] [--output-dir PATH]

Defaults:
    --articles-dir  /Users/oracle/sites/mainstreetindependent/src/content/articles
    --columns-dir   /Users/oracle/sites/mainstreetindependent/src/content/columns
    --output-dir    /Users/oracle/repos/msi-corpus  (this repo root)

On completion, updates manifest.json with live row counts and generation timestamp.
"""

import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("WARNING: PyYAML not installed. Falling back to simple frontmatter extraction.", file=sys.stderr)

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ARTICLES_DIR = Path("/Users/oracle/sites/mainstreetindependent/src/content/articles")
COLUMNS_DIR  = Path("/Users/oracle/sites/mainstreetindependent/src/content/columns")
OUTPUT_DIR   = Path("/Users/oracle/repos/msi-corpus")

BASE_URL = "https://mainstreetindependent.com"

HEDGE_VOCAB = {"confirmed", "attributed", "alleged", "reported", "appears", "contested"}
CORROBORATION_VOCAB = {
    "single_source", "two_independent", "primary_document",
    "primary_plus_secondary", "one_originating_plus_primary_document",
}
OUTLET_CLASS_VOCAB = {
    "wire", "national_daily", "nonprofit", "regional", "trade", "primary_document",
    "government_release", "court_filing", "peer_reviewed", "press_release",
    "social_media", "other",
}

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def split_frontmatter(content: str):
    """Split markdown file into (frontmatter_str, body_str). Returns (None, content) on failure."""
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    fm_str = content[3:end].strip()
    body = content[end + 4:].lstrip("\n")
    return fm_str, body


def parse_frontmatter(fm_str: str) -> dict:
    """Parse YAML frontmatter. Falls back to minimal parsing if PyYAML not available."""
    if HAS_YAML:
        try:
            result = yaml.safe_load(fm_str)
            return result if isinstance(result, dict) else {}
        except yaml.YAMLError as e:
            print(f"  YAML parse error: {e}", file=sys.stderr)
            return {}
    # Minimal fallback: extract simple key: value lines
    result = {}
    for line in fm_str.splitlines():
        m = re.match(r'^(\w[\w_]*)\s*:\s*(.+)$', line)
        if m:
            result[m.group(1)] = m.group(2).strip().strip("'\"")
    return result

# ---------------------------------------------------------------------------
# Body section parsing — Part 4 grammar
# ---------------------------------------------------------------------------

CLAIM_HEADER_RE = re.compile(
    r'^### (c_\d{3,4})\s+[—\-]+\s+(\w+),\s+(.+)$'
)
SOURCE_HEADER_RE = re.compile(
    r'^### (src_\d{3,4})\s+[—\-]+\s+(.+?),\s+(\w+),\s+Tier\s+(\d),\s+(\w+)$'
)
BOLD_FIELD_RE = re.compile(r'^\*\*([^*]+)\*\*:\s*(.*)$')


def parse_claims_section(body: str) -> list:
    """Parse ## Atomic claims section. Returns list of claim dicts."""
    claims = []
    # Find the section
    m = re.search(r'^## Atomic claims\s*$', body, re.MULTILINE)
    if not m:
        return claims
    section_start = m.end()
    # Find the next H2 or end
    next_h2 = re.search(r'^## ', body[section_start:], re.MULTILINE)
    if next_h2:
        section = body[section_start: section_start + next_h2.start()]
    else:
        section = body[section_start:]

    # Split by H3 headers
    parts = re.split(r'^(### .+)$', section, flags=re.MULTILINE)
    i = 1
    while i < len(parts) - 1:
        header_line = parts[i].strip()
        block = parts[i + 1] if i + 1 < len(parts) else ""
        i += 2

        hm = CLAIM_HEADER_RE.match(header_line)
        if not hm:
            continue
        claim_id = hm.group(1)
        hedge_raw = hm.group(2).strip().lower()
        corroboration_raw = hm.group(3).strip().lower().replace(" ", "_")

        # Normalize
        hedge = hedge_raw if hedge_raw in HEDGE_VOCAB else "reported"
        corroboration_level = corroboration_raw if corroboration_raw in CORROBORATION_VOCAB else "single_source"

        # Parse bold key-value fields
        fields = {}
        claim_text = ""
        lines = block.splitlines()
        for line in lines:
            bm = BOLD_FIELD_RE.match(line.strip())
            if bm:
                key = bm.group(1).strip().lower().replace(" ", "_")
                fields[key] = bm.group(2).strip()
            elif line.startswith("> "):
                claim_text += line[2:] + " "
            elif line.startswith(">"):
                claim_text += line[1:] + " "

        claim_text = claim_text.strip()
        subject_entities = [s.strip() for s in fields.get("subject_entities", "").split(";") if s.strip()]
        source_ids_raw = fields.get("source_ids", "")
        source_ids = [s.strip() for s in source_ids_raw.split(",") if s.strip()]

        # Parse object field: "value (type)" → {"value": ..., "type": ...}
        obj_raw = fields.get("object", "")
        obj_type_m = re.match(r'^(.+?)\s+\((\w+)\)\s*$', obj_raw)
        if obj_type_m:
            obj = {"value": obj_type_m.group(1).strip(), "type": obj_type_m.group(2).strip()}
        else:
            obj = {"value": obj_raw, "type": "fact"}

        claims.append({
            "claim_id": claim_id,
            "hedge": hedge,
            "corroboration_level": corroboration_level,
            "subject_entities": subject_entities,
            "predicate": fields.get("predicate", ""),
            "object": obj,
            "temporal": fields.get("temporal", ""),
            "source_ids": source_ids,
            "text": claim_text,
        })

    return claims


def parse_sources_section(body: str) -> list:
    """Parse ## Sources section. Returns list of source dicts."""
    sources = []
    m = re.search(r'^## Sources\s*$', body, re.MULTILINE)
    if not m:
        return sources
    section_start = m.end()
    next_h2 = re.search(r'^## ', body[section_start:], re.MULTILINE)
    if next_h2:
        section = body[section_start: section_start + next_h2.start()]
    else:
        section = body[section_start:]

    # Find the --- disclosure separator if present and trim
    hr = re.search(r'^---\s*$', section, re.MULTILINE)
    if hr:
        section = section[:hr.start()]

    parts = re.split(r'^(### .+)$', section, flags=re.MULTILINE)
    i = 1
    while i < len(parts) - 1:
        header_line = parts[i].strip()
        block = parts[i + 1] if i + 1 < len(parts) else ""
        i += 2

        hm = SOURCE_HEADER_RE.match(header_line)
        if not hm:
            # Try a relaxed parse
            hm2 = re.match(r'^### (src_\d{3,4})\s*[—\-]+\s*(.+)$', header_line)
            if not hm2:
                continue
            source_id = hm2.group(1)
            rest = hm2.group(2)
            outlet = rest.strip()
            outlet_class = "other"
            reliability_tier = 5
            originating_or_republishing = "originating"
        else:
            source_id = hm.group(1)
            outlet = hm.group(2).strip()
            outlet_class_raw = hm.group(3).strip().lower()
            outlet_class = outlet_class_raw if outlet_class_raw in OUTLET_CLASS_VOCAB else "other"
            reliability_tier = int(hm.group(4))
            originating_or_republishing = hm.group(5).strip().lower()

        fields = {}
        for line in block.splitlines():
            bm = BOLD_FIELD_RE.match(line.strip())
            if bm:
                key = bm.group(1).strip().lower().replace(" ", "_")
                fields[key] = bm.group(2).strip()

        sources.append({
            "source_id": source_id,
            "outlet": outlet,
            "outlet_class": outlet_class,
            "reliability_tier": reliability_tier,
            "originating_or_republishing": originating_or_republishing,
            "author": fields.get("author", None) or None,
            "publication_date": fields.get("publication_date", None) or None,
            "access_date": fields.get("access_date", None) or None,
            "title": fields.get("title", None) or None,
            "url": fields.get("url", None) or None,
        })

    return sources

# ---------------------------------------------------------------------------
# Aggregate computation (mirrors Part 6 of the spec)
# ---------------------------------------------------------------------------

def compute_claim_aggregate(claims: list) -> dict:
    hedges = {h: 0 for h in sorted(HEDGE_VOCAB)}
    corroborations = {c: 0 for c in sorted(CORROBORATION_VOCAB)}
    for c in claims:
        h = c.get("hedge", "reported")
        if h in hedges:
            hedges[h] += 1
        cl = c.get("corroboration_level", "single_source")
        if cl in corroborations:
            corroborations[cl] += 1
    return {"count": len(claims), "hedges": hedges, "corroboration": corroborations}


def compute_source_aggregate(sources: list) -> dict:
    if not sources:
        return {
            "count": 0, "outlets": [], "outlet_classes": [],
            "highest_reliability_tier": None,
            "has_originating": False, "has_primary_document": False,
        }
    outlets = sorted({s["outlet"] for s in sources if s.get("outlet")})
    outlet_classes = sorted({s["outlet_class"] for s in sources if s.get("outlet_class")})
    tiers = [s["reliability_tier"] for s in sources if s.get("reliability_tier")]
    highest = min(tiers) if tiers else None
    has_originating = any(s.get("originating_or_republishing") == "originating" for s in sources)
    has_primary_document = any(s.get("outlet_class") == "primary_document" for s in sources)
    return {
        "count": len(sources),
        "outlets": outlets,
        "outlet_classes": outlet_classes,
        "highest_reliability_tier": highest,
        "has_originating": has_originating,
        "has_primary_document": has_primary_document,
    }

# ---------------------------------------------------------------------------
# Single-file processing
# ---------------------------------------------------------------------------

def process_file(path: Path, doc_type: str, errors: list) -> dict | None:
    """
    Parse one article or column markdown file.
    Returns a result dict or None on hard failure.
    doc_type: 'article' | 'column'
    """
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        errors.append({"file": path.name, "error": f"read error: {e}"})
        return None

    fm_str, body = split_frontmatter(content)
    if fm_str is None:
        errors.append({"file": path.name, "error": "missing or malformed frontmatter"})
        return None

    fm = parse_frontmatter(fm_str)
    if not fm:
        errors.append({"file": path.name, "error": "frontmatter parsed to empty dict"})
        return None

    slug = fm.get("slug") or path.stem
    headline = fm.get("headline", "")
    publish_date_raw = fm.get("publish_date", "")
    publish_date = str(publish_date_raw).replace("'", "") if publish_date_raw else ""

    # Derive year and month
    pd_parts = publish_date.split("-") if publish_date else []
    publish_year = int(pd_parts[0]) if len(pd_parts) >= 1 and pd_parts[0].isdigit() else None
    publish_month = f"{pd_parts[0]}-{pd_parts[1]}" if len(pd_parts) >= 2 else None

    # Parse body sections
    claims = parse_claims_section(body)
    sources = parse_sources_section(body)

    # If body claims/sources are empty, fall back to YAML aggregates for counts
    yaml_claims = fm.get("claims") or {}
    yaml_sources_agg = fm.get("sources") or {}
    yaml_figures = fm.get("figures_aggregate") or fm.get("figures") or {}

    # Prefer parsed; fall back to YAML
    if claims:
        claims_agg = compute_claim_aggregate(claims)
    else:
        claims_agg = yaml_claims if isinstance(yaml_claims, dict) else {"count": 0}

    if sources:
        sources_agg = compute_source_aggregate(sources)
    else:
        sources_agg = yaml_sources_agg if isinstance(yaml_sources_agg, dict) else {"count": 0}

    # Figures aggregate from YAML (body figures not separately parsed)
    if isinstance(yaml_figures, dict):
        figures_agg = {
            "count": yaml_figures.get("count", 0),
            "series_ids": yaml_figures.get("series_ids", []) or [],
            "sources": yaml_figures.get("sources", []) or [],
        }
    else:
        figures_agg = {"count": 0, "series_ids": [], "sources": []}

    # Safely coerce list fields
    def safe_list(v):
        if isinstance(v, list):
            return v
        if v is None:
            return []
        return [v]

    primary_entities = safe_list(fm.get("primary_entities"))
    primary_themes   = safe_list(fm.get("primary_themes"))
    topic_tags       = safe_list(fm.get("topic_tags"))
    storyline_nexus  = safe_list(fm.get("storyline_nexus"))
    floor_values     = safe_list(fm.get("floor_values_engaged"))
    cross_links      = safe_list(fm.get("cross_article_links"))

    image = fm.get("image") or {}
    image_source = image.get("source", "") if isinstance(image, dict) else ""

    url_path = f"articles/{slug}" if doc_type == "article" else f"opinion/{slug}"
    url = f"{BASE_URL}/{url_path}"

    record = {
        "slug": slug,
        "headline": headline,
        "publish_date": publish_date,
        "publish_year": publish_year,
        "publish_month": publish_month,
        "primary_entities": primary_entities,
        "primary_themes": primary_themes,
        "topic_tags": topic_tags,
        "storyline_nexus": storyline_nexus,
        "geographic_location": fm.get("geographic_location", ""),
        "floor_values_engaged": floor_values,
        "claims": claims_agg,
        "sources": sources_agg,
        "figures": figures_agg,
        "framework_version": fm.get("framework_version", ""),
        "ai_generated": bool(fm.get("ai_generated", True)),
        "image_source": image_source,
        "license": fm.get("license", "https://creativecommons.org/publicdomain/zero/1.0/"),
        "url": url,
        "cross_article_links": cross_links,
    }

    # Column-specific fields
    if doc_type == "column":
        record["pen_name"] = fm.get("pen_name", "")
        record["parody"] = bool(fm.get("parody", False))
        record["parody_subject"] = fm.get("parody_subject", None)

    return {
        "record": record,
        "claims_parsed": claims,
        "sources_parsed": sources,
        "publish_date": publish_date,
        "slug": slug,
        "primary_entities": primary_entities,
        "topic_tags": topic_tags,
        "storyline_nexus": storyline_nexus,
        "figures_agg": figures_agg,
        "pen_name": fm.get("pen_name", "") if doc_type == "column" else None,
    }

# ---------------------------------------------------------------------------
# JSONL writers
# ---------------------------------------------------------------------------

def write_jsonl(path: Path, rows: list):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")


# ---------------------------------------------------------------------------
# Aggregate builders
# ---------------------------------------------------------------------------

def build_entities_jsonl(results: list) -> list:
    entity_map = defaultdict(lambda: {"article_count": 0, "dates": [], "articles": []})
    for r in results:
        for e in r["primary_entities"]:
            entity_map[e]["article_count"] += 1
            entity_map[e]["articles"].append(r["slug"])
            if r["publish_date"]:
                entity_map[e]["dates"].append(r["publish_date"])
    rows = []
    for entity, data in sorted(entity_map.items()):
        dates = sorted(data["dates"])
        rows.append({
            "entity": entity,
            "article_count": data["article_count"],
            "first_seen": dates[0] if dates else None,
            "last_seen": dates[-1] if dates else None,
            "articles": sorted(set(data["articles"])),
        })
    return sorted(rows, key=lambda r: r["article_count"], reverse=True)


def build_topics_jsonl(results: list) -> list:
    topic_map = defaultdict(lambda: {"article_count": 0, "dates": [], "articles": []})
    for r in results:
        for t in r["topic_tags"]:
            if t:
                topic_map[t]["article_count"] += 1
                topic_map[t]["articles"].append(r["slug"])
                if r["publish_date"]:
                    topic_map[t]["dates"].append(r["publish_date"])
    rows = []
    for tag, data in sorted(topic_map.items()):
        dates = sorted(data["dates"])
        rows.append({
            "topic_tag": tag,
            "article_count": data["article_count"],
            "first_seen": dates[0] if dates else None,
            "last_seen": dates[-1] if dates else None,
            "articles": sorted(set(data["articles"])),
        })
    return sorted(rows, key=lambda r: r["article_count"], reverse=True)


def build_storylines_jsonl(results: list) -> list:
    storyline_map = defaultdict(lambda: {"article_count": 0, "dates": [], "articles": []})
    for r in results:
        for s in r["storyline_nexus"]:
            if s:
                storyline_map[s]["article_count"] += 1
                storyline_map[s]["articles"].append(r["slug"])
                if r["publish_date"]:
                    storyline_map[s]["dates"].append(r["publish_date"])
    rows = []
    for slug, data in sorted(storyline_map.items()):
        dates = sorted(data["dates"])
        rows.append({
            "slug": slug,
            "article_count": data["article_count"],
            "first_seen": dates[0] if dates else None,
            "last_seen": dates[-1] if dates else None,
            "articles": sorted(set(data["articles"])),
        })
    return sorted(rows, key=lambda r: r["article_count"], reverse=True)


def build_figures_jsonl(results: list, doc_type: str) -> list:
    """One row per chart/figure series_id, aggregated from figures_agg."""
    fig_map = defaultdict(lambda: {"article_count": 0, "articles": [], "sources": set()})
    for r in results:
        fa = r["figures_agg"]
        if fa.get("count", 0) == 0:
            continue
        for sid in fa.get("series_ids", []):
            if sid:
                fig_map[sid]["article_count"] += 1
                fig_map[sid]["articles"].append(r["slug"])
                for src in fa.get("sources", []):
                    fig_map[sid]["sources"].add(src)
    rows = []
    for series_id, data in sorted(fig_map.items()):
        rows.append({
            "series_id": series_id,
            "article_count": data["article_count"],
            "sources": sorted(data["sources"]),
            "articles": sorted(set(data["articles"])),
        })
    return sorted(rows, key=lambda r: r["article_count"], reverse=True)


def build_pen_names_jsonl(results: list) -> list:
    pen_map = defaultdict(lambda: {"column_count": 0, "topics": set(), "articles": []})
    for r in results:
        pn = r.get("pen_name", "")
        if pn:
            pen_map[pn]["column_count"] += 1
            pen_map[pn]["articles"].append(r["slug"])
            for t in r["topic_tags"]:
                if t:
                    pen_map[pn]["topics"].add(t)
    rows = []
    for pen_name, data in sorted(pen_map.items()):
        rows.append({
            "pen_name": pen_name,
            "column_count": data["column_count"],
            "topic_coverage": sorted(data["topics"]),
            "columns": sorted(set(data["articles"])),
        })
    return sorted(rows, key=lambda r: r["column_count"], reverse=True)


# ---------------------------------------------------------------------------
# Claims and sources JSONL
# ---------------------------------------------------------------------------

def build_claims_jsonl(results: list, doc_type: str) -> list:
    rows = []
    for r in results:
        slug = r["slug"]
        pub_date = r["publish_date"]
        url = r["record"]["url"]
        topic_tags = r["topic_tags"]
        storyline_nexus = r["storyline_nexus"]
        sources_parsed = r["sources_parsed"]

        # Build source outlet index for denorm
        source_outlet_map = {}
        source_outlet_class_map = {}
        source_tier_map = {}
        for s in sources_parsed:
            sid = s["source_id"]
            source_outlet_map[sid] = s.get("outlet", "")
            source_outlet_class_map[sid] = s.get("outlet_class", "")
            source_tier_map[sid] = s.get("reliability_tier", 5)

        for c in r["claims_parsed"]:
            cid = c["claim_id"]
            global_claim_id = f"{slug}/{cid}"
            global_source_ids = [f"{slug}/{sid}" for sid in c.get("source_ids", [])]

            # Denorm source info
            outlets = sorted({source_outlet_map[sid] for sid in c.get("source_ids", []) if sid in source_outlet_map and source_outlet_map[sid]})
            outlet_classes = sorted({source_outlet_class_map[sid] for sid in c.get("source_ids", []) if sid in source_outlet_class_map and source_outlet_class_map[sid]})
            tiers = [source_tier_map[sid] for sid in c.get("source_ids", []) if sid in source_tier_map]
            highest_tier = min(tiers) if tiers else None

            rows.append({
                "claim_id": global_claim_id,
                "parent_slug": slug,
                "parent_publish_date": pub_date,
                "parent_url": url,
                "text": c.get("text", ""),
                "subject_entities": c.get("subject_entities", []),
                "predicate": c.get("predicate", ""),
                "object": c.get("object", {"value": "", "type": "fact"}),
                "temporal": c.get("temporal", ""),
                "source_ids": global_source_ids,
                "hedge": c.get("hedge", "reported"),
                "corroboration_level": c.get("corroboration_level", "single_source"),
                "source_outlets": outlets,
                "source_outlet_classes": outlet_classes,
                "highest_source_reliability_tier": highest_tier,
                "parent_topic_tags": topic_tags,
                "parent_storyline_nexus": storyline_nexus,
            })
    return rows


def build_sources_jsonl(results: list) -> list:
    rows = []
    for r in results:
        slug = r["slug"]
        pub_date = r["publish_date"]
        for s in r["sources_parsed"]:
            global_source_id = f"{slug}/{s['source_id']}"
            rows.append({
                "source_id": global_source_id,
                "parent_slug": slug,
                "parent_publish_date": pub_date,
                "outlet": s.get("outlet", ""),
                "outlet_class": s.get("outlet_class", "other"),
                "reliability_tier": s.get("reliability_tier", 5),
                "originating_or_republishing": s.get("originating_or_republishing", "originating"),
                "author": s.get("author"),
                "publication_date": s.get("publication_date"),
                "access_date": s.get("access_date"),
                "title": s.get("title"),
                "url": s.get("url"),
            })
    return rows

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_output(output_dir: Path, schema_path: Path):
    if not HAS_JSONSCHEMA:
        print("  jsonschema not installed — skipping validation.")
        return
    try:
        with schema_path.open() as f:
            schema = json.load(f)
    except Exception as e:
        print(f"  Could not load schema.json: {e} — skipping validation.", file=sys.stderr)
        return

    record_type_map = {
        "news/index.jsonl": "Article",
        "news/claims.jsonl": "Claim",
        "news/sources.jsonl": "Source",
        "news/entities.jsonl": "EntityAggregate",
        "news/topics.jsonl": "TopicAggregate",
        "news/storylines.jsonl": "StorylineAggregate",
        "news/figures.jsonl": "Figure",
        "opinion/index.jsonl": "Column",
        "opinion/claims.jsonl": "Claim",
        "opinion/sources.jsonl": "Source",
        "opinion/entities.jsonl": "EntityAggregate",
        "opinion/topics.jsonl": "TopicAggregate",
        "opinion/storylines.jsonl": "StorylineAggregate",
        "opinion/pen_names.jsonl": "PenName",
    }
    for rel_path, type_name in record_type_map.items():
        fpath = output_dir / rel_path
        if not fpath.exists():
            continue
        defs = schema.get("$defs", {})
        if type_name not in defs:
            continue
        # Whole schema + top-level $ref so internal $defs references resolve
        type_schema = {**schema, "$ref": f"#/$defs/{type_name}"}
        validator = jsonschema.Draft202012Validator(type_schema)
        errors_found = 0
        with fpath.open() as f:
            for i, line in enumerate(f, 1):
                try:
                    record = json.loads(line)
                    errs = list(validator.iter_errors(record))
                    if errs:
                        errors_found += 1
                except Exception:
                    pass
        if errors_found:
            print(f"  VALIDATION: {rel_path} — {errors_found} records failed schema check", file=sys.stderr)
        else:
            print(f"  OK: {rel_path}")

# ---------------------------------------------------------------------------
# Manifest update
# ---------------------------------------------------------------------------

def update_manifest(output_dir: Path, news_results, opinion_results,
                    news_claims, news_sources, opinion_claims, opinion_sources):
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists():
        return

    def count_lines(p: Path) -> int:
        if not p.exists():
            return 0
        with p.open() as f:
            return sum(1 for line in f if line.strip())

    with manifest_path.open() as f:
        manifest = json.load(f)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest["generated_at"] = now

    for corpus in manifest.get("corpora", []):
        if corpus["name"] == "news":
            corpus["article_count"] = len(news_results)
            corpus["claim_count"] = len(news_claims)
            corpus["source_count"] = len(news_sources)
            for idx in corpus.get("indexes", []):
                p = output_dir / idx["path"]
                idx["row_count"] = count_lines(p)
        elif corpus["name"] == "opinion":
            corpus["column_count"] = len(opinion_results)
            for idx in corpus.get("indexes", []):
                p = output_dir / idx["path"]
                idx["row_count"] = count_lines(p)

    with manifest_path.open("w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  manifest.json updated (generated_at: {now})")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Rebuild msi-corpus JSONL indexes.")
    parser.add_argument("--articles-dir", default=str(ARTICLES_DIR))
    parser.add_argument("--columns-dir",  default=str(COLUMNS_DIR))
    parser.add_argument("--output-dir",   default=str(OUTPUT_DIR))
    args = parser.parse_args()

    articles_dir = Path(args.articles_dir)
    columns_dir  = Path(args.columns_dir)
    output_dir   = Path(args.output_dir)

    news_out    = output_dir / "news"
    opinion_out = output_dir / "opinion"
    news_mirror    = news_out / "articles"
    opinion_mirror = opinion_out / "columns"

    news_mirror.mkdir(parents=True, exist_ok=True)
    opinion_mirror.mkdir(parents=True, exist_ok=True)

    errors = []

    # ---- Process articles ----
    print(f"\nProcessing news articles from {articles_dir} ...")
    article_files = sorted(articles_dir.glob("*.md"))
    news_results = []
    for path in article_files:
        result = process_file(path, "article", errors)
        if result:
            news_results.append(result)
        # Mirror the file
        dst = news_mirror / path.name
        shutil.copy2(str(path), str(dst))

    print(f"  Parsed: {len(news_results)} / {len(article_files)} articles")

    # ---- Process columns ----
    print(f"\nProcessing opinion columns from {columns_dir} ...")
    column_files = sorted(columns_dir.glob("*.md"))
    opinion_results = []
    for path in column_files:
        result = process_file(path, "column", errors)
        if result:
            opinion_results.append(result)
        dst = opinion_mirror / path.name
        shutil.copy2(str(path), str(dst))

    print(f"  Parsed: {len(opinion_results)} / {len(column_files)} columns")

    # ---- Build JSONL indexes ----
    print("\nBuilding JSONL indexes ...")

    # News
    news_index = [r["record"] for r in news_results]
    news_claims = build_claims_jsonl(news_results, "article")
    news_sources = build_sources_jsonl(news_results)
    news_entities = build_entities_jsonl(news_results)
    news_topics = build_topics_jsonl(news_results)
    news_storylines = build_storylines_jsonl(news_results)
    news_figures = build_figures_jsonl(news_results, "article")

    write_jsonl(news_out / "index.jsonl", news_index)
    write_jsonl(news_out / "claims.jsonl", news_claims)
    write_jsonl(news_out / "sources.jsonl", news_sources)
    write_jsonl(news_out / "entities.jsonl", news_entities)
    write_jsonl(news_out / "topics.jsonl", news_topics)
    write_jsonl(news_out / "storylines.jsonl", news_storylines)
    write_jsonl(news_out / "figures.jsonl", news_figures)

    print(f"  news/index.jsonl      : {len(news_index):>6} rows")
    print(f"  news/claims.jsonl     : {len(news_claims):>6} rows")
    print(f"  news/sources.jsonl    : {len(news_sources):>6} rows")
    print(f"  news/entities.jsonl   : {len(news_entities):>6} rows")
    print(f"  news/topics.jsonl     : {len(news_topics):>6} rows")
    print(f"  news/storylines.jsonl : {len(news_storylines):>6} rows")
    print(f"  news/figures.jsonl    : {len(news_figures):>6} rows")

    # Opinion
    opinion_index = [r["record"] for r in opinion_results]
    opinion_claims = build_claims_jsonl(opinion_results, "column")
    opinion_sources = build_sources_jsonl(opinion_results)
    opinion_entities = build_entities_jsonl(opinion_results)
    opinion_topics = build_topics_jsonl(opinion_results)
    opinion_storylines = build_storylines_jsonl(opinion_results)
    opinion_pen_names = build_pen_names_jsonl(opinion_results)

    write_jsonl(opinion_out / "index.jsonl", opinion_index)
    write_jsonl(opinion_out / "claims.jsonl", opinion_claims)
    write_jsonl(opinion_out / "sources.jsonl", opinion_sources)
    write_jsonl(opinion_out / "entities.jsonl", opinion_entities)
    write_jsonl(opinion_out / "topics.jsonl", opinion_topics)
    write_jsonl(opinion_out / "storylines.jsonl", opinion_storylines)
    write_jsonl(opinion_out / "pen_names.jsonl", opinion_pen_names)

    print(f"\n  opinion/index.jsonl      : {len(opinion_index):>6} rows")
    print(f"  opinion/claims.jsonl     : {len(opinion_claims):>6} rows")
    print(f"  opinion/sources.jsonl    : {len(opinion_sources):>6} rows")
    print(f"  opinion/entities.jsonl   : {len(opinion_entities):>6} rows")
    print(f"  opinion/topics.jsonl     : {len(opinion_topics):>6} rows")
    print(f"  opinion/storylines.jsonl : {len(opinion_storylines):>6} rows")
    print(f"  opinion/pen_names.jsonl  : {len(opinion_pen_names):>6} rows")

    # ---- Validate ----
    print("\nValidating output ...")
    validate_output(output_dir, output_dir / "schema.json")

    # ---- Update manifest ----
    print("\nUpdating manifest.json ...")
    update_manifest(output_dir, news_results, opinion_results,
                    news_claims, news_sources, opinion_claims, opinion_sources)

    # ---- Error report ----
    if errors:
        print(f"\nERRORS ({len(errors)} files failed parsing):")
        for e in errors[:20]:
            print(f"  {e['file']}: {e['error']}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")
    else:
        print("\nNo parse errors.")

    total = len(news_results) + len(opinion_results)
    print(f"\nDone. {total} documents processed ({len(news_results)} articles, {len(opinion_results)} columns).")


if __name__ == "__main__":
    main()
