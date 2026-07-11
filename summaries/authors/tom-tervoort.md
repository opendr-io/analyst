# Topic: Author: Tom Tervoort

## Executive Summary

The available records attributed to Tom Tervoort consist of two 2025 conference entries for the same research topic and title: **“No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol.”** One appears in the Black Hat USA 2025 briefing program, and the other appears as a DEF CON 33 video entry [record_id:7] [record_id:2140]. Together, they describe research into cryptographic weaknesses in **OPC UA**, a standardized protocol widely used in industrial automation, IoT, OT networks, IT/OT bridging, and cloud-connected field systems.

The central contribution described across both records is the identification of **two protocol-level cryptographic flaws** in OPC UA that Tervoort claims could be turned into **practical authentication bypass attacks** against multiple implementations and configurations [record_id:7] [record_id:2140]. The records emphasize that OPC UA’s built-in cryptographic authentication and transport security are often treated as sufficient protection, potentially reducing perceived need for VPN tunnels between OT trust zones. Tervoort’s work challenges that assumption by arguing that if an attacker can hijack an OPC UA server, the operational consequences could be severe for industrial systems controlled through that server [record_id:7] [record_id:2140].

The technical focus is narrow but significant: protocol-level cryptographic attacks involving **signing oracles**, **signature spoofing padding oracles**, and the use of **“RSA-ECB” as a “timing side channel amplifier”** [record_id:7] [record_id:2140]. The evidence base is thin in quantity—only two records—but strong in consistency, because both records describe the same talk and make nearly identical claims.

## Research Landscape

The research landscape represented by these records is concentrated around a single piece of work: a 2025 presentation on cryptographic attacks against OPC UA. The two records come from major security conferences, **Black Hat USA 2025** and **DEF CON 33**, suggesting that the work was positioned for a professional offensive security, vulnerability research, cryptography, and industrial security audience [record_id:7] [record_id:2140].

Both records frame OPC UA as a critical protocol in environments where traditional IT security assumptions intersect with industrial control risk. OPC UA is described as being used:

- within OT networks,
- between OT networks,
- as a bridge between IT and OT environments,
- and to connect field systems with cloud infrastructure [record_id:7] [record_id:2140].

This placement makes the research relevant to several overlapping areas: **OT security**, **IoT security**, **industrial protocol security**, **network security**, **exploit development**, and **applied cryptography**. The Black Hat record explicitly tags the talk under cryptography, cyber-physical systems and IoT, and briefings, while also classifying it under OT and IoT security with secondary relevance to exploit development, vulnerability discovery, network security, and NDR [record_id:7]. The DEF CON record similarly places the talk under OT and IoT security with secondary associations to exploit development and network security, though the raw evidence itself is primarily the talk description [record_id:2140].

The records do not provide a full paper, exploit code, vulnerability identifiers, vendor names, or implementation-specific results. Instead, they provide an abstract-level description of the research claims. That means the landscape is best understood as a conference-presentation snapshot rather than a complete technical corpus.

## Major Themes And Trends

### Challenging Trust In Protocol-Native Security

The dominant theme is skepticism toward the idea that OPC UA’s built-in cryptographic protections remove the need for additional transport protections such as VPNs. Both records state that VPN tunnels have traditionally been used to secure connections between OT trust zones, particularly when connections cross the internet, but that such tunnels are “often considered not to be necessary” when OPC UA is used because the protocol has its own cryptographic authentication and transport security layer [record_id:7] [record_id:2140].

Tervoort’s research, as described, directly challenges this operational assumption. The title “No VPN Needed?” is itself framed as a question, and the talk abstract argues that OPC UA becomes a valuable target precisely because organizations may rely on its native security layer for sensitive OT communications [record_id:7] [record_id:2140].

### Protocol-Level Cryptography As An Attack Surface

A second major theme is that protocol-level cryptographic design can be exploitable even when the intended security model appears sound. The records say Tervoort examined “the cryptography used by the protocol” and found “two protocol flaws” that could be converted into practical authentication bypass attacks [record_id:7] [record_id:2140].

