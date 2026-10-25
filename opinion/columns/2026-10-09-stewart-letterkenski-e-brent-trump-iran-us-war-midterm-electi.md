---
headline: Starlink Bought 45 Megahertz and Called It a Mobile Carrier
publish_date: '2026-10-09'
lede: SpaceX bought forty-five megahertz of public spectrum and called it a mobile carrier.
pen_name: stewart-letterkenski
primary_entities:
- SpaceX
- Starlink Mobile
- Verizon Communications
- AT&T
- T-Mobile US
- BT
- Vodafone
- Elon Musk
primary_themes:
- Telecommunications
- Stock markets
- Satellite internet
- Market competition
topic_tags:
- business information
- economy
- science and technology
storyline_nexus: []
geographic_location: United States
floor_values_engaged:
- value: human_life_and_dignity
  intensity: 0.3
- value: truthfulness
  intensity: 0.3
- value: accountability_of_power
  intensity: 0.9
framework_version: 1.1.0
generation_timestamp: '2026-10-09T01:19:10-07:00'
source_cluster_id: cluster_guardian_2026-10-09_e-brent-trump-iran-us-war-midterm-electi
gdelt_event_ids: []
consensus_floor_version: v0.3.0
publication_mindspec_version: v0.3.0
license: https://creativecommons.org/publicdomain/zero/1.0/
ai_disclosure: This article was generated algorithmically by Main Street Independent from the public sources listed in its Sources section.
ai_generated: true
sources:
  count: 1
  outlets:
  - The Guardian
  outlet_classes:
  - national_daily
  highest_reliability_tier: 2
  has_originating: true
  has_primary_document: false
figures_aggregate:
  count: 0
  series_ids: []
  sources: []
cross_article_links:
- slug: 2026-10-09-spacex-spectrum-purchase-sends-verizon-at-t-and-t-mobile-shares-tumbling
  relation: extends
  strength: 0.2271
  confidence: high
draft: false
---

SpaceX bought forty-five megahertz of public spectrum and called it a mobile carrier. Verizon fell 7 per cent, AT&T 7.5, T-Mobile 6.7, in a single session, on the strength of an announcement. The announcement says the company has acquired a nationwide licence portfolio it describes as low-band and will use it to make Starlink, in its words, "a major mobile carrier in the US." The market took that sentence at face value and repriced three balance sheets against it. What the portfolio actually is, what the radio permits, and what still has to be approved before anything radiates are different questions, and this week they were asked quietly, if at all.

The portfolio consists of the AWS-4 block — twenty megahertz of downlink at 2000–2020 and twenty of uplink at 2180–2200 — plus the H block of the PCS band, five megahertz paired, uplink 1915–1920, downlink 1995–2000. Forty-five megahertz of paired spectrum, sitting at two gigahertz. The release calls it low-band. Low-band is not a price bracket; it is a propagation regime — the sub-gigahertz range where a signal at the same transmitted power covers roughly two to three times the distance and moves through foliage and walls, which is the whole economic rationale for the spectrum rural North America has never had enough of. Two gigahertz is mid-band by any engineering definition anyone in this industry uses. Reaching for the low-band adjective is the first thing in this story worth noticing, because it is a coverage claim the licences in question do not carry.

It is true that the incumbents have earned almost no sympathy here. Verizon, AT&T and T-Mobile have spent two decades collecting licence fees, binding customers with sticky contracts, selling "unlimited" plans whose throttling thresholds are published in their own terms of service, and acquiring spectrum faster than they have radiated on it. The H block makes that last point without any help from me: it entered the world attached to population-coverage deadlines written into its licence, and it now reaches the market as a component of a corporate portfolio. A licence that ends up for sale rather than in the ground tells you something about what the deadlines were worth. [Starlink telegraphed this move in July, filing to target AT&T and Verizon directly](/articles/2026-07-02-spacex-starlink-plans-mobile-service-to-target-at-t-verizon/); the difference is that the July filing was a plan and the spectrum is a permission.

What Starlink Mobile has actually been, until now, is not a carrier business. It is supplemental coverage: satellites carrying a 3GPP base station — an eNodeB or gNodeB, the same protocol stack a tower runs — speaking LTE or 5G NR to an unmodified handset over spectrum borrowed from a terrestrial partner, under the framework the FCC adopted in its 2024 Supplemental Coverage from Space order. The phone does not know it is talking to orbit. That arrangement has genuine value, and I will say so plainly: it covers the sea, the mountains, the reservations and the fire breaks where a tower never penciled in, and the people who live there are not well served by a debate about market structure. Buying the spectrum converts borrowed capacity, with coordination conditions attached, into owned capacity. That is a real legal difference. It is not a physical one.

