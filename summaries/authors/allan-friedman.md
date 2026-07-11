# Topic: Author: Allan Friedman

## Executive Summary

The available corpus for **Author: Allan Friedman** consists of a single DEF CON 33 record: **“What’s Really in the Box? The Case for Hardware Provenance and HBOMs”** [record_id:2034]. The record presents an argument that while software supply chain security has advanced through transparency mechanisms such as SBOMs, hardware supply chains remain comparatively opaque and under-instrumented. Friedman’s contribution, as represented here, is to extend supply-chain transparency thinking from software into hardware by advocating for **hardware bills of materials**, or **HBOMs**, as a way to expose component origin, integrity, provenance, and risk context [record_id:2034].

The talk frames semiconductor and IoT hardware supply chains as security and national-security concerns, emphasizing risks from cloned components, opaque fabrication sources, and hidden inter-organizational dependencies [record_id:2034]. It criticizes blunt policy responses such as bans and onshoring as slow, costly, and often impractical, and instead argues for visibility, traceability, accountability, and risk-informed decision-making through the **HBOM Initiative** [record_id:2034].

Because there is only one record, the evidence base is narrow. The major identifiable theme is hardware supply chain transparency as an analogue and extension of software supply chain transparency. There is no basis in this corpus to characterize Friedman’s broader body of work, historical evolution, disagreements across talks, or recurring themes beyond this single presentation.

## Research Landscape

The research landscape represented by this topic is extremely concentrated: one talk-style record from DEF CON 33 in 2025, attributed to Allan Friedman, focused on hardware provenance and HBOMs [record_id:2034]. The record is positioned at the intersection of **software supply chain security**, **hardware supply chain security**, **IoT security**, **semiconductor trust**, and **national security policy**.

The talk’s starting point is the normalization of software supply-chain transparency through **SBOMs**, or software bills of materials. The record states that “as software supply chains embrace transparency through SBOMs, hardware remains a black box” [record_id:2034]. This contrast defines the overall research area: software has begun to develop structured transparency practices, while hardware—especially chips inside IoT devices—still lacks comparable visibility [record_id:2034].

The dominant source type is a conference talk abstract rather than a paper, tooling repository, policy document, or implementation guide. As a result, the record is strongest as evidence of agenda-setting: it describes a problem, motivates why it matters, introduces a proposed initiative, and invites the hacker and security community to help shape future practices [record_id:2034]. It is weaker as evidence for technical implementation details, adoption status, empirical measurements, or specific HBOM schemas.

The overall research area looks like an attempt to import the logic of SBOM-driven transparency into the hardware domain, while accounting for distinctive hardware challenges: component provenance, chip fabrication opacity, cloned or manipulated parts, and dependencies that cross organizational and geopolitical boundaries [record_id:2034].

## Major Themes And Trends

### Hardware as the Next Supply-Chain Transparency Frontier

The central theme is that hardware supply chains are becoming a critical transparency problem analogous to, but distinct from, software supply chains. The record explicitly contrasts the progress of SBOMs with the opacity of hardware, stating that “hardware remains a black box” even as software supply chains adopt transparency mechanisms [record_id:2034]. This frames hardware as the next frontier for supply-chain security practice.

The talk argues that hardware deserves equal or greater attention because “the chips inside our IoT devices carry just as much — if not more — risk” than software supply-chain components [record_id:2034]. This is an important reframing: IoT device security is not only about firmware, application code, or network exposure, but also about the origin and integrity of the chips and components inside the device.

### From Traditional BOMs to Risk-Aware HBOMs

A second major theme is the insufficiency of traditional bills of materials. The record says traditional BOMs focus on “procurement and production — what gets bought and assembled,” but “rarely capture origin, integrity, or risk context” [record_id:2034]. This distinction is crucial. A conventional BOM may support manufacturing, purchasing, and inventory management, but it does not necessarily answer security questions such as:

- Where did a chip originate?
- Which fabrication facility produced it?
- Can the component be trusted?
- Was it cloned or substituted?
- What hidden dependencies exist across suppliers?
- What geopolitical or operational risks are associated with the component?

The proposed HBOM concept is therefore not merely a hardware inventory list. It is framed as a security and risk-management artifact intended to expose “hidden risks,” trace “chip provenance,” and support “risk-informed decisions” [record_id:2034].

### Semiconductor Supply Chains as National Security Flashpoints

The record situates semiconductor supply chains within national security concerns. It describes the semiconductor supply chain as “fast becoming a national security flashpoint” and identifies risks such as cloned components and opaque fabrication sources [record_id:2034]. This places the talk within a broader strategic environment where chips, fabs, device manufacturers, and supplier relationships are not just technical details but elements of national resilience and geopolitical competition.

The talk also critiques current government responses. According to the record, governments are responding with “blunt tools like bans and onshoring,” but these are characterized as “slow, costly, and often impractical” [record_id:2034]. The implication is that provenance and transparency mechanisms may provide a more adaptable and scalable way to manage risk than relying exclusively on exclusionary or reshoring strategies.

### Visibility, Traceability, and Accountability

The HBOM Initiative is described as an effort to bring “visibility, traceability, and accountability” to the hardware supply chain [record_id:2034]. These terms form the normative core of the talk. Visibility means stakeholders can see what is inside hardware systems. Traceability means they can understand where components come from and how they move through the supply chain. Accountability implies that suppliers, manufacturers, integrators, and buyers can be connected to claims about hardware origin and integrity.

The record suggests that a key goal is to expose “inter-organizational dependencies” and detect “supply chain manipulation” [record_id:2034]. This moves the discussion beyond single-organization asset management and into multi-party trust. Hardware security, in this framing, requires tools and practices that cross company boundaries and reveal relationships that may otherwise remain hidden.

### Community Involvement in Shaping Hardware Trust

The talk is not only descriptive or policy-oriented; it also appeals to the hacker and security community. The record states that the talk will explore “how the hacker and security community can help shape the future of hardware trust” [record_id:2034]. This is significant because it places HBOM development not solely in the hands of governments or large manufacturers, but also within the domain of independent researchers, practitioners, and security communities.

The talk therefore presents hardware provenance as an emerging space where norms, tooling, and practices are still being formed. The record’s language—“why HBOMs are inevitable, what makes them hard”—suggests both confidence in the direction of travel and awareness that practical implementation remains difficult [record_id:2034].

## Methods, Tools, And Approaches Discussed

The main method or approach discussed is the development and use of a **hardware bill of materials**, or **HBOM**, through the **HBOM Initiative** [record_id:2034]. The record describes this initiative as a “new effort” to develop “tools and practices” for a hardware bill of materials [record_id:2034]. While it does not provide a detailed technical architecture, it identifies several intended functions.

First, HBOMs are meant to provide visibility into hardware components, especially chips inside IoT devices [record_id:2034]. This includes moving beyond procurement-oriented BOMs toward records that capture security-relevant information.

Second, HBOMs are meant to support **provenance tracing**. The abstract specifically mentions tracing “chip provenance,” implying a need to record component origin, manufacturing context, and potentially supply-chain path [record_id:2034].

Third, HBOMs are intended to capture **integrity and risk context**, areas that the record says traditional BOMs rarely include [record_id:2034]. This suggests a richer data model that might include authenticity indicators, known supplier risks, fabrication details, substitution risk, clone risk, and other forms of contextual assessment.

Fourth, the approach is framed as a way to detect or expose **supply-chain manipulation**. The record says traditional BOMs were not built to “detect supply chain manipulation,” and positions HBOMs as a response to that limitation [record_id:2034].

Fifth, the approach is explicitly intended to support **risk-informed decision-making** rather than absolute trust or simple allow/block models. The record says HBOMs should “empower sectors to make smarter, risk-informed decisions without sacrificing adaptability or innovation” [record_id:2034]. This is important because it differentiates the approach from blunt policy responses such as bans or onshoring. HBOMs are framed as a flexible transparency layer rather than a prescriptive procurement ban.

