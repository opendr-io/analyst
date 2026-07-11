# Topic: Author: Marko Mitic

## Executive Summary

The available records attributed to Marko Mitic consist of two 2025 conference entries for the same or near-identical talk, co-authored/co-presented with Adam Zabrocki, titled “How to Secure Unique Ecosystem Shipping 1 Billion+ Cores?” The talk appears in both Black Hat USA 2025 and DEF CON 33 materials [record_id:67] [record_id:1944]. Across both records, the core subject is NVIDIA’s transition from its internal Falcon microprocessor to a RISC-V-based architecture used broadly across GPU products, and the security engineering required to protect a proprietary embedded ecosystem deployed at “billion-core” scale [record_id:67] [record_id:1944].

The records collectively frame Mitic’s contribution around platform, hardware, embedded, and large-scale ecosystem security. The talk emphasizes that traditional security models for widely replicated, publicly shared ecosystems do not fully address the challenges of a proprietary architecture deployed across enormous volume. The stated response is a custom software and hardware security architecture, including a purpose-built separation kernel, RISC-V ISA extensions such as Pointer Masking and IOPMP, secure boot and attestation mechanisms, and forward-looking exploration of hardware-assisted memory safety, control-flow integrity, and CHERI-like models [record_id:67] [record_id:1944].

Because the corpus contains only two records, and both appear to describe the same talk, the evidence is strong for this one subject area but thin for broader claims about Marko Mitic’s overall body of work. The records support a focused research profile: Mitic is associated here with securing NVIDIA’s internal RISC-V ecosystem at massive deployment scale, especially where proprietary hardware/software architecture requires custom security design.

## Research Landscape

The research landscape represented by these records is narrow but technically significant. Both records are conference talk listings from major security venues in 2025: Black Hat USA and DEF CON 33 [record_id:67] [record_id:1944]. They are not full papers, transcripts, slides, code repositories, or post-publication analyses. Instead, they are abstract-style descriptions of a talk. As a result, they provide high-level claims about architecture, methods, and lessons learned, but they do not include implementation details, threat models, measurements, vulnerabilities, evaluation methodology, or concrete attack/defense case studies.

The records place the work in the domain of hardware, embedded systems, platform security, and OT/IoT-adjacent security. The Black Hat listing explicitly tags the talk as “Hardware / Embedded” and “Platform Security” [record_id:67]. Both records describe a proprietary microcontroller-like architecture embedded throughout NVIDIA GPU products: NVIDIA’s internal Falcon microprocessor, transitioned beginning in 2016 to a RISC-V-based architecture [record_id:67] [record_id:1944]. The records state that by 2024 NVIDIA had shipped more than one billion RISC-V cores, with each chipset containing approximately 10 to 40 cores [record_id:67] [record_id:1944].

The dominant source type is therefore high-level conference presentation metadata and abstract text. There are no independent corroborating technical records in this topic set. The two records are nearly identical in wording, suggesting they describe the same presentation delivered or listed at two separate venues rather than two distinct research projects. This makes the corpus internally consistent but not diverse.

Overall, the represented research area is the security of large-scale proprietary embedded compute ecosystems. The problem is not merely “how to secure RISC-V” in general, but how to secure a custom RISC-V-derived or RISC-V-based environment embedded inside commercial GPU chipsets at unprecedented scale [record_id:67] [record_id:1944]. The talk positions this as a case where off-the-shelf or community-derived security models are insufficient because the system is both proprietary and deployed at massive volume.

## Major Themes And Trends

### Securing proprietary ecosystems at public-infrastructure scale

The central theme across both records is the challenge of securing something proprietary that has nevertheless reached huge deployment scale. The talk contrasts historical security research on “well-known, widely replicated ecosystems” with the problem of securing an architecture “no one else has” [record_id:67] [record_id:1944]. This framing is important: the ecosystem is not obscure in deployment impact, but it is specialized in design and likely lacks the same external research attention, shared tooling, and mature defensive models available to common platforms.

