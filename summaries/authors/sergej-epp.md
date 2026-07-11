# Topic: Author: Sergej Epp

## Executive Summary

The two records attributed to Sergej Epp come from UNPROMPTED2026 and together portray him in two related but distinct roles: as a contributor to practical AI-enabled conference tooling, and as a security leader analyzing AI-assisted attacks observed in the wild. The stronger and more substantive record is Sergej Epp’s solo talk, **“8 Minutes to Admin. We Caught It in the Wild,”** which describes two AI-assisted attack campaigns: a rapid AWS privilege-escalation operation from stolen credentials to full administrator access, and **EtherRAT**, described as a fileless Node.js implant using Ethereum smart contracts for command-and-control infrastructure [record_id:2355]. The talk’s central claim is not that attackers used novel primitives, but that AI assistance compressed familiar techniques into speeds and scales that challenge traditional detection models [record_id:2355].

The second record, **“Vibe Coded,”** lists Sergej Epp as one of several authors or speakers and is much thinner. It describes a set of micro talks by people who “vibecoded” tools at the conference to improve the event itself [record_id:2352]. This record links Epp to the broader theme of AI-assisted software development and community-oriented security conference operations, but it provides little detail about his specific contribution.

Collectively, the records suggest Sergej Epp’s presence at UNPROMPTED2026 sits at the intersection of AI-enabled making and AI-enabled threat activity: on one side, rapid tool creation for conference improvement; on the other, rapid offensive operations that accelerate cloud compromise and malware-enabled persistence. The evidence base is small, but the available records point to recurring concerns around speed, automation, practical field evidence, and the security implications of “vibe” workflows.

## Research Landscape

The corpus contains only two records, both from **UNPROMPTED2026**, a conference context apparently centered on AI, security, and applied experimentation. One record is a collaborative or multi-speaker micro-talk session, while the other is a solo security talk by Sergej Epp.

The more detailed source is the solo presentation **“8 Minutes to Admin. We Caught It in the Wild.”** Its abstract provides a compact but information-rich summary of a field-based security investigation. It identifies Epp as **CISO, Sysdig**, and frames the talk around real-world evidence from two AI-assisted attack campaigns [record_id:2355]. The topics include AI security, prompt injection and jailbreaking by classification, but the raw text itself focuses more specifically on AI-assisted attack operations, AWS escalation, fileless malware, Node.js implants, Ethereum smart-contract-based command and control, behavioral attribution of AI assistance, and forensic opportunities created by blockchain-based infrastructure [record_id:2355].

The second record, **“Vibe Coded,”** is a lighter conference-community artifact. Its raw text states that “folks vibecoded to make the conference better, and created tools at the conference,” inviting viewers to watch micro talks about what they built [record_id:2352]. This record places Epp alongside Rob T. Lee, Glenn Thrope, and Dan Hubbard as an author or speaker. Unlike the solo talk, it does not specify what Epp personally built, what tools were created, or what methods were used. Its value is therefore contextual: it shows Epp participating in a conference culture of rapid AI-assisted development, but it is not strong evidence for specific technical claims.

Overall, the research landscape is narrow but coherent. Both records are tied to the same event and both revolve around AI’s role in accelerating technical activity. In one case, that acceleration is constructive and community-focused; in the other, it is adversarial and operationally dangerous.

## Major Themes And Trends

### AI as an accelerator rather than a source of entirely new primitives

The most important theme is that AI changes operational tempo more than it necessarily changes the underlying technical primitives. In the solo talk, the abstract explicitly says that neither of the two observed campaigns introduced “novel attack primitives” [record_id:2355]. Instead, their significance lies in compressing “known techniques to speeds and scales that break traditional detection models” [record_id:2355]. This framing is important for downstream researchers: the talk appears to argue against hype-driven claims that AI creates wholly new categories of attack, while still emphasizing that AI-assisted execution can overwhelm defenses tuned to slower human-paced activity.

