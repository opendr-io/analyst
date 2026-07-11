# Topic: Author: Sadegh Momeni

## Executive Summary

The two records attributed to Sadegh Momeni present a compact but coherent view of machine-learning-driven enterprise security research, especially around detection engineering, SOC scalability, and reducing dependence on scarce labeled attack data. Both records are from 2025 and focus on practical ML systems for enterprise threat detection rather than purely theoretical security analytics.

The stronger and more detailed record is the Black Hat USA 2025 briefing on **FACADE: Fast and Accurate Contextual Anomaly DEtection**, coauthored by Sadegh Momeni and others, which describes Google’s internal AI system for detecting malicious insiders. The record emphasizes self-supervised learning, contrastive learning from benign data, contextual anomaly detection across corporate logs, clustering for robustness, and reported very low false-positive rates at Alphabet scale [record_id:87]. The second record, a CAMLIS 2025 paper/talk titled **“Democratizing ML for Enterprise Security: A Self-Sustained Attack Detection Framework,”** attributed directly to Sadegh Momeni, proposes a two-stage hybrid framework combining loose YARA rules, an ML classifier, synthetic data generation via “Simula,” and active learning to create a self-sustained, low-overhead SOC detection workflow [record_id:125].

Collectively, the records suggest recurring interests in: making ML-based threat detection operationally practical; reducing labeling burden and incident-data scarcity; combining ML with security-domain heuristics or context; and designing systems that can function at enterprise/SOC scale. The evidence base is thin—only two short abstracts—but both records point toward a consistent research agenda: high-precision detection systems that are deployable in real organizations and resilient to common SOC constraints such as alert fatigue, limited attack examples, and the need for scalable automation.

## Research Landscape

The records are both conference-style summaries or abstracts from 2025 security and machine-learning venues. One comes from Black Hat USA and describes an enterprise-scale insider-threat detection system used internally at Google/Alphabet [record_id:87]. The other comes from CAMLIS and describes a more general ML framework for enterprise security operations centers [record_id:125]. Both records are categorized around detection engineering, SOC, SIEM, and threat hunting, with the Black Hat record also tied to data loss detection and prevention because it specifically discusses malicious insider behavior and suspicious access to sensitive resources [record_id:87].

The overall research landscape represented here is not broad in volume, but it is focused. The records do not cover exploit development, malware reverse engineering, cryptography, incident response playbooks, identity security, or network defense in general. Instead, they concentrate on **ML-enabled detection architectures** for enterprise environments. Both records address the operational realities of security monitoring: massive log volumes, sparse known-bad examples, false positives, and the need for workflows usable by defenders.

The Black Hat record provides the richest technical and empirical claims. It states that FACADE has been used to protect Alphabet by “scanning billions of events daily over the last 7 years,” and that it uses corporate logs including document accesses, SQL queries, and HTTP/RPC requests [record_id:87]. This record situates Momeni’s work within large-scale production detection engineering at Google. By contrast, the CAMLIS record is more compact and framework-oriented. It describes a “two-stage hybrid framework” that combines loose YARA rules with an ML classifier, synthetic data generation, and active learning to support SOCs [record_id:125]. This indicates an interest in democratizing enterprise ML detection beyond organizations with massive internal datasets and specialized infrastructure.

The records therefore span two related but distinct research settings:

- **Large-scale proprietary enterprise telemetry and production deployment**, represented by FACADE at Google/Alphabet [record_id:87].
- **Generalizable SOC-oriented ML detection frameworks**, represented by the CAMLIS proposal using YARA, synthetic data generation, and active learning [record_id:125].

## Major Themes And Trends

### 1. Enterprise Security Detection As An ML Systems Problem

Both records frame threat detection not simply as a rule-writing or analyst workflow problem, but as an ML systems problem. FACADE is explicitly described as “Google’s internal AI system for detecting malicious insiders,” with a custom model trained on multiple action types from corporate logs [record_id:87]. The CAMLIS record similarly proposes an “ML-based threat detection” framework for enterprise security that combines rules, classifiers, synthetic data, and active learning [record_id:125].

