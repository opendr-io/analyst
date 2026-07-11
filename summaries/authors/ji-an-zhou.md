# Topic: Author: Ji'an Zhou

## Executive Summary

The three records attributed to Ji’an Zhou center on vulnerability discovery in widely deployed software ecosystems, with an emphasis on remote code execution (RCE) risks in systems that users may incorrectly assume are safe. Two records describe substantially the same PyTorch/TorchScript research, presented at Black Hat USA 2025 and DEF CON 33, co-authored with Li’shuo/Lishuo Song. That work challenges the perceived safety of `torch.load` when used with `weights_only=True`, arguing that TorchScript support within that supposedly safer loading path enabled the researchers to discover multiple vulnerabilities and ultimately achieve RCE, acknowledged by PyTorch as CVE-2025-32434 [record_id:2] [record_id:1968].  

The third record expands Ji’an Zhou’s apparent research focus beyond machine learning model security into distributed infrastructure and cloud-facing application security. It describes a DEF CON 33 talk on Apache Kafka, claiming the first exploitable RCE vulnerability affecting Kafka Server/Broker itself, as well as related attacks against other Kafka ecosystem components and potential impact on cloud service providers [record_id:1993].

Collectively, the records portray Ji’an Zhou as a researcher focused on finding high-impact RCE vulnerabilities in trusted, popular infrastructure: deep learning model-loading pipelines in PyTorch and server-side distributed messaging infrastructure in Kafka. A recurring theme is the discovery of dangerous behavior hidden behind components that are widely used, security-relevant, and often implicitly trusted by developers or operators.

## Research Landscape

The available corpus is small but focused: three 2025 conference records, all describing security briefings or talks. The sources are Black Hat and DEF CON 33, which suggests the records represent public conference presentations rather than blog posts, academic papers, or code repositories. The evidence base is therefore abstract-level and promotional rather than deeply technical; the raw records summarize the claims and intended talk contents, but do not provide exploit details, patch analysis, proof-of-concept code, or full vulnerability writeups.

Two of the three records concern the same PyTorch/TorchScript research. The Black Hat USA 2025 record is titled “Safe Harbor or Hostile Waters: Unveiling the Hidden Perils of the TorchScript Engine in PyTorch (PRE-RECORDED)” and is attributed to Ji’an Zhou and Li’shuo Song [record_id:2]. The DEF CON 33 version, “Unveiling the Perils of the TorchScript Engine in PyTorch,” is attributed to Ji’an Zhou and Lishuo Song and appears to be a 34:46 video record [record_id:1968]. The raw text of both records is nearly identical, describing PyTorch model deserialization, the historical risks of Python `pickle`, the introduction of `weights_only`, and the researchers’ finding that `torch.load` with `weights_only=True` supports TorchScript in a way that led to RCE [record_id:2] [record_id:1968].

The third record is a separate DEF CON 33 talk titled “Client or Server? Hidden Sword of Damocles in Kafka,” attributed to Ji’an Zhou, Ying Zhu, and ZiYang ’ Li [record_id:1993]. It concerns Apache Kafka, particularly the Broker/Kafka Server, Kafka’s ecosystem components such as Confluent ksqlDB and Schema Registry, and RCE vulnerabilities affecting Kafka Server and related ecosystem components [record_id:1993].

The overall research area represented by these records is exploit development and vulnerability discovery in high-value software platforms. The PyTorch records fall under machine learning model security and application security, while the Kafka record fits infrastructure, cloud, and application security. Across both areas, the common thread is not merely that bugs exist, but that bugs exist in places where prevailing assumptions may have discouraged scrutiny: `weights_only=True` in PyTorch as a supposedly safer loading mode, and Kafka Server/Broker as a previously unexploited RCE target compared with Kafka Client [record_id:2] [record_id:1968] [record_id:1993].

## Major Themes And Trends

### Challenging “safe” assumptions in widely trusted systems