This same acceleration theme is faintly echoed in the “Vibe Coded” record, where participants created tools at the conference to make the event better [record_id:2352]. Although the record does not explicitly mention AI coding assistants, the phrase “vibecoded” and the classification around AI-assisted software development suggest rapid software construction as the central activity. Taken together, the records present AI-enabled speed as a cross-cutting phenomenon: useful for building conference tools quickly, but dangerous when applied to cloud intrusion and malware operations.

### Real-world AI-assisted attacks and the problem of attribution

Epp’s solo talk claims to examine “two AI-assisted attack campaigns” caught in the wild [record_id:2355]. It also says the presentation introduces “a behavioral methodology for attributing AI-assistance when proof is impossible” [record_id:2355]. This is a notable contribution because attribution of AI use in attacks is inherently difficult: defenders may observe artifacts, timing, command sequences, or operational patterns, but usually cannot directly prove that an attacker used an AI system.

The wording suggests a pragmatic approach. Rather than requiring impossible certainty, Epp’s talk appears to focus on behavioral evidence and forensic patterns. This positions AI attribution as a probabilistic or inferential discipline, grounded in observed behavior rather than direct knowledge of attacker tooling [record_id:2355]. The abstract does not provide the methodology’s details, so the evidence here is limited to the claim that such a methodology is presented.

### Cloud compromise at machine speed

The title **“8 Minutes to Admin”** and the abstract’s description of “an 8-minute AWS escalation from stolen creds to full admin” make cloud attack acceleration a central issue [record_id:2355]. The scenario begins with stolen credentials and ends with full administrative access in AWS within eight minutes. The record does not specify which AWS services, IAM misconfigurations, privilege-escalation paths, or persistence mechanisms were involved, but it strongly emphasizes speed and escalation.

This supports a broader trend in cloud security: identity and access management exposures can be exploited rapidly, and traditional detection models may be too slow if they depend on delayed log review, manual triage, or alert chains that cannot react inside an eight-minute window. The talk’s significance is therefore not only about AI, but also about cloud detection and response under compressed timelines [record_id:2355].

### Malware, blockchain command and control, and defender-side forensics

The second campaign in Epp’s solo talk is **EtherRAT**, described as “a fileless Node.js implant using Ethereum smart contracts for C2” [record_id:2355]. This combines several defensive concerns: fileless execution, JavaScript/Node.js-based implants, and decentralized or resilient command-and-control channels. The abstract frames blockchain C2 as “the attacker’s resilience play,” but also as “the defender’s greatest forensic gift” [record_id:2355].

That final claim is one of the most distinctive ideas in the corpus. It suggests that while attackers may use blockchain infrastructure for durability, censorship resistance, or availability, the transparency and persistence of blockchain records can create unusually rich forensic evidence for defenders. The record does not detail exactly how defenders should exploit that evidence, but the claim points to a potentially important inversion: infrastructure chosen for attacker resilience may also preserve attacker behavior in ways conventional C2 infrastructure does not [record_id:2355].

### “Vibe” as both builder culture and attacker framing

Both records use “vibe” language. The collaborative record is titled **“Vibe Coded”** and describes participants who “vibecoded” tools at the conference [record_id:2352]. Epp’s solo talk includes the phrase “Welcome to VibeHacking” [record_id:2355]. This shared vocabulary suggests that UNPROMPTED2026 was engaging with the emerging cultural language around AI-assisted work: “vibe coding” for software creation and “vibe hacking” for AI-accelerated offensive activity.

The records do not define these terms, and researchers should be cautious not to overinterpret them. Still, the pairing is thematically significant. It implies that the same broad mode of AI-assisted rapid execution may apply to both benign tool building and malicious operations. Epp’s records therefore sit within a broader conversation about what happens when security work, software development, and attack operations become more fluid, automated, and improvisational.

## Methods, Tools, And Approaches Discussed

The corpus mentions several methods and technical approaches, most of them from Epp’s solo talk.

The first major approach is **forensic investigation from primary evidence**. The abstract says the talk “dissects both operations from primary forensic evidence” [record_id:2355]. This establishes the talk as evidence-driven rather than purely speculative. However, the raw record does not provide the forensic artifacts themselves, so downstream researchers would need the video, slides, or related Sysdig reporting to evaluate the claim in detail.

