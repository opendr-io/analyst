# Topic: Detection engineering, SOC, SIEM, and threat hunting

## Meta-Summary

The records portray detection engineering as a full operational lifecycle rather than merely writing signatures. Effective programs must collect trustworthy telemetry, model environment-specific behavior, correlate events into attack narratives, prioritize work according to risk and analyst cost, validate detections with realistic adversary activity, and continuously feed investigation results back into rules, models, and controls.

Several long-running concerns recur:

- **Alert volume is not equivalent to visibility.** Attackers can hide among low- and medium-severity alerts, deliberately generate noise, exploit data caps, or route activity through trusted services. SOC effectiveness therefore depends on contextual prioritization and investigation, not simply producing more alerts [record_id:17] [record_id:59].
- **Context is the central analytical commodity.** Graphs, timelines, clusters, behavioral baselines, temporal sequences, and attack-flow reconstruction repeatedly outperform isolated-event analysis [record_id:84] [record_id:192] [record_id:193] [record_id:196] [record_id:197] [record_id:2525].
- **Detection quality is constrained by data quality and evaluation quality.** Representative labels, realistic train/test splits, cost-aware metrics, weak-signal evaluation, adversary-generated telemetry, and measurements of analyst outcomes are as important as model choice [record_id:142] [record_id:158] [record_id:184] [record_id:194] [record_id:237] [record_id:2322].
- **AI is shifting from isolated classification toward bounded agents.** Later records describe agents that query SIEMs, reconstruct timelines, author and validate rules, triage alerts, and coordinate specialized workers. The strongest proposals reject unrestricted autonomy in favor of deterministic control planes, explicit trust boundaries, human approval, cross-validation, and measurable evaluations [record_id:130] [record_id:2364] [record_id:2380] [record_id:2381] [record_id:2623] [record_id:2666].
- **Threat-informed validation is becoming inseparable from detection engineering.** Purple teaming, assumed-compromise exercises, adversary emulation, synthetic telemetry, and closed-loop exploit-to-defense pipelines are presented as ways to prove whether controls work rather than infer coverage from documentation [record_id:1908] [record_id:2015] [record_id:2562] [record_id:2658] [record_id:2989] [record_id:2995].
- **Visibility gaps are moving into trusted and specialized environments.** The corpus covers CI/CD and GitHub, cloud identity, macOS, AI agents, collaboration platforms, maritime systems, space systems, industrial control networks, mainframes, and other domains poorly represented in traditional SIEM content [record_id:49] [record_id:1913] [record_id:2075] [record_id:2105] [record_id:2341] [record_id:2675] [record_id:3031] [record_id:3111].

Overall, the records support a move from static, indicator-heavy monitoring toward behavior-centered, context-rich, continuously validated detection systems. They also caution that automation magnifies weaknesses in telemetry, assumptions, labels, and evaluation: an automated SOC built on untrustworthy evidence can fail faster and more confidently than a manual one.

## Research Landscape

The collection spans 2017–2026 and is dominated by conference abstracts, technical talks, workshops, demonstrations, and tool announcements from CAMLIS, Black Hat, DEF CON, BSides Las Vegas, Prompt||GTFO, and [un]prompted. CAMLIS records provide much of the earlier methodological foundation: feature engineering, anomaly detection, graph models, model evaluation, data infrastructure, alert clustering, and analyst-facing explainability. Black Hat and DEF CON contribute operational incidents, offensive tradecraft, detection bypasses, threat hunting case studies, and emerging tools. The 2025–2026 Prompt||GTFO and [un]prompted records emphasize practical LLM and agent workflows, while recent BSides and DEF CON workshops focus on deploying, testing, and teaching those workflows.

The evidence falls into several categories:

1. **Production or large-scale operational claims.** Examples include FACADE scanning billions of events over seven years [record_id:87], BEAM training on more than 40 billion web transactions [record_id:23], a phishing telemetry deployment processing 2.3 million emails per day [record_id:2588], Salesforce reducing 1.8 million prompts to approximately 30 alerts [record_id:2377], and the BETH dataset containing more than eight million events [record_id:194]. These provide stronger evidence than purely conceptual proposals, though most are still talk abstracts rather than independently reproducible studies.

2. **Case studies and incident reconstructions.** The tj-actions compromise [record_id:49] [record_id:2004], North Korean IT-worker hunting [record_id:22] [record_id:2124] [record_id:2586], information-stealer screenshot analysis [record_id:26] [record_id:1945], supply-chain compromises [record_id:2731], and persistent nation-state tracking [record_id:2796] illustrate how detections are created from real incidents.

3. **Research prototypes and benchmark-oriented work.** These include anomaly detectors, graph embeddings, reinforcement-learning defenders, model metrics, and agent evaluations [record_id:116] [record_id:120] [record_id:139] [record_id:153] [record_id:175] [record_id:185] [record_id:2390].

4. **Hands-on operational instruction.** Sigma workshops, Active Directory logging labs, cloud adversary exercises, network hunting workshops, and OT validation platforms provide practical implementation guidance [record_id:2388] [record_id:2448] [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492] [record_id:2777] [record_id:2995].

5. **Offensive research with defensive implications.** ETW injection, EDR evasion, covert C2, ephemeral COM registration, WMI providers, and cloud relay abuse reveal assumptions detection engineers must revisit [record_id:17] [record_id:33] [record_id:2622] [record_id:2862] [record_id:2936] [record_id:3040].

