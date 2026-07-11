# Topic: Author: Kai Tu

## Executive Summary

The two records attributed to Kai Tu present a focused body of security research around next-generation cellular systems, especially 5G infrastructure and mobile-network components. Both records are Black Hat US 2025 Briefings in which Kai Tu appears as a coauthor, and both emphasize vulnerability discovery in complex telecommunications systems through automation, fuzzing, reverse engineering, threat modeling, and architecture-aware testing.

Collectively, the records show Kai Tu contributing to research on two adjacent but distinct layers of the 5G ecosystem:

- **Open RAN / O-RAN infrastructure security**, where the work investigates how disaggregated, software-driven radio access network architectures introduce new attack surfaces and remotely exploitable vulnerabilities in RICs, RAN components, and xApps [record_id:57].
- **5G baseband firmware security**, where the work addresses proprietary modem firmware, state-dependent NAS message handling, and dependency-aware fuzzing against emulated Samsung and Pixel basebands [record_id:73].

The strongest recurring theme is that modern cellular security problems are increasingly shaped by **architectural complexity and hidden state dependencies**. Both records describe systems where traditional testing is insufficient: O-RAN introduces cloud-native microservices, standardized interfaces, and third-party components [record_id:57], while 5G basebands introduce new CPU architectures, C++ codebases, redesigned inter-task communication, and complex stateful protocol paths [record_id:73]. In response, the records emphasize **systematic, automated, dependency-aware testing** capable of reaching deep internal logic and uncovering previously unknown memory-corruption or firmware vulnerabilities.

Evidence is narrow but substantial within that narrow scope: both records are conference talk abstracts rather than full papers, but each claims concrete results, including newly discovered vulnerabilities and CVEs. Record 57 reports 26 previously unknown memory-corruption vulnerabilities and 20 new CVEs in O-RAN RIC and RAN implementations [record_id:57]. Record 73 reports 7 previously unknown 5G baseband vulnerabilities, with 5 CVEs assigned so far and several rated high or critical by vendors [record_id:73].

## Research Landscape

The available corpus for Kai Tu consists of **two Black Hat US 2025 briefing records**. Both are technical security presentations in the mobile and wireless domain. Neither record is a blog post, tool release note, interview, or standalone paper in the provided material; the evidence comes entirely from conference briefing descriptions. This means the records are rich in high-level technical framing and claimed contributions, but they do not provide full implementation details, datasets, exploit code, evaluation metrics, or disclosure timelines.

The research landscape represented here is highly concentrated in **5G cellular security**. The two records cover different parts of the cellular stack:

1. **Network-side 5G RAN modernization and O-RAN security**: Record 57 focuses on the transition from tightly integrated, vendor-specific RANs to disaggregated, software-driven O-RAN architectures. It highlights standardized interfaces, RAN Intelligent Controllers, cloud-native microservices, RAN nodes, RICs, xApps, and malicious user equipment as relevant parts of the threat model [record_id:57].

2. **Device-side or modem-side 5G baseband firmware security**: Record 73 focuses on proprietary baseband modems, especially Samsung and Pixel 5G basebands, with attention to Non-Access Stratum messaging, emulation, reverse engineering, and fuzzing of state-dependent firmware behavior [record_id:73].

Both records are classified around vulnerability discovery and exploit development. Record 57 is primarily associated with exploit development and vulnerability discovery, with secondary relevance to network security, network detection and response, and threat modeling [record_id:57]. Record 73 is likewise centered on exploit development and vulnerability discovery, with secondary relevance to operational technology and IoT security due to its firmware and embedded-systems angle [record_id:73].

A notable pattern is that both records present work on **hard-to-test systems where visibility is limited and state complexity is high**. O-RAN systems are open in the sense of standardized interfaces and disaggregation, but their distributed architecture creates new security challenges [record_id:57]. Baseband systems remain proprietary and closed-source, creating visibility and harnessing obstacles for security researchers [record_id:73]. The common response across both talks is automation guided by structural or dependency analysis.

## Major Themes And Trends

### 1. 5G Openness and Modernization Expand the Attack Surface

Record 57 frames O-RAN as a major architectural shift in cellular infrastructure. Traditional RANs are described as tightly integrated and vendor-specific, while O-RAN is described as disaggregated, software-driven, and based on standardized interfaces [record_id:57]. This openness is presented as beneficial for innovation and interoperability, but also as a security risk because it expands the attack surface [record_id:57].

The record specifically identifies exposed interfaces reachable by potentially malicious user equipment and under-protected RAN nodes [record_id:57]. This is important because it moves the security discussion beyond generic software bugs and into the consequences of architectural design. In the O-RAN setting, openness and modularity create new pathways by which malicious UEs, rogue RAN nodes, or vulnerable third-party xApps may interact with sensitive control-plane or optimization functions [record_id:57].

Record 73 addresses a different kind of opacity: proprietary baseband firmware. Here, the trend is not openness but **increasing internal complexity**. The record argues that closed-source development, memory-unsafe C/C++, and proprietary modem implementations form a large attack surface with minimal visibility [record_id:73]. The evolution from 4G to 5G introduces shifts in CPU architecture, movement from C to C++, and redesigned inter-task communication models, making prior manual fuzzing approaches less scalable [record_id:73].

Together, the records imply that 5G security is challenged from both directions: network infrastructure is becoming more open and modular, while baseband firmware remains opaque but more complex.

### 2. Architecture-Specific Security Testing Is Essential

A central theme in both records is that generic fuzzing or conventional testing is insufficient for modern cellular systems. Record 57 explicitly states the importance of “architecture-specific security testing” for emerging O-RAN deployments [record_id:57]. The proposed work maps new attack surfaces, identifies protection challenges from O-RAN’s microservice-based cloud-native architecture, and introduces a taxonomy of attack vectors targeting the O-RAN stack [record_id:57].

Record 73 similarly argues that prior approaches to GSM and LTE baseband fuzzing required extensive manual annotation and harnessing, and that these approaches do not scale to modern 5G systems with complex state dependencies and evolving firmware architectures [record_id:73]. The proposed response is a stateful fuzzing framework that runs directly on emulated baseband firmware and uses iterative symbolic analysis to uncover state variables and preconditions [record_id:73].

The shared trend is toward **domain-aware automation**. In both cases, successful testing depends on understanding system structure:

- O-RAN testing must account for inter-component dependencies among RICs, RANs, and xApps [record_id:57].
- Baseband testing must account for state variables, preconditions, and deep execution paths in NAS message handling [record_id:73].

### 3. Deep State and Inter-Component Dependencies Are Key Obstacles

Both records emphasize that the most important vulnerabilities may be hidden behind internal dependencies that prevent naïve testing from reaching vulnerable code.

In O-RAN, record 57 describes a testing framework that combines dynamic tracing and static analysis to uncover inter-component dependencies and generate constraint-driven test inputs [record_id:57]. The goal is to reach deep internal logic within RICs, RANs, and third-party xApps [record_id:57]. This suggests that O-RAN vulnerabilities may arise not only in individual components, but also in the assumptions and message flows between components.

In baseband firmware, record 73 describes complex state dependencies that make manual harnessing time-consuming and unscalable [record_id:73]. Its fuzzing framework uses iterative symbolic analysis to progressively uncover state variables and their preconditions, enabling fuzzing to target deep, state-dependent paths while mitigating path explosion [record_id:73].

The methodological parallel is strong. Both records are concerned with reaching code that is not easily accessible through shallow input mutation. Both use some form of dependency discovery to guide test generation. The main difference is the environment: distributed cloud-native O-RAN components in record 57, and emulated proprietary baseband firmware in record 73.

### 4. Memory Safety and Low-Level Implementation Risks Remain Prominent

Record 57 reports 26 previously unknown memory-corruption vulnerabilities across widely used O-RAN RIC and RAN implementations [record_id:57]. The impacts include silent service disruptions, performance degradation, component crashes, and system-wide failures [record_id:57]. The record further claims that these vulnerabilities resulted in 20 new CVEs [record_id:57].

Record 73 highlights the reliance of baseband modems on memory-unsafe C/C++ as a major contributor to attack surface [record_id:73]. The talk reports 7 previously unknown vulnerabilities in real-world devices, including Google Pixel and Samsung Galaxy models, with 5 CVEs assigned so far and several rated high or critical by vendors [record_id:73].

