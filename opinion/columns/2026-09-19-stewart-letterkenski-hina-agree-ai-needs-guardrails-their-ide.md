---
headline: Washington Wants AI Guardrails It Refuses to Write
publish_date: '2026-09-19'
lede: The Trump administration leaves AI safety rules unwritten while demanding China discuss them.
pen_name: stewart-letterkenski
primary_entities: []
primary_themes: []
topic_tags: []
storyline_nexus: []
floor_values_engaged: []
framework_version: 1.1.0
generation_timestamp: '2026-09-18T00:49:09-07:00'
source_cluster_id: cluster_wsj_2026-09-17_hina-agree-ai-needs-guardrails-their-ide
gdelt_event_ids: []
consensus_floor_version: v0.3.0
publication_mindspec_version: v0.3.0
license: https://creativecommons.org/publicdomain/zero/1.0/
ai_disclosure: This article was generated algorithmically by Main Street Independent from the public sources listed in its Sources section.
ai_generated: true
sources:
  count: 0
  outlets: []
  outlet_classes: []
  has_originating: false
  has_primary_document: false
figures_aggregate:
  count: 0
  series_ids: []
  sources: []
cross_article_links:
- slug: 2026-09-18-trump-xi-to-discuss-ai-safety-at-washington-summit
  relation: extends
  strength: 1.0
  confidence: high
draft: false
backlog_release: true
---

The Trump administration leaves AI safety rules unwritten while demanding China discuss them.

The narrow truth is that Washington and Beijing have identified overlapping risks. Both governments are concerned about powerful systems assisting cyberattacks, spreading influence operations, or helping people build weapons. Both also appear willing to discuss some form of bilateral process. The trouble is that “AI safety” names different engineering and political problems in the two systems, and neither side has yet shown that it can separate them.

President Donald Trump and President Xi Jinping are expected to discuss artificial intelligence at next Thursday’s Washington summit. Treasury Secretary Scott Bessent is to meet He Lifeng, Xi’s top economic official, in New York beforehand. The Wall Street Journal reports that the two governments are approaching the subject from sharply different premises: the United States has focused on keeping powerful systems under human control, while China has focused on protecting Communist Party rule.

Those are not interchangeable meanings of safety.

Chen Yixin, China’s minister of state security, warned in a party publication that AI could “systemically affect the political-security environment” by enabling mass-produced rumours, “cognitive warfare” and unrest. His proposed answer was “party management of the internet and party management of data.” That is a documented political-control programme, not a neutral technical safeguard. It treats dissent, hostile influence and ordinary disagreement as problems to be managed by the ruling party.

The technical concern underneath it is nevertheless real. A model that can generate persuasive text, target audiences, probe software for weaknesses or automate influence campaigns can alter the information environment at a scale that a human operator could not manage alone. The question is not whether the Party should control the answer. The question is what the system can do, who can operate it, what records exist of its operation, and who has the power to correct an abuse.

The Great Firewall illustrates the distinction. It controls what users can access and what information can circulate inside China. It does not, by itself, prevent an autonomous system from probing networks, discovering vulnerabilities or generating influence material. A filter at the edge of a network is not the same component as a control on a model’s capabilities or permissions. One regulates access to information; the other constrains what a computational system can execute.

That distinction matters because the current debate keeps collapsing several layers into one word. “AI” can mean model weights, training data, a hosted application, an interface, a data centre or a government deployment. Those are different parts of the stack with different failure modes. A model may be open at one layer and closed at another. A system may publish its weights while withholding training data, evaluation methods or the infrastructure needed to reproduce the result. Calling such a system “open” without specifying the layer is a marketing claim, not an engineering description.

The difference between closed and open-weight models is more concrete than the summit rhetoric suggests. OpenAI and Anthropic keep their most capable models behind controlled interfaces. Users send prompts to a provider’s infrastructure and receive outputs through a paid gateway. The provider retains control over access, rate limits, logging, model updates, monitoring and suspension. That arrangement can make it easier to restrict certain uses and to investigate incidents. It also makes the public dependent on a company that can change the model, conceal its evaluations and withdraw access without giving users a portable copy of the system.