The shared theme is that modern enterprise defense requires systems able to handle complex behavioral signals and large volumes of data. FACADE’s focus on billions of events per day underscores scale [record_id:87]. The CAMLIS framework’s emphasis on being “self-sustained” and “low-overhead” suggests a concern with SOC practicality and maintainability [record_id:125].

### 2. Reducing Dependence On Scarce Incident Or Attack Data

A strong recurring concern is the scarcity of labeled malicious examples. The FACADE record says the system uses a “novel contrastive learning strategy that relies solely on benign data to overcome the scarcity of incident data” [record_id:87]. This is central to the system’s framing: malicious insider incidents are rare, sensitive, and not easy to collect publicly, so the model is designed to learn from benign activity.

The CAMLIS record addresses a similar constraint through different mechanisms. It proposes “synthetic data generation (Simula)” and “active learning” as part of a self-sustained detection framework [record_id:125]. Synthetic data can supplement limited real attack examples, while active learning can prioritize the most informative samples for human or model feedback. Although the CAMLIS abstract is brief, it points toward the same practical problem: enterprise ML detection cannot assume abundant, high-quality labeled attack datasets.

Together, the records suggest that Momeni’s attributed work treats data scarcity as a primary design constraint and uses self-supervision, contrastive learning, synthetic data, and active learning to mitigate it [record_id:87] [record_id:125].

### 3. High Precision And False-Positive Reduction

False-positive reduction is explicit in the FACADE record and implicit in the CAMLIS framework. FACADE claims “unparalleled accuracy with a false positive rate lower than 0.01%,” and for single rogue actions such as illegitimate access to a sensitive document, it claims a false-positive rate “as low as 0.0003%” [record_id:87]. The stated motivation is insider-threat detection, where false positives can be especially costly because investigations may involve employee behavior, privacy-sensitive logs, and sensitive organizational processes.

The CAMLIS record does not report metrics, but its description of a “low-overhead solution for SOCs” implies concern with alert burden and operational efficiency [record_id:125]. The use of loose YARA rules followed by an ML classifier also suggests a pipeline meant to preserve broad recall at the first stage while using ML to filter or prioritize findings at the second stage [record_id:125]. This approach aligns with common SOC goals: avoid missing suspicious artifacts while reducing the manual cost of triaging noisy detections.

### 4. Hybrid Detection: Combining Context, Heuristics, And Learning

The records do not present ML as a standalone magic solution. Instead, they describe hybrid or context-rich approaches.

FACADE is based on contextual anomaly detection. It detects suspicious actions “by considering the context surrounding each action,” and it uses a “custom multi-action-type model” trained on logs from document accesses, SQL queries, and HTTP/RPC requests [record_id:87]. It also uses clustering to improve detection robustness [record_id:87]. This suggests a system that models behavior in relation to surrounding activity rather than treating events in isolation.

The CAMLIS framework is explicitly hybrid: it combines “loose YARA rules with an ML classifier” and then adds synthetic data generation and active learning [record_id:125]. YARA rules represent expert-defined or pattern-based detection logic, while the ML classifier provides learned discrimination. The word “loose” implies intentionally broad initial matching, likely to increase coverage, with the classifier helping refine results [record_id:125].

Across both records, the trend is toward detection systems that integrate multiple forms of signal: logs, context, rules, generated examples, clustering, and analyst/model feedback [record_id:87] [record_id:125].

### 5. Democratization And Transfer From Elite Environments To Broader SOCs

The FACADE record describes a system used internally at Google/Alphabet and says the talk will show how to use a “just released Facade open-source version” so others can protect their own organizations [record_id:87]. This is a notable bridge from a highly resourced enterprise environment to broader security practitioners. It suggests that the work is not only about reporting internal capabilities, but also about packaging or releasing a usable version for external organizations.

The CAMLIS title explicitly includes “Democratizing ML for Enterprise Security,” and the abstract emphasizes a “self-sustained, low-overhead solution for SOCs” [record_id:125]. This reinforces the idea that Momeni’s attributed work is concerned with making ML detection more accessible and operationally feasible beyond top-tier AI/security organizations.

