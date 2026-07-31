# Topic: Election security

## Meta-Summary

The records present election security as both a technical problem and a problem of public proof, institutional coordination, and trust. The collection pairs a brief introduction to DEF CON’s Voting Village and symposium—indicating a community forum focused on election-security research—with a detailed description of a county pilot intended to improve voter-roll integrity through open-source tools, distributed custody, public participation, tamper evidence, and alignment with Center for Internet Security Controls [record_id:1863] [record_id:2745].

The strongest substantive theme is that merely asserting that election systems are secure is insufficient. The pilot described in the BSidesLV record seeks security properties that can be made visible and persuasive to losing candidates and a skeptical public. At the same time, the evidence is limited: the records do not provide technical specifications, evaluation results, attack findings, or independent validation.

## Research Landscape

This is a very small collection of two event records from security conferences in 2025 and 2026. One comes from DEF CON 33 and serves only as an introduction to the Voting Village and its symposium [record_id:1863]. Its inclusion shows that election security is being treated as a dedicated research and practitioner domain within a major hacker conference, but the raw text contains no substantive description of particular voting technologies, vulnerabilities, or research findings.

The second record is a BSidesLV talk abstract centered on a real-world county pilot for voter-roll integrity in an unnamed American swing state [record_id:2745]. It dominates the available evidence. The talk frames election security broadly: not just as protection against technical compromise, but as a combination of operational controls, public transparency, tamper evidence, integration with incumbent vendor systems, legal compliance, and the ability to demonstrate security to politically distrustful audiences.

The resulting research landscape is weighted toward governance and operational architecture rather than machine-level analysis. Despite the topic’s broader scope, these records do not substantively discuss voting machines, ballot-marking devices, tabulators, paper ballots, risk-limiting audits, internet voting, cryptographic voting protocols, or certification testing. The collection instead emphasizes community engagement and voter-roll assurance.

## Major Themes And Trends

### Security must be demonstrable, not merely asserted

The most prominent idea is the need for “proof-of-security” that losing candidates and skeptical members of the public can understand or inspect. The BSidesLV abstract argues that election managers are expected to deliver secure elections even though concrete proof of whole-system security has been unavailable [record_id:2745]. This frames verifiability as a social and institutional requirement as much as a technical property.

The proposed response is to make tamper evidence immediately visible to the public and to expose aspects of the process to public scrutiny. The record suggests that transparency and observable controls might reduce the space in which conspiracy theories flourish [record_id:2745]. This is a claim made by the proposed talk, however, not an outcome demonstrated by evidence in the record.

### Open-source components within vendor-constrained environments

The pilot reportedly uses open-source tools but does not assume that jurisdictions can replace their existing election platforms wholesale. Instead, it integrates open-source components with existing vendor systems [record_id:2745]. That reflects a pragmatic trend: election administrators often operate within installed technology stacks, procurement arrangements, certification regimes, and statutory constraints. Improvements may therefore need to supplement rather than immediately displace incumbent systems.

The abstract is explicitly critical of vendor limitations, portraying election managers as boxed in by platforms that may not support all desired security properties [record_id:2745]. Yet it does not identify vendors, products, technical defects, or integration interfaces. The record supports the existence of an integration-oriented strategy, but not an assessment of its engineering quality or compatibility risks.

### Distributed custody and public participation

Distributed custody of records is a core architectural feature of the county pilot [record_id:2745]. Although the raw text does not define the custody model, the phrase implies an effort to avoid placing exclusive control or trust in a single official, organization, or system. This may support resilience and tamper detection, but the record does not explain who holds copies, how versions are reconciled, or how confidentiality and authorization are maintained.

The pilot also contemplates recruiting ordinary citizens as voter-roll auditors ahead of the 2026 midterm election [record_id:2745]. This extends participation beyond passive transparency: members of the public would apparently perform an auditing role. The approach may distribute oversight and make assurance more legible, but it also raises unanswered questions about auditor training, privacy, data access, error handling, partisan capture, and protection against harassment or misuse.

