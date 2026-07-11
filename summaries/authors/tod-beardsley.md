# Topic: Author: Tod Beardsley

## Executive Summary

The two records attributed to Tod Beardsley center on vulnerability governance, vulnerability prioritization, and the institutional systems used to decide which software flaws matter most. They are both 2025 conference records and both deal with the problem of turning vulnerability information into actionable decisions. One record is a Black Hat USA briefing focused on the practical and conceptual limits of vulnerability scoring systems such as CVSS, EPSS, and SSVC [record_id:64]. The other is a BSidesLV panel-style session on the future of the CVE Program amid funding, governance, fragmentation, and policy challenges [record_id:2571].

Collectively, the records portray Beardsley’s contribution in this dataset as a critical, governance-aware voice in vulnerability management. The emphasis is not on exploit development or low-level technical research, but on the systems that mediate vulnerability knowledge: scoring frameworks, advisory shortcuts, vulnerability databases, institutional funding, policymaker communication, and ecosystem trust. The strongest recurring theme is skepticism toward supposedly objective vulnerability infrastructure. The records ask whether scoring and cataloging mechanisms genuinely improve defender decisions, whether they are sustainable, and how they should evolve under political, operational, and international pressure [record_id:64] [record_id:2571].

Because the corpus contains only two records, the evidence base is narrow. Still, the two records are thematically coherent: both concern how security teams and broader institutions classify, prioritize, and govern vulnerability information.

## Research Landscape

The dataset consists of two 2025 conference-session records:

- A Black Hat USA briefing titled “Vulnerability Haruspicy: Picking Out Risk Signals from Scoring System Entrails,” attributed to Tod Beardsley [record_id:64].
- A BSidesLV 2025 session titled “What Should CVE Be When It Grows Up?,” attributed to multiple speakers including Tod Beardsley [record_id:2571].

The landscape is therefore dominated by public conference abstracts rather than full papers, transcripts, slide decks, tools, code repositories, or empirical studies. The records provide session framing and research questions, but not detailed results, experimental data, or final conclusions. They are best read as evidence of topics Beardsley was associated with in 2025, not as complete documentation of his positions.

The broader research area is vulnerability management and governance. The Black Hat record addresses the defender-facing challenge of making risk decisions from scoring systems and signals such as CVSS, EPSS, SSVC, KEV lists, vendor advisories, and practitioner experience [record_id:64]. The BSidesLV record shifts from prioritization mechanisms to ecosystem infrastructure, examining the CVE Program, the US National Vulnerability Database, the EU Vulnerability Database, congressional attention, and possible new governance models [record_id:2571].

Together, these records sit at the intersection of:

- Vulnerability intelligence.
- Risk scoring and prioritization.
- Security operations decision-making.
- Public vulnerability infrastructure.
- Policy and governance.
- Sustainability and funding of shared cybersecurity resources.

The records do not suggest a focus on one narrow technology stack. Instead, they point to high-level security infrastructure: the labels, scores, identifiers, databases, and institutional processes that defenders rely on to decide what to fix.

## Major Themes And Trends

### 1. Skepticism toward vulnerability scoring as objective science

The clearest theme is skepticism about vulnerability scoring systems. The Black Hat abstract opens by saying vulnerability scoring is intended to “bring order to the chaos of risk management,” but in practice can feel “more like reading tarot cards or poking at entrails than applying science” [record_id:64]. This framing suggests a central concern: defenders often treat scoring systems as rational prioritization mechanisms, but the talk questions whether those mechanisms are as scientific or decision-improving as their presentation implies.

The abstract names three major frameworks:

- CVSS, described in the abstract as performing “monkey math to force fractal bell curves” [record_id:64].
- EPSS, described as attempting to “predict exploitation with statistical black magicks” [record_id:64].
- SSVC, described as ditching “math entirely in favor of structured gut feelings” [record_id:64].

The language is intentionally humorous and provocative, but the underlying theme is serious: scoring systems embed assumptions, simplifications, and artifacts. They may help defenders triage, but they may also obscure uncertainty or lend false authority to decisions that remain contextual and judgment-driven.