The second is a **behavioral methodology for attributing AI assistance**. The record states that the talk introduces such a methodology “when proof is impossible” [record_id:2355]. This is potentially one of Epp’s unique contributions in the available corpus. It suggests a structured way to reason about AI involvement in attacks based on observed behavior, rather than relying on direct evidence of model use. The raw text does not enumerate the indicators, thresholds, or analytic framework, so this remains a promising but under-specified method in the record set.

The third is the analysis of **rapid AWS privilege escalation**. The campaign described in the talk moved from stolen credentials to full administrator access in eight minutes [record_id:2355]. This implies attention to cloud identity, credential theft, privilege escalation, and detection-response latency. The record does not describe the exact escalation method, so it supports the existence and framing of the case study but not detailed technical reconstruction.

The fourth is the analysis of **EtherRAT**, described as a **fileless Node.js implant** using **Ethereum smart contracts for command and control** [record_id:2355]. This combines malware analysis, runtime behavior, decentralized infrastructure, and blockchain forensic analysis. The talk’s stated argument is that blockchain C2 can increase resilience for attackers while simultaneously giving defenders durable evidence [record_id:2355].

The “Vibe Coded” session contributes a different kind of method: **rapid tool creation during a conference**. The raw text says the participants “vibecoded to make the conference better, and created tools at the conference” [record_id:2352]. No specific tools or workflows are identified, but the record indicates a hands-on approach to AI-assisted software development or rapid prototyping in a live event setting.

## Notable Talks, Records, And Evidence

The central record is **“8 Minutes to Admin. We Caught It in the Wild.”** It is notable because it is the only solo Sergej Epp record in the set and contains the densest technical claims. It identifies Epp as CISO of Sysdig and frames the talk around two real-world AI-assisted campaigns [record_id:2355]. The first campaign is an AWS escalation from stolen credentials to administrator access in eight minutes; the second is EtherRAT, a fileless Node.js implant using Ethereum smart contracts for command and control [record_id:2355]. The talk’s headline contribution is its argument that the attacks did not rely on novel primitives but instead used known techniques at speeds and scales that undermine traditional detection models [record_id:2355]. It also claims to offer a behavioral methodology for AI-assistance attribution and a defender-oriented view of blockchain C2 forensics [record_id:2355].

The other record, **“Vibe Coded,”** is notable mainly as a collaborative and contextual artifact. It lists Sergej Epp among several speakers or authors and describes micro talks by people who built tools at the conference to improve the conference experience [record_id:2352]. It is representative of the constructive side of the same AI acceleration theme: fast, on-site, likely AI-assisted creation of practical tools. Because the raw text does not specify Epp’s role or contribution, it should be treated as weak evidence for his individual technical work but stronger evidence for his participation in the UNPROMPTED2026 “vibe coded” programming context [record_id:2352].

## Gaps, Limits, And Open Questions

The evidence base is very small. With only two records, both from the same event and year, it is not possible to infer a long-term trajectory of Sergej Epp’s work, speaking themes, or research evolution. The records show what he was associated with at UNPROMPTED2026, but not whether these topics are recurring across other venues.

The most important technical gaps concern the solo talk’s details. The abstract says the AWS campaign escalated from stolen credentials to full admin in eight minutes, but it does not identify the specific AWS services, policies, misconfigurations, API calls, or attacker decisions involved [record_id:2355]. It also does not state what telemetry was available, how detection failed or succeeded, or what response actions were taken. Downstream researchers should seek the full talk, slides, or accompanying research to understand the escalation chain.

Similarly, the EtherRAT description is intriguing but incomplete. The record says it was a fileless Node.js implant using Ethereum smart contracts for C2 [record_id:2355]. It does not describe the implant’s execution path, infection vector, smart-contract interaction model, wallet or contract artifacts, obfuscation, persistence, or how commands were encoded. The claim that blockchain C2 is a forensic gift is important, but the record does not explain the precise forensic workflow.

Another open question is how Epp’s proposed behavioral methodology for AI-assistance attribution works. The record explicitly says proof is impossible and a behavioral method is introduced [record_id:2355], but it does not list behavioral indicators. Important unanswered questions include: