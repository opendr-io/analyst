# Topic: Author: Tianchang Yang

## Executive Summary

The three records attributed to Tianchang Yang present a focused body of offensive security research on next-generation wireless and cellular infrastructure. Across Black Hat Briefings in 2025 and 2026, Yang appears as a coauthor on work examining security failures in emerging communications systems: Open RAN cellular architectures, 5G baseband firmware, and 6 GHz Wi-Fi Automated Frequency Coordination systems [record_id:57] [record_id:73] [record_id:2676].

Collectively, the records emphasize that modernization and openness in wireless infrastructure create new attack surfaces. Open RAN’s disaggregated, microservice-based architecture exposes new interfaces and inter-component dependencies [record_id:57]. Modern 5G basebands remain opaque, proprietary, and difficult to test, while their complex state dependencies make older fuzzing approaches insufficient [record_id:73]. The 6 GHz AFC ecosystem relies on access points truthfully reporting location and environmental inputs, creating a trust boundary problem that can be exploited without breaking cryptography or compromising cloud infrastructure [record_id:2676].

A recurring contribution across the records is systematic security analysis of complex wireless systems, often paired with automated or semi-automated testing methods. The Open RAN work reports a testing framework combining dynamic tracing and static analysis, uncovering 26 previously unknown memory-corruption vulnerabilities and 20 CVEs [record_id:57]. The 5G baseband work presents dependency-aware, stateful fuzzing using iterative symbolic analysis, finding 7 previously unknown vulnerabilities and 5 assigned CVEs at the time of the abstract [record_id:73]. The AFC work claims the first systematic security analysis of the AFC ecosystem, empirically validated on commercial access points from four major vendors, and identifies four attack classes affecting every tested device [record_id:2676].

The evidence is strong at the level of conference abstracts: each record provides concrete systems studied, methods used, vulnerability counts or attack classes, and claimed impacts. However, because the available material consists only of talk descriptions rather than full papers, code, exploit details, CVE lists, or vendor advisories, downstream agents should treat technical specifics as summarized claims awaiting deeper validation.

## Research Landscape

The topic is narrow in record count but coherent in technical domain. All three records are Black Hat Briefings, with two scheduled for Black Hat USA 2025 and one for Black Hat USA 2026 [record_id:57] [record_id:73] [record_id:2676]. Tianchang Yang is not listed as a sole author in any record; all three are collaborative talks. The coauthor sets overlap partially across the cellular records: Kai Tu, Ali Ranjbar, and Syed Rafiul Hussain appear with Yang in the Open RAN and 5G baseband records [record_id:57] [record_id:73]. Syed Rafiul Hussain also appears in the AFC record [record_id:2676]. This suggests a research cluster centered on wireless systems security, with Yang contributing to projects spanning cellular infrastructure, mobile baseband firmware, and Wi-Fi spectrum coordination.

The dominant source type is conference presentation abstract rather than blog post, academic paper, tool release, or advisory. The records therefore describe intended talks and their claimed findings, methods, and demonstrations. They are rich enough to identify research direction and technical themes, but not sufficient to reconstruct full exploit chains or reproduce findings.

The broader research area is security of next-generation wireless infrastructure. Each record focuses on a system undergoing architectural transition:

- 5G Radio Access Networks moving from closed, vendor-specific systems to Open RAN’s disaggregated and software-driven design [record_id:57].
- Cellular baseband firmware evolving from prior GSM/LTE targets toward more complex 5G systems with changed CPU architectures, C++ codebases, and redesigned inter-task communication [record_id:73].
- Wi-Fi expanding into the 6 GHz band using cloud-based Automated Frequency Coordination to protect incumbent spectrum users [record_id:2676].

These systems are operationally important and security-sensitive. The Open RAN record discusses potential silent service disruptions, performance degradation, component crashes, and system-wide failures [record_id:57]. The baseband record discusses SMS and malicious-network-triggered crashes on real-world devices [record_id:73]. The AFC record highlights interference risks to incumbents such as emergency services, utility backhaul, fixed microwave links, and cellular backhaul [record_id:2676].

## Major Themes And Trends

### Security risks introduced by architectural openness and disaggregation