The physics run as follows. The satellites orbit at roughly five hundred and fifty kilometres. A handset transmits about twenty-three dBm from an antenna patterned for a base station two kilometres away rather than one five hundred and fifty kilometres up, and usually with a hand wrapped around it. Free-space path loss at two gigahertz over that distance is a shade over 150 decibels, one way, before rain, before body loss, before anything else. The downlink is fixable: the satellite carries a large phased array and has power to spend. The uplink is the constraint, and it is the reason every direct-to-cell service in existence ships messaging before data. Every decibel of uplink margin consumed is a decibel of downlink capacity you cannot sell. Move the same link down to seven hundred megahertz — the band the release's adjective is meant to evoke — and you recover roughly nine decibels, which at this altitude is the difference between a data service and a text message. Then there is the second constraint, which no press release has solved: at that altitude a satellite is overhead for four or five minutes, and there is no user-plane handover between satellites in the constellation as currently flown. The connection ends when the spacecraft sets. One terrestrial macro sector on twenty megahertz of mid-band, serving a few kilometres, moves an order of magnitude more aggregate traffic than a full pass of satellites moves across a footprint the size of a province. Coverage is not capacity. That is not a slogan; it is arithmetic.

So Starlink Mobile can be one of two things, and the announcement does not distinguish them. As a coverage layer riding on a terrestrial carrier's network, it is a rural and maritime product and it is good at that. As a standalone carrier it needs one of two things: a terrestrial grid of its own — macro sites, backhaul, small cells in the dense places where the revenue is — or roaming arrangements with the incumbents it is supposedly displacing, which would make the challenger a wholesale customer of the duopoly. The announcement is also silent on the sharpest question the purchase raises, which is whether the payloads already in orbit can be configured to transmit and receive in these bands. A licence is a legal instrument. A phased array is a physical one. Neither is reconfigured by press release.

What stands between Friday and a network is a docket. Transfer of AWS-4 and H-block licences requires the FCC's approval on a public-interest standard, with a window for objections from the incumbents and from any competing bidder — a process measured in months and occasionally in years, and one that has denied applications before. The licences carry build-out obligations expressed as population coverage, and whether coverage delivered from orbit satisfies an obligation written for towers is a question the Supplemental Coverage from Space order did not cleanly resolve; somebody will have to answer it in an application and, more likely than not, in a petition for reconsideration. Becoming a carrier also means the unglamorous stack beneath the launch event: E911 location accuracy, CALEA compliance, CPNI rules, universal-service contributions, interconnection agreements, certification in fifty states. None of that is in the release because none of it makes a headline. [The share price is also not a neutral observer of this announcement](/articles/2026-08-04-spacex-shares-down-by-half-from-june-peak-as-earnings-call-nears/), and the timing of a very visible asset purchase is worth holding next to the balance sheet that made it.

Which brings the symmetry to bear. SpaceX is not the corrective to the duopoly; it is assembling a version of the duopoly with a single name on the letterhead. It owns the launch, the constellation, the terminals, the customer billing relationship, and now the spectrum. It sells direct, with no retail store to walk into, no state utility commission to write to, and a terms-of-service agreement it can amend faster than any regulator can read. When Delta chose a rival's satellite service this fall, the response was not a filing; it was a personal attack on Delta's chief executive. A spectrum licence is a public trust held for a term, and a company that buys forty-five megahertz as strategic optionality while the incumbent-holding press tut-tuts about hoarding is doing the thing it is objecting to, in a different key. Cory Doctorow's point about chokepoint capitalism — that the intermediary sitting between two parties and charging both is the business, not a bug in it — applies here with unusual precision to a company that owns the launch, the orbit, the spectrum, the dish, the store and the bill.

The 7 per cent day was the price of an option, priced on a press release, and press releases do not close uplinks. If the transfer is granted, the build-out showing survives, and a network gets built that delivers city-usable capacity at two gigahertz, then the market will have repriced the incumbents on facts and will have been early. That is a live possibility and it should be stated plainly rather than dismissed. Until then the accurate description is narrow: a public resource changed hands, and the right to use it was valued this week at about seven per cent of three competitors' market capitalisation.

My father's mill changed hands in 1995, and the new owner's first announcement was a modernization programme. The tonnage got made later, or it didn't, and it was made on the floor by people whose names were not in the release.

Spectrum licences work the same way. The application number, the objections filed, the build-out deadline — that is where this gets decided, and all three are public records. The share price is the least informative document in this story.

## Sources

### src_001 — The Guardian, national_daily, Tier 2, originating
**Publication date:** 2026-10-09
**Title:** Oil prices fall as Trump pauses Iran attacks, China restarts fuel exports – business live
**URL:** https://www.theguardian.com/business/live/2026/oct/09/oil-prices-crude-brent-trump-iran-us-war-midterm-elections-stocks-bonds-business-live
