# Topic: Author: Josh Harguess

## Executive Summary

The two records attributed to Josh Harguess, both co-authored or co-presented with Chris Ward at BSidesLV 2025, focus on AI risk management from governance and systems-safety perspectives. Together, they present a coherent view of AI security that goes beyond narrow technical vulnerability discovery: AI systems are framed as enterprise and mission-critical socio-technical systems requiring lifecycle oversight, regulatory alignment, incident response preparation, hazard analysis, and proactive control design.

One record is a hands-on workshop on AI governance, emphasizing enterprise AI lifecycle oversight, the NIST AI Risk Management Framework, EU AI Act compliance, and tabletop exercises for AI incidents [record_id:2387]. The other is a talk on applying STPA-Sec, a systems-theoretic hazard analysis method, to military AI systems and AI-enabled environments involving generative and predictive models [record_id:2458]. Across both, Harguess’s apparent contribution is to connect AI security with governance, risk, compliance, safety engineering, and operational assurance rather than treating AI risk solely as a matter of model exploits or prompt-level abuse.

The evidence base is small but thematically consistent. Both records are BSidesLV 2025 session abstracts, not full papers, transcripts, or slide decks. As a result, they strongly establish the topics Harguess presented on, but only thinly document the details of his arguments, case studies, or concrete implementation guidance.

## Research Landscape

The available corpus contains two BSidesLV 2025 records attributed to Josh Harguess, both with Chris Ward as co-author or co-presenter. The records are conference-session abstracts rather than long-form publications. They describe one extended workshop and one shorter talk.

The first record, “AI Governance in Action: Fundamentals & Tabletop Workshop,” is categorized as a Training Ground session at BSidesLV 2025. It is a four-hour workshop scheduled for Tuesday and is centered on practical AI governance for enterprise settings [record_id:2387]. The raw text describes AI systems as increasingly “integral to enterprise operations” and argues that “effective governance is essential to mitigate associated risks” [record_id:2387]. This positions the session within enterprise risk management, compliance, and organizational readiness.

The second record, “Hazard Analysis of Military AI Systems Using STPA-Sec: A Systems-Theoretic Approach to Secure and Assured Autonomy,” is a 45-minute BSidesLV 2025 talk. It applies systems-theoretic hazard analysis to “military AI systems” and “AI-enabled environments,” with emphasis on generative and predictive models [record_id:2458]. The record’s central framing is that “AI systems can fail dangerously without ever ‘breaking,’” which suggests concern with emergent, systemic, and interaction-driven failure modes rather than only conventional defects or attacks [record_id:2458].

The overall research area represented by these records is AI assurance and governance. The two sessions approach that area from complementary directions:

- Enterprise governance, regulation, and incident readiness [record_id:2387].
- Systems-theoretic hazard analysis for secure and assured autonomy, especially in military or high-consequence environments [record_id:2458].

Although the topic query concerns Josh Harguess, both records list Chris Ward alongside Harguess. The records do not distinguish which ideas or sections belong specifically to Harguess versus Ward. Therefore, any attribution should be understood as applying to the co-authored/co-presented sessions rather than uniquely to Harguess alone.

## Major Themes And Trends

### AI security as governance, not only exploitation

A major theme across the records is that AI security is treated as a governance and risk-management problem. In the workshop abstract, AI systems are described as embedded in enterprise operations, and the response is not merely technical hardening but “effective governance,” “AI system lifecycle oversight,” framework alignment, regulatory compliance, and practical response planning [record_id:2387]. This indicates a broad conception of AI security: organizations need structured oversight from design through deployment and incident response.

The STPA-Sec talk reinforces this broader view by focusing on hazards that arise even when the system has not conventionally “broken” [record_id:2458]. The idea that an AI system can “fail dangerously without ever ‘breaking’” points to risks that may emerge from interactions among models, operators, interfaces, feedback loops, mission goals, and recommendations [record_id:2458]. This is consistent with systems safety and assurance thinking, where failure may be caused by inadequate controls or unsafe interactions rather than a single component malfunction.

### Lifecycle and systems thinking

