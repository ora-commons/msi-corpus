---
headline: Google Captures School Search by Making It Depend on AI
publish_date: '2026-11-27'
lede: Google makes school search depend on artificial intelligence to capture school districts.
pen_name: stewart-letterkenski
primary_entities:
- Los Angeles Unified
- Google
- Schools Beyond Screens LA
- Fairfax County Public Schools
- Bridie Lee
- Jack Kelanic
- Chris Phillips
- New York City
primary_themes:
- Classroom artificial intelligence controls
- Education technology procurement
- AI integration in search
- School district responses to AI in classrooms
topic_tags:
- education
storyline_nexus:
- ai-industry-regulation
floor_values_engaged:
- value: accountability_of_power
  intensity: 0.9
- value: human_life_and_dignity
  intensity: 0.6
- value: informed_citizenship
  intensity: 0.6
framework_version: 1.1.0
generation_timestamp: '2026-11-26T21:42:05-08:00'
source_cluster_id: cluster_ap_2026-11-26_google-artificial-intelligence-schools-s
gdelt_event_ids: []
consensus_floor_version: v0.3.0
publication_mindspec_version: v0.3.0
license: https://creativecommons.org/publicdomain/zero/1.0/
ai_disclosure: This article was generated algorithmically by Main Street Independent from the public sources listed in its Sources section.
ai_generated: true
sources:
  count: 1
  outlets:
  - Main Street Independent
  outlet_classes:
  - other
  highest_reliability_tier: 1
  has_originating: true
  has_primary_document: false
figures_aggregate:
  count: 0
  series_ids: []
  sources: []
cross_article_links:
- slug: 2026-11-27-los-angeles-schools-disable-google-ai-summaries-on-district-devices
  relation: extends
  strength: 0.8459
  confidence: high
draft: false
---

Google makes school search depend on artificial intelligence to capture school districts.

It is true that ordinary Google Search is useful, that Los Angeles Unified is one of the two largest school districts in the United States and serves roughly half a million students, and that much of the district’s work runs through Chromebooks, Google Docs and Google Classroom. Chromebooks are the most widely used student laptops in America. Google also made a real concession this autumn: after previously making Gemini available to many K-12 students, it announced in early November 2026 that Gemini and its AI search tools would default off for school accounts in the coming months, with administrators required to enable each tool themselves ([Google says AI tools will default off for school accounts](/articles/2026-11-03-google-says-ai-tools-will-default-off-for-school-accounts/)). To be fair, that changes who carries the burden of saying no. A default-off feature asks the institution to opt in; a default-on feature asks families to discover the problem, understand it and complain. Google calls the change “more choice.” The trouble is that choosing individual artificial-intelligence tools off is not the same as receiving ordinary search with the generated-answer layer removed.

The evidence arrived on a child’s laptop screen. On Friday, November 13, 2026, Schools Beyond Screens LA made its case at the Los Angeles Unified school-board artificial-intelligence committee; the group had asked families to film what their children’s school-issued devices displayed. By Monday, videos circulated showing that AI Overview had disappeared from searches on those devices. LAUSD then confirmed that it had temporarily disabled the feature, calling the aim “age-appropriate and safe,” and said it continually evaluates digital safeguards, including third-party tools. Bridie Lee of Schools Beyond Screens LA said the district’s public disclosure supplied no details about how the block worked or how long it would last. That omission matters. A safety control whose operation and duration the district’s public disclosure does not explain is not yet a safeguard; it is a setting with better public relations. For a safety control, the test is not whether a known surface can be blocked after somebody posts a screenshot. It is whether the system’s state, inputs, version and audit trail are known before it changes. A temporary change of unknown implementation is incident response, not governance.

AI Overview is a layer inside Search: for many queries, Google places a generated answer at the top of the results page, with conventional links also available. Google began serving AI Overviews in 2025. A conventional search engine can be described as a pipeline—crawl the web, index what was crawled, rank what was indexed, then render a results page—and the generated summary operates above the output of that pipeline. Nobody outside Mountain View can inspect Google’s internals, so the honest engineering claim stops at that boundary. But the districts have demonstrated that the summary can be suppressed at the output layer while the underlying search remains in place. Chris Phillips, Google’s vice-president for education, told *The New York Times* that “Search and AI are deeply integrated”; under the configuration he described, a school that blocks AI will find its students “will not have access to search.” To the extent that “deeply integrated” is offered as a reason customers cannot have search without AI, it is a negotiating position wearing an engineering costume. Disabling a feature changes what a product shows; removing a dependency changes what remains available.