### 2. Tension between formal frameworks and real-world defender behavior

Record 64 contrasts formal scoring frameworks with how “security teams actually handle vulnerabilities” [record_id:64]. It says defenders “mix and match shortcuts” including “KEV lists, vendor advisories, and lived experience” to distinguish “the truly urgent from the merely annoying” [record_id:64]. This is an important theme because it suggests that operational vulnerability management is not reducible to a single score.

The record asks whether defenders are “actually making better risk decisions” or simply using frameworks “to justify what we were going to do anyway” [record_id:64]. That question frames scoring not only as a technical problem but as a behavioral and organizational one. Risk systems may function as post-hoc justification, coordination tools, or compliance artifacts rather than as independent decision engines.

This theme links naturally to the BSidesLV record. CVE and NVD are foundational sources of vulnerability data, but the panel abstract suggests that governance and funding pressures can affect the stability of those sources [record_id:2571]. If the underlying identifiers and databases are politically or institutionally fragile, then downstream scoring and prioritization workflows inherit that fragility.

### 3. Vulnerability infrastructure as public-interest governance

The BSidesLV record frames the CVE Program as “a pillar of the cybersecurity ecosystem” and “an authoritative source of data about vulnerabilities for software users” [record_id:2571]. It also says the program is “critical for continuing to drive security into the design and development process” [record_id:2571]. This moves beyond technical enumeration and treats CVE as infrastructure: a shared, public-interest mechanism that supports users, vendors, policymakers, and security practitioners.

The session raises governance questions prompted by funding and institutional stress. It states that over the prior 18 months, both the CVE Program and the US National Vulnerability Database faced “funding challenges” [record_id:2571]. It also notes the creation of the EU Vulnerability Database, congressional interest, and a June request by members of Congress for a formal audit of the program [record_id:2571].

The major trend here is the politicization and internationalization of vulnerability infrastructure. CVE is no longer presented merely as a technical naming scheme; it is a governance object subject to funding models, audits, policymaker communication, and possible ecosystem fragmentation [record_id:2571].

### 4. Avoiding fragmentation of the vulnerability ecosystem

The BSidesLV abstract explicitly asks how challenges facing the CVE Program should be communicated to policymakers “in a way that maintains the critical function and avoids a fractioning of the ecosystem” [record_id:2571]. This is one of the most important policy concerns in the records.

Fragmentation could mean competing vulnerability identifiers, divergent national or regional databases, inconsistent data quality, or incompatible governance practices. The record mentions developments in the European Union leading to the creation of the EU Vulnerability Database [record_id:2571]. It does not portray that development as inherently negative, but it places it in the context of concerns about ecosystem coherence.

This theme complements record 64’s concern with decision quality. If defenders already struggle to interpret CVSS, EPSS, SSVC, KEV lists, advisories, and local experience, then fragmentation in core vulnerability data sources may further complicate prioritization [record_id:64] [record_id:2571].

### 5. Humor and provocation as a communication style

The Black Hat abstract uses deliberately colorful language: “tarot cards,” “entrails,” “monkey math,” “statistical black magicks,” “structured gut feelings,” “rolling a D20 saving throw vs exploitation,” and “astrology jokes” [record_id:64]. This suggests a talk style that uses humor and skepticism to invite debate about familiar but contested security practices.

That communication style matters because vulnerability scoring can be dry, bureaucratic, and compliance-heavy. The record’s rhetorical strategy appears designed to make the topic accessible and contentious, encouraging the audience to question assumptions rather than accept framework outputs as neutral truth [record_id:64].

The BSidesLV abstract is more formal and policy-oriented, but it also frames the topic through open questions: “What are the challenges facing the CVE Program?” “How should these be communicated to policymakers?” and “What are new governance models that should be considered?” [record_id:2571]. Across both records, the talks are framed less as final answers and more as invitations to debate.

## Methods, Tools, And Approaches Discussed

The records do not describe hands-on tools, code, or implementation workflows. Instead, they discuss institutional methods and decision-support approaches for vulnerability management.