Both records emphasize lifecycle or system-level oversight. The governance workshop explicitly focuses on “AI system lifecycle oversight” [record_id:2387]. The STPA-Sec talk introduces “a systems-theoretic method” for identifying and mitigating “hidden hazards in AI-enabled environments” [record_id:2458]. These are different vocabularies—governance lifecycle versus systems-theoretic hazard analysis—but they converge on the idea that AI risk must be understood across time, organizational context, and interacting system components.

This is a notable trend because it moves beyond point-in-time model evaluation. The records imply that AI risk management must include planning, monitoring, feedback, compliance, response, and control mechanisms. In the STPA-Sec record, examples of systemic risk sources include “misaligned recommendations, inadequate feedback loops, and interface ambiguity” [record_id:2458]. These are not simply model accuracy problems; they are problems of system design, human-machine interaction, and operational control.

### Regulatory and framework alignment

The workshop explicitly references recognized AI governance frameworks and regulations, especially the NIST AI RMF and the EU AI Act [record_id:2387]. This suggests that Harguess and Ward’s AI governance work is oriented toward practical organizational alignment with emerging standards and legal obligations.

The record does not describe the workshop’s detailed interpretation of these frameworks, but the mention is significant. It places the session within a maturing AI governance landscape where organizations need to translate high-level frameworks into concrete policies, controls, workflows, and incident response capabilities [record_id:2387].

The STPA-Sec talk does not mention specific legal frameworks, but it does connect AI security to assurance and control. Its title refers to “Secure and Assured Autonomy,” and the abstract describes identifying and mitigating hazards before they cause harm [record_id:2458]. This complements regulatory alignment by addressing how organizations might reason about safety and security in complex AI-enabled systems.

### Incident response and preparedness

The governance workshop includes a “guided tabletop exercise simulating a real-world AI incident” [record_id:2387]. This is important because it shows an operational and experiential approach to AI governance. Instead of presenting governance as a static policy exercise, the workshop appears to train participants in collaborative response strategies and “practical risk mitigation planning” [record_id:2387].

This theme does not appear directly in the STPA-Sec abstract, but both records share a prevention-and-control orientation. The workshop emphasizes preparedness for AI incidents [record_id:2387], while the STPA-Sec talk emphasizes controlling hazards “before they cause harm” [record_id:2458].

### High-consequence AI environments

The second record is explicitly concerned with “military AI systems” and “secure and assured autonomy” [record_id:2458]. It highlights environments involving “generative and predictive models,” suggesting concern with both modern generative AI and predictive decision-support systems [record_id:2458]. The military framing implies high-consequence settings where errors, unsafe recommendations, poor feedback, or ambiguous interfaces can produce serious harm.

The first record is more general and enterprise-focused, but it also treats AI systems as operationally significant and risk-bearing [record_id:2387]. Together, the records show a range from broad enterprise AI governance to specialized hazard analysis for military autonomy.

## Methods, Tools, And Approaches Discussed

The records mention several approaches rather than specific software tools.

The first approach is AI governance lifecycle oversight. The workshop promises a “comprehensive introduction to AI governance” focused on “AI system lifecycle oversight” [record_id:2387]. This likely includes processes for identifying AI systems, assessing risks, assigning accountability, monitoring deployments, and managing incidents, though the abstract does not provide implementation detail. The record’s strongest evidence is that lifecycle oversight is a central method in the workshop, not the exact form that oversight takes.

The second approach is alignment with external frameworks and regulations. The workshop specifically names the NIST AI RMF and the EU AI Act [record_id:2387]. These are presented as reference points for organizational governance and compliance. The abstract frames them as part of practical AI governance rather than purely academic concepts.

The third approach is tabletop exercising. Participants in the workshop “engage in a guided tabletop exercise simulating a real-world AI incident” [record_id:2387]. This is a notable method because it translates AI governance into scenario-based practice. Tabletop exercises are commonly used to test roles, decision-making, escalation paths, communications, and response strategies. In this record, the exercise is used to foster “collaborative response strategies and practical risk mitigation planning” [record_id:2387].

