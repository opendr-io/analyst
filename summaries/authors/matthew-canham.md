# Topic: Author: Matthew Canham

## Executive Summary

The three records attributed to Matthew Canham present a tightly connected research trajectory around **cognitive security**, **AI-mediated social engineering**, and the expanding attack surface created by **LLMs, AI agents, human digital twins, and human-autonomy teams**. Across the records, Canham’s work frames AI security not mainly as a software-only problem, but as a problem of **human perception, cognition, trust, agency, and decision-making under manipulation**.

The 2025 Black Hat talk coauthored with Ben D. Sawyer, “Evil Digital Twin, Too,” argues that large language models exploit human cognitive vulnerabilities and that human digital twins trained on individuals’ interaction patterns enable scalable manipulation, social engineering, and “persistent cognitive cyberwarfare” [record_id:93]. A 2025 BSidesLV talk, “Human Attack Surfaces in Agentic Web,” extends this concern to the emerging “Agentic Web,” where AI agents increasingly mediate online tasks and create bot-vs-bot exploitation scenarios affecting human users indirectly [record_id:2466]. A 2026 BSidesLV talk, “Putting the CAT in the HAT,” formalizes the area further with a “Cognitive Attack Taxonomy” applied to human-autonomy teams, defining cognitive hacking as exploitation of psychophysical, neuroergonomic, and psychosocial limitations to degrade, deny, or deceive decision-making [record_id:2779].

Collectively, the records suggest that Canham’s distinctive contribution is a **human-centered and systems-oriented reframing of cybersecurity**: the relevant attack surface is not only networks, endpoints, models, or applications, but also the cognitive systems that interpret information and make decisions. The evidence base is limited to talk abstracts, so the records reveal themes, claims, terminology, and proposed frameworks more than detailed empirical results. Still, they show a coherent progression from warning about LLM-enabled manipulation, to agent-mediated exploitation, to a broader taxonomy for cognitive attacks in hybrid human-AI systems.

## Research Landscape

The included records are all conference talk abstracts from security events, spanning 2025 to 2026. Two are from BSides Las Vegas, and one is from Black Hat USA. The records are not papers, slide decks, transcripts, or tool repositories; they are promotional or program descriptions. As a result, they provide strong evidence for the **topics Matthew Canham publicly presents on**, the terminology he uses, and the conceptual problems he emphasizes, but weaker evidence for implementation details, experimental validation, or technical findings.

The landscape is dominated by **AI security as it intersects with human factors and social engineering**. The records place Canham’s work adjacent to topics such as prompt injection, jailbreaking, governance, risk, compliance, cybercrime, fraud, social engineering, and threat modeling. However, the raw abstracts emphasize a broader conceptual framing: **cognitive attack surfaces** and **cognitive security**. Rather than focusing narrowly on model exploitation, the talks treat LLMs and agents as catalysts for new forms of manipulation at scale.

The 2025 Black Hat record is framed as a follow-up to an earlier 2023 talk titled “Evil Digital Twin.” It states that the original talk warned that LLMs were exploiting users’ cognitive vulnerabilities and that people would perceive AI as sentient long before true AGI emerged [record_id:93]. The 2025 follow-up claims that the situation had escalated and that many predictions had become realities, especially around human digital twins and AI-enabled social engineering [record_id:93]. This record positions Canham’s work as partly predictive and partly retrospective: it revisits claims from a prior talk and argues that real-world developments have validated them.

The BSidesLV 2025 record shifts the focus from LLMs and human digital twins to **AI agents** and the “Agentic Web.” It describes a future in which machines dominate creation, interaction, and consumption online, with agents performing tasks such as buying goods and services, searching for jobs and homes, and even seeking relationships on behalf of users [record_id:2466]. In this setting, the attack surface includes not only humans directly consuming deceptive content, but also agents acting on humans’ behalf and being exploited by malicious agents [record_id:2466].

The BSidesLV 2026 record is more formal and taxonomic. It defines the “cognitive attack surface” as vectors through which a system’s information-processing capacities can be manipulated without informed consent, and it defines “agentic systems” broadly to include human, artificial, and organizational entities capable of perceiving information and exercising agency [record_id:2779]. It introduces or updates the Cognitive Attack Taxonomy, Version 2.0, and applies it to human-autonomy teams [record_id:2779]. This suggests a movement from descriptive warning to structured threat modeling.

