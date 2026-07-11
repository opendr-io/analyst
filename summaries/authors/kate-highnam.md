# Topic: Author: Kate Highnam

## Executive Summary

The two records attributed to Kate Highnam present a focused body of work at CAMLIS on improving empirical foundations for cybersecurity detection and anomaly research. Both records address a common problem: cybersecurity research depends heavily on data collection, but the usefulness of that data depends on how it is gathered, labeled, structured, and interpreted. The 2021 record introduces the BETH cybersecurity dataset, a large real-world dataset for anomaly detection and out-of-distribution analysis with over eight million data points across 23 hosts [record_id:194]. The 2023 record advances a methodological argument for adaptive experimental design in intrusion data collection, using a controlled honeypot deployment to estimate causal relationships more efficiently than observational studies or conventional randomized-control-style designs [record_id:159].

Collectively, the records suggest that Highnam’s contributions center on making cybersecurity machine learning and detection research more rigorous, realistic, and empirically grounded. The 2021 work emphasizes dataset quality, real anomalies, heterogeneous real-world data, preprocessing guidance, and initial anomaly detection benchmarks [record_id:194]. The 2023 work emphasizes causal inference, experimental design, adaptive allocation, and reducing the cost and duration of intrusion-data experiments while preserving confidence in conclusions [record_id:159]. The evidence base is small—only two records—but coherent: both are CAMLIS presentations concerned with the reliability and practical value of cybersecurity data for detection-oriented research.

## Research Landscape

The records consist of two CAMLIS entries from 2021 and 2023, both attributed to Kate Highnam. They are not general blog posts or broad surveys; they appear to be concise presentation or paper abstracts describing research contributions in cybersecurity data collection and detection research.

The 2021 record, “BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research,” is a dataset-oriented contribution. It presents the BETH dataset as a resource for anomaly detection and out-of-distribution analysis, emphasizing that the data contains real anomalies collected using a novel tracking system [record_id:194]. The record states that the dataset includes “over eight million data points” tracking 23 hosts, with each host containing benign activity and “at most, a single attack,” a design intended to support cleaner behavioral analysis [record_id:194]. This places the work within endpoint or host-based anomaly detection research, especially where researchers need realistic but analytically tractable data.

The 2023 record, “Adaptive Experimental Design for Intrusion Data Collection,” is more explicitly methodological. It critiques common intrusion-data collection practices such as honeypot deployment, device logging, red-team campaigns, and simulated activity because such observational approaches do not clearly identify cause-and-effect relationships between environmental design and recorded data [record_id:159]. It then presents adaptive design as an approach inspired by clinical trials and randomized controlled trials, applying it to a controlled and adaptive honeypot deployment study [record_id:159]. This record sits at the intersection of intrusion detection, network security, experimental design, and causal inference.

Together, the research landscape is narrow but substantive. The records do not show a broad portfolio across many areas of security; instead, they point to a specific research agenda: improving how cybersecurity datasets and intrusion observations are generated so that detection, anomaly, and threat-hunting research can make stronger claims.

## Major Themes And Trends

### 1. Better cybersecurity data for detection research

A dominant theme across both records is the need for higher-quality cybersecurity data. The BETH dataset record directly addresses this by presenting a modern dataset for anomaly detection research, emphasizing real anomalies and heterogeneous real-world data [record_id:194]. The adaptive design record approaches the same broad issue from another angle: even when data are collected from honeypots, logs, red teams, or simulations, the resulting observations may not support reliable causal conclusions if the collection design is weak [record_id:159].

The two records therefore complement each other. One contributes a dataset intended for downstream model development and benchmarking [record_id:194]. The other contributes a method for collecting intrusion data in ways that more efficiently reveal causal relationships between environmental conditions and attacker behavior [record_id:159].

### 2. Realism balanced with analytical cleanliness

Both records value real-world realism but also recognize that raw realism alone is not enough. In the BETH dataset, the record stresses that the dataset contains real anomalies and real-world heterogeneous data, but also that each host has benign activity and “at most, a single attack,” enabling “cleaner behavioural analysis” [record_id:194]. This suggests a deliberate balance: data should be realistic enough to matter for cybersecurity applications, but structured enough for researchers to isolate behavioral patterns.

