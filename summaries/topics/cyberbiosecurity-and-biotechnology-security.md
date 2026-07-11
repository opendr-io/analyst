# Topic: Cyberbiosecurity and biotechnology security

## Executive Summary

The three records collectively frame cyberbiosecurity as an emerging security area where biological engineering, AI-assisted molecular design, do-it-yourself biotechnology, regulatory evasion, embedded bio-devices, and cyberattack patterns converge. The evidence base is small but varied: one DEF CON 33 talk explicitly positions AI-designed proteins and “biological misbehavior” as analogous to cybersecurity threats [record_id:1875]; one BSidesLV 2025 Skytalks session describes circumventing regulatory, licensing, and biosafety barriers for genetically modified organism projects [record_id:2389]; and one BSidesLV 2025 talk explores ransomware targeting NFC bioimplants through an educational project called “LockSkin” [record_id:2482].

Across the records, the dominant theme is not traditional biosafety alone, but the security implications of increasingly programmable biology. The records suggest that biological systems are being discussed in hacker and security-conference spaces as systems that can be designed, modified, exploited, locked, bypassed, or defended. The strongest direct evidence for cyberbiosecurity as a conceptual field is the DEF CON talk description, which explicitly connects AI-designed proteins with cybersecurity threat models and argues for “diverse cyberbiosecurity defenders” [record_id:1875]. The most concrete cyberattack scenario is the ransomware-against-bioimplants talk, which ties bodily embedded NFC devices to hostage-taking attack logic [record_id:2482]. The most ethically and governance-relevant record is the BSidesLV talk proposing methods to bypass regulation, licenses, and biosafety certifications in biotech projects [record_id:2389].

The records are presentation abstracts rather than full papers, demonstrations, or empirical studies, so they provide evidence of topics being discussed and framed in the security community, not proof of technical feasibility, prevalence, or real-world incident frequency. Still, they highlight a research landscape where cyberbiosecurity includes AI-designed biological molecules, biohacking and molecular manipulation, governance bypass, and cyber-physical attacks against implanted biological-adjacent technologies.

## Research Landscape

The record set is composed entirely of 2025 hacker/security conference talks: one from DEF CON 33 and two from BSidesLV 2025. This matters because the records reflect how cyberbiosecurity is being presented to security practitioners, hacker communities, and adjacent technical audiences rather than how it is framed in academic biosafety, public health, or formal regulatory literature.

The DEF CON 33 record, “BiC Village - Petty Proteins When Molecules Go Rogue& Why Cyberbiosecurity,” is the clearest fit for the topic as a cyberbiosecurity overview or awareness talk. Its raw text says the talk will “explore how AI-designed proteins and biological misbehavior mirror cybersecurity threats” and asks why “diverse cyberbiosecurity defenders” are needed [record_id:1875]. This positions the field as a translation layer between cybersecurity thinking and biological systems: proteins and molecular behavior become analogues for malicious or unexpected software behavior, and defenders require cross-disciplinary knowledge.

The BSidesLV record “Advanced BioTerrorism Methods for the Discerning Practitioner (Token 13)” is more provocative and governance-centered. Its raw text describes genetically modified organism projects blocked by “regulation, licenses, or biosafety certifications,” then says the presenters will show “methods” used to “circumvent those roadblocks” [record_id:2389]. It also refers to “Nonconsentually Open-Source” biotech products and “manipulate organisms and ecosystems at the molecular level” [record_id:2389]. Although the abstract frames these activities as attempts to “cure a disease, create a vaccine, or save a species from extinction,” it is still directly relevant to biotechnology security because it foregrounds the bypassing of safety, licensing, and governance controls [record_id:2389].

The third record, “Locking Hands: Ransomware Meets Bioimplants,” is primarily categorized as OT and IoT security but secondarily belongs to cyberbiosecurity because it applies ransomware concepts to NFC bioimplants. The abstract asks what happens when bioimplants are “held hostage” and introduces “LockSkin, an educational ransomware targeting NFC bioimplants” [record_id:2482]. This expands the topic from biological engineering itself to implanted devices and human-body-adjacent cyber-physical systems.

Taken together, the research landscape is broad but shallow: these records cover conceptual cyberbiosecurity, biohacking governance evasion, and implant ransomware, but they do not provide detailed technical data, architectures, experimental outcomes, defensive controls, or regulatory analysis. They show an active conference-discussion space rather than a mature evidence base.

