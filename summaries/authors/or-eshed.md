# Topic: Author: Or Eshed

## Executive Summary

The three records attributed to Or Eshed form a compact but coherent body of security work focused on identity exposure at the boundary between users, browsers, SaaS applications, and emerging agentic systems. Two BSidesLV 2025 talks focus on password and credential risk in modern browser- and SaaS-mediated work environments: hidden non-corporate/non-SSO identities that escape organizational identity governance, and malicious browser extensions that steal passwords and authentication details [record_id:2418] [record_id:2438]. A BSidesLV 2026 talk extends the browser-centered threat model into the AI era, arguing that agentic AI browsers can become exploitable autonomous actors or “autonomous insider threats” through both AI-specific attacks and traditional web exploitation techniques [record_id:2798].

Across the records, Eshed’s recurring contribution is to identify security blind spots created when user identity and browser-based workflows move outside conventional enterprise control planes. In 2025, the blind spot is unmanaged SaaS identities and compromised extensions; in 2026, it is AI-enabled browsers that no longer merely render content but take actions on behalf of users [record_id:2418] [record_id:2438] [record_id:2798]. The records suggest an evolution from password governance and credential theft toward broader browser-mediated exploitation, including prompt injection, memory poisoning, guardrail bypass, CSRF, font-based injection, and RCE in agentic browsing contexts [record_id:2798].

The evidence base is limited to three conference abstract-style records, all from BSidesLV, with no slides, papers, measurements, implementation details, or post-talk artifacts included. Nevertheless, the abstracts provide enough information to identify a consistent research agenda: understanding identity and credential exposure where enterprise identity providers, security policies, endpoint controls, and traditional web assumptions do not fully apply.

## Research Landscape

The records are conference talk descriptions from BSidesLV, spanning 2025 and 2026. They appear to be presentation abstracts rather than full research papers or technical writeups. Two talks are part of the BSidesLV 2025 program and tagged with PasswordsCon, indicating an emphasis on password security and credential exposure [record_id:2418] [record_id:2438]. The third is a BSidesLV 2026 talk tagged “[un]prompted,” placing it in an AI security and prompt-injection-oriented track [record_id:2798].

The landscape is dominated by identity security, password insecurity, browser security, and application security. The 2025 records focus on human and enterprise identity management gaps: non-corporate identities used for work but unmanaged by corporate identity providers, and browser extensions that can steal credential data [record_id:2418] [record_id:2438]. The 2026 record shifts into agentic AI browser security, but it remains strongly connected to the earlier browser and identity themes because it treats browsers as action-taking intermediaries that can be exploited to compromise user and organizational security [record_id:2798].

The overall research area is not traditional password cracking in isolation. Instead, it is about the changing threat surface around credentials and identity in modern workflows. The records highlight several environmental shifts:

- The rise of the “SaaS economy,” which creates non-corporate and non-SSO identities outside corporate IdP governance [record_id:2418].
- The browser as a privileged environment where extensions may access passwords, authentication details, or user identity information [record_id:2438].
- The transformation of browsers into AI-driven, agentic participants that can autonomously interact with web content and systems [record_id:2798].

Taken together, these records position Or Eshed’s work around a key question: what happens when identity-bearing user activity moves into systems that organizations do not fully inventory, govern, or constrain?

## Major Themes And Trends

### Hidden Identity Surfaces Outside Enterprise Governance

The strongest theme in the 2025 material is that enterprise identity programs often cover only part of the real identity surface. In the talk “Cracking Hidden Identities,” Eshed describes the rise of “non-corporate and non-SSO identities” created by the SaaS economy, emphasizing that these identities are “not covered by corporate IdPs” and are “hidden from organizational security systems” [record_id:2418]. The record frames these identities as a practical enterprise risk because they may still be used for work activity and may handle sensitive corporate information, despite being outside identity security policy and password governance [record_id:2418].

This theme broadens the meaning of identity security. Rather than focusing only on managed enterprise accounts, the talk asks whether unmanaged accounts used in business contexts should be treated as part of the organization’s security posture. The abstract indicates that Eshed intends to define and quantify these hidden identities, then analyze password strength, password reuse, and password sharing as specific risks [record_id:2418]. The implied trend is that SaaS decentralization has outpaced centralized identity governance.

