# Topic: Author: Maksim Shudrak

## Executive Summary

The available records attributed to Maksim Shudrak consist of two DEF CON 33 entries for what appears to be the same 2025 talk, titled with minor capitalization variation as “Preventing One of The Largest Supply-Chain Attacks in History” / “Preventing One of The Largest Supply Chain Attacks in History” [record_id:1972] [record_id:2134]. Both records contain identical abstract text, duration metadata, event attribution, and thematic classification. The talk centers on a hypothetical but plausible large-scale software supply-chain compromise rooted in abandoned or compromised AWS S3 buckets, framed as an incident that could have affected thousands of buckets and tens of thousands of hosts globally if not preemptively mitigated [record_id:1972] [record_id:2134].

The core contribution described in the records is a supply-chain risk analysis connecting abandoned cloud infrastructure, backdoored artifacts, large-scale internet measurement, and adversarial automation using big data tooling and custom LLM agents. The talk promises an anatomy of the attack, statistical insights, nine concrete victim-profile or attack-vector stories, and remediation actions intended to eliminate the risk “once and for all” [record_id:1972] [record_id:2134]. Because the corpus contains only this duplicated talk abstract and no slides, transcript, code, paper, or follow-up commentary, the evidence is strong for identifying the talk’s topic and framing, but thin for evaluating its detailed findings, methodology, or remediation claims.

## Research Landscape

The research landscape represented here is narrow but focused: both records are DEF CON 33 video entries from 2025, attributed to Maksim Shudrak, with the same runtime tag of 37:58 and the same abstract text [record_id:1972] [record_id:2134]. The records describe a conference presentation rather than a written technical report. They position the work primarily within software supply-chain security, with secondary relevance to cloud infrastructure and AI-enabled security operations or attacks [record_id:1972] [record_id:2134].

The talk’s scenario is built around a hypothetical global “crypto worm” incident. The abstract imagines a worm targeting more than 100 organizations, affecting approximately 28,000 hosts across 158 countries, including “24 nation state and European union assets, major banks and tech companies” [record_id:1972] [record_id:2134]. It then reveals the imagined root cause: “compromised, abandoned AWS S3 buckets,” with 5,155 buckets affected in the scenario [record_id:1972] [record_id:2134]. The abstract explicitly states that this incident “has never happened,” and that the relevant buckets in the hypothetical scenario were claimed by a security researcher and taken down by the cloud provider [record_id:1972] [record_id:2134].

As a result, the records sit at the intersection of several research areas:

- **Software supply-chain compromise**: the imagined victims use “backdoored artifacts” with “no obvious connections,” suggesting an attack path through widely consumed dependencies, binaries, package references, datasets, or other artifacts retrieved from cloud-hosted locations [record_id:1972] [record_id:2134].
- **Cloud asset lifecycle security**: the root cause is abandoned AWS S3 buckets that remain referenced by external systems or artifacts, creating a takeover opportunity [record_id:1972] [record_id:2134].
- **Large-scale discovery and measurement**: the abstract emphasizes “statistical insights” and “instruments of big data analysis” [record_id:1972] [record_id:2134].
- **AI-assisted adversary scaling**: the talk claims that “custom LLM-agents” could help adversaries automate and scale such attacks [record_id:1972] [record_id:2134].
- **Preventive remediation**: the presentation culminates in remediation actions intended to remove the risk comprehensively [record_id:1972] [record_id:2134].

Because both records appear to describe the same presentation, there is no visible evolution across multiple works by Shudrak in this dataset. Instead, the landscape is best understood as one concentrated case study or research presentation about latent cloud-resource takeover risk in the software supply chain.

## Major Themes And Trends

### Abandoned cloud resources as latent supply-chain attack surfaces

The dominant theme is that abandoned AWS S3 buckets can become a high-impact supply-chain attack vector when they remain embedded in software artifacts, configuration files, update mechanisms, documentation, package metadata, build scripts, or other downstream references. The abstract’s imagined attack hinges on “compromised, abandoned AWS S3 buckets” serving as the hidden source behind apparently unrelated “backdoored artifacts” [record_id:1972] [record_id:2134]. This framing treats cloud storage not merely as infrastructure, but as part of a distributed trust chain: when consumers fetch artifacts from cloud-hosted locations, ownership and integrity of those locations become security-critical.

