# Topic: Author: Rich Harang

## Executive Summary

The two records attributed to Rich Harang span two distinct but related areas of machine learning and security: applied deep learning for malware detection and modern AI-agent security. The earlier record, a 2017 CAMLIS presentation, focuses on optimizing multi-task neural networks for malicious-file detection by estimating how much weight sharing occurs across related tasks using an approximate Fisher information measure [record_id:254]. The later record, a 2025 Black Hat USA briefing coauthored with Rebecca Lynch, shifts to the security risks of large language model-powered agentic systems, emphasizing prompt-driven exploitation, adversarial inputs, enterprise exposure, and defensive design principles for AI agents [record_id:85].

Collectively, the records suggest that Harang’s public work, at least within this small corpus, sits at the intersection of machine learning systems and security engineering. The 2017 work is concerned with making ML models for malware detection more efficient, interpretable in terms of shared representation, and suitable for deployment constraints [record_id:254]. The 2025 work is concerned with the opposite side of AI deployment: how increased model flexibility, expanded modalities, and autonomous tool use create new attack surfaces that require red-team assessment and security-first architecture [record_id:85]. The throughline is practical security use of machine learning systems: how to build, evaluate, deploy, and secure ML-based systems when they interact with real-world malicious behavior or sensitive enterprise environments.

Evidence is thin because the topic contains only two records, separated by eight years and drawn from different venues. However, the contrast between them is informative: Harang’s attributed work moves from model-level questions in security-oriented deep learning to system-level questions in securing LLM-based autonomous agents.

## Research Landscape

The corpus consists of two conference-style records: one from CAMLIS in 2017 and one from Black Hat USA in 2025. They are not full papers in the provided material; they are abstracts or talk descriptions. As a result, the evidence describes themes, methods, motivations, and claimed contributions, but does not provide experimental details, implementation artifacts, results tables, or quantitative outcomes.

The 2017 CAMLIS record is a single-author presentation titled “Estimating weight sharing in multi-task networks via approximate Fisher information” [record_id:254]. It is situated in machine learning for security, specifically the detection of malicious files using deep neural networks. The record frames neural networks as effective and efficient compared with conventional signature-based approaches, while acknowledging that model size remains a deployment concern. It investigates whether related detection tasks can be grouped into a single multi-task network so that shared representations reduce the total deployed model footprint [record_id:254].

The 2025 Black Hat record is a coauthored briefing titled “From Prompts to Pwns: Exploiting and Securing AI Agents” by Rebecca Lynch and Rich Harang [record_id:85]. It is situated in AI security, prompt injection, application security offense, and enterprise AI-agent risk. It focuses on the evolution from relatively rigid retrieval-augmented generation workflows to more autonomous agentic systems with expanded input modalities, dynamic reasoning strategies, and the ability to act on users’ behalf across sensitive systems [record_id:85].

The overall research area represented by these records is not a single narrow technical niche. Instead, it reflects a broader security-ML trajectory: applying ML to security problems, then securing ML-enabled systems as they become more powerful and operationally embedded. In 2017, the central concern is efficient and effective deployment of neural networks for malware detection [record_id:254]. In 2025, the central concern is adversarial exploitation of AI systems themselves, especially when LLMs are connected to tools, data, and enterprise workflows [record_id:85].

## Major Themes And Trends

### From ML-for-security to security-of-ML systems

The clearest trend across the records is a shift in emphasis. The 2017 record treats deep neural networks as tools for improving security outcomes, specifically by detecting malicious files with high performance and potential space/time savings over signature-based approaches [record_id:254]. The questions are model-design questions: how to combine related tasks, how to determine whether a joint model is truly sharing useful representations, and how to right-size models for deployment.

By contrast, the 2025 record treats AI systems as security-critical targets and sources of risk. LLM-based agents are presented as powerful, flexible systems that can access data, execute actions, and automate complex workflows. Those same capabilities expand the attack surface, especially because LLMs are vulnerable to malicious input and may propagate compromised trust into downstream actions [record_id:85].

Together, the records show two sides of machine learning security practice. One side asks how ML can help detect threats efficiently [record_id:254]. The other asks how ML systems themselves can be exploited and defended when deployed in enterprise environments [record_id:85].

