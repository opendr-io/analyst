# Topic: Author: Tamás Vörös

## Executive Summary

The three records attributed to Tamás Vörös span CAMLIS presentations from 2021, 2024, and 2025 and show a progression from large-scale network security detection toward machine learning model security and, more specifically, defenses for large language models. The earliest record focuses on predicting malicious internet infrastructure using deep learning over IP-address-derived signals, with the goal of augmenting or replacing traditional allow/block lists at internet scale [record_id:205]. The later two records shift into LLM security: one studies how to mitigate Trojan/backdoor behavior in LLMs through targeted noising of important neurons while preserving model utility [record_id:150], and the most recent proposes “LLM salting,” a lightweight defense that rotates an internal refusal direction so that previously effective jailbreak prompts become ineffective without degrading utility [record_id:113].

Collectively, these records portray Vörös’s work as security-focused applied machine learning. The recurring concern is how to build scalable, low-overhead defenses against adversarial or malicious behavior when exhaustive inspection or complete prior knowledge is impractical. In the network-security record, the problem is that decrypting or deeply inspecting all traffic is too costly, so a learned pre-filter for suspicious IPs is proposed [record_id:205]. In the LLM-backdoor record, the problem is that public foundation models are opaque and may contain unknown Trojans, so controlled Trojan insertion is used to identify and neutralize suspicious activation patterns [record_id:150]. In the jailbreak-defense record, the problem is that jailbreak prompts can remain effective across models or configurations, so the proposed defense changes the model’s refusal geometry to invalidate previously effective attacks [record_id:113].

The evidence base is small but coherent. All three records are short CAMLIS abstracts rather than full papers, code releases, or experimental appendices. The strongest quantitative evidence appears in the 2024 LLM backdoor record, which reports concrete model families, datasets, noise levels, accuracy drops, and reductions in Trojan unigram recall [record_id:150]. The 2021 network-security record also reports comparative AUC improvements across two datasets [record_id:205]. The 2025 LLM salting record is conceptually important but provides only a brief claim about jailbreak resistance and utility preservation, with little methodological or quantitative detail in the supplied text [record_id:113].

## Research Landscape

The topic consists of three CAMLIS records attributed to Tamás Vörös, covering talks or presentations in 2021, 2024, and 2025. The records are not a broad bibliography; they are event abstracts. Their source material is concise, with varying levels of technical detail.

The landscape divides into two main research areas:

1. **Network security and malicious infrastructure prediction.**  
   The 2021 record, “Bad neighborhoods – learning malicious infrastructure at internet scale,” addresses the practical problem of detecting malicious communication without applying expensive inspection to all traffic. It frames modern malware—including Remote Administration Tools, ransomware, coin miners, and espionage tools—as dependent on internet communications for commands, payload transmission, or data exfiltration [record_id:205]. The proposed response is to learn from existing allow/block lists and predict whether previously unseen IP addresses are likely connected to known malicious behavior [record_id:205].

2. **LLM and model security.**  
   The 2024 and 2025 records focus on large language model vulnerabilities and defenses. “LLM Backdoor Activations Stick Together” is concerned with Trojan attacks in opaque public foundation models and proposes targeted noising of neurons as a mitigation strategy [record_id:150]. “LLM Salting: From Rainbow Tables to Jailbreaks” proposes a lightweight mechanism that rotates the internal refusal direction of LLMs to make previously effective jailbreak prompts, such as GCG, ineffective while preserving utility [record_id:113].

Across the records, the dominant source type is the conference abstract. This means the topic summary can identify themes, methods, claims, and reported metrics, but cannot fully verify experimental setup, reproducibility, threat models, or implementation details beyond what the abstracts state.

The overall research area can be characterized as **security-oriented machine learning for adversarial environments**. Vörös’s attributed work, as represented here, repeatedly tackles cases where defenders must act under constraints: limited compute, incomplete inspection, opaque models, unknown Trojans, or reusable adversarial prompts. The proposed defenses are not purely rule-based; they use machine learning structure, representation learning, pretraining, neuron-level intervention, or internal model geometry.

## Major Themes And Trends

### 1. Security under resource and knowledge constraints

