# Topic: Author: Or Eshed

## Executive Summary

The two available records attributed to Or Eshed are both BSidesLV 2025 PasswordsCon talks focused on password exposure risks in modern identity environments. Together, they frame password insecurity as a problem that has moved beyond traditional corporate account governance. One talk examines “hidden” identities: non-corporate, non-SSO, SaaS-related accounts that may be used for work but fall outside organizational identity provider controls and password policies [record_id:2418]. The other examines malicious or compromised browser extensions as a practical mechanism for stealing passwords and authentication data from users [record_id:2438].

Across the records, Eshed’s recurring contribution appears to be expanding the password-security threat model into under-governed or client-side spaces: identities not visible to centralized identity security systems, and browser extensions operating close to user credentials. Both talks combine threat-surface definition, technical or risk analysis, and defensive guidance. The evidence base is narrow—only two abstracts from the same event and year—but coherent: Eshed’s BSidesLV 2025 work emphasizes the gap between formal identity-security programs and the realities of SaaS usage, browser-mediated authentication, credential reuse, password sharing, and credential theft.

## Research Landscape

The available corpus consists of two conference-session abstracts from BSidesLV 2025, both tagged under PasswordsCon and both attributed to Or Eshed. They are not full papers, slide decks, or transcripts; therefore, the records provide strong evidence of topic selection and talk framing, but limited evidence about detailed empirical findings, measurements, datasets, or implementation specifics.

Both records sit at the intersection of identity security, application security, and password governance. The first record, “Cracking Hidden Identities: Understanding the Threat Surface of Hidden Identities and Protecting them Against Password Exposure,” is primarily about non-corporate and non-SSO identities that are used for work activity yet remain outside corporate identity-provider enforcement [record_id:2418]. The second, “Extending Password (in)Security to the Browser: How Malicious Browser Extensions Are Used to Steal User Passwords,” shifts the focus from identity governance gaps to browser-extension abuse as an endpoint and application-layer credential-theft vector [record_id:2438].

The research area represented by these talks is therefore not password cracking in the narrow sense of offline hash attacks, but broader password exposure in modern work environments. The records emphasize:

- SaaS-driven proliferation of accounts outside corporate identity policy [record_id:2418].
- Non-SSO and non-corporate identities as a hidden attack surface [record_id:2418].
- Password strength, reuse, and sharing risks in unmanaged identity contexts [record_id:2418].
- Browser extensions as an emerging vector for credential and authentication-data theft [record_id:2438].
- Extension permissions, compromise pathways, and technical methods used to steal credentials [record_id:2438].
- Organizational and individual defensive practices [record_id:2418; record_id:2438].

Because both records are abstracts from the same conference, they likely represent a concentrated snapshot of Eshed’s 2025 speaking agenda rather than a comprehensive author bibliography.

## Major Themes And Trends

### 1. Password risk outside traditional identity governance

A central theme across the records is that password security cannot be confined to accounts governed by corporate identity providers, single sign-on, or formal security policies. In the “hidden identities” talk, Eshed explicitly identifies the “SaaS economy” as producing “non-corporate and non-SSO identities” that are “not covered by corporate IdPs” [record_id:2418]. The concern is that these identities may still be used for work and may process or access sensitive corporate information, even though they fall outside conventional controls [record_id:2418].

This framing suggests a broader trend: enterprise identity programs may appear mature when measured through managed accounts, but the practical work environment includes identities created and used beyond those systems. The record characterizes these identities as “hidden from organizational security systems” and outside the “purview of organizational password policies and identity security posture” [record_id:2418]. That language points to a visibility and governance problem as much as a password-complexity problem.

### 2. Credential exposure through unmanaged SaaS and browser ecosystems

The two talks cover different parts of the same extended credential-exposure chain. The hidden-identities talk focuses on the account layer: identities that exist outside organizational control and may have weak, reused, or shared passwords [record_id:2418]. The browser-extension talk focuses on the client-side collection layer: extensions that can steal passwords and authentication details from users [record_id:2438].

