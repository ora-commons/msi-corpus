# Main Street Independent — Public Corpus

AI-generated news with rich claim-level metadata. All content CC0.

**[mainstreetindependent.com](https://mainstreetindependent.com)** | License: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

---

## What this is

Main Street Independent (MSI) publishes algorithmically-generated news articles and opinion columns. Every article carries structured metadata at the claim level: atomic claims (each with a hedge and corroboration level), source citations (with outlet class and reliability tier), entity tags, IPTC topic tags, geographic location, floor values engaged, and typed cross-article links.

All content is dedicated to the public domain under CC0 1.0 Universal — no rights reserved.

---

## Repository layout

```
msi-corpus/
  README.md              this file
  llms.txt               AI-agent landing page
  manifest.json          machine-readable corpus map (row counts, vocabularies)
  schema.json            JSON Schema (draft 2020-12) for all record types

  news/
    articles/            mirror of all news articles (21,590 Markdown files at the current rebuild — live counts in manifest.json)
    index.jsonl          one row per article — filter fields only, no body text
    claims.jsonl         one row per atomic claim — RAG-ready, parent-anchored
    sources.jsonl        one row per source citation
    entities.jsonl       aggregate — one row per primary entity
    topics.jsonl         aggregate — one row per IPTC topic tag
    storylines.jsonl     aggregate — one row per storyline thread
    figures.jsonl        aggregate — one row per chart/data series

  opinion/
    columns/             mirror of all opinion columns (21 heteronyms)
    index.jsonl
    claims.jsonl
    sources.jsonl
    entities.jsonl
    topics.jsonl
    storylines.jsonl
    pen_names.jsonl      one row per heteronym (column count, beat coverage)
```

---

## Worked examples

### I want to do RAG over the news corpus

The fastest path:

1. Clone only `news/` (sparse checkout saves bandwidth):

   ```
   git clone --filter=blob:none --sparse https://github.com/ora-commons/msi-corpus.git
   cd msi-corpus
   git sparse-checkout set news/
   ```

2. Embed `news/claims.jsonl`. Each row's `text` field is the claim text — short, factual, already sentence-length. This is the ideal RAG unit.

3. For full article context after a claim retrieval, use `parent_slug` to look up the article from `news/articles/{parent_slug}.md`.

4. Filter before embedding to reduce index size:

   ```
   jq -c 'select(.hedge != "alleged")' news/claims.jsonl > claims_filtered.jsonl
   ```

### I want statistical analysis of the corpus

Load `news/index.jsonl` directly into DuckDB — no schema declaration needed:

```sql
-- Articles per year
SELECT publish_year, count(*) AS n
FROM 'news/index.jsonl'
GROUP BY 1 ORDER BY 1;

-- Average claim count by source reliability tier
SELECT
  sources.highest_reliability_tier,
  avg(claims.count) AS avg_claims
FROM 'news/index.jsonl'
GROUP BY 1 ORDER BY 1;

-- Top 20 entities by article count
SELECT entity, article_count
FROM 'news/entities.jsonl'
ORDER BY article_count DESC
LIMIT 20;
```

### I want to find every article mentioning a specific entity

Two paths — pick by speed vs. completeness:

Fast (aggregate lookup):

```
jq -c 'select(.entity == "Pope Leo XIV")' news/entities.jsonl
```

Returns: `article_count`, `first_seen`, `last_seen`, and the `articles` slug list.

Precise (stream the index for additional filters):

```
jq -c 'select(.primary_entities | index("Pope Leo XIV"))' news/index.jsonl
```

### I want to validate my pipeline against the schema

`schema.json` defines JSON Schema (draft 2020-12) for every record type.

Python validation:

```python
import json, jsonschema

schema = json.load(open("schema.json"))
claim_schema = {**schema, "$ref": "#/$defs/Claim"}  # keep $defs so nested refs resolve

for line in open("news/claims.jsonl"):
    record = json.loads(line)
    jsonschema.validate(record, claim_schema)
```

JavaScript (ajv):

```js
import Ajv from "ajv/dist/2020.js";
import schema from "./schema.json" assert { type: "json" };

const ajv = new Ajv();
const validate = ajv.compile({ ...schema, $ref: "#/$defs/Article" });
```

(Compile the whole schema with a top-level `$ref` — extracting a single `$defs` entry breaks the internal `#/$defs/...` references used by `Article` and `Column`.)

### I want to fork and add my own annotations

1. Fork `ora-commons/msi-corpus`.
2. Add your annotation fields to a new `annotations/` directory or as extra keys in the JSONL rows (they pass through `schema.json` validation as additional properties by default).
3. Contribute back via PR if your annotations would be broadly useful (entity disambiguation, claim verification results, translation, etc.).

The CC0 license imposes no attribution requirement, but a mention in your fork's README and a PR back are appreciated.

### I want only Tier-1 originating-source claims that are contested

```
jq -c '
  select(
    .hedge == "contested" and
    .highest_source_reliability_tier == 1 and
    (.source_outlet_classes | index("wire") // index("national_daily"))
  )
' news/claims.jsonl
```

To also restrict to articles with cross-article contradiction links:

```
jq -c 'select(.hedge == "contested")' news/claims.jsonl \
  | while read claim; do
      slug=$(echo "$claim" | jq -r .parent_slug)
      jq -c --arg s "$slug" 'select(.slug == $s and (.cross_article_links[]?.relation == "contradicts"))' news/index.jsonl
    done
```

---

## Claim metadata reference

Each claim in `claims.jsonl`:

| Field | Values | Meaning |
|---|---|---|
| `hedge` | `confirmed`, `attributed`, `alleged`, `reported`, `appears`, `contested` | Epistemic qualifier — how strongly the claim is asserted |
| `corroboration_level` | `single_source`, `two_independent`, `primary_document`, `primary_plus_secondary`, `one_originating_plus_primary_document` | How many independent sources support the claim |
| `source_ids` | `{slug}/src_NNN` | References to rows in `sources.jsonl` |
| `parent_slug` | article slug | Foreign key to article in `index.jsonl` and to `articles/{slug}.md` |
| `highest_source_reliability_tier` | 1–5 (1 = highest) | Best tier among cited sources for this claim |

---

## Topic tags

Topic tags follow the **IPTC Media Topics** controlled vocabulary (https://www.iptc.org/standards/media-topics/) — the same standard used by AP, Reuters, AFP, and major wire services. This makes MSI content interoperable with existing IPTC-aware pipelines.

17 Level-1 subjects: arts/culture, conflict/war, crime/justice, disasters, economy, education, environment, health, human interest, labour, lifestyle, politics, religion, science/technology, society, sport, weather.

Level-2 sub-topics cover MSI's actual coverage beats. Full vocabulary in `manifest.json`.

Note: `topic_tags` are populated by a background backfill pass. At the current rebuild, 318 of 21,590 articles (~1.5%) still carry empty `topic_tags: []`. Re-run `rebuild_corpus.py` after the backfill completes to regenerate fully-populated indexes.

---

## Opinion columns

The `opinion/` tree contains columns from 21 named heteronyms. The Diklis Chump column (`pen_name: diklis-chump`) carries `parody: true` — it is satirical, not factual. Filter it out for factual-training use:

```
jq -c 'select(.pen_name != "diklis-chump")' opinion/index.jsonl
```

---

## Rebuilding the indexes

The indexes are pre-built from the current corpus state. `rebuild_corpus.py` parses article/column Markdown from `--articles-dir`/`--columns-dir`, writes the full output tree (mirrors + JSONL indexes) to `--output-dir`, optionally validates against `schema.json`, and updates `manifest.json` row counts when a manifest is already present in the output directory.

Its defaults point at the publisher's local source tree (the private MSI site checkout), so public users pass the mirrored directories explicitly and rebuild into a separate output directory (the script re-copies the mirror into its output tree, so the output directory must differ from the input directories):

```
python3 rebuild_corpus.py \
  --articles-dir news/articles \
  --columns-dir opinion/columns \
  --output-dir ../msi-rebuild-check
```

Requires Python 3 + PyYAML (`pip install pyyaml`; without it the script falls back to a lossy line parser and prints a warning). Optional: `jsonschema` for output validation. Copy `schema.json` and `manifest.json` into the output directory first to enable validation and manifest updates.

---

## License

All content in this repository is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). No rights reserved. Use freely for research, training, analysis, or any other purpose without restriction.

See `manifest.json` for generation timestamp and corpus statistics.
