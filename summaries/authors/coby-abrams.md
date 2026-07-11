# Topic: Author: Coby Abrams

## Executive Summary

The two records attributed to Coby Abrams both describe the same 2025 presentation, **“Rusty pearls: Postgres RCE on cloud databases,”** co-presented with Tal “TLP” Peleg / Tal Peleg. The talk centers on **CVE-2024-10979**, a Remote Code Execution vulnerability discovered by **Varonis Threat Labs**, and frames the vulnerability as significant because it can be exploited to execute arbitrary code on **cloud-hosted PostgreSQL databases** [record_id:2063] [record_id:2528].

Across the available records, Abrams’ attributed work is narrowly focused but technically important: exploit development, vulnerability discovery, managed database security, and defensive testing for cloud database environments. The evidence base is small—only two records—and both contain essentially identical abstract text, but the presence of the talk at both **DEF CON 33** and **BSidesLV 2025** suggests the material was considered relevant to major security conference audiences in 2025 [record_id:2063] [record_id:2528].

The records do not provide exploit details, root-cause analysis, mitigations, affected providers, code samples, or a full research methodology. They do, however, clearly establish a recurring contribution by Abrams around translating a specific PostgreSQL RCE vulnerability into lessons for cloud database exploitation, defense, and vulnerability testing.

## Research Landscape

The research landscape represented here is compact and conference-oriented. Both records are talk abstracts from 2025 security conferences. One record comes from **DEF CON 33**, where the talk is attributed to **Tal “TLP” Peleg and Coby Abrams** [record_id:2063]. The other comes from **BSidesLV 2025**, where the same talk is attributed to **Coby Abrams and Tal Peleg** [record_id:2528]. This ordering difference is minor but useful for downstream researchers: Abrams appears as a co-author or co-speaker in both cases, with co-presenter Tal Peleg.

The shared title, **“Rusty pearls: Postgres RCE on cloud databases,”** indicates a focus on PostgreSQL security in cloud or managed database contexts [record_id:2063] [record_id:2528]. The phrase “Rusty pearls” may imply a technical angle involving Rust, PostgreSQL internals, extensions, or implementation-specific vulnerabilities, but the abstracts themselves do not explain the phrase. Because the raw text only states that the session will “delve into CVE-2024-10979” and explain exploitation leading to arbitrary code execution on cloud-hosted databases, any deeper inference about Rust or implementation details remains speculative [record_id:2063] [record_id:2528].

The dominant research area is therefore **cloud database vulnerability research**, especially where managed infrastructure changes the assumptions around exploitation, testing, and defense. The records situate the work at the intersection of:

- PostgreSQL security;
- Remote Code Execution;
- managed/cloud-hosted database environments;
- exploitability analysis;
- defensive strategies;
- vulnerability testing for managed database services [record_id:2063] [record_id:2528].

Because both records contain the same abstract, there is no evidence of multiple distinct Abrams talks or a broader body of posts, papers, or presentations in this dataset. The topic summary should therefore be read as a focused snapshot rather than a comprehensive biography or bibliography.

## Major Themes And Trends

### PostgreSQL RCE In Cloud-Hosted Environments

The central theme across both records is exploitation of **CVE-2024-10979** to achieve **arbitrary code execution** on **cloud-hosted databases** [record_id:2063] [record_id:2528]. The abstracts emphasize that the vulnerability is “significant,” suggesting the talk likely frames it as more than a narrow local issue. Its importance appears tied to the managed database context: cloud-hosted databases are often assumed to restrict privileged access, OS-level execution, and unsafe configuration paths, so an RCE path in that environment carries elevated operational and security implications.

The records do not identify affected cloud vendors, database configurations, extension mechanisms, privilege prerequisites, or exploit constraints. Still, the repeated phrasing makes clear that Abrams’ contribution in this dataset concerns the practical exploitability of PostgreSQL-related vulnerabilities in cloud contexts, not merely theoretical vulnerability classification [record_id:2063] [record_id:2528].

