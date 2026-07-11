# Topic: Author: Jake Thomas

## Executive Summary

The two available records attributed to Jake Thomas describe CAMLIS 2025 work at the intersection of machine learning security, multimodal model evaluation, and adaptive cyber defense. Together, they suggest a research profile focused on making AI systems more robust in operationally relevant security settings: one record addresses evaluation of Visual Language Models against typographic prompt injection attacks, while the other proposes Contextual Reinforcement Learning for cyber defense agents that adjust policies dynamically based on mission and threat context.

The evidence base is small—only two short abstracts—so conclusions should be treated as preliminary. Still, the records point to two clear contributions: first, adapting text-only safety or alignment datasets into multimodal formats to test VLM susceptibility to prompt injection [record_id:115]; second, using contextual signals such as mission objectives and threat assessments to guide reinforcement-learning-based defensive agents in real time without retraining [record_id:120]. Across both records, the recurring theme is adaptation: adapting evaluation datasets to new model modalities, and adapting cyber-defense policies to changing operational context.

## Research Landscape

The corpus contains two records, both attributed to Jake Thomas and both associated with CAMLIS 2025. The records are not full papers; they are brief descriptions of talks or papers. As a result, the research landscape can be sketched only at a high level.

One record is centered on AI model security, specifically Visual Language Models and prompt injection. It presents “Text2VLM,” described as “a novel pipeline that adapts text-only datasets into multimodal formats” in order to evaluate VLM resilience against “typographic prompt injection attacks” [record_id:115]. This places the work in the broader area of AI security evaluation, especially the problem of assessing whether alignment or safety training that works in text-only settings transfers to multimodal systems.

The second record is situated in machine learning for cyber defense. It introduces “a framework for applying Contextual Reinforcement Learning (cRL) to cyber defense,” emphasizing defensive agents that incorporate contextual signals such as “mission objectives or threat assessments” to adjust policies “in real-time without retraining” [record_id:120]. This places the work closer to autonomous or semi-autonomous cyber operations, adaptive detection and response, and reinforcement learning methods for mission-aware security.

Taken together, the records portray Jake Thomas’s attributed work as concerned with practical security evaluation and adaptive AI-enabled defense. The first work asks how to test increasingly multimodal AI systems against injection-style attacks; the second asks how defensive agents can adapt to operational context without costly retraining. Both are framed as methods or frameworks rather than empirical result summaries, and neither record provides detailed experimental findings, datasets, metrics, implementation specifics, or limitations.

## Major Themes And Trends

### Adaptation as a central research motif

The strongest shared theme is adaptation. In the VLM security record, adaptation refers to transforming existing “text-only datasets into multimodal formats” so they can be used to evaluate Visual Language Models [record_id:115]. The implication is that security and alignment datasets built for text-only models may not be sufficient once models accept visual input, and that evaluators need pipelines that translate or reframe those datasets for multimodal testing.

In the cyber-defense record, adaptation refers to agents that “dynamically incorporate contextual signals” to modulate policies in real time [record_id:120]. Instead of adapting datasets, the proposed framework adapts behavior: cyber-defense agents change policy according to operational context such as mission objectives and threat assessments. The phrase “without retraining” is important because it suggests the framework is intended for changing environments where retraining would be too slow, expensive, or operationally disruptive [record_id:120].

Across both records, adaptation is not merely a convenience but a security requirement. Multimodal AI systems expand the attack surface, requiring adapted evaluation methods [record_id:115]. Cyber defense environments change rapidly, requiring policy adaptation that incorporates situational context [record_id:120].

### Security evaluation for modern AI systems

Record 115 contributes to the theme of security evaluation for AI systems, especially evaluation of VLM alignment training. The record describes Text2VLM as a pipeline for evaluating “the resilience of Visual Language Models (VLMs) against typographic prompt injection attacks” [record_id:115]. This suggests a focus on whether VLMs can be manipulated through text embedded in visual inputs, a known concern for multimodal systems that read and interpret images containing instructions, labels, screenshots, or other textual artifacts.

