# Topic: Author: Yuval Gordon

## Executive Summary

The two records attributed to Yuval Gordon describe the same 2025 talk delivered in two venues—DEF CON 33 and BSidesLV 2025—under nearly identical titles: “The UnRightful Heir / The (Un)Rightful Heir: My dMSA Is Your New Domain Admin” [record_id:1966] [record_id:2547]. Both records focus on a newly introduced Windows Server 2025 Active Directory feature, Delegated Managed Service Accounts, or dMSAs, and present an attack named **BadSuccessor** that abuses dMSAs to escalate privileges in Active Directory environments [record_id:1966] [record_id:2547].

The core contribution described across the records is the discovery and explanation of a privilege-escalation path in Active Directory involving dMSAs, Kerberos ticket issuance, and a “very common, and seemingly benign” Active Directory permission [record_id:1966] [record_id:2547]. The claimed impact is severe: an attacker can allegedly trick a Domain Controller into issuing a Kerberos ticket for any principal, including Domain Admins and Domain Controllers, and can extend the technique to obtain the NTLM hash of every user in the domain without directly touching the domain controller [record_id:1966] [record_id:2547].

The BSidesLV version adds a stronger practitioner-oriented framing: attendees are promised “detection tips, mitigation ideas,” and a broader lesson about obscure Active Directory attributes with outsized security consequences [record_id:2547]. The DEF CON record focuses more on attack mechanics, discovery process, and impact [record_id:1966]. Taken together, the records position Yuval Gordon’s contribution as research into emergent risks in Microsoft identity infrastructure, especially where new account types and delegation semantics interact with legacy Active Directory permissions and Kerberos behavior.

## Research Landscape

The available corpus is very small: only two records, both from 2025 security conference programs, and both apparently describing the same research presentation rather than separate publications or a body of diverse work [record_id:1966] [record_id:2547]. The sources are major hacker/security conference venues: DEF CON 33 and BSidesLV 2025. The topic therefore reflects conference-talk abstracts rather than full papers, code repositories, slide decks, advisories, or post-event transcripts.

The research area is Active Directory security, with emphasis on identity, access delegation, and exploit development. Both records place the work around Microsoft’s **Delegated Managed Service Accounts**, introduced in Windows Server 2025 as a feature intended to improve domain security [record_id:1966] [record_id:2547]. In both abstracts, the central tension is that a security feature designed to improve domain environments instead becomes a privilege-escalation primitive when combined with existing AD permissions and Kerberos issuance behavior [record_id:1966] [record_id:2547].

The records are not broad surveys of Yuval Gordon’s career or all publications. They document a specific research finding—BadSuccessor—and its presentation at two venues. Because the raw evidence is confined to abstracts, the corpus supports conclusions about the talk’s advertised subject matter, claimed attack impact, and intended audience takeaways, but not detailed validation of exploit reliability, patch status, proof-of-concept availability, vendor response, or real-world exploitation.

## Major Themes And Trends

### 1. New Identity Features Can Introduce Unexpected Privilege-Escalation Paths

The dominant theme is the security risk created when new identity-management features are added to mature enterprise ecosystems like Active Directory. Both records describe dMSAs as “Microsoft’s shiny new addition to Active Directory in Windows Server 2025” or “a new type of account introduced in Windows Server 2025,” with the stated purpose of improving domain security [record_id:1966] [record_id:2547]. The abstracts then immediately invert that premise: “As it turns out, that didn’t go so well” [record_id:1966] [record_id:2547].

This framing suggests Gordon’s work is less about a simple implementation bug and more about emergent behavior in a complex identity platform. dMSAs are presented as a defensive or administrative improvement, but the talk claims they can be abused to escalate privileges in Active Directory [record_id:1966] [record_id:2547]. The broader trend is familiar in enterprise identity security: new delegation or service-account mechanisms often inherit risk from old permission models, and the resulting attack surface may not be obvious to administrators.

### 2. Benign-Looking Active Directory Permissions Can Have Domain-Wide Consequences