## Major Themes And Trends

### Cognitive security as an extension of cybersecurity

The central theme across all records is that cybersecurity must expand to address **cognitive security**. Canham’s talks repeatedly move the locus of compromise from infrastructure alone to the human and hybrid systems that process information. The Black Hat abstract says the attack surface is shifting “from networks to minds” and argues for defensive posture that protects “not just digital systems, but the systems that underpin civilization and the human beings they serve” [record_id:93]. The BSidesLV 2025 abstract similarly says the near future of cognitive security will involve “an unrelenting cascade of attack surfaces” as AI agents become common intermediaries in online life [record_id:2466]. The BSidesLV 2026 abstract then defines cognitive attack surface in more general terms as manipulation of information-processing capacities without informed consent [record_id:2779].

This theme gives Canham’s work a clear orientation: AI security is not only about preventing unauthorized code execution, data leakage, or model misuse. It is also about protecting **perception, interpretation, trust, decision-making, and agency**. That framing appears consistently across all three records.

### AI systems as amplifiers of social engineering and manipulation

A second major theme is that AI reduces the cost and increases the scale of deception. The Black Hat talk states that “longitudinal interaction data” enables low-cost social engineering labor and high-power AI-human hybrid attacks [record_id:93]. It also warns of “persistent cognitive cyberwarfare” as the “cost of deception approaches zero” [record_id:93]. The BSidesLV 2025 talk extends this by describing scammers unleashing agents to exploit the agents of unsuspecting humans in “bot-vs-bot warfare” [record_id:2466].

The records suggest a trend from traditional social engineering, where humans deceive humans, toward **automated or semi-automated social engineering ecosystems**. In this view, LLMs, agents, and digital twins are not merely tools for composing phishing emails; they are infrastructure for continuous, personalized, context-aware manipulation. The evidence for this trend in the records is conceptual and forecast-oriented, but it is repeated strongly across the abstracts.

### Human digital twins and simulated persons

The 2025 Black Hat record introduces the idea of **human digital twins** as a central concern. It describes HDTs as systems “trained on the core patterns of human individuals” and says they are being deployed at scale to simulate workflows and relationships [record_id:93]. The abstract promises audience interactions with a human digital twin of a Supreme Court justice and a “perfect AI assistant for insider threat,” as well as a NIST research-based LLM that speaks in phishing emails [record_id:93].

This record suggests that Canham’s research interest includes not only generic conversational AI, but also **personalized AI replicas or simulations** and their implications for manipulation, deception, insider threat, and trust. The record links HDTs to competitions of manipulation and deception in research with the US Military Academy at West Point, where humans and human digital twins are pitted against one another [record_id:93]. The abstract does not provide study methods or results, but it indicates a research direction involving adversarial comparison between humans and AI-generated human representations.

### The Agentic Web and indirect exploitation

The BSidesLV 2025 record adds a distinct but related theme: the rise of the **Agentic Web**, where machines increasingly create, interact with, and consume online content [record_id:2466]. In this scenario, agents will perform consequential tasks for people, including commerce, job search, housing search, and relationships [record_id:2466]. This creates risks because attackers may exploit not only people, but the agents that represent people.

This is a notable shift in threat model. In conventional web security and social engineering, the human user is often the target of deceptive content. In Canham’s Agentic Web framing, the user’s agent becomes both a delegate and a new attack surface. Scammers may deploy their own agents against benign agents, leading to “bot-vs-bot warfare” [record_id:2466]. The human remains affected, but the immediate interaction may occur between software agents. This introduces questions about authorization, user intent, trust boundaries, agency, and accountability.

### From warning to taxonomy

Across the three records, there is an apparent progression in maturity of the framing. The Black Hat 2025 talk is a “two year check-in” on warnings from a 2023 talk, using language of escalation, prediction, and emerging reality [record_id:93]. The BSidesLV 2025 talk forecasts near-future scenarios involving agents and online life [record_id:2466]. The BSidesLV 2026 talk introduces an updated Cognitive Attack Taxonomy Version 2.0 and maps it to human-autonomy teams [record_id:2779].

