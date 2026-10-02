---
headline: Startups Are Turning Engineering Into a Prompting Exercise
publish_date: '2026-09-22'
lede: Simar Singh cuts engineers by treating an unverified automation claim as a staffing plan.
pen_name: stewart-letterkenski
primary_entities:
- Butternut AI
- Lindy
- Emergent
- Retell AI
- AgentCollect
- Y Combinator
- Cowboy Ventures
- First Round Capital
- LinkedIn
- Simar Singh
- Haneen Azhar
- John Banner
- Aileen Lee
- Liz Wessel
- Advait Paliwal
primary_themes:
- AI and automation
- Labor market
- Startups and venture capital
- Workforce composition
topic_tags:
- artificial intelligence
- business information
- technology and engineering
storyline_nexus: []
floor_values_engaged:
- value: accountability_of_power
  intensity: 0.3
- value: truthfulness
  intensity: 0.3
- value: equality_fairness
  intensity: 0.3
framework_version: 1.1.0
generation_timestamp: '2026-09-21T19:51:31-07:00'
source_cluster_id: cluster_wsj_2026-09-21_tech-ai-startup-hiring-ai-staffing-8c626
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
- slug: 2026-09-22-some-startups-use-ai-to-cut-head-counts-or-contractors
  relation: extends
  strength: 0.8242
  confidence: high
draft: false
---

Simar Singh cuts engineers by treating an unverified automation claim as a staffing plan.

It is true that a small company can now do more with fewer people, in the narrow sense that code-generation systems can produce useful drafts, tests, documentation and routine integrations at a speed no junior team can match. The trouble is that a draft is not a system, and a system that can produce an answer is not necessarily a system that can be trusted with a customer.

The Wall Street Journal’s reporting describes a genuine change in startup staffing. Butternut AI fell from nine employees to four after Singh and his co-founder concluded that AI agents could replace five engineers. Lindy laid off marketing staff, stopped using five outside creative agencies and kept its marketing team at two people while adding AI tools. AgentCollect reduced its staff from 50 to about 30 after automating billing coordination, call-quality evaluation and product-management work.

The LinkedIn comparison is suggestive but not dispositive. Startups founded in 2022 with at least five employees in their first year averaged 20.7 employees by year three, compared with 32.5 for similarly sized startups founded in 2018. That is a large change. It does not establish that AI caused the change, still less that the missing twelve workers were replaced by equivalent software. Interest rates, venture funding, business models and the general fashion for avoiding payroll all sit inside the number.

The owner claims therefore require a technical reading. When Singh says AI agents replaced five engineers, what did those engineers actually do?

A software engineer is not a person who types code into a repository. The work includes turning an ambiguous customer requirement into a specification, selecting an architecture, deciding which failures are acceptable, reviewing generated code, writing tests that expose incorrect assumptions, managing data and permissions, deploying changes, monitoring production and deciding what must not be automated. A coding agent can assist with several of those tasks. It does not follow that it can own the entire chain.

Butternut builds no-code websites. An agent in that environment might generate a component from a prompt, translate a request into a database schema, repair a failing build, or suggest a change to a template. Those are useful operations. They are also bounded operations. The question is whether the agent can preserve state across a long project, distinguish a customer’s desired behaviour from an unsafe shortcut, write tests for requirements that were never stated, and stop before it changes data that cannot be recovered.

The published account does not tell us which of those things happened. It does not identify the five engineering functions removed, the tests the agents run, the deployment permissions they hold, the rate at which their output is rejected, or the number of production incidents that remain for the four employees to handle. Without that information, “replaced five engineers” is a staffing description, not an engineering result.

The remaining four may be doing excellent work. They may also be supervising a large collection of generated fragments, correcting failures after customers encounter them, and carrying the architectural knowledge that the departed team used to distribute. Those are not equivalent arrangements. A smaller payroll can mean higher productivity. It can also mean that review, incident response and maintenance have been compressed into the founders’ evenings.

This is the part of the AI staffing story that the phrase “AI can do the work” conceals. The system is not a black box that takes an employee in one side and produces a finished product from the other. It is a loop: instruction, generated output, test, review, correction, deployment and monitoring. Every arrow in that loop is a place where labour, judgment and failure remain.

Lindy’s “AI teammate” makes the same point more clearly because it works inside Slack. An integration of that kind does not possess a general view of the company. It receives the messages, files and channels permitted by its authorisation, retrieves material according to whatever indexing and ranking system the company has built, and invokes the actions its tools allow. A Slack assistant with permission to read a support channel is not the same thing as an employee who understands the customer, the contract and the history of the problem.

The difference matters when a message is ambiguous or adversarial. A customer escalation may be buried in a busy channel. A pasted document may contain instructions aimed at the model rather than the employee. A model may summarise a disagreement while dropping the one sentence that changes the legal or commercial meaning. A tool connected to ticketing, billing or deployment systems may turn a mistaken interpretation into an external action. These are not philosophical objections. They are ordinary interface and permission failures.

The relevant engineering questions are straightforward. Which Slack scopes can the agent use? What data enters its retrieval index? How are tenant boundaries enforced? Can a message cause it to ignore higher-priority instructions? Are tool calls logged and reversible? Who reviews an action that affects a customer? What happens when the model is confidently wrong? The Journal’s reporting does not answer these questions, so Lindy’s claim that two marketers and AI helpers cover the old “surface area” should be treated as a claim about coverage, not proof of equivalent work.