A central theme is that openness, modularity, and cloud-native design can increase security exposure even when they improve interoperability or scalability. The Open RAN record states that 5G RANs are shifting away from tightly integrated, vendor-specific systems toward disaggregated, software-driven architectures, with standardized interfaces and RAN Intelligent Controllers enabling modular optimization [record_id:57]. The same openness is described as expanding the attack surface by exposing critical interfaces to potentially malicious user equipment and under-protected RAN nodes [record_id:57].

This theme is not simply “open systems are insecure.” Rather, the record frames Open RAN as a security challenge because new standardized interfaces and microservice-based architectures create architecture-specific attack surfaces that differ from traditional closed RAN deployments [record_id:57]. The talk’s stated contribution is to map these attack surfaces, introduce a taxonomy of attack vectors, and show why testing must be adapted to the Open RAN stack [record_id:57].

The AFC record shows a related but distinct form of trust-boundary expansion. AFC is a cloud-based control plane that determines allowed channels and transmit power for standard-power 6 GHz access points based on geolocation [record_id:2676]. The record argues that the ecosystem relies on an untested assumption: the access point is a trusted endpoint that reports truthful data over a secure channel [record_id:2676]. The attack surface therefore includes not just backend services or encrypted communications, but also physical and network inputs such as GNSS, Wi-Fi positioning, DNS, and NTP [record_id:2676].

Together, these records suggest a trend in Yang-attributed work: when wireless systems become more programmable, distributed, or cloud-coordinated, traditional security boundaries become insufficient. The researchers look for places where trusted control decisions depend on unverified local inputs, inter-component messages, or exposed interfaces.

### Deep state and dependency challenges in wireless system testing

Another recurring theme is the difficulty of reaching meaningful internal states in complex wireless systems. The Open RAN record reports an automated testing framework that combines dynamic tracing and static analysis to uncover inter-component dependencies and generate constraint-driven test inputs capable of reaching deep internal logic in RICs, RANs, and third-party xApps [record_id:57]. The emphasis on dependencies and deep logic indicates that shallow interface fuzzing may not be enough for O-RAN software.

The 5G baseband record develops this theme more explicitly. It states that prior work on GSM and LTE basebands required extensive manual annotation and harnessing, and that such approaches fall short for modern 5G systems because complex state dependencies and evolving firmware architectures make manual harnessing time-consuming and unscalable [record_id:73]. The proposed response is a stateful fuzzing framework running directly on emulated baseband firmware, using iterative symbolic analysis to uncover state variables and preconditions for reaching different execution paths [record_id:73].

Across these records, the trend is toward dependency-aware analysis: identifying which states, inputs, preconditions, and inter-component relationships must be satisfied before vulnerable code is reachable. This appears to be a distinctive methodological concern in the Yang-attributed corpus, especially for wireless systems where meaningful behavior is often hidden behind protocol state machines, firmware tasks, and distributed controllers [record_id:57] [record_id:73].

### Vulnerability discovery with measurable outputs

The records make concrete vulnerability-discovery claims. The Open RAN talk reports 26 previously unknown memory-corruption vulnerabilities across widely used O-RAN RIC and RAN implementations, resulting in 20 new CVEs [record_id:57]. The 5G baseband talk reports 7 previously unknown vulnerabilities in real-world devices including Google Pixel and Samsung Galaxy models, with 5 CVEs assigned at the time and several rated high or critical by vendors [record_id:73]. The AFC talk does not report a CVE count in the abstract, but it does state that every commercial access point tested from four major vendors was vulnerable to at least one, and often multiple, identified attacks [record_id:2676].

The research therefore appears impact-oriented. The records emphasize not only conceptual weaknesses but also empirical findings, affected products, exploitability, and operational consequences. In the cellular work, the vulnerability outputs are quantified through CVEs [record_id:57] [record_id:73]. In the AFC work, impact is organized into attack classes and vendor/device coverage [record_id:2676].

### Remote and off-path exploitation as an operational concern

The records repeatedly highlight attacks that do not require privileged local access. The Open RAN abstract says vulnerabilities are remotely exploitable via public-facing interfaces by malicious user equipment or rogue RAN nodes [record_id:57]. The 5G baseband abstract mentions real-world exploits such as SMS-triggered and malicious-network-triggered crashes [record_id:73]. The AFC abstract says off-path attackers can remotely manipulate AFC decisions using low-cost, off-the-shelf tools or hardware, without breaking cryptography or compromising backend infrastructure [record_id:2676].