The record does not identify a specific HBOM schema, data format, open-source tool, standardization body, implementation workflow, or verification mechanism. It also does not specify how HBOM claims would be authenticated, how provenance data would be collected, or how organizations would manage proprietary supplier information. Those are open technical and governance questions left unresolved by the available evidence.

## Notable Talks, Records, And Evidence

The single representative record is Allan Friedman’s DEF CON 33 talk, **“What’s Really in the Box? The Case for Hardware Provenance and HBOMs”** [record_id:2034]. It matters because it articulates a clear conceptual bridge from SBOM-based software supply chain transparency to HBOM-based hardware supply chain transparency.

Several aspects make this record notable:

- It identifies a gap between software and hardware transparency, arguing that hardware remains opaque while software supply chains increasingly adopt SBOMs [record_id:2034].
- It elevates chips inside IoT devices as a major risk surface, potentially carrying “just as much — if not more — risk” than software components [record_id:2034].
- It ties semiconductor opacity to national security, citing cloned components, opaque fabs, and the semiconductor supply chain as a national security flashpoint [record_id:2034].
- It critiques bans and onshoring as inadequate or impractical standalone solutions [record_id:2034].
- It distinguishes traditional procurement/production BOMs from security-oriented HBOMs that capture origin, integrity, and risk context [record_id:2034].
- It introduces the HBOM Initiative as a vehicle for tools and practices that improve visibility, traceability, and accountability in hardware supply chains [record_id:2034].
- It calls on the hacker and security community to participate in shaping the future of hardware trust [record_id:2034].

As evidence, the record is best treated as a position-setting conference abstract. It gives strong evidence that Friedman is advocating for HBOMs as an emerging supply-chain transparency mechanism, but it does not provide enough detail to evaluate implementation maturity, technical feasibility, or adoption.

## Gaps, Limits, And Open Questions

The largest limitation is corpus size. With only one record, there is not enough evidence to identify long-term trends in Allan Friedman’s work, compare multiple talks, track evolution over time, or distinguish recurring themes from a single presentation topic [record_id:2034].

The record leaves several substantive questions unanswered.

First, it does not explain what an HBOM should contain in practice. It names origin, integrity, provenance, and risk context as important, but does not define required fields, data models, schemas, or levels of granularity [record_id:2034].

Second, it does not describe how provenance claims would be verified. If an HBOM states that a chip came from a particular source or fabrication facility, the record does not explain whether that claim would be supported by cryptographic attestations, audits, supplier declarations, physical inspection, side-channel analysis, serialization, trusted ledgers, or other mechanisms.

Third, it does not address how HBOMs would handle proprietary or sensitive supplier information. Hardware supply chains often involve confidential supplier relationships, second-source components, brokers, and outsourced manufacturing. The record calls for visibility and traceability but does not discuss confidentiality tradeoffs [record_id:2034].

Fourth, it does not specify who would maintain HBOMs across the lifecycle of a product. Open questions include whether responsibility lies with chip vendors, board manufacturers, OEMs, integrators, distributors, asset owners, or regulators.

Fifth, it does not provide empirical evidence about the prevalence of cloned components, opaque fabs, or supply-chain manipulation. These risks are named as motivators, but the abstract does not include case studies, statistics, or incident analysis [record_id:2034].

Sixth, the record does not compare HBOMs with other hardware trust approaches such as hardware roots of trust, secure elements, component authentication, physical unclonable functions, trusted foundry programs, secure logistics, or device attestation. Future research agents should therefore avoid assuming that HBOMs are presented as a complete replacement for those approaches; the available text frames them as a visibility and accountability mechanism [record_id:2034].

Finally, the record does not make clear how the HBOM Initiative relates to existing SBOM standards, regulatory efforts, or industry consortia. Since the talk explicitly builds from the SBOM analogy, a natural follow-up question is whether HBOMs would reuse SBOM data models, extend them, or require entirely different standards [record