## Major Themes And Trends

### Biology as a programmable and attackable system

A recurring theme is the treatment of biological or body-integrated systems as programmable systems with security properties. The DEF CON talk explicitly links “AI-designed proteins” and “biological misbehavior” to cybersecurity threats [record_id:1875]. This suggests an emerging mental model in which molecular systems can exhibit failure modes, adversarial misuse, emergent behavior, or exploit-like dynamics comparable to software systems.

The bioimplant ransomware talk applies familiar cybercrime mechanics—ransomware and hostage-taking—to NFC implants under the skin [record_id:2482]. This is not molecular biology in the narrow sense, but it reflects the same broader trend: systems embedded in or closely tied to the body are being analyzed as cyberattack surfaces. Bioimplants “unlock new potential,” but the abstract asks what happens when they are “held hostage,” showing the move from beneficial augmentation to adversarial control [record_id:2482].

The biohacking talk similarly treats organisms and ecosystems as systems that can be engineered directly. It calls for reclaiming “the OG meaning of the word BioHacking” and “actually manipulate organisms and ecosystems at the molecular level” [record_id:2389]. In combination, the records indicate that security communities are discussing biology both as code-like design material and as a domain where unauthorized or uncontrolled modification has security implications.

### AI-designed biological systems as a cyberbiosecurity concern

Only one record directly mentions AI, but it is significant. The DEF CON record’s phrase “AI-designed proteins” identifies AI-assisted molecular engineering as part of the cyberbiosecurity threat landscape [record_id:1875]. The abstract does not specify whether the risk is malicious design, accidental biological misbehavior, dual-use protein generation, model misuse, or inadequate screening. However, by pairing AI-designed proteins with cybersecurity threats, the record signals a concern that biological design tools may create new classes of risks requiring security-style defenses.

This is a thin but important theme. There is no supporting detail about model architectures, protein design pipelines, sequence screening, synthesis providers, or lab validation. Still, the record indicates that AI-designed biological components are being used as a hook for cyberbiosecurity education and community-building [record_id:1875].

### Governance, regulation, and deliberate circumvention

The most governance-heavy record is the BSidesLV Skytalks abstract about genetically modified organisms. It says projects may face roadblocks from “regulation, licenses, or biosafety certifications” and promises to show “methods” used to “circumvent those roadblocks” [record_id:2389]. It also discusses “Nonconsentually Open-Source” existing biotech products [record_id:2389]. The language is explicit about bypassing formal controls, even while it presents the motivations as beneficial goals such as curing disease, creating vaccines, or saving species from extinction [record_id:2389].

This record highlights a major tension in cyberbiosecurity: innovation and access versus biosafety, biosecurity, intellectual property, and governance. In software security communities, bypassing controls can be framed as hacking, liberation, or research. In biotechnology, however, bypassing certifications and regulations can implicate environmental release, medical safety, pathogen risk, ecological risk, supply-chain trust, and public consent. The record therefore provides strong evidence that governance evasion is part of the conference conversation around biohacking and biotech security [record_id:2389].

There is no counterbalancing record in this set presenting formal governance frameworks, risk assessment methods, institutional biosafety practices, or policy proposals. As a result, the trend is visible but one-sided: the records show the existence of anti-gatekeeping or regulation-circumvention rhetoric, but not a detailed debate between access-oriented biohackers and regulators.

### Ransomware logic applied to bodily implants

The LockSkin record is a compact but concrete example of cybercrime patterns entering the bioimplant space. The abstract describes “educational ransomware targeting NFC bioimplants” and frames the scenario as “ransomware under the skin” [record_id:2482]. The key security idea is that an implant can become a hostageable asset, extending ransomware beyond files, servers, and industrial systems into personal embedded devices.

The record does not specify whether the NFC bioimplants are medical implants, access-control implants, identity/payment implants, or hobbyist augmentation devices. It also does not describe the technical method, such as NFC tag locking, access key changes, malicious payloads, or denial of legitimate use. Nevertheless, it provides a representative example of the cyberbiosecurity boundary with IoT and human augmentation: when devices are implanted in bodies, cybersecurity failures may have personal, physical, psychological, and identity-related consequences [record_id:2482].

### Need for cross-disciplinary defenders