The area broadens over time. Earlier work often asks how to classify an event or encode a security artifact. Middle-period work asks how to aggregate alerts, reconstruct campaigns, and incorporate analysts. The newest records ask how autonomous systems can plan hunts, author detections, execute tools, validate outputs, and compete against autonomous attackers.

## Major Themes And Trends

### Detection is an evidence pipeline, not a rule-writing task

The corpus repeatedly connects detection outcomes to the entire chain from sensor to analyst. Centralized cloud pipelines make it possible to combine endpoint, email, firewall, and other telemetry, but they also create data-quality, cost, and engineering burdens [record_id:157]. Earlier infrastructure work highlights time-aware malware labels, rollback of historical knowledge, regional aggregation, and scalable storage as prerequisites for credible model development [record_id:214]. OmnibusCyber similarly argues that fragmented schemas obstruct correlation and intelligence exchange [record_id:189].

SIEM economics can directly create blind spots. FLASI is motivated by organizations filtering firewall events because per-event licensing makes full ingestion unaffordable [record_id:2727]. GCP Workload Identity Federation illustrates a related problem: setup activity may be logged for free while evidence of credential use requires paid telemetry, leaving defenders able to see persistence creation but not its exploitation [record_id:2787]. The forward-looking SOC critique likewise identifies fragmented tools, restricted data ecosystems, and disconnected workflows as systemic limitations [record_id:105].

This supports a practical conclusion: a detection specification should include required telemetry, schema assumptions, retention, expected volume, cost, validation data, triage context, and failure behavior—not merely query syntax.

### Telemetry itself is adversarial

Several records directly challenge the assumption that logs faithfully represent reality. ETW event injection can fabricate attack telemetry, mislead analysts, trigger EDR event caps, and suppress subsequent genuine events [record_id:17]. Synthetic passwords can pollute authentication logs and obscure credential attacks [record_id:2556]. SEND goes further by proposing narrative poisoning: generating authentic telemetry and coherent artifacts that steer analysts toward a false causal explanation even if every event is technically detected [record_id:2997].

Attackers also exploit trusted paths where instrumentation is weaker. Web-conferencing TURN servers can carry interactive C2 because enterprises whitelist provider infrastructure and exempt it from inspection [record_id:33] [record_id:1913]. SMTP/IMAP through Outlook can bypass web-isolation assumptions [record_id:2536]. Azure Relay and AWS IoT services can provide C2 through domains organizations cannot easily block [record_id:3040]. COM, WinRT, WMI providers, and dynamically registered COM objects can sever or distort expected process lineage [record_id:2622] [record_id:2862] [record_id:2936].

These records collectively argue for **telemetry diversity and integrity checks**. A process-tree alert should be corroborated with registry, ETW, network, RPC, identity, or application-level evidence. Detection engineers must also test saturation, suppression, spoofing, and causal-story manipulation—not only whether a nominal malicious action produces an alert.

### Context and correlation are the answer to alert overload

Alert overload is one of the strongest themes. “Death by Noise” shows attackers intentionally staying within the medium/low-severity majority that SOCs neglect [record_id:59]. Event clustering proposes reusing historical analyst decisions and resolving groups of related alerts together [record_id:192]. CLEAR-ROAD mines rare, temporally co-occurring signatures around critical alerts without requiring labeled training data [record_id:208]. HeAT reconstructs preceding attack stages around a critical indicator [record_id:196], while pairwise campaign detection connects heterogeneous records into broader incidents [record_id:193].

Graph and sequence representations recur because they preserve relationships that flat tables discard. Incident-report summarization uses dynamic graphs to reduce report size by as much as 61% while improving precision [record_id:197]. Graph-based process analysis exposes suspicious parent-child chains [record_id:221]. Kubernetes sessions [record_id:153], enterprise user-resource interactions [record_id:154], Azure sign-ins [record_id:175], and attack campaigns [record_id:243] are all modeled relationally. Recent workshops explicitly teach analysts to transform endpoint, identity, network, and alert tables into investigative graphs [record_id:2797].

The 2025–2026 records extend this trend to root-cause and attack-flow systems. Lightweight correlation over time, topology, and behavior is proposed for constrained IoT settings [record_id:1935], while Attack Flow Detector uses clustering, temporal knowledge graphs, and Markovian sequencing to map events to ATT&CK [record_id:2525]. Data from 95 red-team engagements suggests operators repeatedly spiral between discovery and credential access rather than follow a linear kill chain, warning that overly rigid attack-stage models may misrepresent real activity [record_id:2722].

### Behavioral baselines are replacing brittle blocklists and isolated indicators

Numerous records favor modeling how an entity normally behaves. BEAM establishes application-specific web-traffic baselines to identify compromised trusted software [record_id:23]. Logrip distinguishes human and automated web access through statistical patterns and hierarchical IP aggregation [record_id:37]. FACADE models action context using benign-only contrastive learning [record_id:87]. AWS principal hunting builds individualized IAM baselines rather than applying one global rule [record_id:2813].

The same principle appears in fraud, infrastructure, and specialized networks. TF-IDF links entities through transaction and device metadata [record_id:78]. Distributional NetFlow features identify botnet hosts [record_id:179]. IP models extend blocklist coverage to unseen addresses [record_id:205]. Domain intelligence and infrastructure fingerprints are used to identify related domains before they become public IOCs [record_id:1877] and to cluster actor infrastructure through TLS, SSH, and web fingerprints [record_id:3118]. Finch favors persistent TLS/HTTP fingerprints over fast-decaying IP lists [record_id:1948].

