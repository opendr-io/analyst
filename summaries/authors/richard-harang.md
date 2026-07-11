# Topic: Author: Richard Harang

## Executive Summary

The two records attributed to Richard Harang show a focused body of work at CAMLIS on machine learning for security, especially malware detection and the reliability of classifier outputs. The 2018 record addresses a core modeling problem: how to estimate uncertainty for binary classifiers in practical security-data-science settings where classifier scores are often mistaken for reliable confidence estimates [record_id:248]. The 2021 record presents SOREL-20M, a large-scale benchmark dataset for malicious Windows PE detection, including pre-extracted features, metadata, labels, vendor detections, malware tags, disarmed samples, and baseline machine-learning models [record_id:195].

Taken together, the records suggest a research agenda concerned not merely with applying machine learning to security problems, but with making those applications scientifically usable: better-calibrated or more meaningful uncertainty estimates, large benchmark datasets, reproducible code, baseline models, and evaluation infrastructure. The evidence base is small—only two abstracts—but the thematic connection is strong: both records are about improving the rigor, reliability, and experimental foundation of security machine-learning systems.

## Research Landscape

The records are both CAMLIS entries and appear to represent conference talks or paper presentations authored by Richard Harang. They are not broad biographical records; they are short technical abstracts. The covered period spans 2018 to 2021, with one record focused on model uncertainty in binary classification and another focused on benchmark data for malware detection.

The 2018 record is primarily methodological. It discusses the limitations of treating a binary classifier’s output score as a faithful measure of uncertainty, especially in modern high-dimensional security applications [record_id:248]. The abstract situates the problem in practical binary classification and then narrows toward security data science, where high-dimensional input spaces, complex classifiers, and transformed representation spaces make uncertainty estimation difficult [record_id:248].

The 2021 record is primarily infrastructural and empirical. It introduces SOREL-20M, described as the Sophos/ReversingLabs-20 Million dataset, “a large-scale dataset consisting of nearly 20 million files” with features, metadata, labels, vendor detections, tags, disarmed malware samples, and baseline models [record_id:195]. This record belongs to the malware detection and endpoint-security research landscape, particularly the construction of reproducible benchmarks for malicious PE detection.

Overall, the research area represented by these records is applied security machine learning. The dominant concerns are:

- How to build reliable classifiers for security use cases.
- How to know when classifier predictions are uncertain.
- How to provide large, labeled datasets and baseline models for repeatable malware-detection research.
- How to support experimentation beyond a single proprietary system by releasing features, metadata, code, and model baselines.

Because there are only two records, the landscape should be treated as a narrow but coherent sample rather than a complete account of Harang’s work.

## Major Themes And Trends

### Reliability of machine-learning predictions in security

A central theme is the reliability of machine-learning outputs. The 2018 record argues that, in binary classification, “knowing the uncertainty of the prediction can be almost as important as knowing the most likely prediction” [record_id:248]. The abstract challenges a common assumption: that the classifier’s 0–1 output score can be used directly as a proxy for confidence or certainty [record_id:248]. It notes that this may be justified only under narrow conditions, such as the specific case of binary cross-entropy loss asymptotically attaining the posterior conditional probability under “rarely-obtained conditions” [record_id:248].

This reflects a broader concern in security operations and detection engineering: a classifier’s raw output is not always enough. Security analysts and automated systems need to know whether a prediction is reliable, ambiguous, out-of-distribution, or poorly supported by training data. The record explicitly emphasizes finite-data settings and “complex modern classifiers” that transform or partition the input space in ways that make score uncertainty difficult to characterize [record_id:248].

### Security data science as a high-dimensional, difficult setting

The 2018 abstract highlights the challenge of uncertainty estimation in high-dimensional security data. It explains that direct uncertainty estimation in simpler classifiers can sometimes be done by examining the support of a test point within the training data, but that “in many areas of security data science, the size of the input space to classifiers can be quite large” and the curse of dimensionality can make this difficult [record_id:248]. It further observes that even if support in the original input space can be estimated, modern classifiers may learn transformed spaces in which the practical support of a point differs from what is visible in the raw feature space [record_id:248].

