# Topic: Author: Ethan Rudd

## Executive Summary

The two records attributed to Ethan Rudd are CAMLIS presentation abstracts from 2021 and 2022, both focused on applying machine learning to malware analysis and classification workflows. Together, they frame malware ML not merely as a binary detection problem, but as a broader operational problem involving uncertainty, concept drift, open-set recognition, downstream triage, capability labeling, transfer learning, storage costs, retraining costs, and integration with analyst or auxiliary detection pipelines.

The 2021 record, “Loss on Demand: Toward Discriminative-Generative Hybrid Models for Malware Classification Confidence,” centers on confidence estimation for malware classification under deployment conditions where new samples may be out-of-distribution or poorly supported by training data. It proposes combining discriminative and generative loss functions to produce latent representations that can support open-set recognition, concept drift measurement, and confidence-aware routing of samples to additional detection technologies or analysts [record_id:202].

The 2022 record, “Efficient Malware Analysis Using Metric Embeddings,” shifts toward streamlining malware analysis pipelines through metric learning. It proposes low-dimensional embeddings enriched with capability labels derived from Mandiant’s CAPA tool, then evaluates their usefulness across downstream tasks such as detection, family classification, and malware attribute classification using datasets including EMBER and SOREL [record_id:172].

Across both records, Ethan Rudd’s attributed work emphasizes practical, deployment-aware malware ML: reducing technical debt, improving confidence and support estimation, making representations reusable across tasks, and improving the efficiency of triage and retraining. The evidence base is narrow—two abstracts, both from CAMLIS—but coherent. The records suggest a research trajectory from confidence-aware classification under open-set conditions in 2021 toward representation learning and efficient reusable embeddings for malware analysis in 2022.

## Research Landscape

The available records consist of two CAMLIS entries, one from 2021 and one from 2022, both attributed to Ethan Rudd. They appear to be presentation or paper abstracts rather than full papers, slides, transcripts, or implementation artifacts. Both records are situated in malware analysis and reverse engineering, with substantial emphasis on machine learning methods for endpoint or security-industry use cases.

The research landscape represented here is therefore concentrated rather than broad. These records do not cover all of Ethan Rudd’s possible work, only the two provided CAMLIS records. Within that limited corpus, the dominant area is machine learning for malware classification and analysis, especially the problem of making ML systems more useful under real-world operational constraints.

The 2021 record focuses on the difficulty of “malware classification in the wild,” naming concept drift and out-of-distribution data as central problems [record_id:202]. It presents malware classification as an open-set recognition problem, where deployed systems must handle samples that are not well represented by training data [record_id:202]. The stated motivation is practical: industry systems often handle drift through periodic retraining, but may not address unsupported or unknown samples directly [record_id:202].

The 2022 record focuses on the complexity and cost of modern malware analysis pipelines. It notes that ML-based malware classification has become a component of defense-in-depth strategies, but that classification systems are typically combined with additional toolchains for detection names, capability information, type information, triage, and remediation [record_id:172]. The record argues that these interconnected systems can incur technical debt, infrastructure costs, and errors [record_id:172]. Its proposed research direction is to use metric learning and low-dimensional embeddings to preserve flexibility while reducing risk, cost, retraining overhead, and storage overhead [record_id:172].

Both records use public or open-source datasets as evaluation anchors. The 2021 record mentions EMBER 2018 and SOREL 20M as examples of open-source malware and goodware datasets [record_id:202]. The 2022 record uses the EMBER dataset and SOREL datasets for transfer-task evaluation and enriches PE-file labels using Mandiant’s CAPA tool [record_id:172]. This common dataset grounding suggests a concern with reproducible or at least benchmark-oriented malware ML research.

## Major Themes And Trends

### Malware ML as an operational system, not just a classifier

A major theme across both records is that malware machine learning must be evaluated in terms of operational usefulness, not only classification accuracy. The 2021 record argues that malware classification in deployment is affected by concept drift and out-of-distribution data, and that models should provide measures of statistical support and concept drift for each sample [record_id:202]. It suggests routing uncertain samples to auxiliary technologies in an escalating sequence: for example, from static detection to dynamic detection, and then to an analyst if needed [record_id:202]. This indicates a pipeline-oriented view of ML, where model output informs workflow decisions.