A central theme is that defenders rarely have the luxury of complete information or unlimited computation.

In the 2021 network-security record, the abstract emphasizes that identifying malicious communication may require firewalls to decrypt encrypted traffic, query cloud infrastructure, or perform other resource-intensive computations, making full data collection impractical for all passing traffic [record_id:205]. The proposed solution is not to eliminate deeper inspection but to use IP allow/block lists and learned prediction as a “computational cheap pre-filter” for more expensive operations [record_id:205].

The same theme appears in the 2024 LLM-backdoor record, but the constraints are different. The challenge is the “opaque nature” of LLMs and their vulnerability to Trojan attacks [record_id:150]. The record explicitly states that the study does not assume prior knowledge about the existence or nature of Trojans in the models [record_id:150]. This is important: the proposed defense is positioned for a world where defenders may not know whether a model is compromised or what trigger behavior to search for.

In the 2025 LLM-salting record, the implied constraint is the difficulty of preventing previously discovered jailbreak prompts from generalizing or remaining effective. The proposed mechanism is described as “lightweight” and intended to render previously effective jailbreak prompts ineffective without degrading model utility [record_id:113]. Although the supplied abstract is brief, it fits the same pattern: a low-overhead defense against adversarial reuse.

### 2. Moving from external infrastructure detection to internal model defense

The records show a chronological shift in security focus. In 2021, the object of analysis is internet infrastructure: IP addresses, malicious neighborhoods, allow/block lists, and traffic pre-filtering [record_id:205]. By 2024 and 2025, the object of analysis is the LLM itself: neurons, activation patterns, Trojans, refusal directions, and jailbreaks [record_id:150] [record_id:113].

This is not a complete departure from the earlier work. The underlying approach remains similar: identify useful structure in a high-dimensional or difficult-to-inspect system, then exploit that structure to make defensive decisions more efficient. In 2021, structure in IP space and learned representations are used to generalize beyond listed IPs [record_id:205]. In 2024, structure in neuron importance and Trojan activations is used to selectively noise model internals [record_id:150]. In 2025, structure in the LLM’s refusal direction is manipulated to break jailbreak transfer or reuse [record_id:113].

The trend therefore appears less like a change in research philosophy and more like a change in application domain, from network defense to AI model defense.

### 3. Generalization beyond known bad examples

All three records are concerned with generalizing beyond a limited set of known threats.

The network-security abstract states that allow/block lists are cheap but cannot be applied to unlisted IPs. The proposed model predicts whether a “previously unseen IP address” is likely to be involved in known malicious behavior [record_id:205]. This directly addresses the brittleness of static lists.

The LLM-backdoor abstract says the researchers insert controlled Trojans into models, not because those are the only Trojans of interest, but to analyze neuron importance and show that the approach can neutralize both introduced Trojans and “pre-existing Trojan activations” [record_id:150]. The key claim is that controlled interventions can reveal mitigation strategies that apply beyond the specific inserted triggers.

The LLM-salting abstract similarly focuses on previously effective jailbreak prompts. By rotating the model’s internal refusal direction, the defense is said to make prior jailbreak prompts such as GCG ineffective [record_id:113]. The analogy in the title—“From Rainbow Tables to Jailbreaks”—suggests an interest in making precomputed or reusable attacks stale, although the supplied text only directly supports the claim about rotating refusal direction and invalidating known jailbreak prompts [record_id:113].

### 4. Preserving utility while reducing malicious behavior

A recurring tradeoff is security versus usability. The records emphasize that defenses must avoid destroying legitimate functionality.

The 2024 LLM-backdoor record gives the clearest evidence. It reports that targeted noising preserves LAMBADA dataset accuracy while significantly neutralizing Trojan triggers [record_id:150]. For Pythia, a noise level of approximately 2e-05 of all available neurons is reported to maintain only a 1.6% LAMBADA accuracy drop while reducing Trojan unigram recall to 1.7% [record_id:150]. For Llama2, a noise level of 1.3e-05 produces an accuracy drop of 3.5% while reducing Trojan unigram recall to 5% [record_id:150]. The abstract contrasts this with random noising, which only mitigates Trojan activation “at the cost of complete usability loss” [record_id:150].