Behavioral models also appear in OT and maritime systems: deterministic NMEA2000 fingerprints [record_id:2049], context-aware CAN analysis [record_id:2102], and a four-model NMEA2000 autoencoder ensemble covering timing, payload, frequency, and device behavior [record_id:3057]. These approaches are promising, but they depend on stable baselines and must handle legitimate change, seasonality, operational transitions, and attacker mimicry.

### Anomaly detection is being reassigned, not abandoned

The records show growing skepticism toward treating anomalies as alerts. Command-line anomaly detection often produces unacceptable false positives [record_id:89]. The proposed remedy is to use anomalies to find diverse benign examples for supervised training. Later work generalizes this into a pipeline that surfaces long-tail benign and malicious files, labels them with calibrated LLM prompts, and augments production classifiers [record_id:2791].

Other work improves anomaly detection itself. DIP-ECOD splits multimodal distributions before scoring outliers [record_id:139]. Point-process models account for temporal dependencies in authentication [record_id:246]. A sticky hierarchical Bayesian model detects temporal attacks across heterogeneous cyber-physical telemetry [record_id:186]. DistilBERT models shell-session syntax and behavior [record_id:169]. Distributional and graph representations similarly aim to make “normal” more context-sensitive [record_id:154] [record_id:179].

The emerging consensus is that anomaly detection is useful for candidate generation, data curation, exploration, and baseline deviation—but often unsafe as an unmediated high-severity alert source.

### Evaluation is becoming cost-aware, adversarial, and workflow-oriented

Several records reject generic accuracy metrics. Cscore incorporates the unequal operational costs of false positives and false negatives and reports average cost savings of 49% over F1-based thresholding [record_id:142]. Firenze evaluates model changes using expert-defined weak signals and statistical tests when ground truth is noisy [record_id:184]. Harder train/test splits expose small but operationally significant malware-model improvements [record_id:158]. Bayesian methods estimate classifier uncertainty rather than treating raw output scores as confidence [record_id:248].

The later agent literature broadens evaluation beyond final answers. Agent effectiveness must include reasoning quality, evidence gathering, and tool-calling behavior [record_id:2322]. CTF-based investigation agents can appear successful by memorizing answers, exploiting leaks, or bypassing logs, turning the benchmark itself into an attack surface [record_id:2789]. A 70% per-step success rate compounds disastrously across a ten-step investigation, illustrating why end-to-end evaluation matters. Red-versus-blue agent benchmarks use offensive execution traces as ground truth and reveal that investigation agents often fail to reconstruct full autonomous kill chains [record_id:2666].

Operational measurement remains unresolved. “Winning From Constraints” argues that many SOCs cannot tell whether they are succeeding against mostly unseen adversaries [record_id:2768]. This aligns with calls for measurable purple-team outcomes rather than alert counts [record_id:1908] [record_id:2015].

### Human factors remain central

Automation is generally framed as analyst augmentation, not analyst elimination. Explainable alert classification gives analysts the prediction, relevant decision path, and features while collecting disagreement feedback [record_id:244]. Incident prioritization models use attention to expose which multimodal features influenced severity [record_id:199]. Structured analytic techniques address cognitive bias in attribution and intelligence work [record_id:2561]. A basketball-officiating analogy emphasizes teamwork and judgment in SOC decisions [record_id:1881].

Training records reinforce the importance of people and organization: role-playing exercises make incident response accessible across technical and nontechnical roles [record_id:2425]; the Cyber Incident Command System addresses coordination rather than sensor logic [record_id:2423]; OT SOCs must preserve safety and continuity [record_id:2079]; and career-path ambiguity can contribute to analyst stagnation and turnover [record_id:2739]. The collection also raises governance concerns about whose incidents receive resources and protection [record_id:2701].

### AI moves from assistant to bounded operator

Early AI use cases include SQL generation, severity classification, IOC summarization, URL categorization, and command classification [record_id:166] [record_id:168] [record_id:191]. Later systems generate prompts for log analysis [record_id:2190], extract structured threat intelligence and create Sigma rules [record_id:2204], automate collection and reporting [record_id:2226], and connect reverse-engineering tools to rule generation [record_id:2228].

The newest records describe multi-agent systems. Timesketch’s agent hunts across large forensic timelines [record_id:84]. Datadog automates hypothesis generation, query refinement, and evidence narrowing while explicitly defining an “automation boundary” [record_id:2364]. Salesforce proposes supervisor-worker architectures rather than monolithic agents [record_id:2380] [record_id:2381]. Roblox’s detection-engineering pipeline separates research, gap analysis, rule engineering, adversarial review, and runtime validation into isolated stages, while its hunting graph uses a bounded state machine [record_id:2623].

Practical records repeatedly favor constrained architectures:

- use deterministic parsing when syntax conversion does not need generative reasoning [record_id:2233];
- separate DLP and anomaly prompts rather than overloading one prompt [record_id:2190];
- use cheap classifiers, fingerprints, or rules before expensive LLM calls [record_id:1948] [record_id:2342];
- keep humans in control for high-impact actions [record_id:130] [record_id:2788] [record_id:3024];
- evaluate traces, not only final responses [record_id:2322] [record_id:2789];
- preserve privacy through local models or fingerprints [record_id:2327] [record_id:2516].

Evidence for fully autonomous SOC operation remains thin. Competition data shows AI can rapidly fill knowledge gaps but is often used reactively, suffers safety-filter mismatches, and does not automatically create strategic defensive behavior [record_id:2734].

### Threat-informed defense and purple teaming become continuous engineering