This theme connects naturally to malware detection in the 2021 record. The SOREL-20M dataset is built around nearly 20 million files and includes pre-extracted features, metadata, labels, vendor detections, and tags [record_id:195]. Although the 2021 abstract does not explicitly discuss uncertainty, it presents the kind of large-scale, complex security dataset that motivates the methodological concerns in the 2018 record.

### Benchmarking and reproducibility for malware detection

The 2021 record’s major contribution is benchmark construction. SOREL-20M is described as a large-scale dataset for malicious PE detection with nearly 20 million files, high-quality labels derived from multiple sources, vendor detection information, and tags that can serve as additional targets [record_id:195]. The record also states that the authors provide pre-extracted features and metadata, Python code to interact with the data and features, and baseline neural network and gradient boosted decision tree models with full training and evaluation code [record_id:195].

This indicates an emphasis on reproducibility and community experimentation. Rather than presenting only a trained model or result, the record describes an ecosystem of data, labels, disarmed samples, code, baseline models, and evaluation tooling [record_id:195]. For downstream researchers, this is likely the most practically significant record because it points to reusable research infrastructure.

### Safe handling and research access to malware samples

The SOREL-20M abstract notes the release of approximately 10 million “disarmed” malware samples, with both `optional_headers.subsystem` and `file_header.machine` flags set to zero [record_id:195]. This detail suggests a concern with enabling deeper feature exploration and detection-strategy research while reducing operational risk from handling malware samples. The record does not claim that such samples are harmless in all contexts, but it clearly frames them as “disarmed” and usable “for further exploration of features and detection strategies” [record_id:195].

This theme is distinct from generic machine-learning benchmarking. It reflects a security-specific challenge: useful malware datasets often require access to real malicious artifacts, but such access introduces safety, legal, and operational constraints. The record’s mention of disarmed samples is therefore an important part of its contribution.

### Moving from abstract modeling concerns to large-scale applied datasets

Chronologically, the records move from a 2018 talk on uncertainty estimation for classifiers to a 2021 dataset paper for malicious PE detection. With only two records, it is not possible to assert a definitive evolution in Harang’s work, but the pairing suggests complementary interests: improving model interpretability or trustworthiness, and improving the empirical basis for training and evaluating malware classifiers.

The 2018 work asks how to understand model uncertainty in security-relevant binary classification [record_id:248]. The 2021 work provides a large, structured dataset and baselines for one of the most important binary classification problems in security: malicious versus benign PE detection [record_id:195]. The records therefore form a coherent arc from model reliability to benchmark infrastructure.

## Methods, Tools, And Approaches Discussed

The 2018 record discusses several approaches to uncertainty estimation, mostly in terms of their limitations before proposing a Bayesian approximation strategy.

First, it describes the common practice of treating distance from either extreme of a 0–1 classifier score as a proxy for certainty or uncertainty [record_id:248]. The record argues that this is generally not a faithful uncertainty estimate except under narrow theoretical conditions [record_id:248].

Second, it discusses support-based uncertainty estimation in simpler classifiers, where uncertainty may be estimated by examining how well a test point is supported by the training data [record_id:248]. This approach is presented as difficult in security data science because of large input spaces and the curse of dimensionality [record_id:248].

Third, it mentions variational methods for estimating uncertainty in deep neural networks regularized via dropout, but notes that this comes at “a significant computational cost” [record_id:248].

Fourth, it discusses multi-half-space classifiers for deep neural networks, which attempt to learn the density of training data as represented by the final layer of the network [record_id:248]. The abstract reports an empirical failure mode: as a network becomes better at separating data in the final pre-classification layer, this method performs worse at estimating the training data distribution [record_id:248].

The proposed direction in the 2018 record is to examine the problem from the perspective of Bayesian approximation, using deep neural networks as approximating functions for parameters of a hierarchical Bayesian model [record_id:248]. According to the abstract, this can produce uncertainty estimates that are robust, avoid the failure mode where the model is “too good,” require comparatively little additional computation, and can often be converted into a maximum a posteriori estimate score for the network [record_id:248].