This is important because the described weaknesses are not merely implementation bugs in one product. The records emphasize flaws at the protocol level, with attacks working against “various implementations and configurations” [record_id:7] [record_id:2140]. If accurate, that suggests a broader class of risk than a single-vendor patch issue.

### From Theoretical Cryptographic Weakness To Practical Exploit

The records repeatedly emphasize the process of turning theoretical cryptographic issues into practical attacks. The Black Hat entry states that the talk explores “the process of turning two theoretical crypto flaws into highly practical exploits” [record_id:7]. The DEF CON entry uses nearly the same framing, describing “the process of turning two theoretical crypto flaws into highly practical exploits” [record_id:2140].

This theme is central to Tervoort’s apparent contribution. The records do not merely claim that cryptographic oddities exist; they claim that these flaws were operationalized into authentication bypass attacks. That positions the research at the intersection of cryptanalysis, protocol analysis, and exploit engineering.

### OT/IoT Consequence Framing

The records also frame the risk in terms of physical or operational consequences. Both state that if attackers could hijack an OPC UA server, they might be able to “wreak havoc” on industrial systems controlled by it [record_id:7] [record_id:2140]. This links the cryptographic research to cyber-physical risk: a flaw in authentication or transport security may translate into unauthorized control or disruption of industrial processes.

The records do not provide concrete incident scenarios, safety consequences, or affected industrial sectors. Still, the risk framing is clear: the value of the attack is amplified by OPC UA’s role in industrial automation and IoT systems.

### Repeated Presentation Across Major Venues

Both records refer to the same talk title and nearly identical abstract, appearing at Black Hat USA 2025 and DEF CON 33 [record_id:7] [record_id:2140]. This suggests that the research was presented to multiple high-profile security audiences in the same year. The DEF CON record includes a video identifier and a duration tag of 36:19, indicating that a recorded talk exists, while the Black Hat record appears to be a scheduled briefing entry [record_id:7] [record_id:2140].

The duplication strengthens confidence that this was a significant and deliberate research topic for Tervoort in 2025, but it does not broaden the subject matter beyond the single OPC UA cryptography project.

## Methods, Tools, And Approaches Discussed

The records describe methods at a high level rather than giving step-by-step technical detail. The core approach is **cryptographic protocol analysis** of OPC UA, followed by exploit development against real implementations and configurations [record_id:7] [record_id:2140].

The notable methods and technical concepts include:

- **Analysis of OPC UA cryptographic authentication and transport security.** Tervoort reportedly examined whether protocol-level flaws could compromise implementations that rely on OPC UA’s native security layer [record_id:7] [record_id:2140].

- **Identification of two protocol flaws.** Both records state that the research identified two flaws in the protocol that could be transformed into authentication bypass attacks [record_id:7] [record_id:2140].

- **Signing oracles.** The attacks are said to involve signing oracles, implying that some aspect of protocol behavior may be abused to obtain or infer valid signatures or signature-like behavior under conditions useful to an attacker [record_id:7] [record_id:2140].

- **Signature spoofing padding oracles.** Both records mention “signature spoofing padding oracles,” suggesting that padding behavior in cryptographic verification or signing workflows may leak information or enable forged authentication artifacts [record_id:7] [record_id:2140].

- **Use of “RSA-ECB” as a “timing side channel amplifier.”** This phrase appears in both records and is one of the more distinctive technical claims. It suggests that a cryptographic construction or mode described as “RSA-ECB” may magnify timing differences into a practical side-channel signal [record_id:7] [record_id:2140].

- **Practical authentication bypass testing across implementations.** The records say the attacks worked against “various implementations and configurations,” indicating that the methodology included testing beyond a single target or lab-only scenario [record_id:7] [record_id:2140].

No specific tooling, scripts, test harnesses, packet captures, fuzzers, proof-of-concept exploit names, or affected product names are included in the raw records. The methods therefore remain abstract, but the recurring emphasis is on taking cryptographic theory into exploit practice.

