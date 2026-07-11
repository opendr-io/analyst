# Topic: Author: Kane Narraway

## Executive Summary

The available Kane Narraway-attributed corpus is small but coherent: two BSidesSF 2025 records centered on AI security in enterprise and cloud-native environments. One record is a solo talk by Narraway on threat modeling enterprise AI search platforms, emphasizing data aggregation, sensitive corporate information exposure, and deployment controls [record_id:2270]. The other is a live Cloud Security Podcast panel featuring Narraway alongside Ashish Rajan, Jackie Bow, and Swathi Joshi, focused on securing cloud-native AI systems, building AI-first SOC teams, and identifying gaps in legacy security tooling [record_id:2259].

Collectively, the records position Narraway’s work in this dataset at the intersection of AI security, cloud security, threat modeling, SOC modernization, monitoring, response, and privacy/data leakage risk. The strongest evidence is for Narraway’s interest in practical enterprise AI security: how organizations should model threats, design controls, monitor AI systems, and adapt security operations to AI-native risks. The evidence base is thin—only two short conference-program abstracts—but the themes are aligned and mutually reinforcing.

## Research Landscape

The records consist entirely of BSidesSF 2025 conference schedule entries or presentation abstracts. They are not full papers, slide decks, transcripts, or technical walkthroughs. As a result, they provide high-level descriptions of topics, intended audience, and likely discussion areas, but they do not provide detailed methodology, case studies, implementation steps, or empirical results.

The two records represent two different formats:

- A multi-speaker live podcast panel titled “CLOUD SECURITY PODCAST - LIVE!” with Ashish Rajan, Jackie Bow, Swathi Joshi, and Kane Narraway [record_id:2259].
- A solo session by Kane Narraway titled “ONE SEARCH TO RULE THEM ALL: THREAT MODELLING AI SEARCH” [record_id:2270].

The research area that emerges is applied AI security for organizations adopting AI systems in cloud and enterprise environments. The panel abstract frames AI as a major shift for security teams, stating that “AI is reshaping security faster than cloud ever did” and focusing on “real-world threat models,” “AI-first SOC teams,” and “gaps legacy tools can't fill” [record_id:2259]. The solo talk narrows this broad AI-security concern to enterprise AI search tools such as Glean and Guru, which “aggregate all your company's data into a single, easy-to-navigate interface” and require “effective threat modelling and controls” during deployment [record_id:2270].

The dominant source type is conference programming text. This means the available records are best treated as evidence of topic focus, not as proof of specific technical claims or deployed controls. They are useful for identifying Narraway’s public speaking themes and the kinds of AI-security problems he is associated with, but they do not allow deep evaluation of his technical methods or conclusions.

## Major Themes And Trends

A central theme across both records is that AI adoption changes the security problem space in ways existing tools and processes may not address. The panel record explicitly contrasts AI’s pace of change with cloud, saying “AI is reshaping security faster than cloud ever did” [record_id:2259]. That framing suggests a trend toward urgent adaptation: security teams are not simply extending cloud controls to AI systems, but are being asked to rethink threat models, monitoring, and response.

Threat modeling appears as the clearest recurring concern. In the panel, threat modeling is mentioned broadly through “real-world threat models” for AI systems [record_id:2259]. In the solo session, threat modeling is the main topic: “THREAT MODELLING AI SEARCH,” with a focus on enterprise AI search tools and controls [record_id:2270]. Taken together, these records suggest that Narraway’s contribution in this corpus is not primarily about abstract AI risk, but about practical modeling of how enterprise AI systems can fail, leak, or be abused.

A second theme is enterprise data exposure. The solo talk describes AI search platforms as aggregating “all your company's data into a single, easy-to-navigate interface” and compares them to “Google, but for juicy, sensitive corporate information” [record_id:2270]. This phrasing highlights a specific AI-security concern: AI-enabled search can increase the accessibility and discoverability of sensitive information. The risk is not only that data exists somewhere in the enterprise, but that AI search may make it easier for users—or attackers with user access—to locate, correlate, and exploit it.

