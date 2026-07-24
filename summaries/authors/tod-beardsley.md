# Topic: Author: Tod Beardsley

## Executive Summary

The three records attributed to Tod Beardsley cluster tightly around vulnerability governance, vulnerability intelligence infrastructure, and the practical problem of turning vulnerability information into decisions. Across the records, Beardsley appears as a contributor to discussions about how the security ecosystem scores, prioritizes, names, funds, governs, and debates vulnerabilities.

The strongest theme is skepticism toward overly mechanical vulnerability prioritization. In the Black Hat 2025 talk “Vulnerability Haruspicy,” Beardsley frames CVSS, EPSS, SSVC, KEV lists, vendor advisories, and practitioner judgment as imperfect tools that defenders use to distinguish urgent vulnerabilities from lower-priority ones, while questioning whether these models actually improve decisions or merely rationalize decisions teams already wanted to make [record_id:64]. The other two records situate Beardsley in public community discussions about the CVE Program: its future governance, funding pressures, relationship to the U.S. National Vulnerability Database, the emergence of the EU Vulnerability Database, and how policymakers should understand the program’s importance [record_id:2571]. A follow-on “AMA” format continues that CVE-focused conversation by explicitly inviting open audience questions and discussion after a prior CVE panel ran out of time [record_id:2732].

Collectively, the records suggest Beardsley’s represented contribution is not a narrow technical exploit-development focus, but rather a public, governance-aware, practitioner-oriented view of vulnerability management: how vulnerability data systems are maintained, how they influence real-world security operations, and how community institutions such as CVE should adapt under political, funding, and operational pressure.

## Research Landscape

The record set is small: three conference-session records, all from 2025–2026 event contexts, with no long-form articles, slides, transcripts, code repositories, or post-event materials included. The sources are Black Hat and BSidesLV, indicating that the evidence base is drawn from public security conference programming rather than from publications or technical artifacts.

The records divide into two related areas:

1. **Vulnerability prioritization and risk scoring.**  
   The Black Hat 2025 briefing “Vulnerability Haruspicy: Picking Out Risk Signals from Scoring System Entrails” focuses on vulnerability scoring and prioritization frameworks. It explicitly names CVSS, EPSS, SSVC, KEV lists, vendor advisories, and “lived experience” as signals defenders use in vulnerability risk management [record_id:64]. This is the only solo-authored record in the set and appears to be the most directly attributable to Tod Beardsley as an individual speaker.

2. **CVE governance and ecosystem sustainability.**  
   The two BSidesLV records are panel or group-format sessions involving Beardsley and other named participants. “What Should CVE Be When It Grows Up?” frames the CVE Program as a foundational cybersecurity institution that has served for more than a quarter century, but one now facing funding challenges, governance questions, policy scrutiny, and potential ecosystem fragmentation [record_id:2571]. “I am CVE, AMA!” appears to continue that discussion in a more interactive audience-question format, explicitly referencing a prior BSidesLV CVE panel that ran out of time for audience questions [record_id:2732].

The research landscape is therefore governance-heavy and vulnerability-management-heavy. There is little evidence here of product-specific security research, malware analysis, offensive tradecraft, reverse engineering, or tool release. Instead, the records portray Beardsley’s role as a public discussant and analyst of vulnerability-management systems, especially the tension between formalized structures and messy operational reality.

## Major Themes And Trends

### 1. Vulnerability scoring as useful but questionable decision support

The clearest theme appears in “Vulnerability Haruspicy,” which treats vulnerability scoring as an attempt to “bring order to the chaos of risk management” while also suggesting that, in practice, it can resemble divination more than science [record_id:64]. The abstract uses intentionally comic and skeptical language: CVSS is said to perform “monkey math,” EPSS is described as trying to predict exploitation with “statistical black magicks,” and SSVC is characterized as abandoning math in favor of “structured gut feelings” [record_id:64].

Behind the humor is a serious research question: whether scoring systems meaningfully improve vulnerability-management decisions. The record says defenders mix CVSS, EPSS, SSVC, KEV lists, vendor advisories, and experience to determine which issues are “truly urgent” and which are “merely annoying” [record_id:64]. The central concern is not just whether scoring models are accurate in abstraction, but whether they help actual security teams prioritize work under constraints.

This theme suggests a pragmatic stance: formal systems are evaluated not by elegance, but by whether they change outcomes for defenders. The talk’s stated intent is to examine “where these models help, where they mislead,” and whether any are better than “rolling a D20 saving throw vs exploitation” [record_id:64]. The framing implies that vulnerability scoring may be both necessary and absurd: necessary because teams need triage, absurd because risk is context-dependent, uncertain, and often reduced to artificial numeric or categorical outputs.

### 2. Vulnerability intelligence depends on public infrastructure and governance

The CVE-focused BSidesLV records shift from scoring to the institutional infrastructure that makes vulnerability management possible. “What Should CVE Be When It Grows Up?” describes the CVE Program as “a pillar of the cybersecurity ecosystem” and an “authoritative source of data about vulnerabilities for software users” [record_id:2571]. It also emphasizes CVE’s role in driving “security into the design and development process,” meaning the program is not framed merely as a database of labels, but as part of a broader software-security feedback loop [record_id:2571].

The same record highlights current stressors: funding challenges affecting both the CVE Program and the U.S. National Vulnerability Database over the preceding 18 months, the creation of the EU Vulnerability Database, congressional attention, and a requested formal audit of the program [record_id:2571]. The central question becomes how to communicate CVE’s challenges to policymakers while preserving its “critical function” and avoiding “fractioning of the ecosystem” [record_id:2571].

This record therefore connects vulnerability intelligence to public policy, transnational governance, funding stability, and institutional legitimacy. It suggests that vulnerability data systems are not self-sustaining technical utilities; they require governance models, public trust, and coordination among national and international actors.

### 3. Concern over fragmentation of vulnerability ecosystems

A recurring concern in the CVE material is fragmentation. Record 2571 explicitly asks how challenges should be communicated to policymakers “in a way that maintains the critical function and avoids a fractioning of the ecosystem” [record_id:2571]. The reference to both the U.S. National Vulnerability Database and the EU Vulnerability Database implies a changing landscape in which multiple vulnerability-data authorities or repositories may coexist, with potential benefits but also risks to consistency and interoperability [record_id:2571].

This concern complements the scoring theme. If vulnerability scoring is already uncertain and context-sensitive, fragmentation in the identifiers and databases that feed vulnerability management could further complicate prioritization. CVE identifiers, NVD enrichment, vendor advisories, KEV catalogs, and scoring systems are all part of the information pipeline defenders rely on. The records do not provide a technical architecture for preventing fragmentation, but they clearly identify it as a governance risk.

### 4. Community discussion as a method for shaping vulnerability institutions

The two BSidesLV records emphasize panel discussion and audience engagement. “What Should CVE Be When It Grows Up?” is framed around open questions: challenges facing the program, communication to policymakers, and new governance models [record_id:2571]. The later “I am CVE, AMA!” record explicitly says the previous BSidesLV panel ran out of time for audience questions and that the new session would be an “Oops all questions!” version [record_id:2732].

This indicates a participatory mode of governance discourse. The CVE Program’s future is not presented as an issue for a single vendor, agency, or technical committee alone, but as a topic for community debate. The AMA record’s statement that “No topic is taboo, modulo the code of conduct” suggests an intention to surface difficult or controversial questions within community norms [record_id:2732].

The trend across these records is toward public, community-facing deliberation on vulnerability management institutions. Beardsley’s presence in these sessions links him to that deliberative style: challenging assumptions, inviting debate, and treating vulnerability infrastructure as a shared responsibility.

### 5. Humor and irreverence used to discuss serious operational problems

The Black Hat abstract is unusually colorful. It invokes “tarot cards,” “entrails,” “statistical black magicks,” “structured gut feelings,” “rolling a D20,” and “astrology jokes” [record_id:64]. This humor is not incidental; it frames the topic as one in which the security community may overstate the scientific precision of vulnerability scoring. The rhetorical style lowers the barrier to discussing a dry governance and metrics problem while sharpening criticism of false precision.

The AMA record also uses informal language: “Alas,” “caught some shade,” and “Oops all questions!” [record_id:2732]. While less analytically dense, this style points to a community-conference register: candid, conversational, and responsive to audience feedback. The shared tone across records suggests that Beardsley-associated sessions may use humor and open discussion to address structural issues in vulnerability management.

## Methods, Tools, And Approaches Discussed

The records do not provide implementation details, experimental protocols, source code, or step-by-step workflows. However, they identify several frameworks, tools, and institutional mechanisms relevant to vulnerability management.

The most concrete methods are vulnerability prioritization systems:

- **CVSS**, presented as a scoring system used to bring order to vulnerability risk, though the Black Hat abstract critiques its mathematical framing and practical limitations [record_id:64].
- **EPSS**, described as a statistical approach that attempts to predict exploitation, again with skepticism about how much predictive value it offers in operational settings [record_id:64].
- **SSVC**, characterized as a structured decision approach that relies less on numeric scoring and more on guided judgment or “structured gut feelings” [record_id:64].
- **KEV lists**, likely meaning known-exploited-vulnerability lists, described as one of the shortcuts defenders use to distinguish urgent vulnerabilities from less urgent ones [record_id:64].
- **Vendor advisories** and **lived experience**, which the record identifies as real-world inputs defenders combine with formal systems [record_id:64].

The approach discussed in record 64 is comparative and evaluative rather than purely technical. The talk proposes to compare CVSS, EPSS, and SSVC against the “reality of how security teams actually handle vulnerabilities” [record_id:64]. This implies a practitioner-grounded evaluation method: models should be judged by their fit with operational triage, not merely by their internal consistency.

The CVE records focus on institutional approaches:

- The **CVE Program** is treated as a central naming and data authority for vulnerabilities [record_id:2571].
- The **U.S. National Vulnerability Database** is presented as closely related to CVE and also affected by funding challenges [record_id:2571].
- The **EU Vulnerability Database** is identified as a new development that changes the governance environment [record_id:2571].
- **Formal audit**, **policymaker communication**, and **new governance models** are raised as mechanisms for reforming or preserving the CVE ecosystem [record_id:2571].
- The **AMA format** is used as a community-engagement method to gather and answer audience questions about CVE after a prior panel lacked enough time for Q&A [record_id:2732].

Together, these records describe a vulnerability-management stack that is partly technical and partly institutional: identifiers, databases, scoring models, known-exploitation signals, advisories, policy decisions, and community processes all shape how defenders understand and act on vulnerabilities.

## Notable Talks, Records, And Evidence

The most substantial and individually attributable record is the Black Hat 2025 briefing “Vulnerability Haruspicy: Picking Out Risk Signals from Scoring System Entrails” [record_id:64]. It matters because it presents a coherent thesis about vulnerability scoring: the field depends on frameworks such as CVSS, EPSS, and SSVC, but these frameworks may oversimplify, mislead, or merely rationalize preexisting judgments [record_id:64]. The abstract is also notable for connecting formal scoring systems to actual defender behavior, including KEV lists, vendor advisories, and lived experience [record_id:64]. For downstream researchers studying Beardsley’s views on risk quantification, vulnerability prioritization, or security metrics, this is the key record in the set.

The BSidesLV 2025 panel “What Should CVE Be When It Grows Up?” is representative of Beardsley’s participation in governance-oriented vulnerability-infrastructure discussions [record_id:2571]. Its importance lies in the breadth of issues it identifies: CVE’s long-standing role, its authority as a vulnerability data source, the relationship between vulnerability disclosure data and secure development, funding pressures on CVE and NVD, the emergence of the EU Vulnerability Database, congressional scrutiny, and possible governance-model reform [record_id:2571]. It is less individually attributable because Beardsley is one of several listed authors or panelists, but it is central for understanding the institutional context of the topic.

The BSidesLV “I am CVE, AMA!” session is important as a continuation of the CVE conversation rather than as a source of detailed claims [record_id:2732]. Its abstract says that a prior BSidesLV 2025 CVE panel ran out of time for audience questions, prompting a return with an “Oops all questions!” format [record_id:2732]. This record suggests sustained community interest in CVE and an effort by panelists, including Beardsley, to create a venue for open discussion.