The 2022 record similarly treats malware ML as part of a larger analysis and defense pipeline. It states that malware detection models are usually combined with other toolchains that provide context for triage and remediation, such as detection names, capability information, and type information [record_id:172]. Rather than accepting the complexity of such systems as inevitable, the 2022 work explores whether learned embeddings can streamline pipelines while preserving downstream functionality [record_id:172].

Together, the records suggest that Rudd’s attributed work is concerned with deployable malware ML systems that reduce analyst burden, infrastructure complexity, and uncertainty in operational decision-making.

### Representation learning as a unifying mechanism

Both records center on latent or embedded representations. In 2021, the focus is on latent spaces shaped by hybrid discriminative-generative losses. The record contrasts discriminative models, which separate classes, with generative models, which characterize data distributions and can shape the spread of points in latent space [record_id:202]. It then proposes combining these loss functions in multi-objective hybrid models, with the goal of supporting classification confidence, open-set evaluation, and concept drift measurement [record_id:202].

In 2022, representation learning becomes even more explicit through metric embeddings. The record describes embedding malicious and benign samples into a low-dimensional vector space enriched with capability information, then using that space for multiple downstream applications such as detection, family classification, and malware attribute classification [record_id:172]. The record also mentions contrastive loss and Spearman rank correlation on malware similarity as training objectives or components for deriving different types of metric embeddings [record_id:172].

The trend across the two records is from latent spaces for confidence and support estimation toward reusable embeddings for efficient multi-task malware analysis. In both cases, the learned representation is expected to carry more operational value than a single binary classification score.

### Handling uncertainty, unknowns, and concept drift

The 2021 record is especially focused on uncertainty under deployment. It explicitly identifies concept drift, out-of-distribution samples, and open-set recognition as key challenges for malware classification [record_id:202]. It argues that industry deployments often use periodic retraining to address drift, but that retraining on a fixed cadence does not directly solve the open-set problem [record_id:202]. The proposed alternative is to measure statistical support and concept drift, enabling uncertain samples to be flagged as “unknowns” or routed to more expensive detection methods before they become false positives or misclassifications [record_id:202].

The 2022 record does not foreground open-set recognition in the same way, but it does address related operational concerns: errors, technical debt, retraining overhead, and transfer to downstream tasks [record_id:172]. Its use of low-dimensional embeddings is framed as a way to quickly retrain for transfer tasks and reduce storage overhead [record_id:172]. This connects indirectly to drift and changing task requirements: if retraining or adaptation is cheaper, systems may respond more flexibly to new malware, new labels, or new analysis needs.

### Enriching malware ML with semantic or capability information

The 2022 record introduces a notable theme not present in the 2021 record: enriching malware representations with capability labels. It describes using Mandiant’s CAPA tool, an open-source toolchain based on disassembly and subject-matter-expert-derived rules and heuristics, to determine malicious capabilities [record_id:172]. These CAPA-derived labels are used to enrich labeling on malicious and benign PE files from the EMBER dataset [record_id:172].

This suggests a bridge between expert-driven reverse engineering knowledge and machine learning representation learning. Instead of training only on coarse malware/goodware labels, the 2022 work attempts to encode capability-oriented information into embeddings, making them potentially useful for downstream tasks beyond binary detection [record_id:172].

### Efficiency, cost reduction, and pipeline simplification

Efficiency is a central concern in the 2022 record and an implicit concern in the 2021 record. The 2022 title itself foregrounds “Efficient Malware Analysis,” and the abstract argues that modern systems can become complex and interconnected, creating technical debt, infrastructure costs, and errors [record_id:172]. The proposed solution is low-dimensional metric embeddings that retain performance across tasks while reducing training and storage overhead [record_id:172].

The 2021 record’s efficiency concern is about routing and resource allocation. It proposes using support or confidence measures to route samples from less expensive to more expensive detection technologies, such as escalating from static detection to dynamic detection and then to analyst review [record_id:202]. This is an efficiency model for operational triage: reserve expensive analysis for cases where the model lacks support or confidence.

Together, the two records indicate a consistent emphasis on making malware ML systems more economical and operationally manageable.