The 2023 adaptive design work similarly seeks to improve the interpretability of real intrusion data. It notes that observational studies may suffer from “spurious correlations” and “errors in measurement or classification” when unconsidered factors influence results [record_id:159]. Its controlled and adaptive honeypot deployment attempts to retain practical intrusion-data collection while adding experimental structure sufficient to support causal claims [record_id:159].

### 3. Movement from dataset creation to experimental methodology

The chronological pattern is notable. The 2021 record focuses on releasing or presenting a dataset and benchmarking anomaly detection on part of it [record_id:194]. By 2023, the focus shifts toward the design of intrusion-data collection experiments themselves [record_id:159]. This may indicate an evolution from providing data for machine learning research toward questioning and improving the mechanisms by which such data are produced.

The records do not provide enough evidence to claim a full career trajectory, but within this small corpus there is a visible progression: from dataset construction and anomaly-detection benchmarking to causal experimental design for intrusion research.

### 4. Concern with bias, causal validity, and experimental confidence

The 2023 record is especially explicit about threats to validity. It argues that observational intrusion studies may fail to distinguish the causal effect of environmental design choices from confounding factors, increasing the chance of biased conclusions [record_id:159]. This concern is not merely theoretical; the record says the authors conducted the first controlled and adaptive honeypot deployment study to identify the causal relationship between an SSH vulnerability and server exploitation rate [record_id:159].

The BETH dataset record is less explicitly about causality, but it also reflects validity concerns through its dataset design. The constraint that each host has benign activity and at most one attack is framed as enabling cleaner behavioral analysis [record_id:194]. Both records therefore emphasize research designs that make interpretation easier and conclusions stronger.

### 5. Efficiency and practical feasibility

The adaptive design record introduces efficiency as a key contribution. It claims the adaptive design method decreases total deployment time by at least 33% while still confidently stating the impact of an environmental change [record_id:159]. It further claims that, compared with an analogous honeypot study with a control group, adaptive design requests 17% fewer honeypots while collecting 19% more attack recordings [record_id:159]. These figures suggest an interest not only in methodological rigor but also in making rigorous data collection more practical.

The BETH dataset record also has practical orientation. It describes downstream applications, preprocessing suggestions, and initial anomaly detection benchmarks [record_id:194]. Rather than simply announcing a dataset, the record frames BETH as a usable research asset for developing anomaly detection algorithms on realistic heterogeneous data [record_id:194].

## Methods, Tools, And Approaches Discussed

The records discuss several research methods and approaches, primarily around data collection, experimental design, and anomaly detection.

The BETH dataset work presents a dataset-construction approach using a “novel tracking system” to collect real anomalies [record_id:194]. The dataset contains more than eight million data points from 23 hosts, where each host has benign activity and at most one attack [record_id:194]. This structure supports behavioral analysis by limiting the complexity of attack overlap per host. The record also mentions preprocessing suggestions and initial anomaly detection benchmarks on a subset of the data, indicating that the contribution includes both raw data and guidance for using it in machine learning workflows [record_id:194].

The adaptive experimental design work discusses several conventional intrusion-data collection approaches: deploying honeypots, logging existing devices, employing a red team for a sample attack campaign, and simulating system activity [record_id:159]. It critiques these as observational studies that do not clearly establish cause-and-effect relationships between environmental design and recorded data [record_id:159]. As an alternative, it introduces adaptive design inspired by clinical-trial methodology, specifically as a variant of randomized controlled trials used to measure how a treatment affects a population [record_id:159].

The 2023 record’s concrete experimental setting is a honeypot deployment study. The study identifies the causal relationship between an SSH vulnerability and the rate of server exploitation [record_id:159]. The adaptive design appears to allocate experimental resources more efficiently than a conventional control-group honeypot study, producing reported savings in time and honeypot usage while increasing attack recordings [record_id:159]. The record does not name a software tool or platform, but it clearly describes an experimental workflow: controlled deployment, adaptive allocation, comparison with observational and randomized-control-style alternatives, and measurement of exploitation outcomes.

Across both records, the most important “tools” are not named products but research instruments: datasets, tracking systems, honeypots, benchmark subsets, preprocessing workflows, and adaptive experimental designs [record_id:194] [record_id:159].

## Notable Talks, Records, And Evidence

