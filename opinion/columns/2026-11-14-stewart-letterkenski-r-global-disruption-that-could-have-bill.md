---
headline: Microsoft Holds the World's Hospitals, Courts, and Payrolls Hostage
publish_date: '2026-11-14'
lede: Microsoft holds the world's hospitals, courts, and payrolls hostage to one company's uptime.
pen_name: stewart-letterkenski
primary_entities:
- Microsoft
- Australia
- Australian Computer Society
- Australian Medical Association
- ASIO
- Service NSW
- United Kingdom
- Japan
primary_themes:
- Technology
- Business
- Government services
- Infrastructure resilience
topic_tags:
- computing and information technology
- disaster
- economy
storyline_nexus: []
floor_values_engaged:
- value: human_life_and_dignity
  intensity: 0.9
- value: accountability_of_power
  intensity: 0.9
- value: informed_citizenship
  intensity: 0.9
framework_version: 1.1.0
generation_timestamp: '2026-11-15T00:38:14-08:00'
source_cluster_id: cluster_guardian_2026-11-13_r-global-disruption-that-could-have-bill
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
- slug: 2026-11-14-microsoft-outage-disrupts-services-worldwide-for-about-18-hours
  relation: extends
  strength: 0.9377
  confidence: high
draft: false
backlog_release: true
---

Microsoft holds the world's hospitals, courts, and payrolls hostage to one company's uptime. For roughly eighteen hours beginning Friday morning, the hostage-taking was visible: some Australian facilities went back to paper for scripts because the software that issues them needed Microsoft's servers to confirm who was holding the pen; courts in South Australia and Victoria lost their email; Service NSW asked people to delay visiting its service centres; schools across the country were affected; federal departments including national security agencies were affected; and US government offices, including congressional ones that live in Outlook, stopped working. Mike Burgess, who runs the domestic spy agency ASIO, reported that its systems "operate on multiple levels" and had been affected "on one level, yes, but not completely" — a sentence you do not want to read about an intelligence service on a Friday. Several British police forces urged people to phone instead of reporting crimes online; in Japan, Sagawa Express could not take online reservations for some services and Taisho handled orders by phone. The disruption ran well past Microsoft's own recovery clock — [our coverage had already tracked it past twenty-two hours across more than seventy countries](/articles/2026-11-13-microsoft-outage-lasts-more-than-22-hours-as-issues-reported-in-more-than-70-cou/) — and the costs in Australia alone are expected to run into the billions of dollars, with warnings that smaller firms will close. Microsoft said it was "deeply sorry," had "addressed the underlying issue," and that the event was a "technical issue," not related to cyber-attacks or AI agents.

It is true that, in the narrow sense in which such statements are usually accurate, that is what happened. The trouble is that "technical issue" names the mechanism and leaves the arrangement alone, and the public discourse has the misleading habit of treating "the cloud" as weather. Microsoft 365 is not weather. It is a single control plane Microsoft owns — one operator, one change domain, one door — that decides whether you may open your mail, sign your prescriptions, file your brief, or run your payroll. On Friday the hospital still had power, the court still had a roof, the payroll numbers still existed somewhere — and none of it could be reached, because permission to reach any of it lived on someone else's computer, and that someone pushed a settings change that jammed the door. The mistake is the small story. The blast radius is the design.

The detail that should follow this outage into every procurement meeting on earth came from Dr Michael Bonning, the Australian Medical Association's president, explaining why some facilities had returned to using paper for scripts: authentication into prescribing software requires multifactor verification, and multifactor verification requires access to your Microsoft-supported email. So the prescribing system never had an identity of its own. It borrowed one — from the vendor, on the vendor's schedule. When the vendor's settings moved, the hospital's front desk discovered that everything behind it was running on borrowed credentials, and routing the second factor through the same vendor that hosts the first is not good practice; it is a lock whose spare key is kept under the doormat of the same house. The AMA reported no impacts on patient care, because paper held and nurses and pharmacists made it hold. The most reliable piece of technology in the building turned out to be a piece of paper, which does not log in to anything.

It is true that Ashwin Pal of RSM Australia earned his flabbergast — "I'm a technologist and I'm actually flabbergasted as to how something like this could have happened … they pushed out a change which should have been tested" — and pushing an untested change at a control plane is operations malpractice at any scale, which is also a remarkably low bar. The trouble is that the testing failure is the least interesting thing that went wrong. The more interesting thing Pal reported is that many businesses had no fallback at all, and that a protracted event "can easily be the straw that breaks the camel's back for smaller entities." A small business that cannot invoice, cannot collect, and cannot reach a government service for eighteen hours is not an outage anecdote; it is a solvency event. Redundancy is a cost centre, and a cost centre is not what a procurement office buys by default. The vendor sells the remedy for the fragility the vendor's concentration produces, and the remedy is more vendor. That is the racket — not the outage, which is ordinary, but the arrangement that makes the outage everyone's problem and the recovery somebody else's property.

The pattern has a name, and Cory Doctorow coined it: enshittification — the four-stage decay by which a platform is first good to its users, then good to its business customers, then strips value from both for itself, then dies. What the four stages track is not greed but the removal of constraints, and Friday was a demonstration of all four lying flat at once. Competition: where, precisely, does a hospital take its email? The market is a duopoly, and switching costs are counted in decades of documents, macros, and muscle memory, which is exactly how a duopoly likes it. Regulation: no regulator on either side of the Pacific treats enterprise identity and mail as critical infrastructure; we regulate the wires the offices sit on and leave the offices themselves to the market's tender mercies. Interoperability — the constraint Doctorow calls the most important and the most deliberately destroyed — would have made Friday an inconvenience to route around rather than a lockdown, because portable mail, documents, and identity can be re-homed while the landlord is down. Labour is the force we cannot see from outside, which is precisely the reason it has to be protected by law instead of left to corporate weather.

