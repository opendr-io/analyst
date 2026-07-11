# Topic: Author: Dwayne McDaniel

## Executive Summary

The available records attributed to Dwayne McDaniel consist of two BSidesLV 2025 PasswordsCon talks focused on non-human identity, workload/application authentication, secrets, governance, and the risks of relying on long-lived credentials. Together, they portray McDaniel’s 2025 work as centered on a specific but increasingly important identity-security problem: machines, services, bots, automation, and workloads are becoming core actors in enterprise environments, yet many organizations still manage them using legacy credential patterns designed around static secrets and implicit trust.

Across the two records, McDaniel emphasizes that traditional credential security is insufficient for the current scale and risk profile of non-human identities. One talk frames the issue conceptually, asking what would happen if application and workload identity were rethought rather than continuing to depend on long-lived credentials [record_id:2468]. The other expands the issue into governance, developer awareness, OWASP guidance, IAM, shadow IT, and AI-driven automation, arguing that non-human identities now outnumber humans “by at least 45 to 1” and have become a major attacker target [record_id:2572].

The strongest recurring theme is a shift from secrets management alone toward broader non-human identity governance. The records suggest McDaniel’s contribution is not merely technical guidance about protecting tokens or credentials, but a call for organizational change: developers, security teams, IAM owners, and governance stakeholders all need a shared model for identifying, prioritizing, and managing non-human identity risk [record_id:2572].

## Research Landscape

The corpus is small: two records, both from BSidesLV 2025, both tagged as PasswordsCon sessions, and both attributed to Dwayne McDaniel. The records are talk abstracts rather than full papers, transcripts, slides, or technical walkthroughs. As a result, the evidence is directional and thematic rather than deeply empirical. It reveals what McDaniel planned to discuss and how the talks were positioned, but it does not provide detailed implementation recommendations, case studies, data sources, or step-by-step methods.

Both records sit in the identity and access-management space. The first, “I’m A Machine, And You Should Trust Me: The Future Of Non-Human Identity,” is categorized primarily under identity, OAuth, and access delegation, with secondary relevance to cloud, infrastructure, and cloud detection/response [record_id:2468]. Its abstract is brief and conceptual, focusing on the shared flawed pattern of trusting humans and machines through long-lived credentials [record_id:2468].

The second, “What to Tell Your Developers About NHI Secrets Security and Governance,” is also primarily tied to identity, OAuth, and access delegation, but its secondary topics include governance, risk, compliance, and application security [record_id:2572]. It is more detailed and operationally oriented than the first record. It mentions service accounts, bots, automation, tokens, credentials, OWASP Top 10 Non-Human Identity Risks, shadow IT, AI-powered automation, IAM, developer education, and organization-wide governance [record_id:2572].

The overall research area represented by these records is therefore non-human identity security, especially as it intersects with secrets, IAM, workload identity, developer practices, and governance. The talks appear to be designed for a security conference audience but with an emphasis on communicating risk and remediation priorities to developers and broader organizational stakeholders.

## Major Themes And Trends

### 1. Long-lived credentials as a foundational security weakness

Both records criticize the continued dependence on long-lived credentials. In the first talk, McDaniel frames “a lot of security” as boiling down to trusting humans and machines to access resources using “the same flawed pattern: long-lived credentials” [record_id:2468]. This is the clearest shared premise across the corpus: static or durable credentials create a fragile trust model when used for both human and machine access.

The second record reinforces this concern by noting that attackers exploit “blind trust in tokens and credentials every day” [record_id:2572]. The phrase “blind trust” is important because it suggests the issue is not only that credentials leak, but that systems often treat possession of a token or secret as sufficient proof of legitimacy. That has implications for secrets management, runtime identity verification, authorization scoping, credential rotation, and detection.

Together, the records point toward a trend in McDaniel’s work: moving away from treating credentials as isolated artifacts to be stored securely and toward treating identity itself as dynamic, governed, and risk-assessed.

### 2. Non-human identities as a rapidly expanding attack surface