Together, they suggest a modern password threat surface shaped by SaaS adoption and browser-based workflows. SaaS accounts create more credential-bearing surfaces; browsers become the interface through which those credentials are entered, stored, managed, or intercepted. Browser extensions, according to the second abstract, can be “used for theft of credential data” and can steal “passwords and other authentication details” through specific permissions and methods [record_id:2438]. This complements the first talk’s concern that unmanaged accounts may be especially vulnerable to password reuse, sharing, and weak governance [record_id:2418].

### 3. Visibility gaps as a root cause

Both talks implicitly or explicitly address visibility. Hidden identities are a visibility problem because organizations may not know the accounts exist or may not enforce policy over them [record_id:2418]. Malicious browser extensions are also a visibility and control problem because they may become compromised, request or abuse permissions, and operate in the browser context where credentials are handled [record_id:2438].

In the hidden-identities abstract, the accounts are described as “hidden from organizational security systems” [record_id:2418]. In the browser-extension abstract, the session promises to analyze “what permissions and methods compromised extensions invoke to steal passwords and other authentication details” [record_id:2438]. Both records therefore point toward the need to discover and monitor areas of identity risk that may sit outside standard identity and access management dashboards.

### 4. Password reuse, sharing, and strength remain relevant, but in new contexts

The hidden-identities record directly names password strength, password reuse, and password sharing as specific risks [record_id:2418]. The significance is not merely that these risks exist, but that they apply to accounts outside the reach of corporate enforcement. Even if an organization has password rules, SSO, MFA, or identity-security posture management for official accounts, those protections may not apply to non-corporate SaaS identities [record_id:2418].

The browser-extension record does not emphasize reuse or strength directly, but it does describe credential theft from the browser, which can defeat even relatively strong passwords if credentials or authentication details are captured at the point of use [record_id:2438]. This broadens the discussion from “are passwords strong enough?” to “where are passwords used, stored, entered, synchronized, exposed, or intercepted?”

### 5. Defensive guidance is a recurring endpoint

Both abstracts conclude with protective methods or best practices. The hidden-identities talk promises “methods and best practices on how to secure” non-corporate and non-SSO identities [record_id:2418]. The browser-extension talk likewise promises “best practices and methods” for how individuals and organizations should protect themselves against malicious-extension tactics [record_id:2438].

The records do not provide the actual recommendations in detail, but the repetition is notable: Eshed’s talks appear structured to move from threat-surface definition, to risk or technical analysis, to practical defense. For downstream researchers, this suggests that full slides or recordings, if available, may contain actionable controls around SaaS identity discovery, password policy extension, extension permission review, browser hardening, and credential-theft monitoring.

## Methods, Tools, And Approaches Discussed

The records are abstracts, so they summarize intended content rather than giving full technical procedures. Still, several methods and approaches are identifiable.

### Defining and quantifying hidden identities

The hidden-identities talk states that it will “define these identities” and “quantify them” [record_id:2418]. This implies an approach that begins with taxonomy and measurement: distinguishing corporate/SSO-managed identities from non-corporate/non-SSO identities, then estimating their prevalence or risk exposure. The abstract does not reveal the data source or methodology for quantification, but the inclusion of quantification suggests the talk may contain empirical or semi-empirical analysis rather than purely conceptual warning [record_id:2418].

### Risk analysis of password strength, reuse, and sharing

The same talk promises to “dive into specific risks such as password strength, password re-use, and password sharing” [record_id:2418]. These are classic password-security categories, but the method is applied to hidden SaaS or non-SSO identities. A likely analytical structure is to examine how unmanaged identities differ from managed corporate accounts in password policy enforcement, credential reuse likelihood, and shared-account practices. The record does not provide findings or metrics, so downstream agents should seek the full talk materials before making quantitative claims.

### Technical analysis of browser-extension permissions

The browser-extension talk explicitly promises “a technical analysis of what permissions and methods compromised extensions invoke to steal passwords and other authentication details” [record_id:2438]. This indicates a method centered on extension permission models and abuse patterns. Browser extensions often operate through declared permissions, content scripts, background scripts, access to web pages, or API capabilities; however, those details are not specified in the record, so they should not be attributed to Eshed without additional evidence. What can be safely said is that the talk focuses on permissions and methods used by compromised extensions for credential theft [record_id:2438].