### Fragmented authority as a security constraint

The BSidesLV abstract describes election managers as accountable to multiple authorities without a unified agenda. It also claims that state and federal law can compel processes that threaten security [record_id:2745]. In this framing, election insecurity does not arise solely from vulnerable technology. It can also result from fragmented governance, conflicting mandates, constrained procurement, and legal requirements that administrators cannot independently change.

This institutional emphasis is important because it argues against purely technical remedies. Even a sound tool must fit statutory processes, vendor platforms, records-management requirements, and divided administrative authority. The abstract’s ambition to develop the pilot into a “full-system protocol” appears intended to address this broader environment [record_id:2745], although no protocol specification is supplied.

### Research communities and practitioner forums

The DEF CON Voting Village introduction demonstrates the continued presence of a specialized venue for election-security discussion within the security community [record_id:1863]. Because the raw text consists only of “Introduction to the Voting Village and the Symposium,” it cannot establish what technical issues were covered during the event. Nevertheless, it situates the topic within a recurring forum where researchers, officials, vendors, and other stakeholders may convene.

Across the two records, the visible trend is therefore toward connecting technical work with operational deployment and public legitimacy. The DEF CON record represents the community setting, while the BSidesLV record describes a particular attempt to implement security and transparency in a county environment [record_id:1863] [record_id:2745].

## Methods, Tools, And Approaches Discussed

The principal methods appear in the county voter-roll pilot described by Fred Mack. The pilot uses open-source tools to address voter-roll integrity while integrating them with existing proprietary vendor platforms [record_id:2745]. The record does not name the software, describe its license, or provide implementation details, so its security properties cannot be assessed from the abstract alone.

A second method is distributed custody of election-related records. This appears intended to make unilateral or concealed modification more difficult and to create evidence of tampering [record_id:2745]. The precise architecture remains unknown: the record does not say whether the approach uses replicated databases, signed snapshots, append-only logs, cryptographic commitments, independent repositories, or manual custody procedures.

The pilot further emphasizes “unprecedented public transparency” and tamper evidence that is instantly visible to the public [record_id:2745]. These are significant design goals because they target both integrity and public confidence. However, there is no explanation of what members of the public would inspect, how authenticity would be established, or whether the published evidence could reveal protected voter information.

Citizen auditing is another proposed workflow. Everyday citizens would be recruited as voter-roll auditors, potentially before the 2026 midterm election [record_id:2745]. The abstract does not specify whether auditors verify additions, removals, duplicate registrations, address changes, list maintenance, or record provenance. Nor does it define safeguards against erroneous challenges or privacy violations.

Finally, the program is said to be grounded in the Center for Internet Security Controls [record_id:2745]. This suggests the use of a general cybersecurity control framework to structure safeguards and operations. The record does not identify which controls were implemented, how they were tailored to election administration, or whether compliance was independently assessed. The claim is therefore evidence of a framework-based design approach, not proof of control effectiveness.

## Notable Talks, Records, And Evidence

The most important substantive record is “The Holy Grail of Election Security: Serious Quest or Theater of the Absurd?” at BSidesLV 2026 [record_id:2745]. It matters because it describes an allegedly real county deployment rather than a purely theoretical proposal. Its notable elements are:

- a focus on voter-roll integrity;
- use of open-source tools;
- integration with incumbent vendor platforms;
- distributed custody of records;
- public-facing tamper evidence;
- potential citizen participation in auditing;
- alignment with Center for Internet Security Controls; and
- an aspiration to develop the approach into a full-system protocol [record_id:2745].

The abstract also foregrounds practical obstacles: political conflict, legal constraints, vendor limitations, fragmented authority, and the challenge of persuading losing candidates and skeptical citizens [record_id:2745]. This makes it representative of election-security work that treats legitimacy and evidence communication as part of system design.

