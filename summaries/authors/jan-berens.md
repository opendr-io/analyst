# Topic: Author: Jan Berens

## Executive Summary

The records attributed to Jan Berens consist of two DEF CON 33 entries from 2025 about vulnerabilities in electric vehicle charging communications. Both records describe the same core research: attacks against widely used EV charging protocols by exploiting flaws in the underlying power-line communication layer, especially the QCA 7000 HomePlug modem series used in CCS and NACS charging systems [record_id:1931] [record_id:2145].

The central contribution of these records is a security analysis of EV charging infrastructure at the modem and power-line communication layer rather than only at higher-level charging protocols. The talks claim to demonstrate multiple new vulnerabilities enabling persistent denial of service, show ways to hijack EV charging communications through the HomePlug link, and present firmware reverse-engineering results leading to code execution [record_id:1931] [record_id:2145]. The records also emphasize real-world deployment exposure through a study of EV chargers and vehicles, suggesting that the weaknesses are not merely theoretical but affect “almost all EVs and chargers” using the targeted technologies [record_id:1931] [record_id:2145].

Because the two records contain identical abstracts, the evidence base is narrow but consistent. The corpus strongly supports identifying Jan Berens with EV charging security research, OT/IoT security, power-line communication attacks, modem vulnerability research, firmware reverse engineering, exploit development, and practical attack scenarios against CCS/NACS charging communications. It does not provide technical details of the vulnerabilities, exploit chains, firmware internals, mitigations, disclosure status, affected firmware versions, or empirical study methodology.

## Research Landscape

The available records are both DEF CON 33 talk records from 2025. They are not blog posts, papers, code repositories, interviews, or standalone advisories. Both are conference-video-style entries with titles, author lists, event metadata, and short talk descriptions. The source material therefore reflects conference presentation abstracts rather than full technical documentation.

The two entries appear to represent either duplicate or closely related versions of the same presentation. Record 1931 is titled “DEF CON 3 3 - Exploiting Vulns in EV Charging Comms” and lists Jan Berens, Marcell Szakály, and Sebastian Köhler as authors [record_id:1931]. Record 2145 is titled “One Modem to Brick Them All -Vulns in EV Charging Comms” and lists Jan Berens and Marcell Szakaly as authors [record_id:2145]. Both records are from DEF CON 33, both are dated 2025, and both have the same raw description text [record_id:1931] [record_id:2145]. The durations differ in the tags, with record 1931 tagged “55:11” and record 2145 tagged “43:23,” which may indicate different uploads, sessions, edits, or metadata variants [record_id:1931] [record_id:2145].

The research area represented is OT/IoT security focused on electric vehicle supply equipment and vehicle charging communications. The abstracts position the work at the intersection of:

- EV charging standards and ecosystems, especially CCS and NACS [record_id:1931] [record_id:2145].
- Power-line communication technologies underlying those charging systems [record_id:1931] [record_id:2145].
- Embedded modem security, specifically QCA 7000 HomePlug modems [record_id:1931] [record_id:2145].
- Vulnerability discovery and exploitation, including persistent denial of service and code execution [record_id:1931] [record_id:2145].
- Network-security implications, including hijacking EV charging communications “even at a distance” through the HomePlug link [record_id:1931] [record_id:2145].
- Deployment security assessment across EV chargers and vehicles [record_id:1931] [record_id:2145].

Overall, the landscape is compact but coherent: Jan Berens appears in this corpus as a co-author or co-presenter of applied security research on systemic vulnerabilities in the communications substrate of modern EV charging.

## Major Themes And Trends

### EV Charging Security Below The Application Protocol Layer

The strongest theme is that EV charging security cannot be evaluated only at the visible charging protocol or application layer. Both records state that the attacks target “the most widely used EV charging protocol” by exploiting “flaws in the underlying power-line communication technologies” [record_id:1931] [record_id:2145]. This frames the research as a lower-layer attack against the communication medium and modem infrastructure that supports higher-level charging protocols.