The records suggest a tension between uniqueness and scale. Unique proprietary systems may benefit from internal control and tailored architecture, but they also lack the broad peer review, standardized hardening practices, and collective security learning that mature public ecosystems receive. At the same time, the scale described—more than one billion RISC-V cores shipped—means security weaknesses could have large systemic consequences [record_id:67] [record_id:1944].

### RISC-V as an internal platform-security foundation

Both records describe NVIDIA’s 2016 transition from its internal Falcon microprocessor to a RISC-V-based architecture [record_id:67] [record_id:1944]. This is presented not as a generic RISC-V adoption story, but as a security-relevant architectural migration. The resulting ecosystem is embedded in “nearly all GPU products,” with each chipset containing 10 to 40 RISC-V cores [record_id:67] [record_id:1944].

The records imply that RISC-V’s extensibility may be central to the security design. The talk mentions “novel RISC-V ISA extensions” such as Pointer Masking and IOPMP, with IOPMP later ratified [record_id:67] [record_id:1944]. The inclusion of ISA-level extensions suggests that Mitic and Zabrocki’s work concerns not only software hardening but hardware/software co-design for platform security.

### Custom security architecture rather than borrowed security models

A recurring claim is that “existing models couldn’t solve” the security challenges associated with this proprietary, billion-core ecosystem [record_id:67] [record_id:1944]. In response, the presenters say they developed or created a custom software and hardware security architecture “from scratch” [record_id:67] [record_id:1944].

The records identify several components of this architecture:

- A purpose-built separation kernel [record_id:67] [record_id:1944].
- RISC-V ISA extensions such as Pointer Masking and IOPMP [record_id:67] [record_id:1944].
- Secure boot mechanisms [record_id:67] [record_id:1944].
- Attestation mechanisms or solutions [record_id:67] [record_id:1944].
- Forward-looking exploration of hardware-assisted memory safety, control-flow integrity, and CHERI-like approaches [record_id:67] [record_id:1944].

The trend here is toward deeply integrated platform security, where isolation, boot integrity, attestation, memory safety, and control-flow protection are treated as parts of a combined ecosystem strategy rather than isolated defenses.

### Future-proofing against evolving threats

Both abstracts explicitly ask how to “future-proof” a proprietary ecosystem against future threats [record_id:67] [record_id:1944]. The forward-looking techniques named are hardware-assisted memory safety, including HWASAN and MTE; control-flow integrity; and CHERI-like models [record_id:67] [record_id:1944]. This indicates that the presentation is not only retrospective about NVIDIA’s RISC-V transition and existing security architecture, but also prospective about next-generation mitigations.

The future-proofing theme reflects a broader security trend: embedded and platform-security systems increasingly need mitigations against memory corruption, control-flow hijacking, and capability or compartmentalization failures. The records do not specify which of these mechanisms are deployed, experimental, planned, or merely under evaluation. However, the fact that they are listed together suggests a roadmap or research direction focused on architectural resilience.

### Security at unprecedented deployment scale

The repeated phrase “1 billion+ cores” is not incidental; it is the core framing of both records [record_id:67] [record_id:1944]. The records present scale as a primary security challenge. The talk does not merely address how to secure one embedded core or one GPU subsystem, but how to design security for an ecosystem where each chipset has many cores and total deployment has passed one billion units [record_id:67] [record_id:1944].

Scale changes the security problem in several ways, though the records only imply rather than fully detail them. A billion-core ecosystem requires robust lifecycle security, update and boot integrity, consistent enforcement across product lines, scalable attestation, and long-term compatibility. The talk’s emphasis on custom architecture, secure boot, attestation, and ISA-level support fits this scale-driven challenge.

## Methods, Tools, And Approaches Discussed

The records describe several technical approaches, though only at abstract level.

One major approach is the design of a custom software and hardware security architecture for NVIDIA’s RISC-V-based internal ecosystem [record_id:67] [record_id:1944]. This architecture is described as purpose-built rather than adopted wholesale from existing security models. The records do not define its complete structure, but they indicate that it spans low-level hardware features, privileged software, boot flows, and attestation.