The record also states that the work “highlights the increased susceptibility of VLMs when visual inputs are introduced” [record_id:115]. This is the strongest substantive claim in the corpus about empirical behavior: visual inputs appear to increase susceptibility. However, the record does not provide details about the experimental design, baseline models, attack examples, quantitative results, or how “resilience” and “susceptibility” are measured. Downstream researchers should treat the claim as an abstract-level summary rather than a fully evidenced conclusion.

### Mission-aware cyber defense

Record 120 presents a different but complementary security theme: mission-aware, context-sensitive cyber defense. The proposed cRL framework allows agents to incorporate “contextual signals” including “mission objectives or threat assessments” [record_id:120]. This indicates an interest in moving beyond generic defensive policies toward policies that respond to what the mission requires and what the threat environment currently looks like.

The record’s phrase “mission-ready cyber defense” is important as a framing concept. It suggests that cyber-defense agents should not merely optimize abstract reward functions; they should adapt behavior according to operational constraints, mission priorities, and real-time threat intelligence. The emphasis on modulating policies “in real-time without retraining” suggests a practical concern with deployability in dynamic environments [record_id:120].

### AI security and cyber defense as connected domains

Although the two records address different technical areas—VLM prompt injection and contextual reinforcement learning for cyber defense—they both fit into a broader pattern of AI systems being evaluated or deployed in security-sensitive contexts. Record 115 focuses on AI as the target of attack: VLMs may be susceptible to typographic prompt injection when visual inputs are introduced [record_id:115]. Record 120 focuses on AI as part of the defensive apparatus: cRL agents may help cyber defenders adapt policies based on mission and threat context [record_id:120].

This pairing reflects a broader trend in security research: AI systems are both assets needing protection and tools used to conduct defense. The corpus does not explicitly connect these two lines of work, but downstream researchers may find it useful to examine whether Thomas’s attributed work bridges AI model robustness and operational cyber-defense automation.

## Methods, Tools, And Approaches Discussed

The most concrete method named in the records is Text2VLM. It is described as “a novel pipeline” that adapts “text-only datasets into multimodal formats” [record_id:115]. The purpose of this pipeline is to evaluate VLM resilience against “typographic prompt injection attacks” [record_id:115]. From the record alone, the workflow appears to involve taking datasets originally designed for text-only evaluation—possibly prompt-injection, jailbreak, safety, or alignment datasets—and converting them into inputs suitable for VLMs, likely by rendering or embedding text into visual formats. The record does not state the exact transformation process, image generation approach, dataset sources, target VLMs, or evaluation metrics.

The attack method discussed in record 115 is typographic prompt injection. The raw text does not define the term, but it clearly places the attack in the context of visual inputs to VLMs [record_id:115]. The phrase implies attacks in which instructions are conveyed through typography or text visible in an image, rather than through the normal text prompt alone. The record’s emphasis on “increased susceptibility” when visual inputs are introduced indicates that multimodal input channels may weaken alignment safeguards or create new pathways for instruction-following failures [record_id:115].

The second methodological contribution is a framework for Contextual Reinforcement Learning in cyber defense. Record 120 says the framework applies cRL so that agents “dynamically incorporate contextual signals” and use those signals “to modulate their policies in real-time without retraining” [record_id:120]. This suggests an architecture where policy behavior is conditioned on contextual features rather than fixed after training. The examples of context are “mission objectives” and “threat assessments” [record_id:120]. Those examples imply a system in which cyber-defense decisions are influenced by both strategic priorities and current risk information.

Record 120 does not specify the reinforcement learning algorithm, state/action space, reward design, simulation environment, deployment setting, or defensive tasks. It also does not identify whether the agents are intended for detection, triage, response, deception, patch prioritization, or other cyber operations. The record’s contribution is therefore best understood as a high-level framework proposal rather than a fully documented toolchain.

## Notable Talks, Records, And Evidence

The most notable record for AI model security is “Text2VLM: Adapting Text-Only Datasets to Evaluate Alignment Training in Visual Language Models” [record_id:115]. It matters because it addresses a pressing evaluation gap: many AI safety and alignment datasets are text-only, while modern systems increasingly accept images and other modalities. The record’s core claim is that Text2VLM adapts such datasets into multimodal formats to evaluate VLM resilience against typographic prompt injection [record_id:115]. Its second important claim is that VLMs become more susceptible when visual inputs are introduced [record_id:115]. This makes the record relevant to downstream research on multimodal jailbreaks, prompt injection, AI alignment evaluation, and benchmark adaptation.

