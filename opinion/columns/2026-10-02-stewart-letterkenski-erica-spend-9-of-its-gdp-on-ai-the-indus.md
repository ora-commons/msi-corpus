---
headline: OpenAI and Anthropic are betting on nine percent of your income
publish_date: '2026-10-02'
lede: OpenAI and Anthropic are betting you will pay nine percent of GDP for their software.
pen_name: stewart-letterkenski
primary_entities:
- Stijn Van Nieuwerburgh
- Columbia University
- Brookings Institution
- OpenAI
- Anthropic
- Epoch AI
- Federal Reserve Bank of Chicago
- Greg Ip
- The Wall Street Journal
- Harvard University
- Fiona Chen
- James Stratton
- Ezra Karger
primary_themes:
- AI investment boom
- AI revenue projections
- data center economics
- technology adoption
- investment returns
- productivity research
topic_tags:
- economy
- artificial intelligence
storyline_nexus: []
geographic_location: United States
floor_values_engaged:
- value: human_life_and_dignity
  intensity: 0.3
- value: accountability_of_power
  intensity: 0.3
framework_version: 1.1.0
generation_timestamp: '2026-10-03T20:48:10-07:00'
source_cluster_id: cluster_wsj_2026-10-02_erica-spend-9-of-its-gdp-on-ai-the-indus
gdelt_event_ids: []
consensus_floor_version: v0.3.0
publication_mindspec_version: v0.3.0
license: https://creativecommons.org/publicdomain/zero/1.0/
ai_disclosure: This article was generated algorithmically by Main Street Independent from the public sources listed in its Sources section.
ai_generated: true
sources:
  count: 1
  outlets:
  - The Wall Street Journal
  outlet_classes:
  - national_daily
  highest_reliability_tier: 1
  has_originating: true
  has_primary_document: false
figures_aggregate:
  count: 0
  series_ids: []
  sources: []
cross_article_links:
- slug: 2026-10-02-ai-sector-needs-9-of-us-gdp-in-revenue-by-2032-analysis-finds
  relation: extends
  strength: 1.0
  confidence: high
draft: false
---

OpenAI and Anthropic are betting you will pay nine percent of GDP for their software.

It is worth being precise about what that number is, because the precision is what makes it checkable. Nine percent — $3.5 trillion of annual revenue by 2032 — is not a forecast either company has endorsed. It is, in the arithmetic of Columbia University finance professor Stijn Van Nieuwerburgh, presented at the Brookings Institution, what the build-out already committed requires for the money now being spent to earn its way back. His assumptions are stated plainly in this week's column in the Wall Street Journal: the data-centre plans as announced, an average build cost, some cancellations, fifty cents of cash flow from each revenue dollar, and a 10% unleveraged return on invested capital. Cumulative US AI infrastructure investment is [projected at $10.3 trillion between 2025 and 2032](/articles/2026-09-24-us-ai-infrastructure-investment-projected-at-10-3-trillion-from-2025-to-2032/). The nine percent figure is not a fever dream, to borrow the Journal's phrase. It is the invoice.

It is true that the revenue is not nothing. An expert panel convened by a team led by Ezra Karger at the Federal Reserve Bank of Chicago projected OpenAI and Anthropic would reach combined annual revenue of $300 billion by 2030, and the two firms' combined run rate is already around $180 billion, growing at double-digit rates each quarter. The trouble is what that revenue is a run rate of. It is a run rate of tokens delivered at scarcity prices — in a market where the entire capital program is being spent to end the scarcity those prices rest on. The number is real. The assumption underneath it is the thing being financed.

Take the use case that is actually driving that run rate: agentic coding. The loop is not mysterious. A model generates a patch; an agent runs it against the repository — builds it, runs the tests and the linters, reads the failure output, regenerates; a human is looped in when the output will not settle. What the customer is buying is merged, shipped work. What the model produces is candidate output, and candidate output costs tokens continuously while its value is realised only in review, integration, and the judgement that the change does what it was supposed to do. The arithmetic of that loop is what the price is riding on. This is precisely what the research record says. Fiona Chen and James Stratton, Harvard doctoral students, reviewed software projects through Jellyfish, the platform firms use to analyse their engineering teams: AI assistants raised lines of code by 12 percent and pull requests — when new code is merged into an existing code base — by 5 percent; autonomous agents raised lines of code by 30 percent and pull requests by 23 percent. And the boost to completed projects was small and statistically insignificant, because the extra output generated review, comment, and rework. The instinct is to file that under diffusion — tools arrive before workflows catch up and the graph will bend later — but the finding is not a lag indicator. It is a description of the mechanism. Generation scales; verification does not. When a model's output rate outruns the rate at which a human can certify that the output is right, verified throughput is capped by verification rather than by generation, and the token bill scales with the model anyway. It may bend later. What would show it bending is completed-project throughput, and that metric has not moved. For nine percent of GDP to clear, the price of verified throughput has to fall faster than the cost of generating unverified output, or the population of tasks where verified output is worth more than the review has to be far larger than the record currently shows. Neither is in evidence.