A second approach is the use of a purpose-built separation kernel [record_id:67] [record_id:1944]. A separation kernel generally provides strong partitioning between components or security domains, but the records do not explain its design, assurance level, scheduling model, memory-isolation mechanism, or relationship to firmware running on the embedded RISC-V cores. Still, its inclusion suggests a strategy of compartmentalization and controlled interaction among software components within the proprietary ecosystem.

A third approach is ISA-level security extension. Both records mention Pointer Masking and IOPMP as novel RISC-V ISA extensions, with IOPMP later ratified [record_id:67] [record_id:1944]. Pointer Masking likely relates to constraining or transforming pointer values for security or address handling, while IOPMP likely refers to I/O Physical Memory Protection. The records do not provide definitions, design rationale, or implementation details, but they clearly present these extensions as part of the custom security architecture.

A fourth approach is secure boot and attestation [record_id:67] [record_id:1944]. Secure boot is presented as a unique mechanism or solution, and attestation is paired with it. This suggests the architecture includes mechanisms to establish trust in the code running on these RISC-V cores and to report or verify that trust state. However, the records do not specify root-of-trust design, key hierarchy, measurement strategy, attestation protocol, lifecycle handling, revocation, provisioning, or verifier model.

A fifth approach is forward-looking memory-safety and control-flow hardening. Both records mention hardware-assisted memory safety, specifically HWASAN and MTE, as well as CFI and CHERI-like models [record_id:67] [record_id:1944]. These are presented as part of how NVIDIA is preparing its RISC-V ecosystem for an evolving threat landscape. The records do not clarify whether HWASAN, MTE, CFI, or CHERI-like mechanisms are already implemented, under active research, prototyped, or discussed as future possibilities. The phrasing “what’s next” and “preparing” suggests that at least some of these mechanisms are roadmap-oriented rather than completed deployments [record_id:67] [record_id:1944].

Together, these methods indicate a layered architecture: separation at the software level, architectural enforcement at the ISA/hardware level, integrity at boot, verifiability through attestation, and future exploit mitigation through memory-safety and control-flow protections.

## Notable Talks, Records, And Evidence

The most important record is the Black Hat USA 2025 briefing listing, “How to Secure Unique Ecosystem Shipping 1 Billion+ Cores?”, attributed to Adam Zabrocki and Marko Mitic [record_id:67]. This record provides a polished abstract and tags the presentation under hardware/embedded and platform security. It states that NVIDIA began transitioning its Falcon microprocessor to a RISC-V-based architecture in 2016, that each chipset now includes 10 to 40 RISC-V cores, and that NVIDIA surpassed one billion RISC-V cores shipped in 2024 [record_id:67]. It also identifies the main security contributions: a custom software/hardware security architecture, a purpose-built separation kernel, Pointer Masking, IOPMP, secure boot, attestation, and future-looking work on HWASAN, MTE, CFI, and CHERI-like models [record_id:67].

The DEF CON 33 record appears to describe the same talk, with nearly identical wording and the same title, authors, and technical claims [record_id:1944]. It is associated with a YouTube URL and a duration tag of 37:05, suggesting it may correspond to a recorded talk rather than only a listing [record_id:1944]. The DEF CON record reinforces the same claims about NVIDIA’s RISC-V transition, billion-core scale, custom software/hardware security architecture, separation kernel, Pointer Masking, IOPMP, secure boot, attestation, hardware-assisted memory safety, CFI, and CHERI-like models [record_id:1944].

The two records matter because they place Marko Mitic in a concrete, high-impact platform-security context: securing NVIDIA’s proprietary RISC-V ecosystem at enormous deployment scale. However, because they are duplicative, they should be treated as mutually reinforcing evidence for one talk rather than independent evidence for multiple research efforts.

The evidence strength is high for the existence and broad topic of the talk, since both records agree closely [record_id:67] [record_id:1944]. The evidence strength is moderate for the listed architectural components, because both abstracts name them, but no technical details are provided [record_id:67] [record_id:1944]. The evidence strength is low for implementation specifics, effectiveness, security guarantees, and deployment status of future mechanisms such as CHERI-like models, because those details are not included in the raw records.

## Gaps, Limits, And