### Bridging Exploitation And Defense

Both records describe the session as covering not only exploitation, but also “strategies for defending and testing managed databases for vulnerabilities” [record_id:2063] [record_id:2528]. This suggests the talk is positioned as dual-use security research: it explains how exploitation works while also offering guidance to defenders, cloud database administrators, and security testers.

This theme is important because cloud-hosted database security often falls between traditional database administration, application security, and cloud infrastructure security. The talk appears to address that gap by showing how a specific RCE vulnerability can be used to reason about broader defensive and validation strategies for managed databases [record_id:2063] [record_id:2528].

### Managed Database Security As A Specialized Attack Surface

The records repeatedly use the phrases “cloud-hosted databases” and “managed databases,” indicating that the research is not just about PostgreSQL in isolation, but about PostgreSQL as deployed through cloud-managed services [record_id:2063] [record_id:2528]. Managed services often constrain user access while adding provider-specific layers for provisioning, patching, isolation, monitoring, and administrative control. A vulnerability that crosses into arbitrary code execution in such an environment may raise questions about tenant isolation, provider hardening, privilege boundaries, patch cadence, and vulnerability validation.

The dataset does not answer those questions directly, but it establishes managed cloud databases as the relevant operating environment for Abrams’ attributed work.

### Conference Reuse And Cross-Audience Relevance

The same talk appears in records from both DEF CON 33 and BSidesLV 2025 [record_id:2063] [record_id:2528]. This indicates that the research was presented, or at least scheduled/listed, in multiple conference contexts. DEF CON and BSidesLV share a broad security audience but often differ in format and community emphasis. The BSidesLV record includes logistical tags—“Breaking Ground,” “Florentine A,” “Tuesday,” and “10:30-10:50”—suggesting a shorter scheduled talk slot at that event [record_id:2528]. The DEF CON record includes a tag of “18:30,” likely reflecting a video duration or schedule-related metadata, but the raw abstract remains the same [record_id:2063].

The reuse of the abstract across venues strengthens confidence that the same core research was being presented consistently, but it does not add independent technical details.

## Methods, Tools, And Approaches Discussed

The records provide only high-level statements about methods. They indicate that the session will “delve into CVE-2024-10979” and “explain how it can be exploited to execute arbitrary code on cloud-hosted databases” [record_id:2063] [record_id:2528]. From this, the supported methodological picture is:

- **Vulnerability deep dive:** The talk is organized around a specific CVE, CVE-2024-10979, rather than a broad survey of PostgreSQL vulnerabilities [record_id:2063] [record_id:2528].
- **Exploit explanation:** The abstracts explicitly state that the speakers will explain how the vulnerability can be exploited for arbitrary code execution [record_id:2063] [record_id:2528].
- **Cloud-managed database testing:** The talks include strategies for “testing managed databases for vulnerabilities,” implying attention to validation workflows suitable for cloud-hosted environments [record_id:2063] [record_id:2528].
- **Defensive strategy development:** The talks also promise defensive guidance, though the records do not enumerate specific mitigations, configurations, detection logic, patching steps, or monitoring approaches [record_id:2063] [record_id:2528].

No specific tools are named in the raw text. The records do not mention proof-of-concept exploit code, scanners, fuzzers, PostgreSQL extensions, cloud provider APIs, detection rules, or hardening frameworks. Therefore, downstream agents should avoid assuming the use of particular tooling unless they consult the underlying video, slides, or external Varonis Threat Labs material.

## Notable Talks, Records, And Evidence

The notable record set consists of two conference listings for the same talk.

