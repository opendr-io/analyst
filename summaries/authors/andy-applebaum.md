# Topic: Author: Andy Applebaum

## Executive Summary

The two records attributed to Andy Applebaum are CAMLIS talks/papers from 2019 and 2021 focused on the intersection of adversarial machine learning, malware classification, and Windows PE malware analysis. Collectively, they show a progression from experimenting with adversarial example generation against malware classifiers to proposing a defensive classifier architecture intended to detect adversarially modified malware.

The 2019 record, “Trying to Make Meterpreter into an Adversarial Example,” reports experiments attempting to make Meterpreter payloads evade a malware classifier using reinforcement-learning-based perturbations through the open-source `gym-malware` package. The results were described as “underwhelming,” with little difference between black-box, gray-box, and random perturbation agents, but the work surfaced an important practical finding: compilation choices made through `msfvenom`—such as templates and encoders—could have larger effects on classifier confidence than post-compilation perturbations [record_id:213].

The 2021 record, “Kipple: Towards accessible, robust malware classification,” describes the development of “Kampff,” a Windows PE malware classifier designed to detect evasion attempts. Kampff uses a portfolio or ensemble of classifiers: a primary classifier for “normal” malware plus additional classifiers trained for specific types of adversarial malware. The record frames this as a practical, accessible defense that makes bypassing a classifier “significantly harder — though not impossible,” and emphasizes lessons learned, methodology, comparative performance against adversarial retraining, and intended open-source release of models, data, and scripts [record_id:210].

Together, the records present Applebaum’s work as pragmatic security-oriented adversarial ML research: not merely showing that ML malware classifiers can be attacked, but exploring what happens when attacks are attempted on real malware tooling, and then developing approachable defensive architectures for practitioners and newcomers.

## Research Landscape

The record set is small but thematically coherent: both records come from CAMLIS, both are attributed to Andy Applebaum, both are tagged with MITRE, and both sit at the boundary between machine learning model security and malware analysis/reverse engineering. The dominant subject is adversarial machine learning applied to Windows PE malware classification.

The 2019 record is experimental and attack-oriented. It asks whether a well-known remote access trojan/payload, Meterpreter, can be transformed into an adversarial example against a malware classifier. The setup uses adversarial example concepts—perturbing correctly classified inputs until misclassification—then applies them in a malware context using `gym-malware`, reinforcement learning, and PE-file perturbations [record_id:213].

The 2021 record is defensive and system-building-oriented. It starts from the observation that static ML malware detection has shown promise but remains vulnerable to adversarial ML, and then describes “Kampff,” a classifier intended to detect evasion attempts through an ensemble-like portfolio of classifiers [record_id:210]. The record’s title metadata says “Kipple: Towards accessible, robust malware classification,” while the raw text repeatedly names the developed system “Kampff.” Based on the raw text, “Kampff” is the tool or classifier actually described [record_id:210].

The overall research area is therefore not general malware detection alone, nor abstract adversarial ML alone. It is practical adversarial robustness for malware classifiers, with a strong focus on Windows PE files, evasion attempts, classifier decision boundaries, and the operational difficulty of building reliable defenses.

## Major Themes And Trends

### 1. Adversarial ML as a practical malware-classification problem

Both records treat adversarial ML as a concrete security concern for malware classifiers rather than a purely academic phenomenon. The 2019 record explains adversarial examples as crafted inputs designed to cross classifier decision boundaries while remaining largely the same underlying instance, and notes that such methods have been shown to apply across domains, including security [record_id:213]. The 2021 record similarly states that ML-based malware classifiers are susceptible to adversarial ML, where attackers tailor malware to evade classifiers by exploiting weaknesses in ML techniques [record_id:210].

This shared framing suggests a recurring concern: static ML malware detection may achieve high accuracy under normal evaluation, but that accuracy can be brittle when attackers adapt their binaries or generation process to exploit classifier behavior.

### 2. Emphasis on Windows PE malware and real tooling

