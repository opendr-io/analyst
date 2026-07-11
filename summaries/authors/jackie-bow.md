# Topic: Author: Jackie Bow

## Executive Summary

The two records attributed to Jackie Bow both come from BSidesSF 2025 and position Bow in the intersection of AI security, cloud-native security operations, and the modernization of SOC workflows. The records show Bow participating in one live panel/podcast about securing cloud-native AI systems and building “AI-first SOC teams” [record_id:2259], and co-presenting a talk arguing that SOCs should stop forcing AI to mimic human analyst workflows and instead let machines solve security problems in machine-native ways [record_id:2292].

Collectively, the records suggest a coherent research and practice focus: AI is changing security operations, legacy SOC tooling and workflows are insufficient for AI-era systems, and security teams need to rethink both threat modeling and analyst-machine collaboration. The evidence base is small—only two conference-session abstracts—so conclusions about Jackie Bow’s broader body of work should be treated as provisional. However, within this limited corpus, Bow is consistently associated with practical AI security operations, cloud-native AI risk, and the organizational design of modern SOCs.

## Research Landscape

The records are both BSidesSF 2025 session descriptions rather than full papers, transcripts, slide decks, or technical writeups. As a result, they provide high-level statements of topic, framing, and intended contribution, but not detailed methodology, experimental data, or implementation specifics.

The first record is a live “Cloud Security Podcast” session featuring Ashish Rajan, Jackie Bow, Swathi Joshi, and Kane Narraway. Its stated topic is “AI Security 101: Securing Cloud-Native AI Systems & Building Modern SOCs” and it frames AI as transforming security faster than cloud did [record_id:2259]. This source appears to be a panel-style discussion, emphasizing practitioner perspectives on “real-world threat models,” “AI-first SOC teams,” and limitations of legacy tools [record_id:2259].

The second record is a dedicated talk by Jackie Bow and Peter Sanford titled “AI’s Bitter Lesson for SOCs: Let Machines Be Machines” [record_id:2292]. It has a more specific thesis: SOCs may be limiting AI by forcing it to imitate human analyst workflows, and experiments at Anthropic suggest AI can address security problems differently, allowing humans to focus on nuanced tasks machines cannot yet handle [record_id:2292].

Together, the landscape is narrow but focused. Both records sit in the area of AI-enabled security operations, especially SOC transformation. The first places that transformation in the broader context of cloud-native AI system security; the second drills into human-AI workflow design inside SOCs.

## Major Themes And Trends

### AI as a disruptive shift in security operations

Both records frame AI as a major forcing function for security teams. The panel abstract in record 2259 states that “AI is reshaping security faster than cloud ever did,” indicating a view of AI as a structural shift comparable to, or greater than, the earlier cloud transformation [record_id:2259]. This framing implies that existing security assumptions, tooling, and organizational patterns may not be sufficient for the AI era.

Record 2292 continues this theme but narrows it to SOC practice. Its central claim is that security teams have been “forcing AI to imitate human analyst workflows,” potentially constraining both the technology and human analysts [record_id:2292]. The shared trend is not simply “use AI in security,” but rather “rethink security operations around AI’s distinctive capabilities and limitations.”

### Building AI-first SOCs rather than merely augmenting old SOCs

A recurring concern is the design of SOCs in a world where AI is deeply embedded in detection, triage, response, and analysis. Record 2259 explicitly mentions “building AI-first SOC teams” and discusses what it takes to “secure, monitor, and respond to threats in AI systems” [record_id:2259]. This suggests an emphasis on team structure, operational readiness, and monitoring architecture, not just model-level safety or abstract AI risk.

Record 2292 advances a related but sharper argument: AI should not merely be added to existing human-centric workflows. The phrase “Let Machines Be Machines” captures a design philosophy in which AI systems may work best when allowed to approach security problems in non-human ways [record_id:2292]. In this framing, the SOC of the future is not just a human analyst queue with AI assistance; it may involve a reallocation of tasks based on what machines and humans each do well.

### Legacy tools and legacy workflows as constraints

The records also share a critique of legacy approaches. Record 2259 refers to “the gaps legacy tools can’t fill” in relation to AI systems and modern SOCs [record_id:2259]. This implies that traditional cloud, SIEM, SOC, or detection tooling may lack coverage for AI-specific risks, telemetry, workflows, or response patterns.

Record 2292 applies a similar critique to workflow design. The problem is not only that old tools are inadequate, but that old mental models may be inadequate. If AI is constrained to mimic human analyst behavior, the SOC may fail to capture the full value of machine reasoning, automation, or large-scale pattern processing [record_id:2292].

### Human-machine division of labor

The strongest conceptual theme across the two records is the future division of labor between AI systems and human security practitioners. Record 2292 explicitly states that allowing AI to tackle security problems “its own way” can allow humans to focus on “the nuanced work machines can’t do (yet)” [record_id:2292]. This is an important position: it does not present AI as a full replacement for analysts, but as a mechanism for changing what analysts spend time doing.

Record 2259’s reference to “AI-first SOC teams” similarly suggests organizational change rather than simple tool adoption [record_id:2259]. The records collectively point toward a SOC model where AI handles certain forms of scale, repetition, or machine-suited analysis, while humans focus on judgment, ambiguity, context, and high-stakes decision-making.

## Methods, Tools, And Approaches Discussed

The records are abstracts and do not name concrete tools, architectures, or codebases. Still, they identify several methodological and operational approaches.

First, the panel in record 2259 emphasizes “real-world threat models” for AI systems [record_id:2259]. This suggests a practical threat-modeling approach to cloud-native AI security: identifying how AI systems can be attacked, monitored, and defended in production rather than treating AI security as purely theoretical.