The fourth approach is STPA-Sec. The second record introduces STPA-Sec as “a systems-theoretic method for identifying and mitigating hidden hazards in AI-enabled environments” [record_id:2458]. The talk applies this method to military AI systems and AI environments involving generative and predictive models [record_id:2458]. The abstract emphasizes that STPA-Sec can reveal risks from “misaligned recommendations, inadequate feedback loops, and interface ambiguity” [record_id:2458]. This suggests a method that looks at control structures, feedback, decision authority, human-machine interfaces, and unsafe interactions rather than only individual component failure.

The fifth approach is proactive hazard control. The STPA-Sec abstract says the method helps identify risks and “control them before they cause harm” [record_id:2458]. This is a prevention-oriented stance aligned with safety engineering. It frames AI risk as something to be anticipated through structured analysis rather than discovered only after failures occur.

## Notable Talks, Records, And Evidence

The most representative governance-focused record is “AI Governance in Action: Fundamentals & Tabletop Workshop” [record_id:2387]. It matters because it situates Harguess’s work in practical enterprise AI governance. The record covers several important governance dimensions in a compact abstract: enterprise AI adoption, lifecycle oversight, NIST AI RMF alignment, EU AI Act compliance, incident simulation, collaborative response, and risk mitigation planning [record_id:2387]. It is also the only record in the corpus that explicitly mentions a hands-on workshop format, indicating an applied training contribution rather than only a lecture.

This workshop is especially useful for downstream researchers interested in how AI governance is being operationalized for security audiences. It suggests that Harguess and Ward were not merely discussing AI policy at a high level; they were offering “actionable insights and tools” for implementing responsible AI governance within organizations [record_id:2387]. However, because only the abstract is available, the actual tools, templates, scenarios, or exercises are not visible in the record.

The most representative safety-analysis record is “Hazard Analysis of Military AI Systems Using STPA-Sec: A Systems-Theoretic Approach to Secure and Assured Autonomy” [record_id:2458]. It matters because it brings a systems-theoretic security and safety method into the AI assurance context. The record’s central claim is that AI systems may fail dangerously without conventional breakage [record_id:2458]. This is a distinctive contribution because it foregrounds systemic hazards such as misaligned recommendations, feedback-loop problems, and interface ambiguity [record_id:2458].

This talk is also important because it extends the AI governance discussion into high-assurance and military contexts. The title explicitly names “Military AI Systems,” “STPA-Sec,” “Systems-Theoretic,” “Secure,” and “Assured Autonomy” [record_id:2458]. Those terms indicate an emphasis on mission-critical AI, system safety, and security assurance rather than only compliance. For downstream research agents, this record is likely the stronger starting point for questions about AI hazard analysis, autonomy assurance, and systemic failure modes.

Taken together, the two records show Josh Harguess associated with a pragmatic, assurance-oriented AI security agenda at BSidesLV 2025. One session is governance and incident-readiness oriented [record_id:2387]; the other is systems-hazard and autonomy-assurance oriented [record_id:2458]. The shared co-author, same event, and overlapping AI risk focus suggest a coordinated body of work, although the records do not explicitly state that the sessions were connected.

## Gaps, Limits, And Open Questions

The main limitation is the small corpus size. Only two records are available, both from the same event year and same source. This makes it difficult to identify long-term evolution in Josh Harguess’s work, compare his BSidesLV material with other venues, or determine whether these themes are representative of his broader career.

The records are abstracts, not full talks, transcripts, slide decks, papers, or workshop materials. They establish topic, framing, and intended learning outcomes, but they do not provide detailed arguments, examples, diagrams, case studies, or step-by-step methods. For example, the governance workshop says attendees will leave with “actionable insights and tools,” but the actual tools are not included in the record [record_id:2387]. The STPA-Sec talk says the method reveals systemic risks and helps control them, but the abstract does not show an example hazard analysis, control structure, unsafe control action, or mitigation pattern [record_id:2458].

The records also do not clarify authorship division between Josh Harguess and Chris Ward. Both records list both names [record_id:2387] [record_id:2458]. Therefore, it is not possible from these records alone to isolate Harguess’s unique claims, methods, or examples.

Several open questions remain for downstream researchers:

- What specific tabletop scenario was used in the AI governance workshop, and what incident type did it simulate [record_id:2387]?
- What concrete governance artifacts were provided, such as