The records imply that a bucket takeover can break assumptions about artifact provenance. Victims may see different backdoored components with “no obvious connections,” while the underlying commonality is that the artifacts or references ultimately depend on reclaimed or compromised storage namespaces [record_id:1972] [record_id:2134]. This is a recurring concern in modern supply-chain security: identifiers, domains, package names, buckets, container registries, and other resource names can outlive their original maintainers, yet remain trusted by automated systems.

### Scale and systemic impact

A second theme is scale. The hypothetical scenario includes more than 100 targeted organizations, around 28,000 affected hosts, 158 countries, and 5,155 affected buckets [record_id:1972] [record_id:2134]. The numerical framing suggests that Shudrak’s talk is not about isolated bucket misconfiguration, but about systemic exposure created by many abandoned references across many organizations. The abstract emphasizes that the industry would struggle to identify the “main source of attack” because the visible symptoms would be distributed across many victims and artifacts [record_id:1972] [record_id:2134].

This scale-oriented framing is important because it turns abandoned S3 buckets from a cleanup or hygiene issue into a potentially strategic attack surface. The scenario includes “nation state and European union assets, major banks and tech companies,” suggesting that the affected population is not limited to small or poorly resourced organizations [record_id:1972] [record_id:2134]. The talk appears to argue that cloud asset abandonment can create broad, cross-sector risk.

### Preemptive research and responsible mitigation

The abstract contains a prevention narrative: the catastrophic incident “has never happened,” because the buckets used in the hypothetical scenario “were claimed by a security researcher and taken down by the Cloud provider” [record_id:1972] [record_id:2134]. This positions the work as preventive security research rather than post-incident forensics. The researcher identifies a plausible large-scale attack path, intervenes before exploitation, and coordinates with the cloud provider to neutralize the risk.

This theme is significant because it frames Shudrak’s contribution as practical risk reduction. The title itself, “Preventing One of The Largest Supply-Chain Attacks in History,” is built around averting a disaster rather than merely describing a vulnerability class [record_id:1972] [record_id:2134]. The abstract’s language suggests that the talk likely includes elements of vulnerability discovery, triage, responsible disclosure or provider coordination, and remediation strategy.

### Adversarial automation through big data and LLM agents

The records also introduce a forward-looking trend: attackers equipped with “instruments of big data analysis and custom LLM-agents” can “automate and scale” these attack scenarios [record_id:1972] [record_id:2134]. This is one of the most distinctive claims in the abstract. The talk appears to argue that the same large-scale analysis used by defenders or researchers to discover abandoned infrastructure could be replicated or enhanced by adversaries.

The LLM-agent reference is not elaborated in the records, but its inclusion indicates a concern that AI systems may reduce the manual effort needed to find abandoned cloud assets, map them to downstream consumers, generate exploitation plans, or triage high-value victims. The records classify the talk secondarily under AI security, prompt injection, and jailbreaking, but the raw text itself supports only the broader claim of custom LLM agents being used for attack automation and scaling [record_id:1972] [record_id:2134]. There is no raw-text evidence here of prompt injection or jailbreaking specifically.

### Story-driven explanation of victim profiles and attack vectors

The abstract promises “9 concrete stories illustrating potential victim profiles and attack vectors” [record_id:1972] [record_id:2134]. This suggests that the presentation likely uses narrative case studies or representative examples rather than only aggregate statistics. Those stories may be intended to show how different types of organizations or systems could be affected by abandoned S3 bucket takeover.

However, the records do not provide the nine stories themselves. Their existence is an important part of the talk’s structure, but downstream researchers should not infer the specific victim categories, artifacts, or exploitation paths without reviewing the video or additional materials.

## Methods, Tools, And Approaches Discussed

The available abstracts mention several methodological components, though without implementation detail.