The 2021 record is more concrete in terms of artifacts and tooling. It describes the SOREL-20M dataset as including:

- Nearly 20 million files [record_id:195].
- Pre-extracted features and metadata [record_id:195].
- High-quality labels derived from multiple sources [record_id:195].
- Vendor detection information for malware samples at the time of collection [record_id:195].
- Additional tags related to malware samples that can serve as additional targets [record_id:195].
- Approximately 10 million disarmed malware samples [record_id:195].
- Python code to interact with the data and features [record_id:195].
- Baseline neural network and gradient boosted decision tree models [record_id:195].
- Full training and evaluation code for further experimentation [record_id:195].

The machine-learning methods explicitly named in the 2021 record are neural networks and gradient boosted decision trees [record_id:195]. The key workflow is benchmark-driven experimentation: use the dataset and provided code, train or compare against baseline models, and evaluate malicious PE detection strategies using the released features, labels, and metadata [record_id:195].

## Notable Talks, Records, And Evidence

The most representative record for Harang’s contribution to malware-detection benchmarking is the 2021 CAMLIS entry, “SOREL-20M: A Large Scale Benchmark Dataset for Malicious PE Detection” [record_id:195]. It matters because it describes a major public research artifact rather than only a conceptual method. Its scale is central: nearly 20 million files and approximately 10 million disarmed malware samples [record_id:195]. The record also emphasizes research usability through pre-extracted features, metadata, labels, tags, vendor detections, Python access code, baseline neural network and gradient boosted decision tree models, and full training and evaluation code [record_id:195]. For downstream agents studying malware ML datasets, endpoint security benchmarks, or reproducible malicious PE detection research, this is the primary record.

The most representative record for Harang’s work on model reliability is the 2018 CAMLIS entry, “Estimating uncertainty for binary classifiers” [record_id:248]. It matters because it frames a practical and theoretical problem that affects many security classifiers: raw classifier scores are often treated as uncertainty estimates, but this can be misleading [record_id:248]. The abstract is unusually detailed in its discussion of why uncertainty estimation is difficult in high-dimensional security data science and modern deep-learning systems [record_id:248]. It also surveys or references several families of methods—score-based proxies, support-based estimation, dropout-based variational methods, multi-half-space classifiers, and hierarchical Bayesian approximation via neural networks [record_id:248]. For downstream agents studying calibrated detection, analyst trust, model confidence, or uncertainty-aware security ML, this is the key record.

The evidence strength differs between the two records. The SOREL-20M record provides concrete artifact claims: dataset size, content types, code, baselines, and sample handling details [record_id:195]. These claims are specific, but the abstract alone does not provide performance results, label-generation methodology details, or dataset access conditions. The uncertainty-estimation record provides a rich conceptual argument and summarizes empirical findings about multi-half-space classifier behavior, but the abstract does not include experiments, datasets, metrics, or quantitative results [record_id:248].

## Gaps, Limits, And Open Questions

The main limitation is the very small evidence base. Only two records are included, both are abstracts, and neither provides the full paper, slides, experimental tables, or implementation details. As a result, this report can identify themes but cannot fully evaluate the technical validity of the claims.

Several open questions remain for the 2018 uncertainty-estimation work:

- What specific hierarchical Bayesian model was used?
- How were neural networks used as approximating functions for model parameters?
- Which datasets or security tasks were used in the evaluation?
- How did the proposed uncertainty estimates compare quantitatively against dropout-based variational methods, calibration methods, ensembles, or density-estimation approaches?
- What does “robust” mean operationally in the abstract’s claim about uncertainty estimates [record_id:248]?
- Under what conditions can the uncertainty estimate be converted into a maximum a posteriori score, and how does that score behave in deployment [record_id:248]?

Several open questions remain for the 2021 SOREL-20M record:

- What exact feature schema is provided?
- How are labels derived from multiple sources, and how are conflicts resolved?
- What are the false-positive and false-negative risks in the labeling pipeline?
- How representative is the dataset of real endpoint telemetry or malware encountered in operational environments?
- What restrictions apply to the disarmed malware samples?
- What baseline performance did the neural network and gradient boosted decision tree models achieve?
- How should researchers account