The records focus specifically on Windows PE malware. The 2019 experiment uses PE files generated from Meterpreter through `msfvenom`, varying compilation options such as templates, encoders, added code, and other settings [record_id:213]. The 2021 defensive system is explicitly described as a “Windows PE malware classifier” [record_id:210].

This is significant because the work is grounded in a file format and ecosystem that matter operationally for malware detection. Rather than focusing on toy datasets or image-classification-style adversarial examples, the records emphasize payload generation, PE perturbations, compilation parameters, and evasion of malware classifiers.

### 3. Pragmatism over theoretical guarantees

A strong theme across the records is practical evaluation with modest claims. The 2019 talk reports negative or underwhelming results: the reinforcement learning approach did not substantially outperform gray-box or random agents, and changing the perturbation-game length from 10 to 20 perturbations did not significantly change outcomes [record_id:213]. Rather than presenting this as failure, the record uses the result to identify future research directions in both pre- and post-compilation adversarial example construction [record_id:213].

The 2021 record also avoids overclaiming. Kampff is described as making bypass “significantly harder — though not impossible” [record_id:210]. This caveat is important: the defense is presented as an improvement in attacker difficulty and robustness, not as a complete solution to adversarial malware.

### 4. Shift from attack experimentation to defensive classifier design

The two records show a chronological movement. In 2019, Applebaum investigates whether adversarial perturbation methods can make Meterpreter evasive [record_id:213]. In 2021, the work shifts toward building a classifier architecture designed to detect evasion attempts [record_id:210].

This progression is not necessarily a direct continuation, but the intellectual trajectory is clear: first, examine the feasibility and limits of adversarial malware construction; then, propose a defensive model portfolio to make classifier evasion harder. The later record’s focus on “lessons learned” and accessibility also suggests a maturation from exploratory experimentation toward reusable guidance and artifacts for the community [record_id:210].

### 5. Accessibility and reproducibility as explicit goals

The 2021 record emphasizes making adversarial malware defense more accessible to newcomers. It states that defending against adversarial ML attacks is challenging, “particularly for those not steeped in the field,” and says the authors intend to include “lessons learned” for newcomers [record_id:210]. It also says they intend to release Kampff’s models, data, and scripts as open-source software [record_id:210].

The 2019 record also relies on open-source tooling, specifically `gym-malware`, and uses `msfvenom` to compile different Meterpreter versions [record_id:213]. While it does not make the same explicit accessibility claim as the 2021 record, it reflects a similar research style: use available tooling to test adversarial ML claims in a malware setting.

## Methods, Tools, And Approaches Discussed

The records discuss several concrete methods and workflows.

In the 2019 record, the core approach is adversarial example construction against a malware classifier using reinforcement learning. The talk describes leveraging the open-source `gym-malware` package, which treats the target classifier as a black box and trains an agent to apply perturbations to PE files in ways that produce evasive malware [record_id:213]. The experiment deviates from prior work by training and testing only on different Meterpreter versions, rather than broadly across malware families. Those Meterpreter variants were compiled using `msfvenom` with varying options, including templates, encoders, added code, and other compilation choices [record_id:213].

The 2019 experiment compares multiple adversarial settings or agent types: fully black-box, gray-box, and random perturbation agents. It also varies the “game length,” comparing 10 versus 20 perturbations per instance [record_id:213]. The reported finding is that these distinctions did not produce major performance differences. More interestingly, the compilation parameters themselves could make samples “naturally evasive,” with encoders increasing classifier confidence and templates—even malicious executable templates—decreasing it [record_id:213]. This points to an important methodological lesson: in malware adversarial ML, the way a binary is generated may matter as much as, or more than, downstream adversarial perturbation.

In the 2021 record, the central method is a classifier portfolio or ensemble. Kampff uses a primary classifier designed to detect “normal” malware, then attaches additional classifiers designed for specific types of adversarial malware [record_id:210]. The raw text characterizes the approach as “simplistic,” but says it significantly increases the difficulty of bypassing the primary classifier [record_id:210]. The record also says this ensemble approach outperforms one based on “simple adversarial retraining,” suggesting that Applebaum’s work contrasts specialized adversarial detectors with the common strategy of augmenting training data with adversarial examples [record_id:210].