The strongest recurring theme is the reversal of perceived safety. In the PyTorch work, the records explicitly frame `weights_only=True` as a recommended safer alternative to unsafe pickle-based model loading. The raw text states that PyTorch initially used pickle to save models, that pickle deserialization created RCE risk when loading models, and that PyTorch later introduced the `weights_only` parameter to improve security [record_id:2] [record_id:1968]. The official documentation is described as stating that `weights_only=True` is considered safe and recommending it over `weights_only=False` [record_id:2] [record_id:1968]. Ji’an Zhou and co-author then claim their research “uncovered unsettling truths,” discovering that `torch.load` with `weights_only=True` supports TorchScript, leading to vulnerabilities and RCE [record_id:2] [record_id:1968].

The Kafka record uses a similar rhetorical structure. It first describes Kafka as an open-source distributed event streaming platform with the Broker as the central server node, then notes that prior research had revealed RCE vulnerabilities in Kafka Client but that exploitable RCE vulnerabilities in Kafka Server were “notably absent” until this work [record_id:1993]. This again positions the research as a challenge to a boundary in the prior threat model: the vulnerable surface was not merely a client-side component, but the server/Broker itself [record_id:1993].

### Remote code execution as the central impact

All three records revolve around RCE. The PyTorch records begin from historical pickle deserialization RCE risk and then assert that the authors achieved RCE through TorchScript support in the `weights_only=True` loading path [record_id:2] [record_id:1968]. The Kafka record claims the “first-ever RCE vulnerability affecting Kafka Server itself” and says similar techniques were used against other Kafka ecosystem components [record_id:1993].

This focus on RCE gives the records a clear severity pattern. Ji’an Zhou’s represented work is not about low-severity misconfiguration, information disclosure, or theoretical hardening alone; it is about code execution in systems that may process untrusted or semi-trusted inputs. The impacts are framed as broad because PyTorch is described as one of the most popular deep learning frameworks used in computer vision and natural language processing [record_id:2] [record_id:1968], while Kafka is described as a central event streaming platform whose ecosystem includes components for real-time analytics and data format standardization across microservices [record_id:1993].

### Ecosystem-level security rather than isolated bugs

Another important theme is ecosystem complexity. The PyTorch records are not only about `torch.load` or pickle in isolation; they connect PyTorch’s model loading behavior with TorchScript internals. The researchers say that discovering `torch.load` with `weights_only=True` supports TorchScript led them to investigate TorchScript’s inner workings, where they found several vulnerabilities [record_id:2] [record_id:1968]. This implies an attack surface created by feature interaction: a safety parameter intended to mitigate one deserialization risk still allowed a complex subsystem to participate in loading behavior.

The Kafka record explicitly emphasizes ecosystem expansion. It describes Kafka’s “real strength” as coming from its growing ecosystem and names components such as Confluent ksqlDB and Schema Registry [record_id:1993]. The talk then claims that “behind the rich components lie hidden security threats,” and that the authors used similar techniques to attack other components in the Kafka ecosystem [record_id:1993]. The security concern is therefore not limited to the Broker alone, but includes interdependent components and cloud services built around Kafka.

### High deployment impact and cloud relevance

The records repeatedly stress widespread impact. PyTorch is described as “one of the most popular deep learning frameworks,” with applications in computer vision and natural language processing [record_id:2] [record_id:1968]. The PyTorch vulnerability is said to have “profound implications for numerous AI applications” [record_id:2] [record_id:1968]. Kafka is described as a central distributed event streaming platform, and the Kafka record states that the vulnerabilities “can also affect the cloud service providers themselves” and that “thousands of Kafka servers are now exposed” [record_id:1993].

These statements suggest that Ji’an Zhou’s public work, at least in this corpus, prioritizes vulnerabilities with broad operational relevance: AI supply chains and model loading on one side, distributed streaming infrastructure and managed cloud services on the other.

### Responsible disclosure appears in the PyTorch records

The PyTorch records state that the researchers “promptly reported” their finding to PyTorch, that PyTorch acknowledged the vulnerability, and that CVE-2025-32434 was assigned [record_id:2] [record_id:1968]. This is the only explicit disclosure-process detail in the corpus. The Kafka record does not mention a CVE identifier, vendor acknowledgment, patch status, or coordinated disclosure timeline in the raw text provided [record_id:1993].

## Methods, Tools, And Approaches Discussed

The records provide only high-level methodological detail, but several approaches are visible.