The same caution applies to the five creative agencies Lindy no longer uses. AI video generation can produce scripts, storyboards, synthetic narration, captions, rough cuts and variations of an advertisement. That may replace a great deal of repetitive production. It does not tell us whether the output has the factual accuracy, brand consistency, accessibility, rights clearance and editorial judgment those agencies supplied. The record does not say what Lindy now produces, how often people reject the generated work, or who checks it before publication.

The distinction is not an appeal to preserve every old workflow. If a model can generate a competent first cut and a person can approve it in minutes, refusing the tool would be wasteful. But the quality bar has to be named. “We covered all the surface area” is not a specification. It is what a specification sounds like before anyone writes down the failure conditions.

AgentCollect’s example makes the operational risk harder to avoid. Billing coordinators, call-quality evaluators and product managers perform different functions. Automating invoice collection might involve reading account records, classifying payment status, sending notices and escalating exceptions. A system can hallucinate an invoice status, misread a disputed charge, send the wrong message to a customer or fail to escalate an account that falls outside its training examples. Call-quality evaluation can misclassify a legitimate conversation because the transcript lacks tone or context. Product management can turn a customer request into a feature that solves the wrong problem very efficiently.

None of those failure modes proves that AgentCollect’s system has failed in that way. The point is narrower: a head-count reduction does not establish that the removed functions disappeared. It establishes that the company chose to assign their risks elsewhere—to software, to the remaining staff, or to customers who discover the error first.

Cory Doctorow’s account of AI as labour discipline is useful here, provided it is not allowed to replace the technical analysis. The system does not need to perform every task reliably to change hiring. It only needs to make the owner believe that supervision is cheaper than employment. That belief can be correct in a narrow workflow and reckless when extended across the whole organisation.

Y Combinator is turning the narrow case into a portfolio story. Emergent reached $15 million in annualized revenue with 15 people; Retell AI reached $60 million with about 40. Those are real operating results, and a small company can plainly build a valuable product. They do not reveal how much work is performed by founders, contractors, customers, unpaid early adopters, model vendors or the infrastructure companies supplying the compute. Nor do they reveal whether the companies can maintain the same service when the founders stop personally reviewing every important output.

Aileen Lee’s qualification is therefore the important one. A two-person team can prototype and test a product before hiring. Enterprise customers paying $60,000 or $75,000 also want humans who can answer for the product. That is not sentimental resistance to software. It is a demand for a responsible party when the software reaches the edge of its specification.

Advait Paliwal’s “Codex as chief technology officer” is the purest version of the claim, and the easiest to misdescribe. Twenty Claude and Codex subscriptions can generate code, explain an error, propose a refactor and produce a working prototype. They do not set the service’s reliability target, choose its data-retention policy, determine its threat model, negotiate its dependencies or accept responsibility when a generated change corrupts production data. Calling the subscription a chief technology officer turns a collection of tools into an office with no decision rights.

The engineering question is not whether generated code can compile. It is whether the system has an owner for architecture, security, testing, operations and failure response. If that owner is Paliwal, then the human work remains; it has been concentrated in one person. If nobody owns it, the company is not lean. It is undocumented.

The column’s [earlier account of large companies rehiring after automation disappointed](/articles/2026-07-27-major-u-s-companies-resume-hiring-as-ai-limits-become-clear/) supplies a useful counterexample, but not a comfort. A large company can restore a team after a failed experiment. A four-person startup has less slack, fewer independent reviewers and a smaller margin for one bad deployment. The cost of being wrong is not removed by having fewer employees. It is assigned to someone else.

The same assignment appears in the résumés of job seekers, who are [adding AI terms because they can see the new screening gate](/articles/2026-08-13-u-s-job-seekers-add-ai-terms-to-r-sum-s-as-employer-demand-shifts/). Applicants are adapting to a system that may later decide the tools are less capable than advertised. The employer has already captured the benefit of the uncertainty: fewer people are hired while the test is still running.

A tradesman’s question applies to this new machinery: where is the inspection point? In a workshop, removing a worker does not remove the torque specification, the safety check or the person responsible when the assembly fails. Software businesses can obscure those steps because the output arrives as text, code or video rather than as a visibly misaligned part.

The remedy is not to preserve every job title as a ceremonial object. It is to require a legible chain of responsibility: documented permissions, reproducible tests, human appeal for consequential decisions, incident records and a clear account of who bears the cost of failure. Open interfaces and portable data would also let a company change model vendors without rebuilding its entire operation around one provider. Worker voice matters for the same reason: the people reviewing generated systems are often the first to see where the specification is false.

The lean startup can be a real engineering achievement. It can also be a method for moving review, maintenance and risk outside the payroll. The difference is not visible in the org chart. It is visible in the tests, the logs, the permissions and the person who answers when the invoice is wrong.

A company can remove the worker. It cannot remove the work; it can only hide where the work went.

## Sources

### src_001 — Main Street Independent, other, Tier 1, originating
**Title:** ## Some startups use AI to cut head counts or contractors
**URL:** https://mainstreetindependent.com/articles/2026-09-22-some-startups-use-ai-to-cut-head-counts-or-contractors/