An open-weight model changes that control surface. If the weights can be downloaded, researchers and developers can run the model locally, inspect its behaviour more directly, fine-tune it for particular tasks and build applications without asking the original provider for permission. That can lower costs and widen competition. It can also remove the provider’s ability to revoke access or apply a single central filter after distribution. The model’s availability becomes harder to contain, and its misuse becomes harder to attribute to one service operator.

Neither architecture is automatically safe. A closed API can be monitored and still be opaque, commercially dependent and difficult to audit. An open-weight release can support independent testing and adversarial research while also making powerful capabilities easier to copy and deploy. The relevant questions are operational: what capabilities are present, what safeguards sit around them, what evidence supports the safeguards, and who bears the cost when they fail.

DeepSeek’s open-weight releases therefore deserve analysis rather than a patriotic label. The source material reports that Chinese analysts view distribution as a way to spread Chinese AI worldwide and blunt American efforts to contain it. That is a plausible strategic use of an open-weight architecture. It does not follow that openness is propaganda, nor that closed access is responsible governance. The architecture distributes capability and reduces dependence on one provider; it does not settle the political question of who governs the resulting systems.

Washington has its own unresolved problem. The administration has played down the need for regulatory guardrails, while prominent American AI executives have called for slowing development to weigh safety concerns. The important issue is not whether an executive sounds cautious at a hearing. It is whether a model’s deployment is subject to enforceable requirements for testing, incident reporting, access control, security review and redress.

A company-controlled API is not self-regulation merely because it has a login screen. It is a private governance system. Its operator decides which uses are permitted, what evidence is disclosed, how failures are classified and whether affected people can appeal. Those choices may reduce some risks while protecting the company from liability or scrutiny. A public rule can constrain that discretion; a press release cannot.

The 2023 United States-China AI dialogue offers a smaller but useful warning. The Biden administration opened a formal channel, and Beijing placed its foreign ministry in charge rather than a technical body. According to officials involved at the time, that limited the substance of the exchange. The lesson is not that diplomacy is pointless. It is that a meeting is not a safety mechanism. A diplomatic channel without technical authority, defined evidence standards and procedures for reporting incidents will produce a communiqué, not control.

The Cold War analogy is useful only up to a point. Robert Hormats has argued that the United States and Soviet Union built increasingly powerful weapons while also negotiating rules to avoid mutual catastrophe. That history demonstrates that rivals can establish limited procedures without resolving their political hostility. It does not demonstrate that AI can be governed by copying the language of nuclear arms control. Nuclear weapons are discrete state-controlled arsenals. AI capabilities can be replicated through software, embedded in commercial services, distributed through open weights and improved by thousands of actors outside formal government programmes.

The United States also has less authority over its own AI system than its summit language implies. Its leading laboratories are private firms. Its government can regulate them, fund them, restrict their exports or condition access to public infrastructure, but it cannot honestly present their internal choices as national policy until those choices are made answerable to public rules. China’s model is different but not cleaner. Party control may impose a unified command structure, yet it also turns “safety” into protection of political supremacy and removes independent channels for reporting abuse.

A workable dialogue would begin by refusing the convenient word. Washington and Beijing should identify the particular system under discussion: frontier-model evaluations, cyber capabilities, autonomous weapons, model-weight distribution, data-centre security, influence operations or political censorship. Each government should publish the incidents and failure conditions it wants addressed, designate technical bodies with authority to inspect evidence, and establish reporting procedures that do not depend on the goodwill of the companies or parties being examined. Open-weight and closed models should be assessed by what users can do with them, what operators can prevent, and what victims can do after something goes wrong.

There is a public difference between a model that cannot be independently inspected and a party that cannot be independently challenged. The two may both use the language of control, but the systems do different things. Engineering begins by keeping those differences intact.

A summit can name a guardrail. It cannot make one hold.
