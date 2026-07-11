# Topic: Author: Meghan Jacquot

## Executive Summary

The two records attributed to Meghan Jacquot present a compact but coherent picture of security work centered on **data exposure, privacy, and risk reduction**. One record is a DEF CON 33 workshop focused on personal privacy, public/private/secret information boundaries, OSINT-based footprint discovery, and obfuscation to reduce an individual’s exposed data surface [record_id:1969]. The other is a BSidesLV 2025 presentation, co-authored with Rafael Ayala, about third-party vendor cyber risk in the context of cloud and artificial intelligence adoption, emphasizing accessible vendor evaluation and onboarding frameworks to protect organizational data [record_id:2481].

Across both records, Jacquot’s work appears to connect two levels of security concern: the **individual privacy footprint** and the **organizational risk ecosystem**. The DEF CON workshop frames privacy as a practical, empowering activity: understand what is publicly discoverable about oneself, then take steps to reduce exposure [record_id:1969]. The BSidesLV talk shifts the scale from individuals to organizations, examining how external vendors can expand attack surfaces and introduce vulnerabilities, especially as cloud and AI adoption grows [record_id:2481]. Together, these records suggest recurring interests in **data access control, exposure reduction, practical education, and actionable frameworks**.

The evidence base is small—only two records, both from 2025 conference contexts—so conclusions about Jacquot’s broader body of work should remain cautious. Still, the available material indicates a consistent orientation toward **making security practices approachable** for attendees, practitioners, and contributors, whether through hands-on privacy work or familiar frameworks for third-party risk management.

## Research Landscape

The records consist of two conference-associated items from 2025:

- A **DEF CON 33 workshop** titled “Private, Private, Private Access Everywhere,” authored by Meghan Jacquot [record_id:1969].
- A **BSidesLV 2025 talk** titled “Let’s Go Shopping: Third-Party Vendors and CyberRisk,” authored by Meghan Jacquot and Rafael Ayala [record_id:2481].

Both records are talk or workshop abstracts rather than full transcripts, papers, slide decks, or detailed technical writeups. As a result, they provide strong evidence of **topics, framing, intended audience, and high-level methods**, but only limited evidence of specific procedures, implementation details, case studies, or empirical findings.

The research area represented by these records sits at the intersection of:

- **Privacy and data leakage** [record_id:1969]
- **Data loss detection and prevention** [record_id:1969]
- **Governance, risk, and compliance** [record_id:2481]
- **Third-party risk management** [record_id:2481]
- **Cloud, infrastructure, and AI-related attack surface expansion** [record_id:2481]

The DEF CON record is framed as a workshop, suggesting a hands-on educational format. It explicitly says attendees should bring a device and be ready to work on “becoming more private,” indicating practical exercises rather than a purely conceptual lecture [record_id:1969]. The BSidesLV record is framed as a presentation and emphasizes an “accessible and familiar framework” for evaluating and onboarding vendors, suggesting an applied governance/risk-management orientation [record_id:2481].

Overall, the landscape is not dominated by exploit development, malware analysis, vulnerability research, or offensive security tooling. Instead, it is dominated by **exposure management**: reducing what can be accessed about individuals and reducing what can go wrong through organizational dependency on third parties.

## Major Themes And Trends

### 1. Data exposure as a central security problem

Both records focus on situations where sensitive or important information may become accessible to unintended parties. In the DEF CON workshop, the concern is direct and personal: if “all of your data is public,” then “anyone can access everything everywhere” [record_id:1969]. The workshop’s goal is to reduce that exposure by examining an individual’s footprint and applying obfuscation techniques [record_id:1969].

In the BSidesLV talk, the exposure problem is organizational rather than personal. As organizations adopt cloud technologies and artificial intelligence, the abstract argues that the “attack surface expands,” increasing the risk of data breaches and incidents [record_id:2481]. Third-party vendors are identified as a major contributor to this dynamic because they may introduce additional vulnerabilities into an organization’s ecosystem [record_id:2481].

The shared theme is that **accessibility of data and systems must be actively managed**. Whether the subject is a person’s online footprint or a company’s vendor environment, the records treat uncontrolled access and unmanaged dependencies as security risks.