## Methods, Tools, And Approaches Discussed

The 2021 record discusses hybrid discriminative-generative modeling for malware classification confidence. It begins from the observation that discriminative models are effective at class separation but may be vulnerable to concept drift and may not work well in open-set recognition regimes [record_id:202]. The record notes that some discriminative losses force separation at a margin but do little to bound the span of class predictions [record_id:202]. It contrasts this with generative models, which characterize data distributions and can shape latent-space distributions [record_id:202].

A specific generative example in the 2021 record is the Variational Auto-Encoder, or VAE. The record states that VAEs enforce Gaussian distributional constraints that can bound the spread of samples in latent space [record_id:202]. It also highlights that VAE loss functions can often be computed without class labels, using reconstruction loss, divergence from a known distribution, or real/fake veracity terms in adversarial learning paradigms [record_id:202]. This matters because losses requiring labels can only be evaluated during training or validation, whereas label-independent losses may be evaluated on new deployment samples [record_id:202].

The proposed 2021 approach is to combine loss functions from generative models with standard discriminative losses into multi-objective hybrid discriminative-generative models [record_id:202]. The record says these models are evaluated for impacts on classification performance and training, using open-source malware and goodware datasets such as EMBER 2018 and SOREL 20M, and applying open-set evaluation protocols based on Scheirer et al.’s open-set recognition work [record_id:202]. It also discusses using latent-space characteristics to motivate measurements of concept drift between source and target distributions, implementing classification confidence measures, and thresholding generative losses during deployment to reduce open-space risk [record_id:202].

The 2022 record discusses metric learning for malware analysis. It proposes embedding malicious and benign samples in a low-dimensional vector space enriched with capability information [record_id:172]. The goal is to support multiple downstream applications, including detection, family classification, and malware attribute classification [record_id:172].

A key tool in the 2022 approach is Mandiant’s CAPA, described in the record as an open-source toolchain that uses disassembly and subject-matter-expert-derived rules and heuristics to determine malicious capabilities [record_id:172]. The record says CAPA labels are used to enrich malicious and benign PE files from the EMBER dataset [record_id:172]. This enriched labeling then supports the derivation of several kinds of metric embeddings.

The 2022 record identifies several training or embedding-derivation techniques: an embedding neural network trained via contrastive loss, Spearman rank correlation on malware similarity, and combinations of these methods [record_id:172]. The resulting embeddings are evaluated on transfer tasks across EMBER and SOREL datasets [record_id:172]. The record reports that low-dimensional metric embeddings can be used for a variety of transfer tasks with little performance decay, enabling faster retraining and reducing training and storage overhead [record_id:172].

In prose, the methodological arc across the records is clear: shape latent spaces so that they encode operationally useful information. In 2021, the latent space is shaped to support confidence, support estimation, open-set detection, and drift measurement [record_id:202]. In 2022, the embedding space is shaped to encode capability-enriched similarity and support efficient transfer across malware analysis tasks [record_id:172].

## Notable Talks, Records, And Evidence

The 2021 CAMLIS record, “Loss on Demand: Toward Discriminative-Generative Hybrid Models for Malware Classification Confidence,” is notable because it establishes the problem of malware classification confidence under real deployment conditions [record_id:202]. It frames malware detection as an open-set recognition problem and argues that deployed classifiers need mechanisms for identifying unsupported samples as unknowns [record_id:202]. The record’s contribution is conceptual and methodological: combine discriminative and generative objectives so that malware classifiers can produce not only class decisions, but also latent-space and loss-based signals relevant to confidence, drift, and open-space risk [record_id:202].

This record matters because it directly addresses a common weakness of malware ML systems: they often perform well on benchmark classification tasks but degrade when faced with novel, shifted, or out-of-distribution samples. The abstract’s emphasis on support measurement, routing to auxiliary technologies, and thresholding generative losses shows an attempt to connect ML model internals to operational triage decisions [record_id:202]. It is also the only record in the corpus that explicitly discusses open-set recognition, concept drift, and hybrid discriminative-generative modeling.

The 2022 CAMLIS record, “Efficient Malware Analysis Using Metric Embeddings,” is notable because it extends the deployment-aware theme