This progression suggests that Canham’s work is moving toward **formal threat modeling for cognitive attacks**. The 2026 record defines terms and organizes attacks across four layers: Structure, Cognitive, Network, and Policy [record_id:2779]. The taxonomy broadens the subject beyond individual users to include “individuals made of flesh, silicon-based agents, a bureaucracy, or a familiar combination of these” [record_id:2779]. This indicates an effort to generalize cognitive threats across humans, AI systems, organizations, and hybrid teams.

### Hybrid human-AI systems as primary security objects

The records increasingly treat security targets as **hybrid systems** rather than isolated humans or machines. The Black Hat record mentions “AI-human hybrid attacks” and research comparing humans and human digital twins in manipulation and deception [record_id:93]. The BSidesLV 2025 record describes humans delegating online actions to AI agents, producing interactions between human interests and machine intermediaries [record_id:2466]. The BSidesLV 2026 record explicitly addresses “human-autonomy teams” and “next generation human-AI hybrid systems” [record_id:2779].

This theme is important for downstream researchers because it implies that Canham’s work is likely relevant to areas such as autonomous systems, decision-support tools, military human-machine teaming, organizational security, fraud prevention, and AI governance—not only to classic prompt-injection or phishing research.

## Methods, Tools, And Approaches Discussed

The records mention several methods, tools, frameworks, and demonstration approaches, though mostly at the abstract level.

The Black Hat 2025 record describes **human digital twins** trained on the “core patterns” of individuals and deployed to simulate human workflows and relationships [record_id:93]. It also mentions demonstrations or audience interactions with a digital twin of a Supreme Court justice, an AI assistant framed around insider threat, and a NIST research-based LLM that speaks in phishing emails [record_id:93]. These examples indicate a demonstration-driven approach: showing how AI systems can imitate, persuade, or operationalize deceptive interaction patterns. The same record references research with the US Military Academy at West Point that pits humans and human digital twins against each other in manipulation and deception competitions [record_id:93]. That suggests an experimental or evaluation-oriented method, though no protocols or results are provided in the abstract.

The BSidesLV 2025 talk focuses on understanding **AI agent mechanics**, economic pressures behind agent adoption, examples of current exploitation, and near-future scenarios [record_id:2466]. The approach appears to combine technical explanation, threat modeling, and scenario analysis. The central methodological move is to treat online agents as both user delegates and adversarial tools, thereby expanding the security model from human-vs-scammer to agent-vs-agent interactions [record_id:2466].

The BSidesLV 2026 record is the most explicit about formal methodology. It defines a **Cognitive Attack Taxonomy (CAT) Version 2.0** and maps cognitive attacks across four layers [record_id:2779]:

- **Layer I, Structure:** physical systems underlying cognition.
- **Layer II, Cognitive:** internal processing and context interpretation.
- **Layer III, Network:** connectedness and trust.
- **Layer IV, Policy:** rules and governance, distinguished from network-level trust by formalized engagements.

The taxonomy is applied to **human-autonomy teams**, meaning systems where humans and autonomous or agentic systems collaborate [record_id:2779]. The record’s example of poisoned dashboard data raises a systems question: if a human’s perception is hijacked through manipulated data, is the human, the machine, or the overall system compromised? [record_id:2779]. This example captures the methodological contribution: cognitive threat modeling asks researchers to locate compromise in the interaction between perception, data, machine interface, and organizational context.

The records do not describe code-level tools, model architectures, datasets, or quantitative benchmarks in detail. The most concrete “tools” are conceptual and demonstrative: human digital twins, agent-based exploitation scenarios, a phishing-email-speaking LLM, and the CAT framework [record_id:93] [record_id:2466] [record_id:2779].

## Notable Talks, Records, And Evidence

The most representative record is the Black Hat 2025 briefing “Evil Digital Twin, Too: The First 30 Months of Psychological Manipulation of Humans by AI,” coauthored by Ben D. Sawyer and Matthew Canham [record_id:93]. It is notable because it situates Canham’s work