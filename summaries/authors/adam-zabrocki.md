# Topic: Author: Adam Zabrocki

## Executive Summary

The two records attributed to Adam Zabrocki describe essentially the same 2025 presentation, co-authored/co-presented with Marko Mitic, on securing NVIDIA’s proprietary RISC-V-based internal controller ecosystem at massive scale. The talk appears in both Black Hat USA 2025 and DEF CON 33 contexts under the same title, “How to Secure Unique Ecosystem Shipping 1 Billion+ Cores?” [record_id:67] [record_id:1944].

Collectively, the records frame the work as a large-scale platform and embedded-systems security case study: NVIDIA transitioned its internal Falcon microprocessor, used across nearly all GPU products, to a RISC-V-based architecture beginning in 2016; by 2024, the company had shipped more than 1 billion RISC-V cores, with each chipset containing roughly 10 to 40 such cores [record_id:67] [record_id:1944]. The central problem is how to secure an architecture that is proprietary, unusual, and deployed at unprecedented scale—an ecosystem where ordinary industry-wide security models and shared patterns may not directly apply [record_id:67] [record_id:1944].

The records emphasize several recurring technical contributions: a custom software and hardware security architecture, a purpose-built separation kernel, RISC-V ISA extensions such as Pointer Masking and IOPMP, secure boot and attestation mechanisms, and forward-looking defenses such as hardware-assisted memory safety, control-flow integrity, and CHERI-like models [record_id:67] [record_id:1944]. The evidence base is narrow but strong for identifying the talk’s subject matter and themes, because both records independently describe the same presentation in very similar language. It is thin, however, on implementation detail, empirical results, threat models, vulnerabilities, or specific design tradeoffs.

## Research Landscape

The record set is small: two conference records, both from 2025, both describing the same or nearly identical talk by Adam Zabrocki and Marko Mitic [record_id:67] [record_id:1944]. One source is a Black Hat USA 2025 briefing entry [record_id:67]; the other is a DEF CON 33 YouTube-linked record with a listed runtime of 37:05 [record_id:1944]. Both records are classified under hardware/embedded or OT/IoT-adjacent security, but the raw text itself is most specifically about GPU-internal controller security, proprietary RISC-V deployment, platform security, secure boot, attestation, separation kernels, memory safety, and future hardware/software defenses.

The included records do not show a broad bibliography of Adam Zabrocki’s work. Instead, they capture one concentrated research area: the security architecture behind NVIDIA’s migration from its internal Falcon microprocessor to a RISC-V-based architecture across GPU products [record_id:67] [record_id:1944]. The scale is the defining landscape feature. The records state that each chipset includes or has 10–40 RISC-V cores, and that NVIDIA surpassed 1 billion RISC-V cores shipped in 2024 [record_id:67] [record_id:1944]. This makes the research area less about isolated embedded-device hardening and more about building repeatable security foundations for a proprietary, high-volume silicon ecosystem.

The talks are positioned as lessons learned from building something “no one else has” and securing it at “billion-core scale” [record_id:67]. They contrast this with security research that historically targets “well-known, widely replicated ecosystems,” where problems and solutions are shared across the industry [record_id:67] [record_id:1944]. That framing suggests the talk is likely a practitioner-oriented architecture presentation rather than a single exploit, vulnerability disclosure, or academic measurement study.

## Major Themes And Trends

### Securing proprietary architectures at massive scale

The dominant theme is the difficulty of securing a unique proprietary ecosystem that lacks the benefit of common external security models. Both records open by contrasting conventional security research—focused on widely replicated ecosystems—with the question of securing an architecture “that’s both proprietary and deployed at billion-core scale” [record_id:67] [record_id:1944]. This establishes the talk’s central contribution: adapting or inventing security architecture for a platform whose scale resembles mainstream computing infrastructure, but whose internals are specialized.

The records repeatedly emphasize that existing security models “couldn’t solve” the challenges created by NVIDIA’s RISC-V transition and deployment scale [record_id:67] [record_id:1944]. That phrase is important because it frames the work not merely as applying standard secure boot or isolation practices, but as requiring custom co-design across hardware and software.