Adversary simulation appears throughout the collection as a source of labeled data and validation evidence. Red-team activity can generate positive labels for supervised detection [record_id:237]. Adaptive honeypot experimentation provides stronger causal conclusions with fewer resources [record_id:159]. Agent-based simulation generates multi-stage telemetry under human-approved plans [record_id:130]. Assumed-compromise purple teaming tests visibility across the complete attack lifecycle rather than spending the exercise proving initial access [record_id:2015].

The newest frameworks aim to close the loop. One proposal turns a successful exploit into Falco, WAF, Sigma, and Terraform defenses within minutes, with each output serving as a test case [record_id:2658]. ICSForge generates safe industrial traffic and PCAPs for 500-plus scenarios mapped to 68 ATT&CK for ICS techniques [record_id:2995]. Identity-first playbooks specify expected telemetry, hypotheses, failure points, and scoring [record_id:3017]. ThreatPatrol links intelligence, atomic tests, detections, and coverage gaps in one relational platform [record_id:3078].

This is a shift from “do we have a rule?” toward “have we observed, tested, and measured this defensive behavior under realistic conditions?”

## Methods, Tools, And Approaches Discussed

### Detection logic and portable rules

Sigma is the most visible portable detection format. Workshops describe authoring, translating, and integrating Sigma into hunting workflows across SIEM and EDR platforms [record_id:2448] [record_id:2529]. RAGnarok uses a local quantized model, retrieval, and specialized agents to generate environment-aware Sigma rules without sending telemetry externally [record_id:2516]. Splunk2Sigma demonstrates that an LLM can help create a deterministic converter, but deterministic parsing is faster and more reliable for routine translations [record_id:2233].

Rule generation extends beyond Sigma. LLMDYara combines expert-extracted strings, function signatures, DNAHash, billion-scale allowlist filtering, and LLM interpretation to generate explainable YARA rules [record_id:61]. Binary Ninja’s MCP integration produces YARA, Suricata, and Sigma content from malware analysis [record_id:2228]. Tree-sitter analyzes script syntax trees to detect and deobfuscate PowerShell payloads and AMSI bypasses [record_id:2430]. GAVEL and SYARA adapt rule metaphors to neural activation states and multimodal semantic threats [record_id:2652] [record_id:2342].

The records favor layered rule systems: cheap deterministic checks first, contextual or semantic models second, and human or runtime validation before deployment.

### Alert triage, prioritization, and analyst interfaces

Nearest-neighbor clustering reuses prior analyst resolutions and exposes cluster-level timelines, maliciousness estimates, and label diversity [record_id:192]. Neural severity scoring integrates TTP, attack success, duration, source and destination roles, service, location, and textual description [record_id:199]. Night Beacon combines a locally fine-tuned BERT model, custom rule sets, log translation, and analyst feedback inside a SOAR workflow [record_id:2240].

Other systems emphasize explanation and visualization. Model decision paths help analysts validate predictions [record_id:244]. Dynamic-graph summarization identifies core sequences and removes low-value branches [record_id:197]. HeAT and CLEAR-ROAD surface related stages or co-occurring signatures around critical indicators [record_id:196] [record_id:208]. Cognitive-agent proposals add business impact, intent, and timeline reconstruction [record_id:2530].

### Threat hunting and investigation

Hypothesis-driven hunting appears in enterprise, OT, cloud, and agent contexts. Datadog’s agents generate and refine hypotheses [record_id:2364]; OT hunting emphasizes safe testing and operational coordination [record_id:2980]; AWS hunting establishes principal-specific baselines [record_id:2813]; and maritime SOC/NOC collaboration starts with asset discovery and operational baselining [record_id:3031].

Graph workflows are especially prominent. Threat intelligence embeddings enable personalized retrieval and pivoting [record_id:145]. Campaign models vectorize heterogeneous logs [record_id:193]. Attack Flow Detector constructs temporal graphs [record_id:2525]. Tour de Graph teaches Cypher-based investigative iteration [record_id:2797]. Causal graphs built from red-team terminal sessions reveal operator knowledge flow and overlooked failed-action artifacts [record_id:2722].

AI-assisted investigation methods include parallel agents and self-generated plans with cross-validation [record_id:2222], autonomous Timesketch analysis [record_id:84], reusable investigation skills and trace-based evaluation [record_id:2801], and bounded SIEM state machines [record_id:2623].

### Behavioral and machine-learning methods

The records cover:

- graph neural networks for Kubernetes and authentication [record_id:153] [record_id:175];
- matrix factorization and link prediction for insider behavior [record_id:154];
- contrastive learning on benign enterprise activity [record_id:87];
- TF-IDF entity similarity for fraud [record_id:78];
- DistilBERT and shell-specific tokenization for command analysis [record_id:169] [record_id:191];
- random forests over lexical URL features [record_id:223];
- security-specific encoders for IPs, domains, usernames, URLs, and geography [record_id:224];
- point processes for authentication timing [record_id:246];
- autoencoders and deep sequence models for CAN/NMEA traffic [record_id:2102] [record_id:3057];
- hierarchical and multi-stage models for attacks spanning several entities and data sources [record_id:251] [record_id:257] [record_id:258];
- distributional features and dynamic ensembles for network detection [record_id:179] [record_id:2390].

The repeated design lesson is that domain representation and object definition matter more than selecting a fashionable model. The web-shell case study, for example, carefully defines connected objects from host, destination, URI, source, and user-agent relationships before modeling [record_id:174].

### Data generation, labeling, and simulation