### 2. Privacy and risk reduction through practical action

The DEF CON workshop explicitly emphasizes action. It is not merely about explaining privacy concepts; it proposes that attendees use OSINT techniques to see what an individual’s footprint is and then use obfuscation techniques to lessen that footprint [record_id:1969]. The phrase “Being private can help set you free” frames privacy as both a protective and liberatory practice [record_id:1969].

The BSidesLV talk similarly emphasizes applied risk reduction. It promises a framework for evaluating and onboarding potential vendors, aimed at organizations, practitioners, and individual contributors [record_id:2481]. The stated outcome is that attendees will learn how to mitigate risks and protect critical organizational data through third-party risk management strategies [record_id:2481].

In both cases, the records suggest Jacquot’s work is oriented toward **practical security enablement**: helping participants perform concrete assessments and adopt mitigations, rather than only warning about risk in abstract terms.

### 3. The public/private boundary as a security concern

The DEF CON record opens with a quotation attributed to Gabriel García Márquez: “All human beings have three lives: public, private, and secret” [record_id:1969]. This quotation sets the conceptual frame for the workshop: people have different categories of information, and not all information should be equally visible or accessible. The workshop is said to focus on “our public and private lives” as well as things “one might want to keep secret” [record_id:1969].

This public/private/secret framing is not repeated verbatim in the BSidesLV abstract, but it resonates with the vendor-risk discussion. Organizations also have different classes of information and operational dependencies, including critical data that must be protected from breach or misuse [record_id:2481]. The vendor-risk record does not discuss secrecy in philosophical terms, but it does frame critical organizational data as something that must be protected through governance and risk management [record_id:2481].

A trend across the records is therefore an interest in **who can access what**, and how individuals or organizations can make intentional decisions about visibility, disclosure, and dependency.

### 4. Attack surface expansion through modern technology adoption

The BSidesLV abstract directly identifies cloud technologies and artificial intelligence as drivers of expanded attack surface [record_id:2481]. It argues that as organizations adopt these technologies, the risk of data breaches and security incidents increases [record_id:2481]. Third-party vendors are presented as part of this expanded ecosystem and as possible sources of additional vulnerability [record_id:2481].

The DEF CON record does not specifically mention cloud or AI, but it addresses a related phenomenon: a broad public data footprint that makes personal information accessible “everywhere” [record_id:1969]. The workshop title, “Private, Private, Private Access Everywhere,” appears to play on the DEF CON 33 theme of “access everywhere” while pivoting toward “shutting down access to your data” [record_id:1969].

Together, the records suggest a broader trend: modern digital environments make access easier, broader, and more distributed. Jacquot’s talks respond by emphasizing **limiting exposure and creating boundaries**.

### 5. Security education for broad audiences

Both records are framed in accessible terms. The DEF CON workshop tells attendees to bring a device and be ready to work on becoming more private, suggesting a participatory format that could be useful to a wide audience concerned about personal privacy [record_id:1969]. The BSidesLV talk states that it aims to provide “organizations, practitioners, and individual contributors” with an “accessible and familiar framework” for vendor evaluation and onboarding [record_id:2481].

This suggests that a notable contribution across these records is not only the topic selection, but the **educational framing**. The talks appear designed to make privacy and cyber risk management understandable and actionable for people who may not be specialists in those specific domains.

## Methods, Tools, And Approaches Discussed

The records do not provide detailed tool names, step-by-step procedures, or technical architectures. However, they do identify several methods and approaches.

### OSINT-based personal footprint assessment

The DEF CON workshop explicitly says it will “go over both OSINT techniques to see what an individual’s footprint is” [record_id:1969]. This indicates an approach where attendees investigate what information about a person can be found through open sources. The record does not specify which OSINT tools, platforms, search strategies, datasets, or operational safeguards are included. Still, it clearly positions OSINT as a diagnostic method for understanding personal exposure [record_id:1969].

### Obfuscation to reduce personal exposure