The DEF CON talk explicitly argues for “diverse cyberbiosecurity defenders” [record_id:1875]. This implies that conventional cybersecurity expertise alone is insufficient, and that defenders may need literacy in molecular biology, AI design tools, lab workflows, biosafety, bioethics, and systems security. The other records support this implication indirectly: the GMO circumvention talk sits at the intersection of biotech practice, regulation, and molecular manipulation [record_id:2389], while the implant ransomware talk combines cybercrime, NFC technology, implants, and human-body risk [record_id:2482].

A trend across the set is therefore convergence: cyberbiosecurity is not a single subdiscipline but a meeting point for software security, hardware/IoT security, synthetic biology, AI, laboratory practice, governance, and human augmentation.

## Methods, Tools, And Approaches Discussed

The records are abstracts and provide limited methodological detail, but several approaches are identifiable.

One approach is analogy-based threat modeling between biological systems and cybersecurity. The DEF CON record says the talk explores how “AI-designed proteins and biological misbehavior mirror cybersecurity threats” [record_id:1875]. This suggests using cybersecurity concepts—such as rogue behavior, adversarial design, misuse, failure modes, or defensive roles—to reason about biological molecules and engineered proteins. The record does not provide a formal framework, but the phrase “why Cyberbiosecurity” indicates an educational or field-building approach [record_id:1875].

A second approach is practical biohacking or molecular manipulation outside conventional gatekeeping structures. The BSidesLV Skytalks abstract discusses genetically modified organism projects and the presenters’ methods to “circumvent” regulation, licenses, or biosafety certifications [record_id:2389]. It mentions two long-running projects “in the pipeline for over seven years” and a possible third example involving how to “Nonconsentually Open-Source” existing biotech products [record_id:2389]. The abstract does not disclose the specific techniques, organisms, or products, but it clearly indicates a workflow or methodology oriented toward bypassing access barriers in biotechnology.

A third approach is educational offensive simulation against bioimplants. The LockSkin talk introduces “an educational ransomware targeting NFC bioimplants” [record_id:2482]. The educational framing suggests a demonstration or proof-of-concept intended to raise awareness about risks rather than necessarily to document active criminal use. The method appears to transpose ransomware concepts onto NFC implant technology, but the abstract does not specify implementation details [record_id:2482].

These approaches differ sharply in maturity and evidentiary depth. The DEF CON record appears conceptual and educational; the GMO record appears practice-oriented and intentionally provocative; the implant record appears demonstration-oriented, with a named educational ransomware project. None of the records provides reproducible technical details in the supplied text.

## Notable Talks, Records, And Evidence

The most representative record for the overall topic is Tia Pope’s DEF CON 33 talk, “BiC Village - Petty Proteins When Molecules Go Rogue& Why Cyberbiosecurity” [record_id:1875]. It directly names cyberbiosecurity and connects AI-designed proteins with cybersecurity threats. Its importance lies in framing: it suggests that biological systems, especially AI-designed proteins, can be discussed using cyber threat concepts, and that the field needs defenders with diverse backgrounds [record_id:1875]. For downstream research agents, this record is likely the best starting point for questions about how cyberbiosecurity is being introduced to hacker-conference audiences.

The most governance-relevant and potentially controversial record is Dr. Mixael S. Laufer’s BSidesLV talk, “Advanced BioTerrorism Methods for the Discerning Practitioner (Token 13)” [record_id:2389]. The abstract’s title itself is provocative, and the content discusses genetically modified organism projects impeded by regulation, licenses, or biosafety certifications, followed by an offer to show methods used to circumvent those roadblocks [record_id:2389]. It also mentions “Nonconsentually Open-Source” biotech products and manipulating organisms and ecosystems at the molecular level [record_id:2389]. This record matters because it surfaces a central cyberbiosecurity concern: motivated actors may intentionally bypass governance systems, even when claiming beneficial goals.

The most concrete cyberattack-style scenario is Mauro Eldritch’s BSidesLV talk, “Locking Hands: Ransomware Meets Bioimplants” [record_id:2482]. It introduces “LockSkin,” described as “educational ransomware targeting NFC bioimplants,” and invites the audience to consider “ransomware under the skin” [record_id:2482]. This record is valuable because it translates a well-understood security threat model into a bodily implanted technology context. It also connects cyberbiosecurity to IoT/OT-adjacent security and human augmentation.

## Gaps, Limits, And Open Questions

The largest limitation is that