Across both records, memory safety remains an important root concern despite the modernization of cellular systems. New architectures, microservices, emulation, C++ transitions, and 5G protocol changes do not remove traditional vulnerability classes; instead, they may create more complex contexts in which those vulnerabilities are harder to find and potentially more operationally significant.

### 5. Real-World Exploitability and Operational Impact Are Emphasized

Both records go beyond vulnerability counts and describe real-world attack consequences.

Record 57 claims that O-RAN vulnerabilities are remotely exploitable via public-facing interfaces by malicious UEs or rogue RAN nodes [record_id:57]. The stated operational impacts include silent service disruptions, performance degradation, component crashes, and system-wide failures [record_id:57]. This positions O-RAN vulnerabilities as threats not only to software correctness but to cellular network availability and resilience.

Record 73 states that the talk will demonstrate real-world exploits such as SMS-triggered crashes and malicious network-triggered crashes [record_id:73]. These examples are significant because baseband vulnerabilities can be triggered through wireless or messaging paths that may not require physical device access.

The shared emphasis is on **remote exploitability in deployed cellular contexts**. The records do not provide exploit code or detailed step-by-step exploit chains, but they present the vulnerabilities as operationally meaningful rather than merely theoretical.

## Methods, Tools, And Approaches Discussed

The records describe several methodological contributions and technical approaches.

For O-RAN security, record 57 describes a systematic process beginning with attack-surface mapping. The work contrasts O-RAN’s microservice-based, cloud-native architecture with traditional closed RANs, then introduces a taxonomy of attack vectors targeting the O-RAN stack [record_id:57]. This taxonomy appears intended to support threat modeling and defense strategy [record_id:57].

Record 57 also describes what it calls the first automated security testing framework designed for O-RAN [record_id:57]. The framework combines:

- **Dynamic tracing**, used to observe runtime behavior and inter-component interactions [record_id:57].
- **Static analysis**, used to infer structure and dependencies in code or component logic [record_id:57].
- **Inter-component dependency discovery**, focused on RICs, RANs, and third-party xApps [record_id:57].
- **Constraint-driven test input generation**, intended to reach deep internal logic [record_id:57].

For baseband security, record 73 describes reverse engineering and emulation of Samsung and Pixel 5G basebands, focusing on Non-Access Stratum messaging [record_id:73]. The work identifies challenges introduced by the evolution from 4G to 5G, including CPU architecture shifts, migration from C to C++, and redesigned inter-task communication [record_id:73].

Record 73’s primary method is a **stateful fuzzing framework** that runs directly on emulated baseband firmware [record_id:73]. Its core technique is described as **iterative symbolic analysis**, which progressively uncovers state variables and their preconditions [record_id:73]. This allows fuzzing to reach different execution paths, target deep state-dependent behavior, and mitigate path explosion [record_id:73].

The methodological overlap between the two records is notable. Both research efforts combine program analysis with automated test generation. Both are designed to overcome reachability problems in complex systems. Both target real implementations rather than toy systems. However, they operate in different environments: one in distributed O-RAN infrastructure and one in emulated proprietary modem firmware.

## Notable Talks, Records, And Evidence

The most representative O-RAN record is **“Open RAN, Open Risk: Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN”** [record_id:57]. This record matters because it connects an industry-wide architectural transition—the adoption of O-RAN—to concrete security risks. It argues that disaggregation, standardized interfaces, RICs, and cloud-native architecture create new exposed interfaces and protection challenges [record_id:57]. It also reports substantial vulnerability discovery results: 26 previously unknown memory-corruption vulnerabilities and 20 new CVEs [record_id:57]. The record is especially important for researchers interested in RAN security, O-RAN threat modeling, xApp security, RIC testing, and the operational impact of cellular infrastructure vulnerabilities.

The most representative baseband record is **“Uncovering ‘NASty’ 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing”** [record_id:73]. This record matters because it addresses a historically difficult target: proprietary cellular baseband firmware. It situates its contribution against prior GSM and LTE baseband fuzzing work, arguing that manual annotation and harnessing are inadequate for modern 5G systems [record_id:73]. It then proposes