The emphasis on QCA 7000 HomePlug modems is especially important. The talks identify this modem series as used by “the two most popular EV charging systems, CCS and NACS” [record_id:1931] [record_id:2145]. That creates a supply-chain or component-level security theme: vulnerabilities in a shared modem platform may propagate across different vehicle and charger ecosystems. Rather than treating CCS and NACS as isolated protocol stacks, the records suggest that common underlying hardware can create cross-ecosystem exposure.

### Systemic Impact Across Vehicles And Chargers

Both records use broad language about scope, stating that the exploited power-line communication technologies affect “almost all EVs and chargers” [record_id:1931] [record_id:2145]. They also describe a study of EV chargers and vehicles intended to understand the scope of the issues and to show “widespread insecurities in existing deployments” [record_id:1931] [record_id:2145].

This theme is significant because it moves the work beyond a single-device exploit demonstration. The records claim that the researchers examined real deployments and found recurring weaknesses. The abstracts do not provide counts, sampling methods, vendor lists, geographic scope, or measurements, so the evidence for the scale claim is summary-level rather than independently assessable from these records alone. Still, across both records, the framing is clearly systemic: the issue is not merely one charger, one vehicle, or one lab setup, but a class of insecurity in deployed EV charging communications [record_id:1931] [record_id:2145].

### Denial Of Service And “Bricking” As Practical Risks

Persistent denial of service is a recurring and explicit impact. Both records say the researchers demonstrate “multiple new vulnerabilities in the modems, enabling persistent denial of service” [record_id:1931] [record_id:2145]. Record 2145’s title, “One Modem to Brick Them All,” reinforces the idea of disabling or rendering charging communication equipment unusable, although the raw abstract itself uses the more precise phrase “persistent denial of service” [record_id:2145].

The practical risk suggested by the records is that EV charging availability can be attacked at the modem communication layer. For EV infrastructure, denial of service is not simply an IT nuisance; it may interrupt charging operations, affect fleet logistics, impair public charging reliability, or undermine user trust. The records do not specify whether “persistent” means surviving reboots, requiring physical intervention, corrupting configuration or firmware, or causing repeated protocol failure. That remains an important gap. But the presence of persistent DoS as a claimed demonstrated outcome is one of the main technical findings of the corpus [record_id:1931] [record_id:2145].

### Hijacking EV Charging Communications Through HomePlug

Another major theme is communication hijacking using the HomePlug link. The records say the presenters show “a variety of practical real-world scenarios where the HomePlug link can be used to hijack EV charging communications, even at a distance” [record_id:1931] [record_id:2145]. This is a notable claim because EV charging communication is often physically constrained by the charging cable and connector. The abstracts suggest that the power-line communication layer may create attack opportunities beyond direct physical access to the endpoint.

The phrase “even at a distance” is important but under-specified. It could refer to signal propagation, nearby electrical coupling, malicious equipment connected to the same line, or some other remote-adjacent attack condition. The records do not define the distance, attacker placement, equipment needed, environmental constraints, or whether attacks require proximity to a charger, vehicle, electrical circuit, or charging cable. Nonetheless, both records consistently frame HomePlug as an attack surface that can be used for practical communication hijacking [record_id:1931] [record_id:2145].

### Firmware Reverse Engineering And Code Execution

The records culminate in firmware reverse engineering and code execution. Both say the talk presents “results from reverse engineering the firmware” and describes “how we can gain code execution” [record_id:1931] [record_id:2145]. This indicates that the research was not limited to black-box protocol manipulation or packet injection. It apparently involved embedded firmware analysis and exploit development against modem firmware.

This theme links the work to broader embedded and IoT exploitation practices: firmware extraction or analysis, vulnerability discovery, exploit construction, and execution control on a constrained communications device. The records do not state whether code execution is local or remote, authenticated or unauthenticated, persistent or transient, or whether it is achieved on the modem, charger-side controller, vehicle-side component, or a development setup. The abstract’s wording points to the modem firmware, but the exact target and exploit preconditions remain unspecified [record_id:1931] [record_id:2145].

### Shared Presentation With Slight Metadata Variation