The second record makes the scale claim explicit: “Non-Human Identities (NHIs) like service accounts, bots, and automation now outnumber humans by at least 45 to 1” [record_id:2572]. This statistic is presented as evidence that machine identities are no longer a niche operational concern; they are a dominant part of the identity landscape.

The first record’s title and abstract also point to machine identity as a future-facing issue: “I’m A Machine, And You Should Trust Me” and the question of rethinking application and workload identity [record_id:2468]. The corpus therefore presents NHIs as both a current risk and a future architectural challenge.

A key trend is proliferation. Service accounts, bots, automation, and workloads are multiplying across modern environments, especially as cloud infrastructure, CI/CD pipelines, SaaS integrations, and automated operations expand. The second record adds that “shadow IT and AI-powered automation are accelerating the problem” [record_id:2572]. That line broadens the issue from managed infrastructure to unmanaged or semi-managed automation, where identities may be created outside formal governance channels.

### 3. Secrets security is necessary but not sufficient

The second talk’s title explicitly combines “NHI Secrets Security and Governance,” but the abstract warns that “simply securing secrets is not enough” [record_id:2572]. This distinction is central. McDaniel appears to be drawing a boundary between traditional secrets management—finding, storing, rotating, and protecting credentials—and a more comprehensive approach to identity governance.

This theme complements the first record’s question: “What if we rethought application and workload ‘identity’?” [record_id:2468]. If long-lived credentials are the flawed pattern, then the answer cannot be limited to better vaulting of those credentials. The records collectively suggest that organizations need to rethink how machines prove identity, how privileges are granted, how trust is evaluated, and how identity lifecycle is governed.

### 4. Governance and IAM as organizational rather than purely technical concerns

The governance emphasis is strongest in the second record. McDaniel describes NHI security as an “urgent, organization-wide challenge that goes far beyond IT” [record_id:2572]. He also argues that “strong identity governance and access management (IAM)” are essential as shadow IT and AI-powered automation accelerate the problem [record_id:2572].

This framing matters because it positions developers not just as consumers of security rules, but as participants in governance. The abstract says developers need to understand the risks, leverage best practices, and advocate for a holistic approach to NHI security [record_id:2572]. In other words, McDaniel’s talk appears to bridge security awareness, developer enablement, governance policy, and technical IAM controls.

### 5. Emerging standardization through OWASP NHI guidance

The second record references “the release of the OWASP Top 10 Non-Human Identity Risks in 2025” as providing “clear guidance on where the biggest threats lie and how to prioritize remediation” [record_id:2572]. This is significant because it situates McDaniel’s talk in a broader industry moment: NHI risk is being formalized into named categories and prioritized lists, similar to other OWASP risk frameworks.

The record also states that “OWASP isn’t alone” and that industry experts agree NHI security is urgent [record_id:2572]. Although the abstract does not name those experts or provide sources beyond OWASP, it signals a broader consensus trend that downstream researchers may want to investigate.

### 6. Developer education as a lever for reducing NHI risk

The second talk is explicitly framed around “What to Tell Your Developers” [record_id:2572]. This suggests McDaniel’s contribution is partly translational: converting non-human identity risk into guidance that developers can understand and apply.

The abstract stresses that developers should “understand the risks,” “leverage the latest best practices,” and “advocate for a holistic approach to NHI security” [record_id:2572]. This is not merely a security-team message. It implies that developers create, configure, embed, and operate many NHIs and therefore must be part of remediation.

The first record does not mention developers directly, but it concerns application and workload identity [record_id:2468], which are areas closely tied to development and platform engineering. Together, the talks appear to target both strategic identity rethinking and practical developer-facing governance.

## Methods, Tools, And Approaches Discussed

Because the records are abstracts, they do not provide detailed tool demonstrations or implementation recipes. However, several approaches are identifiable.

First, McDaniel appears to advocate rethinking application and workload identity away from long-lived credentials [record_id:2468]. The abstract does not specify alternatives such as short-lived tokens, workload identity federation, SPIFFE/SPIRE, cloud-native identity, mutual TLS, just-in-time access, or certificate-based identity, so those should not be attributed directly to the record. What can be said is that the talk frames long-lived credentials as flawed and proposes reconsidering the identity model for applications and workloads [record_id:2468].