In the PyTorch/TorchScript research, the method begins with revisiting a security assumption around model loading. PyTorch’s older pickle-based model saving/loading is described as risky because insecure pickle deserialization can lead to RCE [record_id:2] [record_id:1968]. PyTorch’s `weights_only` parameter is presented as the mitigation, with `weights_only=True` documented as safer [record_id:2] [record_id:1968]. The researchers then found that `torch.load` with `weights_only=True` supports TorchScript, which shifted the investigation into the “inner workings” of the TorchScript engine [record_id:2] [record_id:1968]. The raw records do not specify the exact bug classes, payload construction, bytecode or IR mechanisms, or exploit primitives, but they do state that the investigation produced “several vulnerabilities” and culminated in RCE [record_id:2] [record_id:1968].

The important methodological pattern is therefore feature-interaction analysis: examine a security boundary, identify unexpected supported formats or execution paths within that boundary, and then audit the deeper engine responsible for parsing or executing that content. In this case, the boundary is `weights_only=True`, and the deeper engine is TorchScript [record_id:2] [record_id:1968].

In the Kafka research, the method is framed as extending prior attack knowledge from client-side Kafka RCE research to the server and ecosystem. The record says prior research had revealed RCE vulnerabilities in Kafka Client, but not exploitable RCE in Kafka Server, until the presented work [record_id:1993]. It further says the authors used “similar techniques” to attack other Kafka ecosystem components [record_id:1993]. The raw record does not identify those techniques, the vulnerable APIs, serialization paths, protocol features, authentication assumptions, or exploit chains. Still, the described approach appears to involve analyzing the Kafka Broker/Kafka Server attack surface and then generalizing the technique across adjacent components such as those in the Kafka ecosystem [record_id:1993].

The tools and platforms explicitly discussed are:

- PyTorch, as a machine learning library based on Torch and used in computer vision and natural language processing [record_id:2] [record_id:1968].
- `torch.load`, specifically with `weights_only=True`, as the model-loading API implicated in the PyTorch research [record_id:2] [record_id:1968].
- TorchScript, as the PyTorch subsystem whose support in `weights_only=True` loading led to vulnerability discovery [record_id:2] [record_id:1968].
- Apache Kafka, especially the Broker/Kafka Server as the central server node in a Kafka cluster [record_id:1993].
- Kafka ecosystem components including Confluent ksqlDB and Schema Registry, mentioned as examples of components that expand Kafka’s capabilities and may be part of the broader security landscape [record_id:1993].

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 PyTorch briefing is one of the core records because it provides the most formal conference framing and includes the full provocative title: “Safe Harbor or Hostile Waters: Unveiling the Hidden Perils of the TorchScript Engine in PyTorch (PRE-RECORDED)” [record_id:2]. Its contribution is the claim that a PyTorch loading configuration considered safe, `weights_only=True`, could still lead into TorchScript-supported behavior that enabled RCE [record_id:2]. The record also includes the important disclosure claim that PyTorch acknowledged the vulnerability and assigned CVE-2025-32434 [record_id:2]. It notes that the session was pre-recorded and that the speaker would not present in person, which is logistical rather than technical, but relevant for understanding the record type [record_id:2].

The DEF CON 33 PyTorch talk appears to be the same research adapted for a DEF CON audience, under the shorter title “Unveiling the Perils of the TorchScript Engine in PyTorch” [record_id:1968]. Its raw text closely mirrors the Black Hat description, repeating the claim that `torch.load` with `weights_only=True` supports TorchScript, that the researchers investigated TorchScript internals, found several vulnerabilities, achieved RCE, and received CVE-2025-32434 after reporting to PyTorch [record_id:1968]. This duplication strengthens confidence that the PyTorch/TorchScript work is a central and deliberate research contribution by Ji’an Zhou rather than an incidental mention. However, because the two records are not independent technical writeups and appear to share nearly identical abstract text, they should not be treated as two independent confirmations of exploit details.

The DEF CON 33 Kafka talk, “Client or Server? Hidden Sword of Damocles in Kafka,” is the most distinct record in the corpus [record_id:1993]. It broadens the author profile from AI/ML security into distributed systems and cloud infrastructure. The record’s key claim is that the authors present the first exploitable RCE vulnerability affecting Kafka Server itself, not just Kafka Client [record_id:1993]. It also