### Deployment constraints and operational realism

Both records are concerned with real deployment conditions, not just abstract model performance.

In the 2017 CAMLIS record, deployment constraints appear through the problem of neural network size on disk. The abstract notes that although deep neural networks offer strong performance and savings over conventional signature-based approaches, their size is still “not negligible” [record_id:254]. The proposed interest in grouping related tasks into a single network is motivated by reducing the deployed footprint relative to multiple task-specific networks.

In the 2025 Black Hat record, operational realism appears through enterprise agent deployments. The record describes agentic systems that interact with sensitive data and systems, automate workflows, and act independently on users’ behalf [record_id:85]. The risk is not merely that the model produces a bad answer, but that adversarial input can influence downstream actions in systems with real permissions and consequences.

This shared operational framing is an important recurring concern. Harang’s attributed work, as represented here, is not solely about theoretical ML performance; it is about how ML systems behave when deployed under practical constraints, adversarial pressure, and enterprise requirements [record_id:254] [record_id:85].

### Measuring hidden properties of ML systems

The 2017 record focuses on a property that is difficult to observe directly: the degree to which a multi-task network actually shares weights or representations across related tasks [record_id:254]. The abstract states that while the performance of joint networks is straightforward to evaluate, “the degree to which weight sharing is taking place is often less so.” The proposed approach is to use a simple approximation to the Fisher information measure to evaluate redundancy exploitation across layers [record_id:254].

The 2025 record similarly concerns a difficult-to-observe system property: whether agentic workflows remain trustworthy when exposed to malicious input [record_id:85]. The abstract states that proof-of-concept exploits developed by an AI Red Team all leverage a core finding: LLMs are uniquely vulnerable to malicious input, and exposure to such input can significantly affect trust in downstream actions [record_id:85].

Although the technical domains differ, both records are interested in latent properties that standard success metrics may not fully capture. In 2017, accuracy alone does not reveal whether a model has achieved meaningful weight sharing [record_id:254]. In 2025, usability and task completion do not reveal whether an agent’s downstream actions are trustworthy under adversarial input [record_id:85].

### Adversarial context as a defining condition

The 2017 record is explicitly grounded in malicious-file detection. It compares deep neural network approaches with conventional signature-based approaches and frames the tasks as detecting malicious files [record_id:254]. While the abstract does not discuss adaptive adversaries or evasion, the application domain is security detection.

The 2025 record is more directly adversarial in its framing. It discusses exploitation, proof-of-concept attacks, prompt-driven compromise, malicious input, and internal red-team assessments against agentic applications [record_id:85]. The abstract emphasizes that expanded AI-agent capability creates “significantly more opportunity for exploitation” and that agentic systems deployed in enterprise environments can go wrong when vulnerable to adversarial inputs [record_id:85].

Across the corpus, adversarial conditions are not incidental. They shape the motivation for both efficient ML security models and secure AI-agent design.

### Scaling capability creates scaling risk

The two records both address consequences of increasing ML capability, though in different ways.

In 2017, stronger deep neural networks improve malicious-file detection and offer space/time savings over signature-based methods, but their own size creates deployment concerns [record_id:254]. Increased model sophistication requires methods for combining tasks, assessing redundancy, and right-sizing models.

In 2025, more flexible and autonomous LLM agents expand usefulness by supporting richer modalities and more sophisticated reasoning, but those same improvements increase access to data, ability to execute actions, and exploitation opportunities [record_id:85]. The record explicitly states that “as their utility increases, so too does their attack surface” [record_id:85].

The broader theme is that capability growth in ML systems must be paired with evaluation and control mechanisms. In one case, the controls are model measurement and sizing approaches [record_id:254]. In the other, they are red-team assessment and security-first agent interaction design [record_id:85].

## Methods, Tools, And Approaches Discussed

The 2017 CAMLIS record discusses multi-task neural networks for malicious-file detection. The motivating idea is to group related tasks with similar features into a single neural network, hoping that weight sharing will allow a combined model to be smaller than two separate task-specific networks [record_id:254]. This approach is framed as a possible answer to deployment-size constraints in deep learning-based malware detection.

