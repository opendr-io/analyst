# Topic: Author: Subhabrata Majumdar

## Executive Summary

The available record set for Subhabrata Majumdar is very small: two CAMLIS-attributed records, one from 2022 and one from 2025. Only one record contains substantive raw abstract text. That substantive record describes machine-learning-based detection of botnet command-and-control hosts in large-scale IP traffic using NetFlow data, with an emphasis on “distributional features” derived from IP-level NetFlow variable distributions and validated against malicious-IP denylists and deep packet inspection [record_id:179]. The other record is a 2025 CAMLIS entry titled “Red Teaming AI Red Teaming,” but its raw record text is empty, so it provides no direct evidence about the talk’s argument, methods, or findings beyond the bibliographic metadata supplied with the record [record_id:133].

Collectively, the evidence suggests that Majumdar’s represented work spans at least two security-facing areas: applied machine learning for network intrusion detection, and—based only on title/metadata—AI red teaming or AI security. However, the evidentiary basis is uneven. The network-security record provides a clear technical abstract and supports detailed synthesis. The AI-red-teaming record cannot be analyzed substantively because no raw description is available [record_id:133].

## Research Landscape

The record set consists of CAMLIS conference-style records attributed to Subhabrata Majumdar. The landscape is therefore not a broad bibliography of papers, code, blog posts, or operational reports; it is a narrow set of talk or presentation entries. Within that small set, the only content-rich record is the 2022 CAMLIS talk “Network Security Modelling with Distributional Data,” whose raw text frames the work as an investigation into botnet C2 detection in “massive IP traffic” using machine learning over NetFlow-derived features [record_id:179].

The 2022 record sits squarely in network security analytics, intrusion detection, and machine-learning-assisted traffic analysis. It focuses on identifying whether an IP belongs to “known botnet families” using two feature sets: conventional NetFlow variables and distributional features based on those variables [record_id:179]. The work also emphasizes validation, reporting that predictions were checked against published malicious-IP denylists and deep packet inspection [record_id:179].

The 2025 CAMLIS entry, “Red Teaming AI Red Teaming,” appears from its title and metadata to concern AI red teaming, prompt-injection/jailbreaking, or application security. But the raw record text is blank, so it cannot be used as evidence for specific claims about its content, scope, methodology, or conclusions [record_id:133]. For downstream agents, this means the landscape should be treated as bifurcated but highly asymmetric: a well-described network-security ML presentation in 2022, and an under-described AI-security presentation in 2025.

## Major Themes And Trends

### Machine learning for security detection

The strongest theme in the available evidence is the use of machine learning to detect malicious infrastructure in network telemetry. The 2022 abstract explicitly states that the work investigates “the detection of botnet command and control (C2) hosts in massive IP traffic using machine learning methods” [record_id:179]. This places the work in a practical security-detection setting rather than a purely theoretical ML context.

The target problem—botnet C2 host detection—is operationally significant because C2 infrastructure is central to many malware and botnet campaigns. The record frames the task as predicting whether an IP address belongs to known botnet families, implying a supervised or label-driven detection workflow built from historical or known malicious examples [record_id:179].

### NetFlow as a practical security data source

Another major theme is reliance on NetFlow. The raw text calls NetFlow “the industry standard for monitoring of IP traffic,” and uses it as the basis for both conventional traffic variables and derived distributional features [record_id:179]. This suggests a focus on scalable, metadata-level traffic analysis rather than packet-payload inspection as the primary modeling substrate.

That choice matters because NetFlow-style telemetry is commonly available at enterprise and network-provider scales, while full packet capture may be expensive, privacy-sensitive, or impractical. The record’s emphasis on “massive IP traffic” further suggests a concern with methods that can operate over large-scale network observability data [record_id:179].

### Distributional feature engineering

The most distinctive technical theme is the use of distributional data representations. The 2022 record contrasts “conventional NetFlow variables” with “distributional features based on NetFlow variables” [record_id:179]. Instead of relying only on static summaries, the work uses “quantiles of their IP-level distributions as input features” for predictive models [record_id:179].

This is the central unique contribution visible in the record. The abstract argues that these distributional features, combined with techniques capable of modeling complex feature spaces, produce “highly accurate predictions” [record_id:179]. In other words, the talk appears to advocate for representing IP behavior not simply through averages, totals, or fixed summaries, but through richer summaries of the distribution of traffic characteristics associated with each IP.

### Validation against external security evidence

The 2022 record also emphasizes validation. It states that results were validated by matching predictions to “existing denylists of published malicious IP addresses” and through “deep packet inspection” [record_id:179]. This is notable because it ties model output to external security evidence rather than reporting model performance in isolation.

However, the abstract does not provide metrics, dataset details, time windows, ground-truth construction methods, false-positive rates, or deployment outcomes. So the evidence supports the claim that validation was performed, but not a detailed assessment of robustness, generalizability, or operational readiness [record_id:179].

### Possible later shift toward AI red teaming

The 2025 record’s title, “Red Teaming AI Red Teaming,” suggests a later interest in AI security and possibly the evaluation of AI red-team practices themselves [record_id:133]. However, because the raw text is empty, this should be treated only as a bibliographic signal, not substantive evidence. There is not enough raw material to determine whether the 2025 talk addresses prompt injection, jailbreaking, model evaluation, adversarial testing, governance, application security, or meta-red-teaming methodology [record_id:133].

If downstream researchers pursue this author’s trajectory, they should treat the apparent movement from network-security ML in 2022 to AI red-team-related work in 2025 as a hypothesis requiring additional sources, not as a proven trend from the current record set.