### Password Exposure Through Browser-Centric Attack Surfaces

The second BSidesLV 2025 talk moves from unmanaged identities to browser extension compromise. “Extending Password (in)Security to the Browser” identifies malicious browser extensions as an “emerging attack vector” for stealing user identity information and passwords [record_id:2438]. The abstract promises a technical breakdown of how browser extensions steal credential data, including the permissions and methods compromised extensions invoke, the types of password and credential data that can be stolen, and live examples [record_id:2438].

This talk complements the hidden identities talk. If hidden SaaS accounts create unmanaged credentials, malicious extensions create a browser-resident mechanism for credential theft. Both talks treat passwords not merely as secrets stored in a vault or typed into a login page, but as artifacts exposed across workflows, browser features, application integrations, and user behavior [record_id:2418] [record_id:2438].

A recurring concern is that existing organizational controls may not see the full risk. Corporate identity providers may not govern non-SSO accounts [record_id:2418], while endpoint or browser management may not adequately prevent extension-based credential theft [record_id:2438]. The records therefore share a common structure: identify a modern convenience or productivity pattern, show how it escapes standard controls, then propose security practices to reduce exposure.

### The Browser Evolves From Passive Surface to Agentic Actor

The 2026 record marks a notable shift from conventional browser security to AI-enabled browser security. In “Abusing Agentic AI Browsers,” Eshed argues that AI browsers are transforming the browser “from a passive observer of the web into an active, agentic participant” [record_id:2798]. The key security claim is that this shift can turn AI browsers into “autonomous insider threats” when exploited [record_id:2798].

This is an important trend because it reframes the browser not just as an execution environment for web content or extensions, but as an actor capable of making decisions and taking actions. The record says the talk will examine building blocks and architectures for “LLM, SLM, and MCP-based deployments,” then demonstrate how each can be exploited and compromised [record_id:2798]. This suggests a systematic approach to comparing different agentic browser architectures and their respective attack surfaces.

The talk also links AI-native attacks with traditional web exploitation. The abstract lists prompt injection, bending guardrails, and AI memory poisoning alongside CSRF, font-based injections, and RCEs “that have been given new life by agentic browsers” [record_id:2798]. This creates a bridge between AI security and established application/browser exploitation: agentic browsing does not replace traditional web risk, but amplifies or recontextualizes it.

### Continuity Between Password Security and AI Browser Exploitation

Although the 2026 talk appears to belong to a different AI security track, it fits the broader pattern of Eshed’s records. All three talks concern trust boundaries around user-mediated access. In the 2025 password talks, the concern is that credentials and identities are exposed through unmanaged SaaS accounts or compromised browser extensions [record_id:2418] [record_id:2438]. In the 2026 AI browser talk, the concern is that agentic browsers may act with user authority and therefore become exploitable intermediaries [record_id:2798].

The trend across the records is a widening of the identity threat surface:

1. Accounts outside centralized identity governance create hidden password risks [record_id:2418].
2. Browser extensions can capture identity and authentication data from user browsing activity [record_id:2438].
3. AI browsers can be manipulated into autonomous action through both AI-specific and traditional web attacks [record_id:2798].

This progression suggests an authorial focus on how security assumptions fail when user access is mediated by increasingly complex browser and SaaS ecosystems.

## Methods, Tools, And Approaches Discussed

The records do not provide implementation details, code, datasets, or named tools, but they do describe several methodological approaches.

In the hidden identities talk, Eshed proposes to “define” and “quantify” non-corporate and non-SSO identities, then analyze their implications for password security and exploitation [record_id:2418]. The stated analytical dimensions include password strength, password reuse, and password sharing [record_id:2418]. This implies an approach grounded in identity inventory, measurement, and risk characterization. The talk also promises “methods and best practices” for securing these identities, though the abstract does not enumerate them [record_id:2418].