First, the talk claims to “dissect the anatomy” of the attack [record_id:1972] [record_id:2134]. This implies a step-by-step decomposition of how abandoned AWS S3 buckets could become the source of backdoored artifacts and downstream compromise. The likely conceptual workflow includes identifying abandoned buckets, determining whether they are still referenced by consumers, assessing what artifacts or software flows depend on them, and evaluating how malicious replacement content could propagate. The records, however, do not provide enough detail to confirm the exact workflow.

Second, the records describe the use, or at least the relevance, of “big data analysis” [record_id:1972] [record_id:2134]. This indicates large-scale scanning, correlation, or measurement across many cloud resources and references. The abstract’s numbers—5,155 affected buckets, approximately 28,000 hosts, and 158 countries—suggest that the analysis spans a broad dataset rather than a handful of examples [record_id:1972] [record_id:2134]. The records do not specify the data sources used, such as package registries, software repositories, web crawls, telemetry, certificate logs, DNS, code search, object storage enumeration, or internet-wide scans.

Third, the talk mentions “custom LLM-agents” as instruments that could allow adversaries to automate and scale the scenario [record_id:1972] [record_id:2134]. This points to an AI-assisted workflow, but the raw text does not clarify whether the agents were actually built by the researcher, simulated, or only discussed as a plausible adversarial capability. It also does not specify agent tasks, models, prompts, orchestration frameworks, safeguards, or evaluation results.

Fourth, the records refer to “statistical insights” [record_id:1972] [record_id:2134]. These likely quantify exposure patterns, victim profiles, bucket counts, affected sectors, geographic distribution, or artifact types. The abstract gives headline numbers but not distributions, confidence intervals, sampling strategy, or validation methods.

Fifth, the talk promises “remediation actions that would eliminate the risk once and for all” [record_id:1972] [record_id:2134]. The records do not enumerate those actions, but the context implies possible remediation categories such as cloud-provider namespace controls, bucket-name quarantine or reservation, artifact integrity verification, dependency reference cleanup, ownership monitoring, and organizational asset lifecycle management. These are plausible interpretations of the problem space, not explicit claims in the records. The explicit evidence is only that remediation actions are discussed and that some buckets were claimed by a researcher and taken down by the cloud provider [record_id:1972] [record_id:2134].

## Notable Talks, Records, And Evidence

The central and only substantive work in the corpus is the DEF CON 33 talk attributed to Maksim Shudrak. Record 1972 lists the title as “Preventing One of The Largest Supply-Chain Attacks in History,” while record 2134 lists it as “Preventing One of The Largest Supply Chain Attacks in History” without the hyphen in “Supply Chain” [record_id:1972] [record_id:2134]. Both records are from DEF CON 33 in 2025, both have a 37:58 tag, and both provide the same abstract text [record_id:1972] [record_id:2134]. They likely represent duplicate or alternate video entries for the same presentation rather than separate talks.

This talk matters because it combines several active security research concerns into one scenario:

- A software supply-chain attack with many apparently unrelated backdoored artifacts [record_id:1972] [record_id:2134].
- A hidden common cause in abandoned AWS S3 buckets [record_id:1972] [record_id:2134].
- Large-scale global impact estimates, including organizations across 158 countries [record_id:1972] [record_id:2134].
- Preventive intervention before the hypothetical attack occurred [record_id:1972] [record_id:2134].
- The risk of adversaries using big data tooling and custom LLM agents to automate discovery and exploitation [record_id:1972] [record_id:2134].
- A promised set of nine concrete stories and remediation actions [record_id:1972] [record_id:2134].

The evidence strength is highest for the existence and framing of the talk. The records directly support that Shudrak presented, or was listed as presenting, a DEF CON 33 talk about preventing a major hypothetical supply-chain attack rooted in abandoned AWS S3 buckets [record_id:1972] [record_id:2134]. The evidence is weaker for the details of the research. The abstract does not provide the statistical methodology, the actual remediation recommendations, the content of the nine stories, or the mechanics of any LLM-agent system.

A notable feature of the abstract