A third theme is the modernization of security operations. The panel discusses “building AI-first SOC teams” and what it takes to “secure, monitor, and respond to threats in AI systems” [record_id:2259]. This suggests an operational lens: AI security is not just an application-security or governance problem, but a SOC and detection engineering problem. The record implies that teams need new skills, workflows, and possibly tooling to detect and respond to AI-specific threats.

A fourth theme is the insufficiency of legacy tooling. The panel explicitly references “the gaps legacy tools can't fill” [record_id:2259]. Although the abstract does not specify which tools or gaps, the statement aligns with the broader framing that AI systems introduce new observability, detection, and control requirements. In combination with the AI-search talk, likely areas of concern include access control, data governance, monitoring of queries and responses, and prevention or detection of sensitive-data exposure, though the records do not provide enough detail to confirm exact mechanisms.

There is no evidence of disagreement across the records. Instead, the two entries are complementary: one provides a broad panel-level perspective on AI security and AI-first SOCs [record_id:2259], while the other provides a narrower enterprise AI search threat-modeling use case [record_id:2270].

## Methods, Tools, And Approaches Discussed

The primary method explicitly discussed is threat modeling. The solo talk is directly framed around “effective threat modelling and controls” for enterprise AI search deployments [record_id:2270]. The panel also refers to “real-world threat models” for AI systems [record_id:2259]. The records do not identify a specific threat-modeling framework—such as STRIDE, PASTA, LINDDUN, attack trees, or misuse cases—but they strongly indicate that structured assessment of AI-system threats is a key approach.

Enterprise AI search platforms are the most concrete technology category named. The solo abstract identifies “Enterprise AI search tools like Glean and Guru” and describes them as aggregating company data into a unified interface [record_id:2270]. These named products appear as representative examples of a broader class of tools that combine search, enterprise knowledge management, and AI-enabled discovery. The security concern is that centralization and ease of navigation may magnify exposure of “juicy, sensitive corporate information” [record_id:2270].

Controls are mentioned but not specified in detail. The solo talk promises exploration of “controls when deploying these tools” [record_id:2270]. Based strictly on the record text, the controls are deployment-oriented and tied to threat modeling AI search. The abstract does not enumerate whether these controls include identity and access management, permission trimming, data classification, logging, red teaming, prompt-injection defenses, retrieval filtering, or data-loss prevention. Those are plausible research directions, but not directly evidenced by the record.

The panel discusses building “AI-first SOC teams” and the ability to “secure, monitor, and respond to threats in AI systems” [record_id:2259]. This points to operational approaches such as AI-aware monitoring and incident response, but again without a detailed toolchain. The record’s mention of “gaps legacy tools can't fill” suggests that conventional SOC, SIEM, or cloud-security tooling may be insufficient for AI systems, but it does not specify whether the solution is new telemetry, new detections, model-level monitoring, application-layer logging, specialized AI security platforms, or changes in staffing and process [record_id:2259].

Overall, the records emphasize applied approaches rather than theoretical AI safety. The implied workflow is: identify AI system architecture and data flows, model threats, define controls, build operational monitoring and response, and adapt security teams to AI-specific risks [record_id:2259; record_id:2270].

## Notable Talks, Records, And Evidence

The most focused Narraway record is “ONE SEARCH TO RULE THEM ALL: THREAT MODELLING AI SEARCH,” a solo BSidesSF 2025 session attributed to Kane Narraway [record_id:2270]. It matters because it provides the clearest statement of Narraway’s specific AI-security contribution in the dataset. The talk targets enterprise AI search systems, naming Glean and Guru as examples, and frames them as tools that aggregate company data into a single interface [record_id:2270]. The phrase “Google, but for juicy, sensitive corporate information” captures the core risk model: AI search can transform diffuse enterprise information into a highly discoverable, centralized access surface [record_id:2270]. The session promises to cover threat modeling and controls for deployments, making it the strongest evidence for Narraway’s focus on practical enterprise deployment risk [record_id:2270].