Second, the records discuss secrets security as part of, but not equivalent to, non-human identity security. The second record says that “simply securing secrets is not enough” because attackers exploit blind trust in tokens and credentials [record_id:2572]. This implies an approach that includes governance, risk prioritization, and access management in addition to secrets protection.

Third, McDaniel’s developer-focused talk references the OWASP Top 10 Non-Human Identity Risks in 2025 as a prioritization framework [record_id:2572]. The method here is risk-based remediation: using a recognized taxonomy to identify the biggest threats and prioritize action. The record does not enumerate the OWASP categories, but it clearly presents OWASP as a source of “clear guidance” [record_id:2572].

Fourth, the second record emphasizes identity governance and access management. “Strong identity governance and access management (IAM)” is presented as essential for controlling NHI proliferation, especially under pressure from shadow IT and AI-powered automation [record_id:2572]. This suggests lifecycle controls, accountability, inventory, ownership, policy enforcement, and access governance as likely areas of concern, though the abstract does not spell out a full governance model.

Fifth, the records point to awareness-building and cross-team governance as an approach. McDaniel argues that by “raising awareness and driving governance across teams,” organizations can “start to control the chaos” as NHIs proliferate [record_id:2572]. This is a social and organizational method, not just a technical one: it involves communication to developers, shared responsibility, and policy alignment across teams.

## Notable Talks, Records, And Evidence

The first record, “I’m A Machine, And You Should Trust Me: The Future Of Non-Human Identity,” is notable because it provides the conceptual foundation for McDaniel’s treatment of the topic [record_id:2468]. Its abstract is short but direct: it identifies long-lived credentials as a common flawed pattern for both human and machine access and asks whether application and workload identity should be rethought [record_id:2468]. This talk appears to be forward-looking and architectural, asking how trust should work for machines rather than merely how existing secrets should be stored.

The second record, “What to Tell Your Developers About NHI Secrets Security and Governance,” is the richer evidence source and the more practical of the two [record_id:2572]. It names specific NHI examples—service accounts, bots, and automation—and states that NHIs outnumber humans by at least 45 to 1 [record_id:2572]. It also identifies attackers’ exploitation of tokens and credentials, the inadequacy of secrets-only approaches, the emergence of OWASP Top 10 Non-Human Identity Risks in 2025, the acceleration caused by shadow IT and AI-powered automation, and the need for strong IAM and organization-wide governance [record_id:2572].

Together, these two talks form a coherent mini-series or paired treatment of the same problem. The first appears to ask the foundational identity question: how should machines be trusted? [record_id:2468]. The second appears to translate that concern into guidance for developers and governance stakeholders: what risks should they understand, what frameworks should they use, and why does the problem require organization-wide action? [record_id:2572].

The evidence is strongest for McDaniel’s emphasis on non-human identity as an urgent and growing identity-security domain. It is also strong for his critique of long-lived credentials and secrets-only thinking, because those points are explicit in both records [record_id:2468] [record_id:2572]. The evidence is thinner for specific implementation prescriptions, because neither record provides technical steps, architecture diagrams, or named tools beyond OWASP guidance and IAM as a category [record_id:2572].

## Gaps, Limits, And Open Questions

The main limitation is the small corpus size. Only two records are available, both from the same event and year. This makes it difficult to assess McDaniel’s broader body of work, historical evolution, recurring talks over time, or whether his 2025 focus on NHI reflects a longer-term specialization.

The records are also abstracts, not full talks. They do not include speaker notes, slides, audience Q&A, demos, references, or detailed examples. As a result, downstream researchers should avoid overclaiming about specific technologies or frameworks that are not named in the raw text.

Several open questions remain:

- What concrete alternatives to long-lived credentials did McDaniel recommend in the “Future Of Non-Human Identity” talk? The abstract raises the question of rethinking application and workload identity but does not specify the proposed model [record_id:2468].
- Which exact OWASP Top 10 Non-Human Identity Risks did McDaniel prioritize, and