### Migration from Falcon to RISC-V as a security inflection point

Both records describe a historical transition beginning in 2016, when NVIDIA started moving its internal Falcon microprocessor—used as a logic controller in nearly all GPU products—to a RISC-V-based architecture [record_id:67] [record_id:1944]. This migration appears to be the enabling context for the security work. The move to RISC-V created both opportunity and risk: opportunity because RISC-V could be extended and architected for new security goals, and risk because NVIDIA had to secure a large internal controller ecosystem embedded across products.

The records imply that the internal controller environment is pervasive inside NVIDIA GPU products. In the Black Hat description, Falcon is described as “used as a logic controller in nearly all GPU products” [record_id:67]. The DEF CON record similarly says it is “used in nearly all GPU products” [record_id:1944]. This pervasiveness makes the security architecture significant: weaknesses or design limitations could have broad platform implications, while strong primitives could improve security across many product lines.

### Custom hardware/software co-design

A second major theme is that security was approached as a custom software and hardware architecture rather than as a single protection layer. Both records state that NVIDIA developed or created a “custom SW and HW security architecture from scratch” to address the unique challenges [record_id:67] [record_id:1944]. The described components span kernel design, instruction-set extensions, boot integrity, attestation, memory safety, and control-flow protection.

This co-design theme is especially clear in the list of technologies: a purpose-built separation kernel, RISC-V ISA extensions such as Pointer Masking and IOPMP, secure boot and attestation, hardware-assisted memory safety, control-flow integrity, and CHERI-like models [record_id:67] [record_id:1944]. The talks appear to argue that securing a proprietary billion-core embedded ecosystem requires coordinating mechanisms at multiple layers instead of relying on one conventional control.

### Isolation and compartmentalization

The purpose-built separation kernel is a recurring technical centerpiece. Both records mention a “Separation Kernel” or “Separation Kernel SW” as part of the custom architecture [record_id:67] [record_id:1944]. Although neither record explains its implementation, the inclusion suggests that isolation between components, tasks, firmware domains, or privilege levels is a major concern in the NVIDIA RISC-V controller ecosystem.

The separation-kernel theme fits the overall problem: many embedded controller cores across a chipset likely perform different functions, and a compromise in one component should not necessarily compromise the whole device or trust chain. The evidence does not specify these domains, but the repeated mention of separation-kernel software indicates that formalized compartmentalization is one of the architectural pillars [record_id:67] [record_id:1944].

### RISC-V extensibility as a security mechanism

The records highlight “novel RISC-V ISA extensions” including Pointer Masking and IOPMP, with IOPMP described as “later ratified” [record_id:67] [record_id:1944]. This is a notable theme because it shows RISC-V not only as a processor choice but as a customizable security substrate. The talks appear to treat instruction-set architecture features and platform protection mechanisms as part of the secure design.

Pointer Masking suggests attention to pointer manipulation or memory-address hardening, while IOPMP points toward I/O physical memory protection. The records do not define either mechanism in detail, so downstream researchers should avoid over-reading the exact behavior from this dataset alone. Still, the records are strong evidence that Zabrocki and Mitic’s presentation identifies ISA-level security extensions as core to NVIDIA’s approach [record_id:67] [record_id:1944].

### Secure boot, attestation, and platform trust

Both records list “unique secure boot and attestation mechanisms” or a “unique secure boot and attestation solution” as part of the custom architecture [record_id:67] [record_id:1944]. This suggests that the talk treats platform trust establishment as a first-class challenge. In a billion-core proprietary controller ecosystem, it is not enough for code to be isolated at runtime; the system also needs reliable startup integrity and a way to prove or measure trust state.

The records do not describe the chain of trust, key management, measurement model, attestation verifier, or update lifecycle. However, their inclusion alongside separation kernels and ISA extensions implies an architecture in which boot integrity, runtime isolation, and hardware-backed enforcement are integrated [record_id:67] [record_id:1944].

### Future-proofing against evolving threats