The second record, “CLOUD SECURITY PODCAST - LIVE!,” is broader and multi-speaker, with Narraway listed alongside Ashish Rajan, Jackie Bow, and Swathi Joshi [record_id:2259]. Its subtitle or description, “AI Security 101: Securing Cloud-Native AI Systems & Building Modern SOCs,” frames the conversation as introductory but practical [record_id:2259]. This record matters because it situates Narraway in a wider practitioner conversation about cloud-native AI security, AI-first SOC teams, threat models, monitoring, response, and limitations of legacy tools [record_id:2259]. It is less specific to Narraway’s individual views because it is a panel record, but it establishes that his public speaking presence in this dataset includes broader AI security operations topics, not only AI search.

Together, these records show two scales of analysis. At the platform scale, Narraway is associated with threat modeling a specific class of enterprise AI tooling: AI search over corporate data [record_id:2270]. At the organizational scale, he is associated with broader questions about how security teams should secure, monitor, and respond to threats in AI systems, and how SOCs should evolve for AI-native environments [record_id:2259].

## Gaps, Limits, And Open Questions

The most important limitation is the size and depth of the evidence base. There are only two records, both short event abstracts. They provide no full session transcript, slides, code, architecture diagrams, survey data, incident examples, or detailed recommendations. As a result, the report can identify themes but cannot reconstruct Narraway’s complete technical position.

Several open questions remain:

- What specific threat-modeling framework does Narraway recommend for enterprise AI search, if any? The solo talk mentions “threat modelling and controls” but does not name a methodology [record_id:2270].
- What concrete controls are proposed for tools like Glean and Guru? The abstract signals that controls are discussed, but does not list them [record_id:2270].
- How does Narraway define an “AI-first SOC team”? The panel mentions the concept but does not describe staffing models, detection content, telemetry sources, escalation paths, or incident-response playbooks [record_id:2259].
- What are the “gaps legacy tools can't fill”? The panel raises this issue, but the abstract does not identify which legacy tools are inadequate or what capabilities are missing [record_id:2259].
- Does Narraway focus on prompt injection, data leakage, authorization failures, insider risk, retrieval-augmented generation vulnerabilities, auditability, or model behavior? The topic classifications suggest relevance to AI security and privacy/data leakage, and the raw text supports concern about sensitive corporate information, but the records do not provide a complete taxonomy of risks [record_id:2270].
- Are the talks based on real deployments, case studies, red-team exercises, or conceptual guidance? The panel references “real-world threat models” [record_id:2259], but neither record provides evidence details.

Future research agents should seek slides, recordings, speaker notes, podcast audio, or related blog posts from Kane Narraway to fill these gaps. In particular, the AI search talk appears likely to contain the most concrete material and should be prioritized if more source material becomes available [record_id:2270].

## Coverage And Evidence Notes

This report covers both expected records.

Record 2259 is a BSidesSF 2025 live Cloud Security Podcast panel titled “CLOUD SECURITY PODCAST - LIVE!” featuring Ashish Rajan, Jackie Bow, Swathi Joshi, and Kane Narraway [record_id:2259]. It is important as evidence of Narraway’s participation in a broader conversation about “AI Security 101,” cloud-native AI systems, AI-first SOC teams, real-world threat models, monitoring, response, and legacy-tool gaps [record_id:2259]. Because it is a multi-speaker panel abstract, it is weaker evidence for Narraway’s individual claims than the solo talk.

Record 2270 is a BSidesSF 2025 solo session titled “ONE SEARCH TO RULE THEM ALL: THREAT MODELLING AI SEARCH” by Kane Narraway [record_id:2270]. It is the strongest record for Narraway-specific thematic attribution. It focuses on enterprise AI search tools such as Glean and Guru, the aggregation of company data into a unified search interface, sensitive corporate information exposure, threat modeling, and deployment controls [record_id:2270].

The collective evidence is strongest for the conclusion that Kane Narraway’s records in this dataset concern practical AI security for enterprise environments, especially threat modeling and operational security around AI systems [record_id:2259; record_id:2270]. The evidence is thinner for detailed technical methods, named controls, or mature research outputs, because the available records are short conference descriptions rather than full technical artifacts.