A recurring concern across both records is that a “very common, and seemingly benign” AD permission can be leveraged in a way administrators may not expect [record_id:1966] [record_id:2547]. The exact permission is not named in the raw abstracts, but the described consequence is dramatic: it can allow an attacker to trick a Domain Controller into issuing a Kerberos ticket for any principal, including Domain Admins and Domain Controllers [record_id:1966] [record_id:2547].

This theme is important because it shifts attention from obviously dangerous privileges to permissions that may be widespread and underestimated. The BSidesLV abstract reinforces this lesson by stating that attendees will gain “a new appreciation for obscure AD attributes that can punch far above their weight” [record_id:2547]. That phrasing suggests the research highlights a mismatch between how defenders perceive certain AD attributes or permissions and the actual authority those attributes can confer in specific protocol flows.

### 3. The Attack Does Not Require Active Use of dMSAs by the Target Domain

One of the most notable claims in both records is that BadSuccessor works “even if your domain doesn’t use dMSAs at all” [record_id:1966] [record_id:2547]. This is a key theme because it broadens the potential affected population. If risk were limited to organizations actively deploying dMSAs, defenders could treat the issue as a feature-adoption problem. Instead, the abstracts imply that merely having an environment where the dMSA-related behavior exists may be enough, regardless of whether dMSAs are operationally used [record_id:1966] [record_id:2547].

For downstream researchers, this claim is one of the most important points to verify through external sources, technical details, and Microsoft guidance. It affects exposure assessment: administrators may otherwise assume that avoiding or delaying dMSA deployment eliminates risk.

### 4. Kerberos Abuse and Principal Impersonation Are Central to the Impact

Both records describe the attack in Kerberos terms. The stated capability is to trick a Domain Controller into issuing a Kerberos ticket for “any principal,” explicitly including Domain Admins and Domain Controllers [record_id:1966] [record_id:2547]. This places the research in the tradition of Active Directory attacks that exploit relationships among account attributes, delegation, ticket issuance, and privilege semantics.

The emphasis on tickets for arbitrary principals suggests the talk likely deals with impersonation, privilege escalation, or unauthorized service/account identity assertion. However, the abstracts do not provide enough detail to classify the precise Kerberos extension, attribute flow, or ticket type involved. The important evidence-supported conclusion is that the talk claims dMSA abuse can yield Kerberos tickets for highly privileged principals [record_id:1966] [record_id:2547].

### 5. Credential Exposure Beyond Direct Domain Controller Interaction

The records also claim that the technique can be extended to obtain the NTLM hash of every user in the domain “without ever touching the domain controller” [record_id:1966] [record_id:2547]. This is a second major impact beyond ticket issuance. It implies the attack may allow broad credential material access without the attacker needing to directly compromise or interact with the domain controller in the usual way.

The “without ever touching the domain controller” phrase is significant because many defensive strategies focus heavily on monitoring domain controllers for credential-dumping activity. If the described technique allows domain-wide NTLM hash acquisition while avoiding direct DC contact, it would challenge some common assumptions in detection and response [record_id:1966] [record_id:2547]. The BSidesLV record’s explicit mention of detection tips and mitigation ideas suggests the speaker intended to address this defensive implication [record_id:2547].

### 6. Movement from Attack Explanation Toward Defensive Guidance

The DEF CON abstract promises to “walk through how we found this attack, how it works, and its potential impact on AD environments” [record_id:1966]. The BSidesLV abstract includes the same core content but adds that attendees will leave with “detection tips, mitigation ideas” [record_id:2547]. This difference may reflect a venue-specific emphasis or an expanded version of the talk description.

Across the two records, the research appears to combine vulnerability discovery, exploit mechanics, and defender guidance. The evidence for detailed detection and mitigation content is strongest in the BSidesLV record because it explicitly names those takeaways [record_id:2547]. The DEF CON record supports an impact and mechanics framing but does not explicitly promise defensive recommendations [record_id:1966].

## Methods, Tools, And Approaches Discussed

The records do not provide implementation-level methodology, but they do identify several technical approaches and research activities.

First, both records introduce **BadSuccessor** as the named attack technique [record_id:1966] [record_id:2547]. The attack abuses Delegated Managed Service Accounts to escalate privileges in Active Directory [record_id:1966] [record_id:2547]. The name appears as plain text in the DEF CON record and with HTML emphasis in the BSidesLV record, but the substance is the same.