The democratization theme is supported by both records, though in different ways: FACADE through an open-source version of a production insider-threat detection system [record_id:87], and the CAMLIS framework through a general architecture meant for SOC adoption with lower overhead [record_id:125].

## Methods, Tools, And Approaches Discussed

The records mention several methods and system components relevant to enterprise threat detection.

FACADE is described as a self-supervised ML system for contextual anomaly detection [record_id:87]. Its full name is given as “Fast and Accurate Contextual Anomaly DEtection,” and it is designed to identify malicious insiders by scanning enterprise activity at very large scale [record_id:87]. The model uses corporate logs of document accesses, SQL queries, and HTTP/RPC requests, indicating a multi-modal or multi-event-type approach to user and action modeling [record_id:87]. Its core technical mechanism is described as contrastive learning that uses only benign data, a design choice intended to address the lack of sufficient incident data [record_id:87]. The record also mentions an “innovative clustering approach” to improve detection robustness [record_id:87]. Finally, it says an open-source version of FACADE was released or would be shown during the talk [record_id:87].

The CAMLIS record describes a different but related enterprise detection architecture. It proposes a two-stage hybrid framework that first uses loose YARA rules and then applies an ML classifier [record_id:125]. YARA is commonly associated with pattern-matching rules for malware or artifact detection, but the record itself only states that loose YARA rules are part of the framework; it does not specify target artifacts, feature extraction, or rule content [record_id:125]. The framework also uses synthetic data generation, specifically naming “Simula,” and active learning [record_id:125]. These are intended to make the system “self-sustained” and “low-overhead” for SOCs [record_id:125].

Taken together, the approaches include:

- **Self-supervised learning** for detection without labeled attack examples [record_id:87].
- **Contrastive learning on benign data** to model normal versus suspicious behavior when incident data is scarce [record_id:87].
- **Contextual anomaly detection** across multiple action types and log sources [record_id:87].
- **Clustering** to increase detection robustness [record_id:87].
- **Hybrid rule-plus-ML pipelines** that combine broad YARA-based matching with classifier refinement [record_id:125].
- **Synthetic data generation** through Simula to supplement training or evaluation data [record_id:125].
- **Active learning** to reduce labeling overhead and support a self-sustaining SOC workflow [record_id:125].
- **Open-source deployment pathways** for adapting an internal enterprise detection system to external organizations [record_id:87].

The records do not provide implementation details such as model architecture, feature schemas, training procedures, evaluation datasets, deployment requirements, or analyst feedback loops. However, they provide enough evidence to characterize Momeni’s attributed work as centered on operational ML detection systems for enterprise security.

## Notable Talks, Records, And Evidence

The most detailed and evidentially significant record is the Black Hat USA 2025 briefing **“FACADE: High-Precision Insider Threat Detection Using Contrastive Learning”** [record_id:87]. Sadegh Momeni is one of several listed authors, along with Alex Kantchelian, Elie Bursztein, Birkett Huber, Casper Neo, Yanis Pavlidis, and Ryan Stevens [record_id:87]. The briefing matters because it provides concrete claims about deployment scale, duration, data sources, modeling strategy, and performance. It says FACADE has protected Alphabet by scanning billions of events daily over seven years [record_id:87]. It identifies the problem domain as malicious insider detection and frames the system as filling a public knowledge gap about how to detect insider attacks effectively [record_id:87]. It also reports very low false-positive rates, including below 0.01% overall and as low as 0.0003% for single rogue actions such as illegitimate access to a sensitive document [record_id:87].

This record is important not only because of its technical detail but also because it suggests production maturity. A system operating over billions of events daily for seven years is qualitatively different from a proof-of-concept model evaluated only on a benchmark dataset. That said, the record is still an abstract; it does not include independent validation, experimental design, or full metric definitions. Downstream researchers should treat the performance numbers as claims made in the talk description, not as independently verified results [record_id:87].

The second notable record is the CAMLIS 2025 entry **“Democratizing ML for Enterprise Security: A Self-Sustained Attack Detection Framework”** [record_id:125]. This