Bruce Schneier has a name for the arrangement: feudal security. You do not own the defences of the system you depend on, you rent them, along with the right to be told afterwards what went wrong; a tenant does not debug the castle. It is the right frame for this week, because the questions Australia is now asking — which critical systems depend on a single provider, where the backups are, who pays when there are none — are questions a tenant has no standing to ask and no lever to answer. The Australian Computer Society has renewed its call for a federal review of exactly those questions, a request the company's statement does not touch.

Tim Wu's history of the information industries, *The Master Switch*, documents the pattern every medium has followed: an open and chaotic competitive phase, then consolidation, then a single chokepoint — a master switch — that one firm controls and through which everything must pass. The master switch is not a metaphor for Friday. Microsoft 365 is a master switch for administrative life, and it was thrown by accident. Wu's companion argument, in *The Curse of Bigness*, is that scale itself is the hazard: an enterprise large enough that its own testing cannot reliably protect the world from its own changes is not a well-run firm having a bad day. It is a structural risk wearing a lanyard.

Harold Innis taught Canadian political economy that a staples economy — one that ships raw material to a distant metropole and buys back finished goods — is never merely an arrangement of trade; it is an arrangement of dependence, and the dependence organizes everything downstream of it. Prins Ralston, chief executive of the Australian Computer Society, drew the political conclusion the morning forced: the outage "exposed Australia's reliance on foreign technology," and Australians "who couldn't get paid, couldn't send an invoice, or couldn't reach a government service this morning are entitled to be worried." The bundle a government now buys — identity, mail, documents, storage, meetings — behaves like a staple in exactly that sense: produced elsewhere, shipped in, and made the base of everything the local economy does. Ralston's phrase is the staples observation arriving decades late by way of a chief executive instead of an economist. The new staple is administrative capacity itself: invoices, prescriptions, court filings, identities, extracted from a hundred economies, processed in Redmond, and returned on sufferance, reclaimable whenever the metropole misconfigures its own machines. The same dependence sits in Ottawa, which folded federal departmental IT into Shared Services Canada more than a decade ago on precisely the efficiency logic that produced Friday. The review Ralston is asking for should be convened here in the same week. The question is not whether we like Microsoft. The question is which of our critical systems has exactly one door, and who owns the door.

My father spent thirty years as a millwright on the bar mill in Selkirk, and that mill tripped, stalled, and threw rolls often enough that coming back was not an event; it was a shift's routine work. It came back because the knowledge of how to bring it back lived on the floor, distributed across the crew on turn — not in a binder, and not in a control room belonging to somebody else's company. In 1995 Gerdau of Porto Alegre bought Manitoba Rolling Mills; he kept his job, several of my uncles did not, and what changed first was not the steel. It was who the mill answered to. Microsoft 365 was built on the opposite principle from that floor: all the keys, all the knowledge, one room — and the room is in Redmond. Friday was what that principle looks like when the room has a bad morning. The playbook is older than the mechanism, and so are the responses to it — they are simply harder to sell to a procurement office.

It is true that the alternatives carry their own outage histories — Google has locked people out of their documents before, and AWS has taken substantial portions of the internet down with it — and that no operator at this scale has a clean record. It is also true that Microsoft's customers are not fools; the enterprise agreements were signed in good faith, on the theory that one vendor's reliability beats ten vendors' chaos. The trouble is that the remedy for concentration has never been a better concentration, and that the theory priced uptime and never priced dependence. The answer, then, is not a deeper apology; it is rules with exit built in: interoperability and data-portability mandates, so that identity, mail, and documents can move the way ported phone numbers learned to move; procurement law requiring that any system whose failure stops prescriptions, payrolls, or courts carry a fallback that is exercised on a schedule rather than documented in a binder nobody opens; and the Competition Bureau, ours included, asking how the market for the world's back office arrived at one door. Federated identity is the technical term for the arrangement — each organisation authenticates its own people and the service accepts that authentication, rather than one vendor holding the credentials for everyone — and it was designed precisely so that no single company would have to be the front door of everything. None of it requires breaking Microsoft up. It requires making it possible to leave.

The market, meanwhile, has already told us what it thinks the gap between uptime and dependence is worth: eighteen hours of paper scripts, silent courts, and unsendable invoices moved Microsoft's stock 1.1 percent when Wall Street opened, to $516.86 — [our coverage followed the same dip through Maersk, Euronext, and congressional offices](/articles/2026-11-13-microsoft-shares-fall-about-1-as-outage-disrupts-maersk-euronext-house/). Both of those numbers are true. They are not the same kind of number. One is what the outage cost the country; the other is what the market took off Microsoft's price. The rent stream was never in danger. The hostages had signed multi-year contracts.

There is an image from Friday that will outlast the apology, and it is not the share price. It is a doctor with a paper pad, writing by hand because the electronic alternative had to ask Microsoft first whether the hand holding it belonged to a doctor. The hospital kept its patients. Microsoft kept the keys. Eighteen hours settled which of the two was negotiable.

Paper did not go down; it was waiting at the desk, where it always is. A hospital that can prescribe only when a foreign vendor's settings are correct does not have a floor. It has a subscription.

## Sources

### src_001 — Main Street Independent, other, Tier 1, originating
**Title:** ## Microsoft outage disrupts services worldwide for about 18 hours
**URL:** https://mainstreetindependent.com/articles/2026-11-14-microsoft-outage-disrupts-services-worldwide-for-about-18-hours/