The notable methodological contribution in that record is the proposed use of a simple approximation to the Fisher information measure. The purpose of this approximation is to evaluate how much a joint network exploits redundancies in representation across different layers [record_id:254]. The record also describes using this measure for “right-sizing” models, meaning it may help determine whether a model is larger than necessary or whether shared structure is being used effectively [record_id:254]. The abstract additionally connects the work to “recent work on progressive learning in networks,” suggesting possible future research directions, though it does not define those directions in detail [record_id:254].

The 2025 Black Hat record discusses offensive and defensive assessment of agentic AI systems. The methods described include internal assessments and proof-of-concept exploits developed by an AI Red Team [record_id:85]. The targets include “a range of agentic applications,” from popular open-source tools to enterprise systems [record_id:85]. The common exploit basis is malicious input against LLMs, with the consequence that compromised model behavior can affect the trustworthiness of downstream actions [record_id:85].

The 2025 record also describes the architectural evolution that creates the relevant attack surface. Earlier RAG systems are characterized as rigid and predictable, with controlled sequences of model interaction with external systems [record_id:85]. Modern agentic systems are described as using expanded input modalities such as speech and vision, more sophisticated inference strategies such as dynamic chain-of-thought reasoning, and the ability to act independently on users’ behalf [record_id:85]. The defensive approach is summarized as designing agent interactions to mitigate risk and establishing a security-first foundation for safe and scalable adoption, specifically in the context of NVIDIA’s approach to securing emerging agentic workflows [record_id:85].

No specific tools, codebases, datasets, exploit payloads, mathematical formulas, or implementation details are provided in the raw records. The methods are described at the abstract level.

## Notable Talks, Records, And Evidence

The most representative early record is the 2017 CAMLIS talk “Estimating weight sharing in multi-task networks via approximate Fisher information” [record_id:254]. It matters because it shows Harang working on practical machine learning for malware/security detection before the current LLM-agent security wave. Its core contribution is an evaluation method for understanding whether multi-task networks actually share representations in a way that can reduce deployment size. The record is especially useful for downstream researchers interested in model compression, multi-task learning, malware detection, and metrics beyond raw performance [record_id:254].

The most representative later record is the 2025 Black Hat USA briefing “From Prompts to Pwns: Exploiting and Securing AI Agents,” coauthored by Rebecca Lynch and Rich Harang [record_id:85]. It matters because it places Harang in the contemporary AI security conversation around agentic systems, prompt-driven exploitation, AI red teaming, and enterprise deployment risk. The talk description identifies a shift from constrained RAG workflows to more autonomous agents with broader modalities and action capabilities. It argues that these agents are uniquely exposed to malicious input and that such input can affect downstream actions in sensitive enterprise contexts [record_id:85].

Taken together, these records indicate that Harang’s attributed work is not limited to one generation of ML security problems. The 2017 work is model-centric and concerned with making deep learning detection systems compact and measurable [record_id:254]. The 2025 work is system-centric and concerned with securing LLM-powered agents against adversarial inputs and downstream action compromise [record_id:85]. The records are separated by venue, time, and technical focus, but both are anchored in applied security consequences of machine learning.

## Gaps, Limits, And Open Questions

The evidence base is small. With only two records, it is not possible to draw strong conclusions about the full scope of Rich Harang’s work, publication history, research agenda, or organizational roles. The records support a narrow synthesis of two public talks or presentations, not a comprehensive biography or bibliography.

The records are abstracts rather than full technical artifacts. For the 2017 CAMLIS presentation, the abstract does not provide the exact Fisher approximation used, the malware detection tasks studied, the architecture of the multi-task networks, the datasets, the degree of model-size reduction achieved, or empirical validation results [record_id:254]. Downstream researchers would need slides, paper materials, recordings, or related publications to evaluate the technical method.

For the 2025 Black Hat briefing, the abstract does not provide details about the proof-of-concept exploits, the specific open-source tools or enterprise systems assessed, the red-team methodology, the exploit success conditions, or the concrete mitigation patterns NVIDIA uses [record_id:85]. It gives