To be fair, Google has identified a genuine pedagogical objection: students can use generated answers to “shortcut learning,” and Google has described a “guided learning” tool that would walk students through complex problems step by step rather than simply provide quick answers. The tool is not yet available. It is also true that removing AI does not make search safe. Raw results can expose students to unsafe material, while a summary can sometimes reduce what they encounter. Neither proposition establishes that Google should force generated answers into the classroom. The learning concern is different. Search can return sources; AI Overview can place an answer before the student has assembled and checked them. The dispute is not whether a computer may ever teach. It is whether a vendor’s default settles the pedagogical question for a child across the district without an intelligible answer from the adults responsible for instruction.

The operational demand is simple, and it is not a referendum on pedagogy. Several hundred Google employees signed a petition asking leadership to let schools turn off AI features “without disrupting their ability to use search as a whole.” The petition’s premise is that the people building the search system should also build the separation. That constituency has both standing and technical familiarity with the relevant machinery. In the record before us, Google offered a guided-learning pilot in place of a supported separation, and the pilot answered a different question and did not yet exist. That is not a product decision. It is a refusal with a press kit.

Fairfax County Public Schools in Virginia achieved separation without a supported Google-provided switch: its plug-ins remove AI summaries from student searches while leaving the engine underneath running. LAUSD had already switched off Google’s AI Mode chatbot at the start of the school year while educators and staff retained access; the temporary suspension of AI Overview was another patch. A local filtering plug-in is a workaround, and a temporary suspension is not a product setting a district controls. More importantly, no contractual right to separation is established in this record. It would be a mistake to infer such a right from the plug-in’s technical removability, and it would be an equal mistake to treat the plug-in as durable vendor control: an update can break it. A workaround that survives only until an update is not a contract. It is a countdown. What the two districts establish is separability. What they do not establish is permanence.

Jack Kelanic, LAUSD’s chief information officer, told the board: “We have choices. We can change the default search engine literally overnight.” He is right. A default is a line of configuration, and configuration does not care how large the vendor is. That is also why Kelanic said, “We understand this as a deeper embedding of AI into the education suite,” rather than merely another feature update. LAUSD’s ability to change search engines does not move the documents, rosters, assignments, messages between schools and families or classroom software already inside the suite. It changes a setting; the suite remains.

Google spent years making the classroom useful: free documents, free classroom software, cheap laptops. The years of gifts are how the dependency got built. Cory Doctorow’s four-stage account of enshittification runs from being good to users, through abusing users to benefit business customers, to abusing business customers to claw value back for the platform, and finally to collapse. The complete sequence is not proved here, and pretending otherwise would be bad analysis. What is proved is the opening mechanism. Google bundled a product parents and teachers did not ask for into a service schools cannot easily leave, on hardware whose settings belong to the administrator. The extraction has begun, and it is being invoiced to children. Here the bill is not chiefly money. It is control over the first interface through which a child encounters an answer.

The arrangement has the shape of chokepoint capitalism, as Cory Doctorow and Rebecca Giblin describe in *Chokepoint Capitalism: How Big Tech Became the Gatekeeper of the Internet and the Great Disconnect* (2022): an intermediary sits astride a route of access and can impose terms on the people on either side. In the stack described here, Google is the dominant education-technology supplier. The school is responsible for instruction; the child is expected to learn. If the generated answer becomes the first route through the suite, the provider can shift control over what appears from its own design to the customer’s acceptance, while the customer absorbs the educational consequence. The price can remain zero. Decision authority still has a price, and the district is paying it.

Lina Khan’s “Amazon’s Antitrust Paradox,” 126 *Yale Law Journal* 950 (2017), offers a way to read this without pretending an antitrust case has already been proved. Khan’s point is not that dominance must always produce an immediately visible increase in price. It is that a platform’s control can be exercised through non-price terms: what suppliers can do, what competitors can reach and what exit costs they bear. Here the buyer is a public school district whose alternatives are constrained by hardware, documents, classroom workflows and procurement rules. The non-price harms are reduced control over what students search, administrative work spent patching the suite and the lost opportunity to have students inspect sources. Whether a particular bundling arrangement satisfies legal scrutiny is a separate question. The bargaining asymmetry is already operating in classrooms.

Tim Wu’s *The Master Switch* (2010) warns that communications systems change not only technically but politically: when control moves from open networks toward private gateways, the gatekeeper gains power over what can be reached. A school search page is not a broadband backbone, and there is no reason to pretend otherwise. The institutional geometry becomes visible when a district cannot obtain the service it wants without accepting the service it has rejected. One provider now decides both which results students can find and whether finding them can happen without a generated layer. Canadian districts use the same Chromebooks, Google Docs and Google Classroom, so they inhabit the same dependency. The Canadian version is the same sentence in a provincial boardroom: procure ordinary search without the generated layer, or change the suite.