Threat emulation is used to generate realistic malicious examples [record_id:174] [record_id:237]. BETH provides host-level benign and attack activity [record_id:194], while the Splunk dataset project gives researchers curated material for experimentation [record_id:236]. Simula and active learning support a self-sustaining hybrid YARA/ML framework [record_id:125]. Marinade injects validated synthetic vulnerabilities into realistic applications for scanner and red-team evaluation [record_id:2344].

Adaptive experimental design improves honeypot data collection [record_id:159]. The agent simulation framework provisions controlled infrastructure and executes approved adversary plans [record_id:130]. Space, maritime, automotive, and nuclear testbeds provide otherwise scarce domain-specific data [record_id:2049] [record_id:2071] [record_id:2978] [record_id:3024] [record_id:3057].

### Deception and tripwires

Honeytokens provide low-overhead alerts when attackers search for credentials [record_id:2755]. LOTLE creates environment-specific decoy credentials, documents, and landing zones with Caldera, Engage, OpenCanary, and Blue Agave [record_id:2657]. Azazel aims to delay automated attackers through an actively engaging gateway [record_id:2397]. A fictional, automated company expands deception from a single honeypot into believable business infrastructure [record_id:2834]. ICS deception is aligned to MITRE Engage and an APT44 case study [record_id:2095].

The corpus also covers offensive counter-deception. SEND targets analyst reasoning rather than sensors [record_id:2997], making a strong case that defenders should evaluate whether decoy or attack artifacts distort incident narratives.

### Specialized telemetry and domain methods

Endpoint records include AMSI inspection of PowerShell [record_id:216], registry item-set mining [record_id:183], hardware performance counters for Spectre detection [record_id:209], in-memory artifact clustering [record_id:250], Apple Endpoint Security [record_id:1964], macOS queue and XPC telemetry [record_id:2635], and built-in macOS telemetry for contemporary malware [record_id:2793].

Network methods include Zeek metadata [record_id:174], NetFlow distributions [record_id:179], TLS/HTTP fingerprints [record_id:1948], DNS and domain intelligence [record_id:1877], Rayhunter cellular control-plane analysis [record_id:1922], rogue wireless and WIDS testing [record_id:2700], and firewall-log pipelines [record_id:2727].

Cloud and identity work covers Azure authentication graphs [record_id:175], MFA reverse-proxy detection [record_id:156], Jamf API abuse [record_id:77], multi-cloud investigations [record_id:2599], OAuth authorization phishing [record_id:2775], GCP WIF [record_id:2787], and identity-first adversary emulation [record_id:3017].

OT and cyber-physical approaches stress passive visibility, safety, baselines, and simulation: MOSAICS [record_id:2075], specialized OT SOC operations [record_id:2079], CAN correlation [record_id:2102], neural OT attack-surface-reduction rules [record_id:2113], NMEA fingerprints [record_id:2049], hands-on OT hardening [record_id:2719], ICSForge [record_id:2995], NICSSIM [record_id:3024], and SpaceCOP [record_id:3111].

## Notable Talks, Records, And Evidence

### High-value operational evidence

FACADE is one of the strongest production claims: seven years of use, billions of daily events, benign-only training, and reported false-positive rates below 0.01%, including 0.0003% for single rogue actions [record_id:87]. The record is unusually concrete, though independent validation and implementation details remain necessary.

BEAM is notable for scale and its shift from software provenance to runtime application behavior. It reports training on over 40 billion HTTP/HTTPS transactions, 65 behavioral signals, and more than 95% accuracy, rising to 99% for predictable applications [record_id:23]. Its accuracy claims need class-balance and operational false-positive context, but the underlying idea is highly relevant to trusted-software compromise.

The email-to-SIEM study reports 18 months of operation, 2.3 million daily emails, five Sigma rules, a 72% detection improvement, and reduction of detection time from 4.2 hours to 12 minutes [record_id:2588]. It is representative of detection engineering that begins where a preventive control’s operational constraints end.

Salesforce’s agent ecosystem hunting offers another useful scale reference: 1.8 million prompts and contextual baselines distilled into fewer than 30 daily alerts [record_id:2377]. It supports the claim that rarity and behavioral complexity can make user-defined agent environments operationally monitorable.

### Representative SOC workflow records

The alert-clustering workflow is an early, concrete attempt to incorporate prior analyst decisions into current triage and expose group-level context without removing the analyst from the decision [record_id:192]. Incident-report summarization provides quantifiable analyst-facing gains rather than only model metrics [record_id:197]. The SOC transformation talk captures the organizational problem of fragmented tools and data [record_id:105], while Microsoft’s account emphasizes real-time feedback among intelligence, hunting, incident response, and bounty programs [record_id:95].

Night Beacon [record_id:2240], cognitive agents [record_id:2530], and the Agentic SOC supervisor-worker architecture [record_id:2380] [record_id:2381] show the progression from ML-assisted reprioritization to coordinated autonomous action. Roblox’s bounded multi-agent detection and hunting frameworks provide the clearest architecture for this shift [record_id:2623].

### Representative validation and purple-team records

“Labeling Red” is foundational because it treats adversary simulations as labeled detection data while acknowledging bias and imbalance [record_id:237]. “Letthemin” provides a repeatable assumed-compromise method focused on visibility across defense layers [record_id:2015]. The agent-based simulation framework adds adaptive planning, real execution, telemetry generation, human approval, and safety boundaries [record_id:130].

The most ambitious closed-loop proposal converts a validated exploit into deployed defensive outputs in under five minutes [record_id:2658]. ICSForge provides more measurable, domain-specific validation by generating safe, ATT&CK-mapped industrial traffic [record_id:2995]. These records collectively represent the strongest direction for converting threat intelligence into testable defenses.