The most notable record for adaptive cyber defense is “Adaptive by Design: Contextual Reinforcement Learning for Mission-Ready Cyber Defense” [record_id:120]. It matters because it proposes cRL as a way for defensive agents to incorporate operational context dynamically. The record specifically names mission objectives and threat assessments as contextual signals and emphasizes real-time policy modulation without retraining [record_id:120]. This makes it relevant to downstream research on reinforcement learning for cybersecurity, autonomous defense, mission-aware decision-making, and adaptive security operations.

The two records are representative in different ways. Record 115 is representative of AI-security evaluation work focused on the vulnerabilities of modern foundation-model interfaces [record_id:115]. Record 120 is representative of AI-for-cyber-defense work focused on using learning agents to improve operational responsiveness [record_id:120]. Their shared importance lies in their attention to security systems under changing conditions: new modalities in one case, changing mission and threat context in the other.

## Gaps, Limits, And Open Questions

The largest limitation is the small size and brevity of the evidence base. There are only two records, and both are short abstracts or descriptions rather than full technical reports. They state proposed contributions but do not provide enough detail to evaluate implementation quality, empirical strength, reproducibility, or operational feasibility.

For Text2VLM, major open questions include:

- Which text-only datasets are adapted into multimodal formats?
- How exactly does the pipeline convert text-only examples into visual or multimodal test cases?
- Which VLMs are evaluated?
- What are the baselines?
- How are typographic prompt injection attacks constructed?
- What metrics define “resilience” and “susceptibility”?
- How large is the reported increase in susceptibility when visual inputs are introduced?
- Are failures due to OCR-like perception, instruction hierarchy confusion, alignment weaknesses, or other mechanisms?

The record states that VLMs show “increased susceptibility” with visual inputs, but does not include quantitative evidence or methodological detail [record_id:115]. Downstream researchers should seek the full talk, paper, slides, or associated artifacts before relying on this as a demonstrated empirical result.

For the cRL cyber-defense framework, major open questions include:

- What cyber-defense tasks are modeled?
- What contextual variables are used beyond mission objectives and threat assessments?
- How are context signals represented to the agent?
- What reinforcement learning method is used?
- How are policies modulated without retraining?
- What environments or simulations are used for evaluation?
- How is mission success measured?
- How are safety, explainability, and operator control handled?
- What happens when context signals are noisy, adversarial, stale, or conflicting?

The record describes a framework but does not provide evidence of deployment, experiments, or comparative performance [record_id:120]. It is therefore best used as a pointer to a research direction rather than as proof that cRL improves cyber defense in practice.

A broader open question is whether the two lines of work connect. The records do not state whether Jake Thomas’s VLM security evaluation work informs his adaptive cyber-defense work, or whether the same threat models, evaluation principles, or operational assumptions appear in both. Future research could examine whether these projects share a common methodology around robustness testing, contextual decision-making, or security evaluation under changing input conditions.

## Coverage And Evidence Notes

This report covers both records specified in the topic request.

Record 115 is a CAMLIS 2025 record titled “Text2VLM: Adapting Text-Only Datasets to Evaluate Alignment Training in Visual Language Models.” Its raw text describes Text2VLM as a pipeline that adapts text-only datasets into multimodal formats to evaluate VLM resilience against typographic prompt injection attacks, and it claims that visual inputs increase VLM susceptibility [record_id:115]. It is central to the themes of multimodal AI security, prompt injection, and alignment evaluation.

Record 120 is a CAMLIS 2025 record titled “Adaptive by Design: Contextual Reinforcement Learning for Mission-Ready Cyber Defense.” Its raw text describes a framework for applying Contextual Reinforcement Learning to cyber defense, where agents use contextual signals such as mission objectives or threat assessments to adjust policies in real time without retraining [record_id:120]. It is central to the themes of adaptive cyber defense, reinforcement learning, and mission-aware security operations.

No record in the provided set is purely logistical or unrelated. Both