### Comparative evaluation of scoring systems

Record 64 centers on comparing CVSS, EPSS, and SSVC against “the reality of how security teams actually handle vulnerabilities” [record_id:64]. The abstract says the talk will explore “where these models help, where they mislead,” and whether any are meaningfully better than chance-like or game-like decision-making, expressed humorously as “rolling a D20 saving throw vs exploitation” [record_id:64].

The approach implied is comparative and critical:

- Examine each scoring or decision framework.
- Identify its strengths and weaknesses.
- Compare model outputs or assumptions to operational practice.
- Evaluate whether the framework improves decisions or merely rationalizes them.

The talk appears to treat vulnerability prioritization as both a measurement problem and a sociotechnical decision problem [record_id:64].

### Use of multiple risk signals

The Black Hat abstract identifies several practical inputs defenders use:

- CVSS.
- EPSS.
- SSVC.
- KEV lists.
- Vendor advisories.
- Lived experience [record_id:64].

This indicates an approach in which vulnerability management depends on signal fusion rather than one authoritative source. Security teams “mix and match shortcuts” to determine urgency [record_id:64]. The phrase “shortcuts” is notable: it implies that actual practice involves heuristics under time pressure, not purely formal analysis.

### Governance-model analysis

Record 2571 focuses on governance questions around the CVE Program. It asks what “new governance models” should be considered [record_id:2571]. Although the abstract does not enumerate those models, it clearly positions governance design as a method for preserving or improving vulnerability infrastructure.

The session’s approach appears to include:

- Assessing challenges facing the CVE Program.
- Considering communication strategies for policymakers.
- Evaluating how to maintain critical functions.
- Avoiding fragmentation.
- Considering alternative governance models [record_id:2571].

### Policy communication

The BSidesLV record explicitly raises the question of how challenges should be “communicated to policymakers” [record_id:2571]. This is an approach rather than a tool: vulnerability infrastructure sustainability depends not only on technical merit but also on effective explanation to funders, auditors, legislators, and public institutions.

The record’s mention of congressional audit interest reinforces that vulnerability management infrastructure is now within the policy oversight domain [record_id:2571].

## Notable Talks, Records, And Evidence

### “Vulnerability Haruspicy: Picking Out Risk Signals from Scoring System Entrails” — Black Hat USA 2025

Record 64 is the most direct evidence of Beardsley-associated work on vulnerability scoring and risk prioritization. It is notable because it challenges the credibility and usefulness of major vulnerability scoring systems while acknowledging that defenders need some way to prioritize risk [record_id:64].

The abstract’s key contribution is not a new scoring model, but a critical synthesis of existing models and real-world defender behavior. It frames CVSS, EPSS, and SSVC as imperfect attempts to impose order on vulnerability chaos [record_id:64]. It also recognizes that teams supplement formal frameworks with KEV lists, vendor advisories, and experience [record_id:64].

This record matters because it captures a mature vulnerability-management concern: the field has many signals, but not necessarily clear evidence that those signals produce better decisions. The talk’s central question — whether teams are improving risk decisions or just justifying preexisting preferences — is highly relevant to governance, compliance, and operational security [record_id:64].

### “What Should CVE Be When It Grows Up?” — BSidesLV 2025

Record 2571 is notable as a co-speaker or panel record involving Tod Beardsley alongside Jerry Gamblin, Madison Oliver, Bob Lord, and Chris Butera. It concerns the future of the CVE Program and its role in the cybersecurity ecosystem [record_id:2571].

The abstract emphasizes that CVE has served for more than a quarter century as an authoritative source of vulnerability data and supports secure design and development processes [record_id:2571]. It then places CVE in a period of stress: funding challenges for both CVE and NVD, creation of the EU Vulnerability Database, congressional attention, and a formal audit request [record_id:2571].

This record matters because it broadens the topic from scoring individual vulnerabilities to sustaining the systems that make vulnerability identification and coordination possible. It points downstream researchers toward questions of institutional resilience, international coordination, and governance reform [record_id:2571].

### Relationship between the two records

Taken together, the records