### Representative adversarial telemetry records

ETW injection is critical because it attacks the evidentiary substrate itself [record_id:17]. “Death by Noise” targets severity and analyst prioritization rather than EDR installation [record_id:59]. TURNt abuses trusted real-time communications infrastructure [record_id:33] [record_id:1913]. Surrogate Ghost and COM/WinRT research reveal gaps created by telemetry models centered on known identifiers and command-line ancestry [record_id:2622] [record_id:2936]. SEND generalizes this line of work to analyst cognition and causal narratives [record_id:2997].

### Representative AI evidence

Timesketch’s autonomous timeline agent reports evaluation on 100 compromised systems [record_id:84]. The “vibes investigating” record reports near-complete success on intermediate CTF tasks but only about 50% on harder tasks, offering a useful picture of current limitations [record_id:2222]. Datadog explicitly discusses hallucinations, trust, and where automation should stop [record_id:2364]. The red-versus-blue agent benchmark is important because it evaluates full investigations under machine-speed adversarial pressure rather than static questions [record_id:2666].

The deterministic Splunk-to-Sigma experience is a valuable counterweight to agent enthusiasm: the LLM was most useful for building a parser, while the resulting deterministic tool performed conversions in fractions of a second [record_id:2233]. The evidence supports selective rather than universal use of generative models.

## Gaps, Limits, And Open Questions

### Most claims are abstracts rather than full evaluations

Many records provide headline accuracy, scale, or latency without prevalence, confidence intervals, deployment duration, analyst acceptance, or comparison against realistic baselines. Even apparently strong claims—BEAM’s accuracy [record_id:23], FACADE’s false-positive rates [record_id:87], dynamic ensemble accuracy [record_id:2390], and semantic-rule performance [record_id:2342]—require full papers, code, datasets, and reproducibility work before generalization.

Several records contain little or no raw detail, particularly ARNIE [record_id:178], malicious MDA enrollment [record_id:188], scalable temporal analytics [record_id:255], and self-organizing-map anomaly detection [record_id:260]. They establish topic presence but cannot support substantive conclusions.

### Cross-environment generalization remains uncertain

Behavioral baselines may perform well in one organization and fail under organizational change, mergers, seasonal operations, or novel workloads. The corpus rarely quantifies model drift, retraining burden, or transfer across tenants. TERLA, contextual reinforcement learning, and network-agnostic campaign extraction explicitly tackle generalization [record_id:116] [record_id:120] [record_id:196], but the broader question remains open.

### The human outcome is undermeasured

Some work reports reduced report size, fewer alerts, or analyst praise [record_id:192] [record_id:197] [record_id:244], but few records measure investigation accuracy, time to containment, burnout, missed incidents, or consistency over long deployments. Claims of automation benefits should be tested against complete workflows, including handoffs and escalation.

### Agent security and agent reliability collide

Agents can accelerate hunting while introducing new incidents, as shown by AI coding assistants causing destructive production changes that resemble breaches [record_id:2699]. AI infrastructure is itself scanned and attacked [record_id:3012] [record_id:3113]. Prompt-injection fingerprints [record_id:2327], semantic rules [record_id:2342], activation monitoring [record_id:2346] [record_id:2652], and GenAI endpoint observability [record_id:2341] are emerging responses, but standardized schemas, forensic retention, and access-control patterns are not settled.

Open questions include:

- What minimum audit trail is required to reconstruct an agent’s tool calls and authority changes?
- How should SOCs distinguish malicious agent behavior from over-permissioned but non-adversarial mistakes?
- How can evaluation datasets prevent memorization and benchmark gaming?
- Which actions may agents take autonomously, and which require human approval?
- How should agent-generated detections be tested for hallucinated fields, impossible predicates, and unsafe response logic?

### Detection economics are insufficiently studied

The records identify SIEM licensing [record_id:2727], paid cloud logging [record_id:2787], LLM token costs [record_id:2190], and scarce analyst time [record_id:59], but do not provide a common model for optimizing total detection cost. Cscore is a useful foundation [record_id:142], yet future work should include ingestion, retention, compute, analyst review, response disruption, and missed-incident cost.

### Specialized environments still lack shared datasets

Maritime, space, nuclear, automotive, and industrial environments repeatedly cite scarce telemetry and operational constraints [record_id:2049] [record_id:2071] [record_id:2978] [record_id:3024] [record_id:3057] [record_id:3111]. Simulation platforms help, but realism, transfer to operational systems, and safety-preserving validation remain open problems.

### Threat intelligence still struggles to become deployed defense

Personalization, graph representations, structured analysis, and automated collection all attempt to reduce irrelevant intelligence [record_id:145] [record_id:215] [record_id:2226] [record_id:2561]. Yet fragmentation across providers and long attribution delays remain severe [record_id:2439]. The most important research question is not how many indicators a system ingests, but how reliably it converts intelligence into tested, environment-specific hypotheses and controls.

## Coverage And Evidence Notes

The early CAMLIS material establishes the methodological roots of this topic. It covers scalable and security-specific feature engineering, model selection, temporal analysis, graph reasoning, and operational datasets: anticipatory defense [record_id:232], community datasets [record_id:236], adversary-simulation labels [record_id:237], attribution clustering [record_id:243], analyst explanations [record_id:244], authentication timing [record_id:246], fake-account bursts and their ethical risks [record_id:247], uncertainty estimation [record_id:248], memory-based malware detection [record_id:250], multi-stage classification [record_id:251], social-media threat classification [record_id:252], scalable nearest-neighbor analysis [record_id:253], temporal coordination analytics with no detailed abstract [record_id:255], hyperparameter optimization [record_id:256], hierarchical enterprise detection [record_id:257], low-volume denial-of-service modeling [record_id:258], conversational security interfaces [record_id:259], self-organizing-map anomaly detection with no substantive raw text [record_id:260], and behavioral network pipelines [record_id:261].