This is a notable pattern: the research is concerned with how wireless-facing, network-facing, or environment-facing inputs can trigger failures in systems that may otherwise appear protected by conventional controls. The AFC record is particularly explicit that cryptography alone is not enough if the endpoint’s reported environment remains trusted and unverified [record_id:2676].

### Protection of critical communications infrastructure

All three records connect technical vulnerabilities to broader infrastructure risk. Open RAN is framed in the context of major operators worldwide accelerating adoption of O-RAN [record_id:57]. 5G basebands are described as the unseen engines of cellular communication, with vulnerabilities affecting widely used Samsung and Pixel devices [record_id:73]. The AFC record ties 6 GHz Wi-Fi coordination to coexistence with mission-critical incumbents, including fixed microwave links, cellular backhaul, emergency services, and utility backhaul [record_id:2676].

The collective concern is not merely device compromise or isolated crashes; it is the reliability and safety of communications systems that support large populations and critical services. The records emphasize service disruption, interference, infrastructure exhaustion, and degraded availability [record_id:57] [record_id:73] [record_id:2676].

## Methods, Tools, And Approaches Discussed

The Open RAN record describes a systematic testing approach tailored to O-RAN architecture. It begins with mapping attack surfaces and protection challenges introduced by microservice-based, cloud-native O-RAN designs, contrasting them with traditional closed RANs [record_id:57]. It then introduces a taxonomy of attack vectors targeting the O-RAN stack [record_id:57]. The testing framework combines dynamic tracing and static analysis to uncover inter-component dependencies, then generates constraint-driven test inputs to reach deep internal logic in RICs, RANs, and third-party xApps [record_id:57]. This combination suggests a workflow that first models component interactions and then uses that model to guide input generation.

The 5G baseband record focuses on reverse engineering, emulation, and stateful fuzzing. The talk examines Samsung and Pixel 5G basebands, especially Non-Access Stratum messaging [record_id:73]. It identifies challenges introduced by 5G evolution, including CPU architecture shifts, movement from C to C++, and redesigned inter-task communication [record_id:73]. The proposed framework runs directly on emulated baseband firmware and uses iterative symbolic analysis to progressively uncover state variables and their preconditions [record_id:73]. The stated purpose is to guide fuzzing into deep, state-dependent paths while mitigating path explosion [record_id:73]. This is presented as a way to reduce the manual annotation and harnessing burden associated with earlier baseband fuzzing work [record_id:73].

The AFC record uses systematic ecosystem analysis validated on commercial hardware. The tested devices come from HPE Aruba, RUCKUS, Ubiquiti, and ASUS [record_id:2676]. The record describes four attack classes: location spoofing, persistent denial-of-service through time or location manipulation, response injection through flawed TLS certificate validation, and service exhaustion through repeated coordination requests [record_id:2676]. The mitigations proposed include certificate pinning, geofencing, and secure network protocols [record_id:2676]. Methodologically, this work appears to combine protocol/security-boundary analysis with empirical testing against commercial implementations.

A shared methodological pattern is visible across the records:

1. Identify a new or evolving wireless architecture.
2. Model its trust assumptions, interfaces, states, or dependencies.
3. Build a testing or analysis method suited to that architecture.
4. Validate against real implementations or commercial devices.
5. Demonstrate operationally meaningful attacks or vulnerabilities.

This pattern is clearest in the Open RAN and baseband records because they describe automated frameworks [record_id:57] [record_id:73]. It is also present in the AFC record through its systematic analysis and multi-vendor empirical validation [record_id:2676].

## Notable Talks, Records, And Evidence

The Open RAN talk, “Open RAN, Open Risk: Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN,” is representative of the corpus’s interest in architectural security for emerging wireless infrastructure [record_id:57]. It is notable for combining threat modeling, taxonomy development, automated testing, and concrete vulnerability discovery. The abstract’s strongest evidence claims are the discovery of 26 previously unknown memory-corruption vulnerabilities and 20 new CVEs across widely used O-RAN RIC and RAN implementations [record_id:57]. It also matters because it frames O-RAN security as architecture-specific: disaggregated, microservice-based systems expose attack surfaces that require different testing strategies from traditional closed RANs [record_id:57].

The 5G baseband talk, “Uncovering ‘NASty’ 5G Base