## Methods, Tools, And Approaches Discussed

The substantive methodological content comes from the 2022 NetFlow-based botnet-detection record.

First, the work uses NetFlow data as the observational foundation. NetFlow variables are described as the industry-standard representation for monitoring IP traffic, and the models are built over features derived from that traffic metadata [record_id:179]. The record distinguishes between two broad feature families: conventional NetFlow variables and distributional features based on NetFlow variables [record_id:179].

Second, the record describes feature engineering at the IP level. Instead of relying only on static summaries, it uses quantiles of IP-level distributions as model inputs [record_id:179]. This implies a workflow where traffic records are grouped or aggregated by IP, distributions of relevant NetFlow variables are computed per IP, and quantile-based summaries are extracted as predictive features. The record does not list the specific NetFlow variables used, but the method depends on transforming traffic behavior into richer distributional representations [record_id:179].

Third, the approach uses predictive machine-learning models to classify or score whether an IP address belongs to known botnet families [record_id:179]. The raw text does not name specific algorithms, but it refers to “ML models,” “predictive models,” and “techniques that enable modelling complex input feature spaces” [record_id:179]. That phrasing suggests use of models capable of capturing nonlinear or high-dimensional structure, though the exact model classes cannot be determined from the record alone.

Fourth, the work is positioned as contributing to intrusion detection systems. The abstract states that the models “were used to develop intrusion detection systems to predict traffic traces identified with malicious attacks” [record_id:179]. This points to an applied security-engineering workflow: traffic telemetry feeds model features; models generate predictions about malicious IPs or attack traces; outputs can support intrusion detection.

Finally, the validation approach combines at least two evidence sources: published malicious-IP denylists and deep packet inspection [record_id:179]. Denylist matching provides an external reference against known malicious infrastructure, while deep packet inspection provides a deeper traffic-content or protocol-level validation mechanism. The record does not specify whether these were used for labeling, post-hoc validation, triage, or error analysis, so downstream researchers should avoid assuming a specific experimental design without additional documentation [record_id:179].

No methods can be responsibly extracted from the 2025 “Red Teaming AI Red Teaming” record because its raw text is empty [record_id:133].

## Notable Talks, Records, And Evidence

The most important record is the 2022 CAMLIS entry “Network Security Modelling with Distributional Data,” because it is the only record with substantive raw content [record_id:179]. It matters for several reasons.

First, it clearly defines a security problem: detecting botnet command-and-control hosts in massive IP traffic [record_id:179]. Second, it identifies the data source: NetFlow, described as a standard for IP traffic monitoring [record_id:179]. Third, it presents a feature-engineering contribution: augmenting conventional NetFlow variables with quantile-based distributional features at the IP level [record_id:179]. Fourth, it connects the method to operational intrusion detection systems and validates predictions against external evidence sources including malicious-IP denylists and deep packet inspection [record_id:179].

The record’s strongest contribution is the framing of distributional features as a way to improve machine-learning detection of malicious IP behavior. The statement that these features, combined with methods for complex feature spaces, result in “highly accurate predictions” is important, but it remains an abstract-level claim without numerical results in the available text [record_id:179].

The 2025 CAMLIS entry “Red Teaming AI Red Teaming” is notable mainly because of its apparent topical shift toward AI security or red-team evaluation, but the raw record contains no abstract or description [record_id:133]. As a result, it should be treated as a pointer to a potentially relevant talk rather than evidence of specific research findings. Downstream researchers should seek the CAMLIS page, slides, video, transcript, or related publication before drawing conclusions about Majumdar’s position on AI red teaming [record_id:133].

## Gaps, Limits, And Open Questions

The biggest limitation is the size and completeness of the corpus. There are only two records, and one has no raw content [record_id:133]. This makes it impossible to produce a confident account of Majumdar’s overall research program, recurring arguments, or evolution over time. The 2022 record supports a detailed account of one network-security ML presentation, but it cannot establish whether that topic is representative of the author’s broader work [record_id:179].

Several technical gaps remain in the 2022 record. The abstract does not identify the specific machine-learning algorithms used, the size or composition of the NetFlow dataset, the botnet families studied, the labeling strategy, the exact conventional NetFlow variables, the quantiles selected, or the feature-selection process [record_id:179]. It also does not provide performance metrics such as precision, recall, ROC-AUC, false-positive rate, detection latency, or comparisons against baselines [record_id:179]. The claim of “highly accurate predictions” is therefore promising but not independently assessable from the raw text alone [record_id:179].

The validation description also leaves open questions. Matching predictions to published malicious-IP denylists can provide useful corroboration, but denylists may be incomplete, stale, biased toward already-known infrastructure, or vulnerable to temporal mismatch. Deep packet inspection can provide stronger confirmation in some contexts, but the record does not explain what DPI evidence was inspected or how it was integrated into evaluation [record_id:179]. Downstream researchers should look for the full paper, slides, or experimental appendix to assess validation quality.

For the 2025 AI-red-teaming record, nearly all substantive questions remain open. The current record does not say whether the talk concerns red teaming of AI systems, red teaming practices used by AI systems, evaluation of AI red-team benchmarks, prompt injection, jailbreaks, application security, governance, or adversarial testing methodology [record_id:133]. It also provides no evidence about tools, datasets, frameworks, case studies, recommendations, or conclusions [record_id:133].

A further open question is whether there is continuity between the 2022 and 2025 records. One possible interpretation is that Majumdar’s work