Both records explicitly ask how to “future-proof a proprietary ecosystem against tomorrow’s threats” [record_id:67] [record_id:1944]. The forward-looking portion of the talk includes hardware-assisted memory safety—listed as HWASAN and MTE—control-flow integrity, and CHERI-like models [record_id:67] [record_id:1944]. This positions the work not just as a retrospective on NVIDIA’s migration to RISC-V, but as a roadmap for continued hardening.

The choice of future-looking defenses is significant. Memory safety, CFI, and CHERI-like capabilities are all associated with reducing exploitability and constraining corrupted execution. The records therefore suggest that the authors view future threats through the lens of memory corruption, control-flow subversion, and stronger architectural enforcement, though the records do not provide concrete threat scenarios or evaluation results [record_id:67] [record_id:1944].

## Methods, Tools, And Approaches Discussed

The records describe an architecture-led approach rather than a tool release or single exploit technique. The main method is building a custom software and hardware security architecture for NVIDIA’s RISC-V-based internal controller ecosystem [record_id:67] [record_id:1944]. This architecture is said to have been developed “from scratch,” implying that the constraints of the proprietary ecosystem required bespoke design rather than adoption of an off-the-shelf security stack [record_id:67] [record_id:1944].

A purpose-built separation kernel is one of the clearest software approaches discussed [record_id:67] [record_id:1944]. The records do not state whether this kernel is formally verified, microkernel-like, hypervisor-like, or tailored to a specific privilege model. Still, its repeated mention indicates an approach centered on isolating components and mediating access within the embedded controller environment.

At the hardware and ISA layer, the talks discuss RISC-V extensions, specifically Pointer Masking and IOPMP [record_id:67] [record_id:1944]. IOPMP is described as later ratified, which may indicate that at least one mechanism moved beyond an internal design into a standardized or ratified form [record_id:67] [record_id:1944]. These records suggest a workflow in which proprietary security requirements can influence architectural extensions that become more broadly formalized.

The architecture also includes secure boot and attestation [record_id:67] [record_id:1944]. These are not described as generic features but as “unique” mechanisms or a “unique” solution, suggesting adaptation to NVIDIA’s specific internal controller ecosystem and deployment model [record_id:67] [record_id:1944]. The likely purpose is to establish trust in firmware/software running on these RISC-V controllers and to support verification of device or subsystem state, though the records do not provide enough detail to determine the exact attestation design.

For future hardening, the records list hardware-assisted memory safety approaches including HWASAN and MTE, control-flow integrity, and CHERI-like models [record_id:67] [record_id:1944]. These are presented as examples of how NVIDIA is preparing its RISC-V ecosystem for an evolving threat landscape. The methods imply layered exploit mitigation: detecting or preventing memory misuse, constraining indirect control transfers, and exploring capability-like memory/object models.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 record is one of the two core pieces of evidence. It presents “How to Secure Unique Ecosystem Shipping 1 Billion+ Cores?” as a briefing by Adam Zabrocki and Marko Mitic [record_id:67]. Its description is relatively rich for a conference abstract and provides the clearest framing of the talk as a platform-security problem: securing a proprietary architecture deployed at billion-core scale, after NVIDIA’s transition from Falcon to RISC-V beginning in 2016 [record_id:67]. It also lists the major architectural components: separation kernel software, Pointer Masking, IOPMP, secure boot, attestation, HWASAN, MTE, CFI, and CHERI-like models [record_id:67].

The DEF CON 33 record appears to be the same presentation or a closely matched version, also titled “How to secure unique ecosystem shipping 1 billion+ cores?” and attributed to Adam Zabrocki and Marko Mitic [record_id:1944]. It includes a YouTube source and a runtime tag of 37:05, suggesting that the record may point to a recorded talk rather than only an abstract [record_id:1944]. Its text closely mirrors the Black Hat abstract, reinforcing confidence in the core facts: Falcon-to-RISC-V transition, 10–40 cores per chipset, more than 1 billion RISC-V cores shipped by 2024, and the custom security architecture spanning software and hardware [record_id:1944].

Together, the two records are representative of a single contribution: Zabrocki’s work, with Mitic, on how a major hardware vendor secures a proprietary RISC-V