The 2025 LLM-salting record also claims that its defense renders previously effective jailbreak prompts ineffective “without degrading model utility” [record_id:113]. However, it does not provide the experimental detail that the 2024 record provides.

In the 2021 network-security record, the utility tradeoff is expressed in operational rather than model-performance terms. The motivation is to avoid expensive computations on all traffic while improving the coverage of allow/block lists [record_id:205]. The reported AUC improvements suggest better detection performance, but the abstract does not quantify operational cost savings or false-positive consequences in deployment [record_id:205].

### 5. Targeted intervention over random or exhaustive approaches

The records favor selective, learned, or targeted defenses instead of random modification or exhaustive inspection.

In the 2021 record, exhaustive deep inspection of all traffic is described as impractical, so a learned model is proposed as a pre-filter [record_id:205]. In the 2024 record, targeted noising of neurons is contrasted with random noising, with targeted noising preserving usability and random noising causing complete usability loss when it mitigates Trojan activation [record_id:150]. In the 2025 record, LLM salting is described as a lightweight defense that rotates a specific internal refusal direction rather than broadly retraining or filtering every possible prompt [record_id:113].

This theme is one of the strongest links across the small corpus: the work seeks precise defensive leverage points.

## Methods, Tools, And Approaches Discussed

The records describe several concrete approaches, though at abstract level.

The 2021 record discusses using machine learning to expand the coverage of IP allow/block lists. The method is framed as building an ML model that can “accurately predict if a previously unseen IP address is likely to be involved in known malicious behavior” [record_id:205]. The record states that predicting malicious traffic based only on IP address is difficult, but that the approach improves on existing baselines using two different deep learning architectures and pretraining [record_id:205]. It reports evaluation on two distinct datasets, where combining architectures and pretraining improves area under the curve from .89 to .93 on one dataset and from .992 to .995 on another [record_id:205]. The practical architecture is a learned augmentation or replacement for traditional allow/block lists, with possible importance for IPv6, where manual list maintenance may become intractable [record_id:205].

The 2024 record presents a neuron-level defense for LLM Trojans. The approach is “targeted noising of neurons,” guided by analysis of neuron importance with respect to Trojans [record_id:150]. The researchers do not assume knowledge of existing Trojans; instead, they insert controlled Trojans into the models to study and mitigate Trojan behavior [record_id:150]. The record claims that this procedure neutralizes inserted Trojans and also mitigates pre-existing Trojan activations [record_id:150]. The experiments use Pythia and Llama2 models, with LAMBADA accuracy as a utility measure and Trojan unigram recall as a measure of triggered malicious behavior [record_id:150]. The reported method depends on carefully choosing a very small fraction of neurons to noise, rather than perturbing the model randomly [record_id:150].

The 2025 record introduces “LLM salting,” described as a lightweight defense mechanism that rotates the internal refusal direction of LLMs [record_id:113]. The stated security goal is to make previously effective jailbreak prompts, including GCG, ineffective without degrading model utility [record_id:113]. The supplied text does not explain the exact implementation of the rotation, how the refusal direction is estimated, whether the method requires fine-tuning or inference-time changes, or how robustness and utility are measured. Still, the approach is notable because it treats jailbreak prompts as reusable artifacts whose effectiveness can be disrupted by changing an internal model property [record_id:113].

Across the methods, several technical motifs recur:

- **Pre-filtering or selective intervention:** ML scoring of IPs before expensive inspection [record_id:205]; targeted noising of important neurons [record_id:150]; refusal-direction rotation rather than broad model changes [record_id:113].
- **Use of learned structure:** deep learning and pretraining for malicious infrastructure prediction [record_id:205]; neuron-importance analysis for Trojan mitigation [record_id:150]; internal refusal geometry for jailbreak resistance [record_id:113].
- **Utility-aware defense:** AUC improvements for malicious IP prediction [record_id:205]; LAMBADA accuracy preservation under targeted noising [record_id:150]; claimed utility preservation under LLM salting [record_id:113].
- **Defense against unknown or reusable threats:** unseen IPs [record_id:205]; unknown or pre-existing Trojans [record_id:150]; previously effective jailbreak prompts [record_id:113].