The 2019–2023 CAMLIS records deepen operational detection research. They include scalable malware-label infrastructure [record_id:214], social-media intelligence extraction [record_id:215], AMSI-based PowerShell detection [record_id:216], parent-child process graphs [record_id:221], lexical malicious-URL detection [record_id:223], domain-specific feature encoders [record_id:224], shell preprocessing [record_id:191], alert clustering [record_id:192], campaign detection [record_id:193], the BETH dataset [record_id:194], HeAT campaign extraction [record_id:196], incident summarization [record_id:197], severity prioritization [record_id:199], insider-incident visualization [record_id:201], malicious infrastructure learning [record_id:205], temporal alert mining [record_id:208], hardware-counter detection [record_id:209], adversarial-drift monitoring [record_id:211], web-shell detection [record_id:174], Azure sign-in graphs [record_id:175], homoglyph-domain modeling [record_id:177], ARNIE’s artifact-vectorization topic with an empty abstract [record_id:178], NetFlow distribution modeling [record_id:179], registry mining [record_id:183], weak-signal evaluation [record_id:184], explained reinforcement-learning defense [record_id:185], cyber-physical temporal modeling [record_id:186], malicious device-enrollment detection with no raw detail [record_id:188], and security knowledge representation [record_id:189].

The remaining CAMLIS records cover the transition toward more sophisticated ML and agentic defense: web filtering through LLM distillation [record_id:166], LLM security benchmarks [record_id:168], transformer-based shell anomaly detection [record_id:169], Kubernetes graph embeddings [record_id:153], enterprise insider graphs [record_id:154], MFA-proxy detection [record_id:156], SQL-driven MLOps [record_id:157], harder malware benchmarks [record_id:158], adaptive intrusion experiments [record_id:159], reinforcement-learning exfiltration analysis [record_id:162], generalizable cyber-defense agents [record_id:116], test-time compute for alert triage [record_id:117], contextual reinforcement learning [record_id:120], open-source social-threat modeling [record_id:123], hybrid YARA/ML detection [record_id:125], safe agent-based simulation [record_id:130], LLM-assisted TTP attribution [record_id:137], multimodal anomaly detection [record_id:139], cost-aware evaluation [record_id:142], personalized threat intelligence [record_id:145], malware benchmark design [record_id:158], and graph/sequence approaches already discussed.

The 2025 Black Hat records provide a cross-section of contemporary operational problems. They include telemetry manipulation [record_id:17], North Korean worker OSINT [record_id:22], application-behavior supply-chain detection [record_id:23], stealer screenshot analysis [record_id:26], partial detection of z/OS Unix attacks [record_id:27], conferencing-based C2 [record_id:33], bot-log visualization [record_id:37], tj-actions incident detection [record_id:49], criminal traffic-distribution infrastructure [record_id:52], SOC noise exploitation [record_id:59], automated YARA generation [record_id:61], enterprise AI attack-chain detections [record_id:71], Jamf abuse detection [record_id:77], TF-IDF fraud analytics [record_id:78], Timesketch agents [record_id:84], insider detection [record_id:87], benign-anomaly training [record_id:89], unified Microsoft intelligence and hunting [record_id:95], Black Hat NOC operations [record_id:98], and SOC architecture reform [record_id:105].

DEF CON 33 adds domain-specific hunts and operational practice. DNS intelligence [record_id:1877], AI-enabled phishing defense [record_id:1878], SOC teamwork [record_id:1881], airborne evil-twin investigation [record_id:1892], modern purple teaming [record_id:1908], TURNt [record_id:1913], cellular PCAP collection [record_id:1922], IoT attack-flow context [record_id:1935], adversarial mindset [record_id:1939], infostealer artifact extraction [record_id:1945], fingerprint-aware bot blocking [record_id:1948], mainframe Unix detection [record_id:1949], macOS Endpoint Security [record_id:1964], Cowrie honeypot history [record_id:1986], quantum-platform monitoring [record_id:1996], community cyber defense [record_id:2001], tj-actions reconstruction [record_id:2004], assumed-compromise purple teaming [record_id:2015], anti-cheat/EDR parallels [record_id:2017], Reddit-scale defense [record_id:2019], Russian APT adoption of offensive research [record_id:2024], Chinese relay networks [record_id:2025], intercepted malware communications [record_id:2027], researcher-targeting investigations [record_id:2032], maritime fingerprints [record_id:2049], automated TTP selection [record_id:2056], blockchain investigation [record_id:2060], climate-related OT threats [record_id:2070], space purple teaming [record_id:2071], maritime OSINT [record_id:2074], naval MOSAICS [record_id:2075], OT SOC operations [record_id:2079], ICS deception [record_id:2095], CAN anomaly detection [record_id:2102], spacecraft indicators of behavior [record_id:2105], neural OT rules [record_id:2113], corporate-network fraud hunting [record_id:2124], continuous crisis simulation [record_id:2129], and maritime incident response [record_id:2133].