In the browser extension talk, the method is more technical and attack-analysis oriented. The session will break down how browser extensions can be used for credential theft, analyze the permissions and methods used by compromised extensions, examine how extensions become compromised, and explore the kinds of password and credential data that can be stolen [record_id:2438]. The inclusion of “live examples” indicates a demonstrative format, likely showing extension behavior or credential access patterns in practice, although the record does not specify exact examples or browser APIs [record_id:2438].

In the AI browser talk, the approach is explicitly exploit-based and architecture-aware. Eshed plans to examine the building blocks of AI browsers and key architectures for “LLM, SLM, and MCP-based deployments,” then systematically demonstrate exploitation and compromise pathways for each [record_id:2798]. The listed attack categories include:

- AI-specific attacks: prompt injection, guardrail bending, and AI memory poisoning [record_id:2798].
- Traditional exploitation pathways revived or intensified by agentic browsers: CSRF, font-based injections, and RCEs [record_id:2798].

The record’s phrase “exploit-based approach” and its emphasis on “real-life exploitation pathways” suggest a practical offensive-security framing rather than a purely conceptual AI safety discussion [record_id:2798]. It also suggests that the talk treats agentic AI browser security as a hybrid domain combining LLM threat modeling, browser architecture, web application security, and exploit chains.

Across the records, the repeated workflow is:

- Identify a newly important or overlooked identity/browser surface.
- Explain why existing organizational controls may not cover it.
- Analyze concrete mechanisms of exposure or compromise.
- Demonstrate or quantify the risk where possible.
- Offer best practices or defensive methods [record_id:2418] [record_id:2438] [record_id:2798].

## Notable Talks, Records, And Evidence

The most representative record for Eshed’s password and identity governance work is “Cracking Hidden Identities: Understanding the Threat Surface of Hidden Identities and Protecting them Against Password Exposure” from BSidesLV 2025 [record_id:2418]. Its importance lies in its framing of non-corporate and non-SSO identities as a hidden enterprise threat surface. The abstract explicitly links SaaS adoption to identities that are outside corporate IdPs, outside password policies, and outside identity security posture, yet still used for work and sensitive data handling [record_id:2418]. This is the clearest record for researchers interested in unmanaged identities, SaaS sprawl, password reuse, password sharing, and enterprise identity governance gaps.

The most representative record for Eshed’s browser credential-theft work is “Extending Password (in)Security to the Browser: How Malicious Browser Extensions Are Used to Steal User Passwords,” also from BSidesLV 2025 [record_id:2438]. It matters because it identifies malicious browser extensions as an emerging vector for theft of passwords and user identity information, and it promises technical analysis of permissions, methods, compromise routes, stolen credential types, and live examples [record_id:2438]. For downstream researchers, this record is the strongest evidence that Eshed’s work includes browser extension security and credential exfiltration mechanisms.

The most forward-looking record is “Abusing Agentic AI Browsers: An Exploit-Based Approach” from BSidesLV 2026 [record_id:2798]. It expands the browser-security theme into AI security by treating agentic AI browsers as systems that can be exploited and compromised. The record is notable for combining AI-specific attack vectors—prompt injection, guardrail bending, AI memory poisoning—with traditional exploitation pathways such as CSRF, font-based injections, and RCE [record_id:2798]. It is also the only record that mentions AI browser architectures, specifically LLM, SLM, and MCP-based deployments [record_id:2798].

Together, these three talks show a progression from password exposure in unmanaged identity contexts, to browser-mediated credential theft, to AI browser exploitation. The evidence is strong for identifying the topics Eshed presents on, but weaker for evaluating empirical results, novelty, or technical validity because the records are abstracts rather than full artifacts.

## Gaps, Limits, And Open Questions

The main limitation is that the corpus contains only three records, all conference abstracts. There are no transcripts, slide decks, videos, code repositories, datasets, measurement results, or post-event writeups included. As a result, the records reveal what the talks claim to cover, but not what evidence was ultimately presented.

For the hidden identities talk, important unanswered questions include how non-corporate and non-SSO identities are detected, what data sources are used to quantify them, how password strength or reuse is measured, and what defensive controls are recommended beyond general “methods and best practices” [record_id:2418].