The 2021 CAMLIS record, “BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research,” is notable because it presents a dataset intended to support anomaly detection and out-of-distribution analysis on real cybersecurity data [record_id:194]. Its major contribution is the BETH dataset itself: over eight million data points across 23 hosts, real anomalies collected using a novel tracking system, and a host structure designed to support cleaner behavioral analysis [record_id:194]. The record is representative of dataset-centered security machine learning research, especially the recurring need for realistic data with enough structure to support controlled model evaluation.

The 2023 CAMLIS record, “Adaptive Experimental Design for Intrusion Data Collection,” is notable because it moves beyond dataset release into the design of intrusion experiments [record_id:159]. It explicitly identifies weaknesses in common observational data-collection practices and proposes adaptive design as a way to infer causal effects more efficiently [record_id:159]. The record’s reported empirical results are concrete: at least 33% less deployment time, 17% fewer honeypots requested, and 19% more attack recordings compared with an analogous honeypot study with a control group [record_id:159]. It is the stronger of the two records for understanding Highnam’s methodological contribution to causal and experimental rigor in security data collection.

Together, the records provide evidence of a coherent research niche. The 2021 record contributes a real-world anomaly-detection dataset and benchmarking context [record_id:194]. The 2023 record contributes an adaptive experimental design for collecting intrusion data and estimating causal effects [record_id:159]. Both are relevant to detection engineering, threat hunting, anomaly detection, and security machine learning, though the raw records are presentation abstracts rather than full papers.

## Gaps, Limits, And Open Questions

The evidence base is limited to two short CAMLIS records, so conclusions about Kate Highnam’s broader research agenda should be cautious. The records provide abstracts but not full methodological detail, dataset schemas, code, experimental parameters, statistical models, or evaluation results beyond headline claims.

For the BETH dataset, the record does not specify what features are captured, what attack types are included, how labels are assigned, what the “novel tracking system” technically does, or how the initial anomaly detection benchmarks perform [record_id:194]. It also does not state licensing, access mechanisms, known biases, or how representative the 23 hosts are of broader enterprise environments [record_id:194]. Downstream researchers would need the full dataset documentation or paper to assess suitability for specific anomaly detection tasks.

For the adaptive experimental design work, the record does not describe the exact adaptive algorithm, sample-size rules, randomization scheme, statistical confidence criteria, honeypot configuration, or details of the SSH vulnerability being tested [record_id:159]. It reports efficiency improvements, but the abstract alone is insufficient to assess generalizability beyond the specific honeypot study [record_id:159]. Open questions include whether the adaptive design works for more complex multi-factor environments, multi-stage attacks, enterprise telemetry, or adversaries that adapt to experimental exposure.

A broader gap is that the two records do not directly discuss operational deployment in a SOC, integration with SIEM or EDR tools, or real-world analyst workflows. They are highly relevant to detection research, but the raw text focuses on data collection and research methodology rather than production detection engineering.

Finally, the records do not show disagreement or debate among approaches. The 2023 record contrasts observational studies, randomized controlled trials, and adaptive design, but only from the perspective of motivating the proposed method [record_id:159]. There is no evidence here of external critique, replication, or comparison by independent groups.

## Coverage And Evidence Notes

This report covers both records specified for the topic.

Record 159 is a 2023 CAMLIS entry titled “Adaptive Experimental Design for Intrusion Data Collection,” attributed to Kate Highnam [record_id:159]. It is central to the themes of causal inference, adaptive experimental design, honeypot deployment, and efficient intrusion-data collection. It provides the strongest evidence for Highnam’s work on methodology and experimental rigor in cybersecurity data collection [record_id:159].

Record 194 is a 2021 CAMLIS entry titled “BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research,” attributed to Kate Highnam along with Kai Arulkumaran, Zachary Hanif, and Nicholas R. Jennings in the raw text [record_id:194]. It is central to the themes of real-world cybersecurity datasets, anomaly detection, out-of-distribution analysis, preprocessing guidance, and benchmarking [record_id:194].

No record appears purely logistical or irrelevant. Both records fit the overall topic, though both are brief abstracts rather than full research artifacts. The strongest synthesis supported by the available evidence is that Kate Highnam’s represented work emphasizes rigorous, realistic, and useful cybersecurity data for anomaly detection and intrusion research, spanning both dataset construction and