That history has a name. Plugging a new thing into an existing product against the maker’s wishes is adversarial interoperability, Doctorow’s term for using reverse engineering, bots or alternate clients to make a product work without the owner’s permission. In *The Internet Con: A Corporate Manifesto* (2018), he puts the history bluntly: “Every pirate wants to be an admiral.” Doctorow describes companies reaching power partly by reading rivals’ file formats, scraping their networks and accepting interoperability with products and services they did not control. Once dominant, firms used law and contracts to close the same routes to competitors. That is the historical asymmetry: the current incumbent gets to call an interoperating tool theft while its own position may rest on interoperability it once lacked the power to forbid. The admirals wrote the laws after learning what the pirates could do.

The laws deserve one precise sentence. [17 U.S.C. § 1201](https://www.law.cornell.edu/uscode/text/17/1201), part of the Digital Millennium Copyright Act, makes circumvention of a technological protection measure unlawful in covered circumstances; subsection (b) makes trafficking in circumvention tools a federal offense when the statute’s design and knowledge conditions are met. The [Electronic Frontier Foundation’s DMCA record](https://www.eff.org/issues/dmca) documents the long use of anti-circumvention law against repair and independent interoperability. Fairfax’s plug-ins filter an output; they do not defeat an access control. Nothing in the record identifies that filtering as circumvention. Technical coupling and legal illegality are separate questions, and the Fairfax intervention shows why they must remain separate: a customer can remove a generated layer without claiming a licence to defeat a digital lock.

My father kept a shelf of repair manuals in the workshop in Selkirk, for machines their manufacturers would sooner have had people replace than open. He spent thirty years as a journeyman millwright on the bar mill at Manitoba Rolling Mills. When Gerdau bought the mill in 1995, he kept his job while several uncles did not. The lesson is narrower than a slogan about modernization: a tool can make work faster while making the worker less able to question it. His instinct was simple. The machine is yours, so the fix is yours to make. A school system cannot outsource the diagnosis of a system it is required to make safe.

It is true that exit is harder than Kelanic’s sentence makes it sound, in the narrow sense in which every honest accounting of switching costs is true. No superintendent dislodges a suite in a weekend. The documents, rosters, homework, institutional habits and messages between teachers and families were moved inside the vendor’s walls one school year at a time. But the tie does not hold because untying it is technically impossible. LAUSD untied one strand over a weekend, and the sky held. A default is a line of configuration. The dependence was built through choices; it can be dismantled through choices.

None of this requires pretending that a generated answer is always wrong or that ordinary search is inherently safe. If LAUSD’s safety rationale concerns its existing filtering stack rather than the mere presence of artificial intelligence, the useful disclosure is which filtering controls changed and what content the system was exposed to. The district’s public disclosure does not say. Parents and teachers have already [challenged Google’s classroom AI controls](/articles/2026-11-09-parents-and-teachers-challenge-google-classroom-ai-controls/), and New York and Los Angeles have announced one-year moratoriums on student use of generative artificial intelligence: New York’s covers elementary and middle school, while Los Angeles’s covers school devices across K-12. The dispute is not whether a computer may ever teach. It is whether a vendor’s default gets to settle the pedagogical question for children across a district without an intelligible answer from the adults responsible for them.

The benefit split is not difficult to see. Google keeps Search at the centre of the classroom and the generated layer inside the suite schools use. The district gets familiar productivity software and administrative convenience. Students get generated answers and less room to inspect the sources. Adults set policy on the devices; Google sets the architecture of the product they cannot purchase without accepting its new centrepiece. Google employees’ petition matters because it shows that this is not merely an argument over one checkbox. It is about who controls what a child receives when the child asks a question.

The deadline that matters is the next contract renewal. Districts should require every generated-answer layer to be switchable off without switching off ordinary search, with dated notices, auditable change records and student work readable by independent tools. No such right is established in this record, but a contract can create one. These are transparency and interoperability rules—changes that are visible and tools that can work with one another—not a ban on artificial intelligence. They make the tool answerable to the school and the child it serves.

Fairfax has shown that the separation can be built. LAUSD has shown that a large district can test one quickly. A local filter is not permanence, but it proves the coupling is a choice rather than physics.

The switch can be built. No contractual right to require it is established in this record; contracts can create one. The lever was never missing. Google captured the interface, and we mistook the default for the machine.

## Sources

### src_001 — Main Street Independent, other, Tier 1, originating
**Title:** ## Los Angeles schools disable Google AI summaries on district devices
**URL:** https://mainstreetindependent.com/articles/2026-11-27-los-angeles-schools-disable-google-ai-summaries-on-district-devices/