The 2021 record further highlights methodology and performance notes, though the raw text does not provide detailed metrics. It indicates that the paper reports on the process of developing Kampff and includes lessons learned for newcomers, along with an intention to release models, data, and scripts [record_id:210]. For downstream researchers, this makes the record important not only for its classifier design but also for its promise of reproducible artifacts—though the record itself does not confirm whether release occurred.

## Notable Talks, Records, And Evidence

The most representative early record is the 2019 CAMLIS talk “Trying to Make Meterpreter into an Adversarial Example” [record_id:213]. Its importance lies in its practical adversarial ML experiment. Rather than merely asserting that malware classifiers can be attacked, it tests a concrete scenario: can Meterpreter, a well-known and heavily signatured RAT/payload, be made into an adversarial example? The experiment uses `gym-malware`, reinforcement learning, and multiple Meterpreter builds generated through `msfvenom` [record_id:213]. Its negative findings are especially valuable: black-box, gray-box, and random agents yielded little difference, and increasing perturbation length did not significantly improve results [record_id:213]. The talk’s most notable insight is that compilation parameters may cause natural evasion before adversarial perturbations are even applied [record_id:213].

The most representative later record is the 2021 CAMLIS record “Kipple: Towards accessible, robust malware classification” [record_id:210]. Despite the title naming “Kipple,” the raw text describes a system called “Kampff,” a Windows PE malware classifier designed to detect evasion attempts [record_id:210]. Its importance lies in proposing a defensive architecture: a primary malware classifier paired with classifiers specialized for adversarial malware types [record_id:210]. The record explicitly positions this as a way to make adversarial bypass harder, as an accessible example defense, and as a resource for newcomers through lessons learned and intended open-source release [record_id:210].

Together, these records are notable because they cover both sides of the adversarial malware problem. The 2019 talk investigates adversarial construction and reveals the messy role of malware build parameters [record_id:213]. The 2021 paper/talk proposes a structured defensive response and emphasizes accessibility, reproducibility, and comparison against adversarial retraining [record_id:210].

## Gaps, Limits, And Open Questions

The evidence base is narrow: only two records, both from CAMLIS, both short abstracts or descriptions rather than full papers. As a result, the records give strong evidence of topic focus and research direction, but limited detail on experimental design, datasets, metrics, implementation, or reproducibility outcomes.

Several open questions remain:

- **What exact classifiers were used?** The 2019 record refers to a target classifier but does not specify architecture, feature representation, training data, or baseline performance [record_id:213]. The 2021 record mentions a primary classifier and additional adversarial classifiers but does not describe their model types, features, dataset sizes, or thresholds [record_id:210].

- **How large and representative were the datasets?** The 2019 record focuses on Meterpreter variants generated with `msfvenom`, which is intentionally narrow and useful for the research question, but it may not generalize to other malware families [record_id:213]. The 2021 record says Kampff was built from data intended for open-source release, but the abstract does not specify the data composition [record_id:210].

- **How robust is the ensemble approach against adaptive attackers?** The 2021 record says Kampff makes bypass significantly harder but not impossible [record_id:210]. It remains unclear how it performs against attackers aware of the full classifier portfolio, or against attacks optimized jointly against all classifiers.

- **Did the intended open-source release occur?** The 2021 record states an intention to release Kampff’s models, data, and scripts [record_id:210]. The record itself does not establish whether those artifacts were eventually released, where they are hosted, or whether they remain usable.

- **What is the relationship between “Kipple” and “Kampff”?** The record title says “Kipple,” while the raw text describes “Kampff” as the developed classifier [record_id:210]. Downstream researchers should verify whether this reflects a title/tool-name distinction, a typo, a project rename, or metadata inconsistency.

- **How should pre-compilation and post-compilation adversarial strategies be compared?** The 2019 record’s most interesting observation is that `msfvenom` compilation options could produce natural evasion effects, sometimes more meaningfully than reinforcement-learning perturbations [record_id:213]. This raises a broader research question