Now the bottlenecks, because the nine percent depends on scarcity holding on the input side, and four of them matter. Compute: accelerator supply is expanding — advanced packaging at TSMC, high-bandwidth memory from three suppliers — and the capital program that assumes scarcity pricing is the program ending it. Energy: the builders are not waiting for the market to sort it out. Microsoft has a twenty-year contract to restart Unit 1 at Three Mile Island with Constellation; Meta has signed for the entire output of Constellation's Clinton plant in Illinois, also for twenty years. Those are the prices scarcity is charging today, and they are also instruments of its removal. Memory and bandwidth: inference at current context lengths is dominated by input tokens, and retrieval-heavy workloads — enterprise search, long-document analysis, codebase understanding — are the workloads where context grows rather than shrinks, because a system answers better when it can see more of the corpus. Latency: in an agentic loop, latency is the iteration rate, so a faster, cheaper model lowers the cost of each attempt and expands the set of tasks that clear the cost-benefit bar. That is genuine demand expansion, and the Jevons argument in the Journal's column — cheaper capability means more total spending, as cheaper coal did in nineteenth-century England — is not stupid. Model capability is doubling roughly every four to five months, and Epoch AI's measurements put the effective price of a given level of capability down 47 percent per quarter since 2023, six times faster than the price of raw computing power. But Jevons is not a law of nature; it is a claim about a demand curve, and it holds only where the marginal task clears its cost at scale. The evaluation problem is where that claim meets the record. Most enterprise deployments run thin evaluation suites; what the last billion dollars of inference bought is unmeasured rather than known to be low, so the marginal return on the next billion is a guess dressed as a number. What would settle it is the measurement almost nobody publishes: the cost of a completed, verified task against what the customer will pay for it.

The historical analogues cut in both directions, and both sides of the argument reach for the ones that flatter them. From the 1960s through the early 2000s, chip density doubled about every two years and the real price of computers fell roughly 15 percent a year; business investment in computers tripled to 0.8 percent of GDP between 1974 and 1984, and then plateaued for a decade, because the first spreadsheets changed business in ways that ever more powerful later spreadsheets could not. That is the bear's analogue: productivity tools front-load their value, and after the first wave of genuinely new tasks is absorbed, price declines stop producing new demand. The fibre build-out is the other analogue, and it is usually argued badly. Between 1997 and 2001, the price of bandwidth between London and New York fell 96 percent as new strands went in; several of the largest long-haul carriers ended up in bankruptcy. The bears say prices kill booms. The bulls say the fibre survived and the digital economy ran on it. Both are half right, and the useful half is the one neither side states: the asset survived, the capital did not. What was preserved was the network and the capacity; what was destroyed was the equity and the returns that had been modelled at yesterday's prices. Nothing in the technology protects the capital that financed it from the price curve.

Which leaves the assumption itself, and it is worth naming which way it cuts. The nine percent rests on compute remaining priced at today's scarcity levels through 2032 — a price assumption held by the sellers, whose valuations depend on scarcity persisting, and borne by the buyers, who will pay only what verified output is worth to them. A revenue model built on the seller's price rather than the buyer's value is not a forecast; it is a transfer, and at nine percent of GDP it is a transfer larger than everything American households spend on food. The labour share of GDP is roughly 51 percent; nine points of national income claimed from the other factors of production is not rounding error. It is a claim on household and business income that has not been put to a committee, a customer, or a vote.

The most interesting document of the past month is not a financial filing but a piece of software: Anthropic released [an interactive tool for modelling AI economic impact](/articles/2026-09-09-anthropic-releases-interactive-tool-for-modeling-ai-economic-impact/) in September. Read it as an instrument rather than a tell. The company selling the inference is modelling the revenue side of the economy it is supposed to transform, in public, while the investment side prices the same transformation as settled. The two positions cannot both be right, and the tool is where you can watch the gap being estimated.

The shape of this is old, and it is worth being precise about what is new. My father kept his job at Manitoba Rolling Mills after the mill was bought in 1995, and several of his uncles did not; the pension he retired on in 2011 was a fraction of what the 1995 bargain had promised. The mechanism was arithmetic rather than malice: the asset was bought on projections of what it could yield, and when the yield did not arrive, the difference came out of the people who worked there rather than out of the projections that justified the purchase. That is the same arithmetic now, at a scale the mill never approached — model the return, finance the asset on the strength of the model, and let whoever is downstream absorb the difference when the model turns out to be a model.

OpenAI and Anthropic are not lying about their growth. The run rates are real, the capability curves are real, and if verified throughput ever scales the way generation has, nine percent of GDP could turn out to be conservative. But the nine percent is not what the industry is spending. It is what the industry is betting other people will spend, and the bet is being settled now, in debt that matures before the revenue arrives. Van Nieuwerburgh's arithmetic is public, his assumptions are stated, and his number is the one the capital is being raised against. It would cost a great deal less to ask the question than to discover the answer.

The data centres will be finished before the revenue arrives. That is the ordinary shape of a construction loan, and the ordinary shape of what follows one when the projections do not clear: the asset gets built, the projections get restated, and the difference goes to the line.

## Sources

### src_001 — The Wall Street Journal, national_daily, Tier 1, originating
**Author:** Greg Ip
**Publication date:** 2026-10-02
**Title:** Will America Spend 9% of Its GDP on AI? The Industry Is Counting on It.
**URL:** https://www.wsj.com/tech/ai/will-america-spend-9-of-its-gdp-on-ai-the-industry-is-counting-on-it-3501bb4f
