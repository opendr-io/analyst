# Topic: Author: Philip Tully

## Executive Summary

The two records attributed to Philip Tully portray him as a security data science practitioner applying machine learning to high-volume, analyst-constrained security problems. The records span two CAMLIS talks, one from 2017 on social media security and one from 2019 on malware string triage. Together, they emphasize a recurring problem: security analysts face more data than they can manually inspect, while adversaries and benign variation create noisy, fast-changing environments. Tully’s contributions in these records center on building machine-learning-assisted workflows that help prioritize, classify, or automate security tasks without fully removing human expertise from the loop.

The 2017 talk, “Lean, Data-Driven Social Media Security,” focuses on social-platform threats such as malware, phishing links, financial scams, fake news, spam botnets, spear phishing, and steganography. It describes a flexible machine learning workflow for classifying text, image, and behavioral data across social networks, with attention to adversarial drift and the need to align software development cycles with interrupt-driven threat research [record_id:252].

The 2019 talk, “Learning to Rank Relevant Malware Strings Using Weak Supervision,” is more technically specific. It introduces StringSifter, an open-source machine-learning tool that ranks printable strings extracted from binaries by estimated relevance for malware analysis. The talk describes training on strings derived from malicious PE files in the EMBER dataset, using Snorkel-based weak supervision from subject-matter-expert labeling functions, and evaluating learning-to-rank models with nDCG metrics [record_id:229].

Across both records, the central theme is pragmatic machine learning for security operations: using statistical methods to reduce analyst fatigue, handle scale, adapt to evolving adversarial behavior, and convert expert judgment into repeatable workflows.

## Research Landscape

The available corpus is small: two CAMLIS presentation records, both attributed to Philip Tully. The records are not full papers or transcripts; they are talk abstracts or presentation descriptions. As a result, they provide strong evidence about the subjects, goals, and high-level methods of the talks, but limited evidence about implementation details, empirical results, deployment outcomes, or audience reception.

The two records cover different operational security domains:

- **Malware analysis and reverse engineering**: The 2019 CAMLIS talk presents StringSifter, a machine-learning-based tool for ranking strings extracted from binaries in order to help analysts identify relevant clues faster [record_id:229].
- **Social media threat detection and automation**: The 2017 CAMLIS talk addresses malicious and abusive content on social platforms, describing machine learning workflows for classifying network-agnostic text, image, and behavioral data, as well as automating attack workflows for red-team simulations [record_id:252].

The research area that emerges from these records is not a single narrow technical specialty but rather applied security machine learning. Both records are concerned with how to use machine learning in practical analyst workflows where data volume, labeling cost, ambiguity, and adversarial adaptation are central challenges. The talks appear to be aimed at audiences interested in cybersecurity data science, operational detection, malware triage, and applied machine learning.

The records also show a shift in specificity over time. The 2017 record is broad and programmatic, discussing social media risks and a general workflow for classification and automation [record_id:252]. The 2019 record is narrower and more concrete, presenting a named open-source tool, a specific data source, a weak supervision framework, ranking models, and an evaluation metric [record_id:229]. This suggests a progression from broad data-driven security workflows toward more deeply specified, reproducible machine-learning systems for security analysis.

## Major Themes And Trends

### Machine learning as a response to security data scale

Both records frame machine learning as a response to scale. In the malware analysis talk, the problem is that binaries may produce “upwards of thousands of strings,” relevant strings are comparatively rare, and manual filtering causes analyst fatigue and errors [record_id:229]. StringSifter is designed to rank strings so analysts can focus on those most likely to matter [record_id:229].

In the social media security talk, the scale problem is the volume and diversity of social data. The abstract notes that human experts can distinguish threatening from benign content, but “the scale of social data demands more statistical methods that are robust to adversarial drift” [record_id:252]. This framing parallels the malware talk: expert knowledge remains valuable, but manual review is insufficient at operational scale.

### Analyst augmentation rather than analyst replacement