The same workshop also says it will cover “obfuscation techniques to lessen that footprint” [record_id:1969]. The abstract does not define these techniques, so the evidence does not support claims about specific tactics such as data broker removal, aliasing, account hardening, metadata minimization, search engine removal requests, privacy settings, or browser configuration. What can be stated from the record is that obfuscation is presented as a way to reduce the discoverability or clarity of an individual’s public footprint [record_id:1969].

### Hands-on workshop learning

The DEF CON record’s instruction that attendees should bring their device and be ready to work on becoming more private indicates a hands-on workflow [record_id:1969]. This likely means the workshop was designed around practical exercises rather than only lecture content, but the abstract does not provide the exercise sequence or outputs.

### Third-party vendor evaluation and onboarding framework

The BSidesLV presentation promises “an accessible and familiar framework for evaluating and onboarding potential vendors” [record_id:2481]. This is the clearest method in the vendor-risk record. The abstract suggests the framework is intended to help organizations assess vendor risk before or during onboarding, with the ultimate goal of mitigating risks and protecting critical data [record_id:2481].

The record does not name the framework, list control categories, cite standards, or specify whether it aligns with known practices such as questionnaires, security reviews, contractual controls, cloud security assessments, SOC 2 review, ISO 27001 evaluation, data processing agreements, or continuous vendor monitoring. Therefore, downstream researchers should treat the framework as an identified topic but not infer its contents without additional evidence.

### Third-party risk management strategies

The BSidesLV record states that attendees will learn to implement “effective third-party risk management strategies” [record_id:2481]. It links those strategies to mitigating risk and protecting organizational critical data [record_id:2481]. The evidence supports the conclusion that the talk is about practical risk-management workflows for vendors, but not the details of the specific strategies.

## Notable Talks, Records, And Evidence

### DEF CON 33: “Private, Private, Private Access Everywhere” [record_id:1969]

This record is important because it provides the strongest evidence of Jacquot’s focus on **individual privacy and personal data exposure**. The workshop is built around a public/private/secret framing and directly responds to the idea of ubiquitous access by emphasizing the need to “shut down access to your data” [record_id:1969]. It combines OSINT footprint discovery with obfuscation techniques, indicating a two-step practical model: first identify what is exposed, then reduce or obscure that exposure [record_id:1969].

The record is also notable because it is explicitly hands-on. Attendees are told to bring a device and be ready to work on becoming more private [record_id:1969]. That makes it representative of a practical educational style: privacy is treated not merely as a policy concern but as something individuals can actively improve through guided work.

Evidence strength: moderate for topic and intent; thin for technical details. The abstract clearly establishes the workshop’s subject matter and pedagogical style, but it does not identify specific OSINT sources, obfuscation tactics, privacy tools, or threat models.

### BSidesLV 2025: “Let’s Go Shopping: Third-Party Vendors and CyberRisk” [record_id:2481]

This record is important because it shows Jacquot’s work extending into **organizational cyber risk**, particularly third-party vendor risk. Co-authored with Rafael Ayala, the talk argues that cloud and AI adoption expand organizational attack surfaces and increase the risk of breaches and incidents [record_id:2481]. It identifies third-party vendors as significant participants in that expanded ecosystem and potential sources of additional vulnerabilities [record_id:2481].

The talk’s proposed contribution is an accessible framework for evaluating and onboarding vendors [record_id:2481]. This gives the record a governance, risk, and compliance orientation, but with an emphasis on usability for organizations, practitioners, and individual contributors [record_id:2481].

Evidence strength: moderate for high-level risk framing and intended audience; thin for framework specifics. The abstract clearly states the problem and goal, but does not provide the actual framework, criteria, examples, metrics, or case studies.

## Gaps, Limits, And Open Questions

The evidence base is limited in several important ways.

First, there are only two records. Both are from 2025 and both are conference abstracts. This makes it difficult to identify long-term evolution in Jacquot’s work, compare early and later themes, or determine whether privacy and third-party risk are recurring topics across a larger career.

Second, the records do not include full talk transcripts, slide decks, workshop materials, demos, audience questions, or post-event writeups. As a result, specific claims about technical depth, recommended tools, case examples, or detailed methodology cannot be supported from the available evidence.

Third, the DEF CON workshop mentions OSINT and ob