The DEF CON 33 record identifies the talk as **“Rusty pearls: Postgres RCE on cloud databases”** by **Tal “TLP” Peleg and Coby Abrams**. Its abstract states that the session will examine **CVE-2024-10979**, discovered by **Varonis Threat Labs**, and explain exploitation leading to arbitrary code execution on cloud-hosted databases. It also says the audience will learn strategies for defending and testing managed databases for vulnerabilities [record_id:2063]. This is the strongest evidence connecting Abrams to a major security conference presentation on PostgreSQL RCE in cloud databases.

The BSidesLV 2025 record lists the same title, **“Rusty pearls: Postgres RCE on cloud databases,”** attributed to **Coby Abrams; Tal Peleg**. It uses the same abstract text, again tying the talk to CVE-2024-10979, Varonis Threat Labs, arbitrary code execution on cloud-hosted databases, and defensive/testing strategies for managed databases [record_id:2528]. This record matters because it independently places the same work in another 2025 security conference setting and shows Abrams as first-listed author/speaker in that listing.

Together, these records provide strong evidence that Abrams was associated with a specific, repeated presentation on PostgreSQL RCE in cloud environments. They provide weak evidence about the exact technical content beyond the abstract, because neither record includes slides, transcript, exploit chain, affected versions, or mitigation specifics.

## Gaps, Limits, And Open Questions

The evidence base is limited in several ways.

First, both records contain identical abstract text. This means there are two event records but only one substantive description of the research. The duplication supports the existence and relevance of the talk, but it does not broaden the thematic range of Abrams’ work [record_id:2063] [record_id:2528].

Second, the records do not include technical detail about **CVE-2024-10979**. They do not identify the vulnerable PostgreSQL component, the vulnerability class, exploitation prerequisites, affected versions, cloud provider exposure, patch status, or severity metrics. They also do not explain why the title includes “Rusty,” whether Rust code is involved, or whether the vulnerability relates to PostgreSQL extensions, foreign data wrappers, procedural languages, cloud control-plane behavior, or another mechanism [record_id:2063] [record_id:2528].

Third, the defensive material is only described generally. The records promise “strategies for defending and testing managed databases for vulnerabilities,” but they do not describe those strategies. Open questions for downstream research include:

- What concrete defensive controls did Abrams and Peleg recommend?
- Were the recommendations aimed at cloud providers, customers, database administrators, or security researchers?
- Did the talk include detection methods for exploitation attempts?
- Did it propose safe testing methods for managed database environments?
- Were specific cloud database platforms evaluated?
- Did the exploit require elevated database privileges, extension installation rights, SQL injection, misconfiguration, or provider-specific behavior?
- Did Varonis Threat Labs publish a companion blog post, advisory, proof of concept, or technical whitepaper?

Fourth, the records do not establish Abrams’ broader research portfolio. They show attribution to one specific talk at two venues, but they do not provide evidence of other talks, posts, tools, advisories, or publications by Abrams.

## Coverage And Evidence Notes

This report covers all records provided for the topic.

- **[record_id:2063]** is a DEF CON 33 listing for **“Rusty pearls: Postgres RCE on cloud databases”** by Tal “TLP” Peleg and Coby Abrams. It is a secondary-topic record under cloud/infrastructure/CDR and primarily categorized as exploit development and vulnerability discovery. The raw text describes a session on CVE-2024-10979, discovered by Varonis Threat Labs, explaining arbitrary code execution on cloud-hosted databases and strategies for defending and testing managed databases.
- **[record_id:2528]** is a BSidesLV 2025 listing for the same talk, attributed to Coby Abrams and Tal Peleg. It carries logistical tags including “Breaking Ground,” “Florentine A,” “Tuesday,” and “10:30-10:50.” Its raw text is the same as the DEF CON record and supports the same conclusions about the talk’s focus on CVE-2024-10979, PostgreSQL RCE, cloud-hosted databases, and managed database defense/testing.

No records are minor in the sense of being unrelated; both directly support the topic because both are attributed to Coby Abrams. However, because both records describe the same presentation with the same abstract, the evidence is narrow and should be treated as a focused view of Abrams’ conference work rather than a complete account of his research output.