### Compromise-pathway analysis

The browser-extension abstract says the session will discuss “how they become compromised” [record_id:2438]. This suggests a lifecycle view of malicious extensions: not only purpose-built malicious add-ons, but also benign extensions that become compromised. The record does not detail whether compromise occurs through developer account takeover, supply-chain acquisition, malicious updates, dependency abuse, or other means. The abstract supports only the broader claim that extension compromise pathways are part of the presentation [record_id:2438].

### Live examples and practical demonstrations

The browser-extension talk states that it will “show live examples” [record_id:2438]. This is important evidence about the talk format: it likely includes demonstrations of credential theft or extension behavior, not merely conceptual discussion. The abstract does not identify the extensions, browsers, code samples, or test environment. Still, live examples make this record the more explicitly technical and demonstrative of the two [record_id:2438].

### Best-practice-oriented mitigation

Both talks include a defensive component. The hidden-identities talk offers “methods and best practices” for securing hidden identities [record_id:2418]. The browser-extension talk discusses best practices for individuals and organizations to protect against malicious-extension tactics [record_id:2438]. The abstracts do not enumerate controls, but they imply that Eshed’s work is aimed at practitioner audiences seeking mitigations, not solely at academic threat characterization.

## Notable Talks, Records, And Evidence

### “Cracking Hidden Identities” and the unmanaged identity problem

“Cracking Hidden Identities: Understanding the Threat Surface of Hidden Identities and Protecting them Against Password Exposure” is the clearest record for Eshed’s thinking on identity governance gaps caused by SaaS adoption [record_id:2418]. Its central claim is that the rise of the “SaaS economy” has led to more non-corporate and non-SSO identities, which are not covered by corporate identity providers and therefore may not be governed by corporate password policies [record_id:2418].

This talk matters because it reframes password exposure as an organizational blind spot. The abstract argues that these identities are often used for work activity and may handle sensitive corporate information, even though they are outside organizational identity-security systems [record_id:2418]. It also identifies concrete risk categories: password strength, reuse, and sharing [record_id:2418]. For downstream research agents, this record is the primary evidence for Eshed’s contribution around “hidden identities” and SaaS-era password governance.

The evidence strength is moderate for topic and framing, but weak for details. The abstract says the talk will define and quantify hidden identities, but it does not provide the definitions, quantities, sample population, or measurement technique [record_id:2418]. Any detailed claims about prevalence or severity require the full talk.

### “Extending Password (in)Security to the Browser” and browser-extension credential theft

“Extending Password (in)Security to the Browser: How Malicious Browser Extensions Are Used to Steal User Passwords” is the more technical of the two records [record_id:2438]. It presents malicious browser extensions as an “emerging attack vector” for stealing identity information and passwords [record_id:2438]. The abstract promises a detailed breakdown of extension-based credential theft, including the permissions and methods used by compromised extensions, the types of password and credential data that can be stolen, and live examples [record_id:2438].

This talk matters because it connects password security to browser extension ecosystems and endpoint/browser security. It moves the password discussion from policy and governance into the browser execution environment, where extensions may be able to observe or manipulate authentication flows [record_id:2438]. It also emphasizes both individual and organizational defense, suggesting relevance for enterprise browser management, extension allowlisting or monitoring, and user-level hygiene, though the exact controls are not specified in the abstract [record_id:2438].

The evidence strength is strong for identifying the subject of the talk and the kinds of technical analysis promised, but weak for any specific implementation details. The record does not list actual permissions, attack code, examples, browsers, extension stores, or mitigations [record_id:2438].

## Gaps, Limits, And Open Questions

The records form a coherent but very small corpus. Several important limitations remain.

First, both records are abstracts from BSidesLV 2025, not full transcripts or technical papers. They indicate what the talks planned to cover but do not supply the actual findings, measurements, examples, or recommendations. For the hidden-identities talk, the abstract says Eshed will “define” and “