A final trend is metadata variation around the same research. The two records have identical abstracts but different titles, durations, and author lists. Record 1931 includes Sebastian Köhler as a co-author, while record 2145 lists only Jan Berens and Marcell Szakaly/Szakály, with a spelling variation in Marcell’s surname between records [record_id:1931] [record_id:2145]. This suggests downstream agents should treat the two records as strongly overlapping evidence rather than independent technical confirmations. They are useful for coverage of the same DEF CON 33 research, but they should not be counted as two separate studies without further corroboration.

## Methods, Tools, And Approaches Discussed

The records discuss several methods and approaches, though only at the abstract level.

First, the researchers focus on the QCA 7000 HomePlug modem series as the key technical target [record_id:1931] [record_id:2145]. The modem-centered approach is notable because it treats the charging communication hardware itself as the vulnerability locus. The talks specifically connect the QCA 7000 series to CCS and NACS, describing it as used by the two most popular EV charging systems [record_id:1931] [record_id:2145]. This implies an approach based on finding common components across otherwise distinct charging ecosystems.

Second, the records describe vulnerability discovery in modem implementations. They claim “multiple new vulnerabilities in the modems” that enable persistent denial of service [record_id:1931] [record_id:2145]. While no CVEs, bug classes, packet formats, or exploit primitives are provided in the records, the methodology appears to include analysis of modem behavior under adversarial communication conditions.

Third, the researchers conducted a study of EV chargers and vehicles to assess scope and deployment exposure [record_id:1931] [record_id:2145]. The abstracts say this study showed “widespread insecurities in existing deployments” [record_id:1931] [record_id:2145]. The available records do not specify the sampling strategy or methodology, but the inclusion of a deployment study indicates the work included empirical field or lab evaluation across multiple chargers and vehicles, not solely a single-device proof of concept.

Fourth, the talks include practical attack-scenario construction. Both records say the researchers show “a variety of practical real-world scenarios” where the HomePlug link can be used to hijack EV charging communications [record_id:1931] [record_id:2145]. This suggests scenario-based security analysis: identifying attacker positions, communication paths, and operational contexts in which the HomePlug layer can be abused. However, the details of those scenarios are not in the raw records.

Fifth, the research includes firmware reverse engineering. Both records explicitly mention reverse engineering modem firmware and gaining code execution [record_id:1931] [record_id:2145]. This is the most technically advanced method described in the abstracts. It indicates that the researchers likely analyzed embedded binaries or firmware images and developed exploitation techniques leading to execution control. The records do not name reverse-engineering tools, debugging setups, hardware interfaces, or exploitation methods.

Together, the methods suggested by the records form a layered research workflow: identify a widely deployed shared modem platform, analyze its power-line communication behavior, discover vulnerabilities, validate impact through denial-of-service and hijacking scenarios, assess deployment prevalence across vehicles and chargers, and reverse engineer firmware to reach code execution [record_id:1931] [record_id:2145].

## Notable Talks, Records, And Evidence

The two records are both important because they appear to document the same DEF CON 33 research from slightly different metadata perspectives.

Record 1931, “DEF CON 3 3 - Exploiting Vulns in EV Charging Comms,” is a 2025 DEF CON 33 record attributed to Jan Berens, Marcell Szakály, and Sebastian Köhler [record_id:1931]. It is representative of the corpus because it contains the full abstract describing attacks against EV charging protocols through power-line communication flaws, the targeting of QCA 7000 HomePlug modems, persistent denial-of-service vulnerabilities, a study of EV chargers and vehicles, HomePlug-based communication hijacking, firmware reverse engineering, and code execution [record_id:1931]. This record is especially useful for identifying the full co-author set as represented in one metadata version.

Record 2145, “One Modem to Brick Them All -Vulns in EV Charging Comms,” is also a 2025 DEF CON 33 record and is attributed to Jan Berens and Marcell Szakaly [record_id:2145]. It contains the same abstract as record 1931, so it corroborates the same technical themes: QCA 7000 HomePlug modem vulnerabilities, CCS and NACS relevance, persistent denial of service, widespread deployment insecurities, practical HomePlug hijacking scenarios, firmware reverse engineering, and code execution [record_id:2145]. Its title