Its evidentiary strength is nevertheless modest. The raw text is promotional conference material for a previously unpublished story. It contains no measurements, threat model, incident data, architecture diagrams, audit results, or independent corroboration. Phrases such as “model for any jurisdiction” and claims that the pilot “answers the challenge” should be treated as the speaker’s assertions pending further evidence [record_id:2745].

The DEF CON 33 “Voting Village” record is notable primarily as evidence of venue and community organization [record_id:1863]. Its raw text only identifies an introduction to the Voting Village and symposium. It does not support conclusions about particular vulnerabilities, defenses, demonstrations, or policy positions. Its importance lies in documenting that election security remained a dedicated subject of security-community programming in 2025.

## Gaps, Limits, And Open Questions

The collection is too small to establish broad field-wide trends with confidence. Only one record contains substantive claims, and that record is an event abstract rather than a paper, technical report, demonstration transcript, or evaluation [record_id:2745]. The other is a one-line introductory description [record_id:1863].

Key unanswered technical questions about the pilot include:

- What exact voter-roll threats does it address: unauthorized alteration, accidental deletion, stale data, insider abuse, synchronization failures, or false eligibility challenges?
- What open-source tools are used, and have they undergone code review, penetration testing, reproducible builds, or supply-chain assessment?
- How is distributed custody implemented, and what threshold of custodians is needed to detect or resist tampering?
- What cryptographic or procedural mechanism makes tamper evidence publicly visible?
- How does the system distinguish malicious changes from authorized list-maintenance operations?
- How does it protect voter privacy while enabling public review?
- How are citizen auditors trained, authenticated, supervised, and held accountable?
- What happens when auditors disagree or submit erroneous findings?
- Which Center for Internet Security Controls were adopted, and what evidence demonstrates effective implementation?
- What are the costs, staffing needs, failure modes, and scalability limits for other jurisdictions?

The records also leave major portions of election technology unaddressed. There is no substantive treatment of ballot-marking devices, optical scanners, tabulation systems, election-management systems, electronic pollbooks, voting-system certification, software independence, post-election audits, ballot secrecy, accessibility, internet voting, end-to-end cryptographic verification, physical security, or incident response.

The connection between voter-roll security and election outcomes also requires careful analysis. Protecting registration records is important, but it is only one component of election integrity. The abstract’s ambition to become a “full-system protocol” is not accompanied by evidence that the pilot covers ballot generation, casting, tabulation, canvassing, certification, or recounts [record_id:2745].

There is also an unresolved tension between transparency and risk. Public access can improve accountability, but poorly designed publication can expose personal data, facilitate voter targeting, or encourage ungrounded challenges. Likewise, public tamper evidence may increase trust only if it is comprehensible, authenticated, and interpreted consistently. The records do not examine these tradeoffs.

Future research should seek the full BSidesLV presentation, implementation documentation, the participating jurisdiction’s perspective, architecture and threat-model materials, independent security reviews, and empirical results from the pilot. Researchers should also determine whether the contemplated citizen-auditor program was deployed for the 2026 midterm cycle and whether it measurably improved detection, operational security, or public confidence.

## Coverage And Evidence Notes

Both records are directly relevant to election security, but they differ sharply in substantive value.

The DEF CON 33 record documents an introduction to the Voting Village and symposium [record_id:1863]. It provides evidence that a dedicated election-security forum existed at the event, but nothing in the raw text supports claims about specific technologies, vulnerabilities, or research findings. It should be treated as contextual and logistical evidence.

The BSidesLV 2026 record provides nearly all of the collection’s technical and governance content [record_id:2745]. It describes a county voter-roll-integrity pilot built around open-source integration, distributed record custody, public transparency, citizen auditing, visible tamper evidence, and CIS Controls. Because the source is only a talk abstract and characterizes the story as previously unpublished, all performance and generalizability claims remain unverified. It is best used to identify an emerging operational model and associated research questions, not as conclusive evidence that the model is secure or effective.