## Notable Talks, Records, And Evidence

The most important record is the Black Hat USA 2025 briefing entry, because it provides the core abstract and situates the work as a formal conference briefing titled **“No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol”** [record_id:7]. It states that OPC UA is widely used in industrial automation and IoT, that its native cryptographic authentication and transport security may lead organizations to avoid VPNs, and that Tervoort identified two protocol flaws enabling practical authentication bypass attacks [record_id:7]. It also names the main attack concepts: signing oracles, signature spoofing padding oracles, and transforming “RSA-ECB” into a “timing side channel amplifier” [record_id:7].

The DEF CON 33 record is also important because it appears to represent the same research as a recorded talk, with the same title and a video URL [record_id:2140]. Its abstract closely mirrors the Black Hat text, again emphasizing OPC UA’s industrial and IoT deployment, the risk of relying on built-in cryptographic security instead of VPNs, and the conversion of two protocol flaws into practical authentication bypass attacks across implementations and configurations [record_id:2140]. The DEF CON record’s duration tag of 36:19 indicates that downstream researchers may be able to obtain more technical detail from the video itself, though the record text provided here remains only an abstract-level summary [record_id:2140].

Taken together, the two records are mutually reinforcing rather than complementary. They do not describe separate projects, but they show that the same research was presented or distributed through at least two major security venues [record_id:7] [record_id:2140].

## Gaps, Limits, And Open Questions

The evidence base has several important limits.

First, the corpus contains only two records, and both appear to describe the same talk. This makes thematic synthesis straightforward but narrow. The records do not provide evidence of other Tom Tervoort talks, blog posts, papers, tools, disclosures, or projects beyond the OPC UA cryptographic attack research [record_id:7] [record_id:2140].

Second, the records are abstract-level descriptions. They do not name affected OPC UA implementations, vendors, versions, CVEs, disclosure timelines, mitigations, patches, or configuration-specific prerequisites [record_id:7] [record_id:2140]. The claim that attacks worked against “various implementations and configurations” is significant, but the records do not identify which ones.

Third, the exact nature of the two protocol flaws remains unclear from the provided evidence. The records mention signing oracles, signature spoofing padding oracles, and an RSA-related timing side-channel amplification technique, but they do not map those mechanisms to precise OPC UA message flows, handshake steps, security policies, or authentication modes [record_id:7] [record_id:2140].

Fourth, the operational impact is framed broadly. The records state that hijacking an OPC UA server could allow an attacker to affect industrial systems controlled by it, but they do not provide case studies, simulated plant scenarios, safety analysis, or real-world exposure measurements [record_id:7] [record_id:2140].

Open research questions for downstream agents include:

- Which OPC UA security policies, profiles, or versions are affected?
- Were the two flaws assigned CVEs or addressed by the OPC Foundation or vendors?
- Which implementations and configurations were tested?
- What attacker position is required: internet exposure, network adjacency, man-in-the-middle, access to a client, access to a server, or oracle access?
- What mitigations are recommended beyond VPN use?
- Does disabling particular cryptographic options or moving to newer profiles eliminate the issues?
- Are these attacks feasible in high-latency OT/cloud environments, especially the timing side-channel component?
- How do these findings affect architectural guidance for IT/OT segmentation and remote industrial connectivity?

## Coverage And Evidence Notes

This report covers all provided records attributed to Tom Tervoort.

The Black Hat USA 2025 record is a briefing entry for **“No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol.”** It provides the clearest statement of the research motivation, threat model, and claimed technical results: OPC UA is widely used in industrial automation and IoT; it is often trusted because of built-in cryptographic security; and Tervoort identified two protocol flaws leading to practical authentication bypass attacks involving signing oracles, padding oracles, and RSA-related timing side-channel amplification [record_id:7].

The DEF CON 33 record is a second entry for the same titled work and appears to correspond to a recorded talk. It repeats the same central claims and adds evidence that the research was also presented or made available through DEF CON, with a listed video URL and duration metadata [record_id:2140].