The Prompt||GTFO records are practical demonstrations rather than controlled studies. They cover threat-hunting notebooks and LLM detection discussion [record_id:2187], prompt-generated log analysis [record_id:2190], structured threat-intelligence extraction [record_id:2204], parallel CTF investigators [record_id:2222], n8n intelligence automation [record_id:2226], Binary Ninja MCP [record_id:2228], deterministic versus LLM query translation [record_id:2233], linguistic phishing triage [record_id:2235], Night Beacon SOC assistance [record_id:2240], and minimal-token social-engineering prompts [record_id:2244].

The [un]prompted records focus on agent measurement and AI-native telemetry. They include multidimensional agent evaluation [record_id:2322], privacy-preserving AI threat fingerprints [record_id:2327], multi-agent incident triage [record_id:2332], endpoint observability for AI-spawned processes [record_id:2341], semantic YARA-like rules [record_id:2342], synthetic vulnerability generation [record_id:2344], activation-level monitoring [record_id:2346], the automation boundary for hunting [record_id:2364], internet-scale detection and deception agents [record_id:2365], a comparison topic for traditional ML and LLM classification with little detail [record_id:2371], production prompt-abuse baselining [record_id:2377], and supervisor-worker Agentic SOC presentations [record_id:2380] [record_id:2381].

BSidesLV 2025 contributes implementation and training material: AD attack/defense logging [record_id:2388], dynamic network ensembles [record_id:2390], active deception and delay [record_id:2397], incident-command organization [record_id:2423], role-playing exercises [record_id:2425], syntax-tree script detection [record_id:2430], fragmented CTI [record_id:2439], Sigma hunting [record_id:2448], quantum-era anomaly detection [record_id:2457], four linked multi-cloud workshop sessions [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492], RAG/MCP support for triage and compliance [record_id:2515], local-LLM hunting [record_id:2516], attack-flow correlation [record_id:2525], Sigma rule portability [record_id:2529], cognitive SOC agents [record_id:2530], Outlook C2 detection [record_id:2536], dMSA privilege-escalation detection [record_id:2547], synthetic-password noise [record_id:2556], MISP-enhanced investigations [record_id:2559], structured intelligence analysis [record_id:2561], adversary-emulation exercises [record_id:2562], and LLM fine-tuning as covert C2 [record_id:2573].

Black Hat 2026 records extend several themes: forensic evidence and detection strategies for North Korean workers [record_id:2586], phishing detections outside gateway controls [record_id:2588], multi-cloud incident reconstruction [record_id:2599], ephemeral COM analytics [record_id:2622], bounded agentic detection and hunting [record_id:2623], macOS concurrency telemetry [record_id:2635], neural-state rules [record_id:2652], environment-native deception [record_id:2657], closed-loop exploit-to-defense automation [record_id:2658], adversarial agent benchmarks [record_id:2666], and GitHub behavioral EDR [record_id:2675].

BSidesLV 2026 broadens the operational and governance landscape. It includes AI-induced incident triage [record_id:2699], rogue-wireless validation [record_id:2700], bias in defensive resource allocation [record_id:2701], practical OT security [record_id:2719], empirical red-team action graphs [record_id:2722], lower-cost firewall analytics [record_id:2727], npm incident-response telemetry [record_id:2731], AI performance under competition pressure [record_id:2734], SOC career development [record_id:2739], honeytokens [record_id:2755], outcome measurement [record_id:2768], OAuth authorization phishing [record_id:2775], AI-assisted network hunting skills [record_id:2777], GCP WIF hunting [record_id:2787], on-device IoT log explanation [record_id:2788], adversarial benchmark integrity [record_id:2789], long-tail training-data augmentation [record_id:2791], macOS malware telemetry [record_id:2793], persistent counterintelligence [record_id:2796], graph investigations [record_id:2797], investigation-agent engineering [record_id:2801], threat-actor intelligence training [record_id:2807], North Korean malware hunting [record_id:2810], AWS principal baselines [record_id:2813], social-engineering sequences [record_id:2831], AI-assisted package monitoring [record_id:2832], large-scale deception [record_id:2834], and Windows credential-theft signal mapping [record_id:2840].

Finally, DEF CON 34 records emphasize adversarial validation and specialized environments. They cover distributed WMI post-exploitation [record_id:2862], COM/WinRT telemetry gaps [record_id:2936], North Korean C2 infrastructure agents [record_id:2975], aerospace defense research environments [record_id:2978], hypothesis-driven OT hunting [record_id:2980], threat-intelligence-to-simulation workflows [record_id:2989], ICS coverage validation [record_id:2995], a lightly described major-breach account [record_id:2996], investigation-narrative poisoning [record_id:2997], AI-infrastructure honeypots [record_id:3012], identity-first emulation [record_id:3017], guarded nuclear-OT agents [record_id:3024], maritime SOC/NOC hunting [record_id:3031], multi-agent supply-chain scanning [record_id:3032], trusted-cloud C2 [record_id:3040], AI-orchestrated industrial attack emulation [record_id:3046], maritime autoencoder IDS [record_id:3057], autonomous reconnaissance and its detectable signatures [record_id:3060], realistic expectations for AI red teams [record_id:3069], integrated intelligence and validation [record_id:3078], game-cheat detection as a peripheral detection case [record_id:3096], onboard spacecraft IDS [record_id:3111], exposed-agent reconnaissance [record_id:3113], autonomous adversary emulation [record_id:3115], and infrastructure-centric threat hunting [record_id:3118].

Taken together, even the peripheral records reinforce the central finding: modern detection engineering succeeds when telemetry, context, analyst workflows, adversary behavior, and validation are treated as one continuously measured system.