Second, the approach involves manipulating Active Directory permission and attribute semantics. Both abstracts say a common, seemingly benign permission can allow the attacker to trick a Domain Controller into issuing a Kerberos ticket for any principal [record_id:1966] [record_id:2547]. The BSidesLV abstract’s closing reference to “obscure AD attributes” suggests the talk likely explains which attributes are involved and why they are unexpectedly powerful [record_id:2547].

Third, the method centers on Kerberos ticket issuance. The described technique causes a Domain Controller to issue a Kerberos ticket for arbitrary principals, including highly privileged accounts such as Domain Admins and Domain Controllers [record_id:1966] [record_id:2547]. The records do not specify whether this involves service tickets, ticket-granting tickets, S4U flows, resource-based constrained delegation, or another Kerberos mechanism. Therefore, downstream agents should avoid over-classifying the technique based solely on these abstracts.

Fourth, the talk claims an additional path to obtaining NTLM hashes for all domain users without directly touching the domain controller [record_id:1966] [record_id:2547]. The records do not describe the exact workflow, toolchain, or protocol sequence for doing so. The claim is nevertheless central to the advertised impact.

Fifth, the talk includes a vulnerability-discovery narrative. Both records state that the speaker will explain “how we found this attack” [record_id:1966] [record_id:2547]. This implies a research method involving analysis of Windows Server 2025 Active Directory behavior, dMSA design, and permission interactions. However, no tooling, fuzzing method, reverse-engineering process, lab setup, or disclosure timeline is described in the raw text.

Finally, the BSidesLV record adds defensive methods: “detection tips” and “mitigation ideas” [record_id:2547]. These are not detailed in the abstract, but their mention indicates that the talk is not purely offensive. It likely aims to help defenders identify risky configurations, detect attack activity, or reduce exposure related to dMSA abuse and AD attributes [record_id:2547].

## Notable Talks, Records, And Evidence

The two records are best understood as separate conference listings for the same underlying research.

The DEF CON 33 record, titled “The UnRightful Heir My dMSA Is Your New Domain Admin,” presents BadSuccessor as an Active Directory privilege-escalation attack against Microsoft’s new dMSA feature in Windows Server 2025 [record_id:1966]. This record is notable because DEF CON is a major venue and because the abstract concisely lays out the core offensive claims: dMSA abuse, escalation even in domains not using dMSAs, Kerberos tickets for any principal, and NTLM hash access for every domain user without touching the domain controller [record_id:1966]. It also emphasizes the research process by promising to explain how the attack was found, how it works, and its potential impact [record_id:1966].

The BSidesLV 2025 record, titled “The (Un)Rightful Heir: My dMSA Is Your New Domain Admin,” is a closely matching abstract with some additional defender-focused language [record_id:2547]. It repeats the same core claims about dMSAs, BadSuccessor, arbitrary-principal Kerberos ticket issuance, and domain-wide NTLM hash access [record_id:2547]. Its distinctive contribution is the explicit promise that attendees will leave with “detection tips, mitigation ideas,” as well as an appreciation for obscure AD attributes with outsized impact [record_id:2547]. This makes the BSidesLV listing the stronger evidence for the talk’s operational security and blue-team relevance.

The evidentiary strength is high for identifying the talk topic and claimed impact because both records independently repeat nearly identical language [record_id:1966] [record_id:2547]. The strength is lower for technical specifics because both are abstracts rather than full technical writeups. The records do not include exploit code, diagrams, screenshots, defensive rules, affected build numbers, CVE references, vendor statements, or measured prevalence.

## Gaps, Limits, And Open Questions

The largest limitation is that the corpus contains only two abstracts for what appears to be the same talk. It does not provide a transcript, slide deck, demonstration details, post-publication blog, advisory, or independent analysis. As a result, the records establish the existence and advertised claims of the BadSuccessor research but do not fully substantiate the technical mechanism.

Several important open questions remain:

- **Precise vulnerable permission or attribute:** Both records mention a “very