The records do not present machine learning as a fully autonomous replacement for security experts. Instead, they describe systems that help experts work faster and more consistently. StringSifter is “built to sit downstream from the Strings program,” taking extracted strings as input and returning the same strings ranked by relevance [record_id:229]. Its goal is to make “an analyst’s life easier,” directing attention to the top of the ranked output [record_id:229]. The analyst still interprets the binary and investigates findings.

Similarly, the 2017 social media security talk emphasizes learning attacker patterns to predict incoming threats, but it also frames the work through “security data practitioners” remaining agile in threat research [record_id:252]. The machine learning workflow supports practitioners dealing with an interrupt-driven environment; it is not described as eliminating human analysis.

### Expert knowledge converted into scalable models

The strongest example of encoding expert judgment appears in the 2019 StringSifter talk. The record describes using Snorkel, a weak supervision procedure, to train a generative model over “SME-derived signatures,” also called labeling functions, which resolve conflicts and produce probabilistic labels [record_id:229]. This allows reverse engineers’ subject-matter expertise to be incorporated into a model without hand-labeling the full corpus [record_id:229].

The 2017 talk is less explicit about expert knowledge representation, but it similarly recognizes that human experts can distinguish threatening from benign social content while arguing that statistical methods are needed at scale [record_id:252]. Both records therefore treat human judgment as a scarce resource to be amplified by machine learning.

### Robustness to noisy, evolving, adversarial environments

The social media record explicitly names adversarial drift: social threats are “diverse and continuously evolving,” and statistical methods need to be robust to changing attacker behavior [record_id:252]. It lists a broad threat landscape including malware, phishing links, financial scams, fake news, and spam botnets [record_id:252]. The talk’s emphasis on learning attacker patterns to predict new threats indicates a concern with generalization beyond already-seen examples [record_id:252].

The malware strings record addresses a related but different kind of noise and ambiguity. Relevant strings are rare, irrelevant strings dominate, and the definition of relevance can vary among analysts [record_id:229]. The use of probabilistic labels from Snorkel reflects a method for handling noisy, conflicting labeling functions and uncertain ground truth [record_id:229]. While the record does not explicitly discuss adversarial evasion in malware string generation, it does address ambiguity, label scarcity, and generalization to holdout datasets [record_id:229].

### Learning-to-rank and prioritization as security workflows

A distinctive contribution in the 2019 record is the application of learning-to-rank to malware string analysis. The talk notes that learning-to-rank has historically been used in web search and recommendation engines, then applies that lens to ranking extracted strings by relevance for malware analysis [record_id:229]. This is notable because it frames a common reverse-engineering task as an information retrieval and prioritization problem rather than a binary classification problem.

The 2017 record also contains a prioritization logic, although less explicitly. It discusses classifying social-network-agnostic text, image, and behavioral data so that attacker patterns can be learned and incoming threats predicted [record_id:252]. In both cases, the underlying workflow is about surfacing the most relevant or threatening items from noisy streams of candidates.

### Lean and agile security data practice

The 2017 talk’s title and abstract emphasize “Lean” and the alignment of “batch-driven software development life cycle” with the “interrupt-driven nature of threat research” [record_id:252]. This suggests a methodological theme beyond model architecture: the difficulty of building production security systems when threat research produces urgent, unpredictable demands. The talk appears to advocate workflows that let security data practitioners remain agile while still using disciplined software development practices [record_id:252].

The 2019 talk does not use the same lean/agile language, but its proposed tool is operationally pragmatic: it sits downstream from an existing utility, consumes a familiar artifact, and returns ranked outputs usable in an analyst workflow [record_id:229]. Both records therefore emphasize deployable security workflows, not just abstract modeling.

## Methods, Tools, And Approaches Discussed

The most concrete tool discussed is **StringSifter**, described as an open-source machine-learning-based tool for automatically ranking strings extracted from binaries [record_id:229]. It is designed to operate after the Unix-style `strings` workflow: it takes a list of printable strings as input and returns the same strings ranked according to relevance for malware analysis [record_id:229]. The goal is to reduce analyst fatigue and help analysts inspect likely-useful strings first [record_id:229].

The StringSifter approach includes several methodological components:

- **Large-scale training data from malware binaries**: The model is trained on a sample of 3.1 billion individual strings extracted from `Strings` outputs of 400,000 malicious PE files in the EMBER dataset [record_id:229].
- **Weak supervision using Snorkel**: Strings are labeled with ordinal ranks obtained from Snorkel, which is described as training a generative model over subject-matter-expert-derived signatures or labeling functions [record_id:229].
- **Conflict resolution and probabilistic labels**: Snorkel produces probabilistic labels for strings, accounting for correlation structure among labeling functions [record_id:229].
- **Data programming**: The record characterizes the approach as data programming, enabling cheap and rapid annotation of a large string corpus while incorporating reverse-engineering expertise [record_id:229].
- **Learning-to-rank models**: Weakly supervised labels and transformed string features are fed into competing discriminative models with learning-to-rank loss functions [record_id:229].
- **Ranking evaluation**: The models are evaluated using mean normalized discounted cumulative gain, or nDCG, borrowed from search and recommendation evaluation [record_id:229].
- **Live demonstration**: The talk planned to demonstrate predictions on sample binaries [record_id:229].

The 2017 record discusses a broader **machine learning workflow for social media security** rather than a named tool. The workflow is described as flexible and capable of classifying “social network-agnostic text, image and behavioral data” [record_id:252]. The record indicates that real-world examples would show how attacker patterns can be learned to predict new and incoming threats [record_id:252]. It also mentions the use of social data for red-team simulations and the automation of traditionally manual attack workflows such as spear phishing and steganography using machine learning [record_id:252].

Together, these approaches show Tully’s interest in multiple machine learning modes:

- Classification of malicious or abusive social media content [record_id:252].
- Behavioral, textual, and image-based feature use across social platforms [record_id:252].
- Predictive modeling of attacker patterns [record_id:252].
- Red-team automation using machine learning for spear phishing and steganography simulations [record_id:252].
- Weak supervision and learning-to-rank for malware reverse-engineering support [record_id:229].

A notable methodological bridge across the records is that both treat machine learning as part of a workflow embedded in operational security practice. The 2017 talk focuses on agile workflows for threat research and software development alignment [record_id:252]. The 2019 talk focuses on inserting a ranking model into an established static-analysis process [record_id:229].

## Notable Talks, Records, And Evidence

The most technically detailed record is the 2019 CAMLIS talk, “Learning to Rank Relevant Malware Strings Using Weak Supervision” [record_id:229]. It matters because it provides a concrete example of an applied security machine-learning system: StringSifter. The record identifies a specific pain point in malware analysis, explains why manual inspection of strings is difficult, and proposes a tool that ranks strings by relevance [record_id:229]. It is also the strongest evidence for Tully’s engagement with weak supervision, Snorkel, learning-to-rank, large-scale malware datasets, and evaluation through nDCG [record_id:229]. For downstream agents studying security ML workflows, this record is likely the anchor source.

The 2017 CAMLIS talk, “Lean, Data-Driven Social Media Security,” is broader and important for understanding Tully’s earlier framing of security machine learning in an operational environment [record_id:252]. It lays out a threat landscape of social media abuse, including malware, phishing links, financial scams, fake news, and spam botnets [record_id:252]. It also addresses classification across text, images, and behavioral data, adversarial drift, red-team simulations, and automation of spear phishing and steganography workflows [record_id:252]. This record is especially relevant for downstream research into social media security, detection engineering, adversarial adaptation, and the organizational challenge of keeping machine-learning workflows agile in threat research contexts.

Taken together, the two talks show a consistent orientation toward **applied, security-specific machine learning**. The 2017 record presents a broad operational philosophy for social threat detection and agile security data practice [record_id:252]. The 2019 record demonstrates a more narrowly scoped but technically detailed implementation in malware analysis [record_id:229].

## Gaps, Limits, And Open Questions

The evidence base is thin because it consists of only two presentation abstracts. The records identify topics and planned content, but they do not provide full technical papers, slide decks, source code repositories, experimental tables, or post-deployment results. As a result, downstream researchers should be cautious when inferring details not present in the raw text.

Several gaps remain:

1. **Empirical performance details are limited.**  
   The StringSifter record states that the presentation will discuss “generalizable nDC