Second, record 2259 discusses securing, monitoring, and responding to threats in AI systems [record_id:2259]. This implies an end-to-end operational security approach covering prevention, observability, detection, and incident response for AI-enabled or AI-native infrastructure.

Third, record 2259’s mention of “AI-first SOC teams” points to organizational and process design as a method: building teams, workflows, and responsibilities around AI-era threats instead of attempting to retrofit legacy SOC models [record_id:2259].

Fourth, record 2292 introduces experimentation as evidence. The abstract says the presenters will show, “through realworld experiments at Anthropic,” how allowing AI to address security problems in its own way can shift human work toward tasks machines cannot yet perform [record_id:2292]. The abstract does not explain the experiments, but it indicates that the talk is grounded in applied internal work rather than only speculation.

Finally, record 2292 proposes a design principle: do not require AI to imitate human analyst workflows when solving SOC problems [record_id:2292]. This may include alternative machine-native workflows, though the record does not specify whether those involve autonomous triage, agentic investigation, non-linear reasoning, large-scale correlation, or other techniques.

## Notable Talks, Records, And Evidence

The most broadly scoped record is the live “Cloud Security Podcast” panel, “AI Security 101: Securing Cloud-Native AI Systems & Building Modern SOCs” [record_id:2259]. It matters because it places Jackie Bow in a multi-speaker discussion about AI security and cloud-native operations. The abstract identifies several key concerns: AI’s rapid impact on security, real-world AI threat models, AI-first SOC construction, and gaps in legacy tooling [record_id:2259]. For downstream researchers, this record is useful as evidence that Bow’s attributed work includes public discussion of both AI system defense and SOC modernization.

The more focused and arguably more distinctive record is “AI’s Bitter Lesson for SOCs: Let Machines Be Machines,” co-authored by Jackie Bow and Peter Sanford [record_id:2292]. This talk appears to make a specific argument about the mistake of forcing AI into human-shaped SOC workflows. Its reference to “realworld experiments at Anthropic” gives it a potentially stronger empirical grounding than a general panel abstract, although the record does not provide details about the experimental setup or results [record_id:2292]. This record is the clearest evidence of a unique contribution: advocating for machine-native approaches to AI in security operations, paired with a deliberate redefinition of human analyst responsibilities.

The two records are complementary. Record 2259 frames the high-level operational problem: AI systems require new threat models, monitoring, response practices, and SOC structures [record_id:2259]. Record 2292 proposes a more specific principle for that transformation: machines should be allowed to operate in ways suited to machines, while humans should focus on nuanced tasks where human judgment remains important [record_id:2292].

## Gaps, Limits, And Open Questions

The evidence base is thin. There are only two records, both from the same event year and source. Neither record contains a transcript, slides, detailed examples, technical architecture, experimental results, or a list of concrete tools. As a result, it is not possible to evaluate the technical novelty, reproducibility, or measurable impact of the claims.

Several open questions remain:

- What specific “real-world threat models” for AI systems were discussed in the live podcast panel? The abstract in record 2259 names threat modeling but does not describe the threats [record_id:2259].
- What exactly are the “gaps legacy tools can’t fill”? The record implies insufficiency in legacy tools but does not specify gaps in telemetry, detection logic, response automation, model observability, prompt security, data governance, or infrastructure coverage [record_id:2259].
- What were the “realworld experiments at Anthropic” referenced in record 2292? The abstract does not describe their design, scope, evaluation criteria, outcomes, or limitations [record_id:2292].
- What does it mean operationally to let AI “tackle security problems its own way”? The phrase is conceptually important, but the abstract does not specify concrete workflows, architectures, or guardrails [record_id:2292].
- How should SOCs divide work between humans and machines in practice? Record 2292 suggests humans should focus on nuanced work that machines cannot yet do, but it does not define those categories or explain how to govern handoffs [record_id:2292].
- How does Bow’s work relate to other AI security areas such as prompt injection, model abuse, data leakage, agent security, cloud identity, or detection engineering? Record 2259 is categorized under AI security and cloud/SOC themes, but the raw abstract itself remains broad [record_id:2259].

Future research would benefit from locating full session recordings, slides, speaker notes, follow-up blog posts, or related Anthropic publications that clarify the experiments and operational recommendations.

## Coverage And Evidence Notes

This report covers both expected records: 2259 and 2292.

Record 2259 is a BSidesSF 2025 live Cloud Security Podcast session titled “CLOUD SECURITY PODCAST - LIVE!” featuring Ashish Rajan, Jackie Bow, Swathi Joshi, and Kane Narraway [record_id:2259]. The raw text frames the session as “AI Security 101: Securing Cloud-Native AI Systems & Building Modern SOCs,” emphasizing AI’s rapid effect on security, real-world threat models, AI-first SOC teams, legacy-tool gaps, and securing, monitoring, and responding to threats in AI systems [record_id:2259]. Because it is a panel/podcast abstract with multiple speakers, it is useful evidence of Bow’s participation in the topic area but does not isolate Bow’s individual claims.

Record 2292 is a BSidesSF 2025 talk titled “AI’S BITTER LESSON FOR SOCs: LET MACHINES BE MACHINES,” attributed to Jackie Bow and Peter Sanford [record_id:2292]. It argues that forcing AI to imitate human analyst workflows may hold back both machines and humans, and it references real-world experiments at Anthropic showing how AI can address security problems differently while humans focus on nuanced work [record_id:2292]. This is the strongest evidence in the small corpus for Bow’s specific viewpoint on AI-native SOC design.

No records appear purely logistical or irrelevant. Both records are conference-session abstracts tied directly to Jackie Bow and to AI-era security operations.