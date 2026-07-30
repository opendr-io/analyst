# Topic: Author: Roey Ben Chaim

## Meta-Summary

The three records attributed to Roey Ben Chaim focus on security risks created by autonomous or tool-using AI agents. They present two complementary research directions: discovering internet-exposed agents before attackers exploit them, and dynamically analyzing malicious artifacts that agents acquire and execute at runtime. The first direction appears in substantially similar presentations at [un]prompted 2026 and DEF CON 34, where Ben Chaim and Avishai Efrat describe finding thousands of reachable, enumerable, or over-permissioned agents and introduce the PowerPwn reconnaissance tool [record_id:2368] [record_id:3113]. The second is a Black Hat USA 2026 briefing with Francesco Montorsi, Lana Salameh, and Michael Bargury that proposes an “agent detonation chamber” for identifying malware in agent skills and other AI supply-chain artifacts [record_id:2669].

Collectively, the records argue that conventional assumptions—security through obscurity, build-time static scanning, and LLM-based judgments about behavior—are inadequate for agentic systems. Ben Chaim’s distinctive contribution within this small corpus is an emphasis on empirical, externally observable evidence: enumerate deployed agents, measure their exposure, observe runtime behavior at the kernel level, and turn those observations into familiar security outputs such as reconnaissance findings, malware detonation reports, threat-intelligence feeds, and detection opportunities.

## Research Landscape

The corpus consists entirely of 2026 conference presentation descriptions rather than full papers, transcripts, demonstrations, or independently reproduced results. Two records describe the same talk, **“Total Recon: How We Discovered 1000s of Open Agents in the Wild,”** presented with Avishai Efrat in different conference settings [record_id:2368] [record_id:3113]. The third is the multi-author Black Hat briefing **“Promptware EOD: Skillful Agent Detonation”** [record_id:2669]. Conference talks therefore dominate the evidence, and the available material is prospective and promotional: it describes what the speakers intend to show, release, or demonstrate, but does not include the underlying datasets, implementation details, or evaluation results.

The overall research area lies at the intersection of AI-agent security, application security, attack-surface management, malware analysis, software supply-chain security, and detection engineering. The external-exposure work treats copilots, custom agents, AI middleware or backends, and other internet-connected deployments as a newly discoverable attack surface [record_id:2368] [record_id:3113]. The detonation work moves inward, examining what happens when agents retrieve, install, write, and execute code or skills during operation [record_id:2669].

Together, these records cover two phases of a plausible agent-focused attack lifecycle:

1. **Discovery and targeting:** adversaries identify exposed or over-permissioned agents reachable from the internet.
2. **Artifact delivery and execution:** agents consume malicious skills, servers, model-related components, or online content and then perform harmful runtime actions.

This is a coherent but narrow body of work. It is concerned less with abstract model alignment than with deployed systems, permissions, network reachability, runtime execution, malware behavior, and operational security controls.

## Major Themes And Trends

### AI agents as a new external attack surface

The most repeated claim is that organizations are unintentionally publishing agentic systems to the internet. The records identify copilots, custom agents, middleware, backends, and assorted deployments that may be reachable, enumerable, or over-permissioned without defenders realizing it [record_id:2368] [record_id:3113]. The “Total Recon” presentations frame this not as a hypothetical future risk but as an existing exposure problem, claiming that the researchers used technical discovery details to locate thousands of agents in the wild.

A core implication is that deployment visibility has not kept pace with adoption. Agents may be treated as internal assistants or obscure endpoints even when their surrounding infrastructure exposes them externally. Both versions of the talk explicitly argue that obscurity fails as a protective measure and that exposure should instead be measured and tested [record_id:2368] [record_id:3113].

### Runtime autonomy undermines traditional supply-chain controls

The Black Hat record extends the security problem from exposed services to the software and content that agents consume. It describes an agent supply chain containing skill Markdown files, “rug-pulled” MCP servers, misaligned models, and weaponized posts. These artifacts can influence agents that pull, write, install, or execute code at runtime [record_id:2669].

The briefing argues that conventional build-time static scanning is poorly suited to this environment. In an ordinary software pipeline, dependencies can often be examined before release. Agentic systems, by contrast, may acquire or generate executable material after deployment. This shifts meaningful analysis from build-time artifact inspection toward controlled runtime observation [record_id:2669].

### Semantic manipulation as a malware-evasion technique

One of the corpus’s more distinctive claims is that malicious artifacts can evade analysis by directing an AI-based scanner not to recognize their maliciousness. The detonation briefing reports that cryptominers and information stealers used trivial natural-language instructions likened to “these aren’t the droids you’re looking for,” allegedly blinding static scanning tools for months [record_id:2669].

This suggests an agent-specific evasion layer: malicious content need not only conceal executable behavior through traditional obfuscation; it can also manipulate the model or LLM judge responsible for interpreting that content. The record calls these “semantic compromises”—cases in which an agent’s account of what it did diverges from the behavior visible at the operating-system level [record_id:2669].

### Observable system behavior over model self-reporting

Across both research directions, the preferred evidence source is external observation rather than trust in an agent’s own representations. “Total Recon” focuses on what an outsider can enumerate and reach, not what an inventory claims is deployed [record_id:2368] [record_id:3113]. “Promptware EOD” similarly proposes comparing what a victim agent “thinks” it did against what the kernel records actually happening [record_id:2669].

This creates a consistent methodological principle: agent security should be grounded in externally verifiable facts. Network exposure, service enumeration, permissions, process activity, file changes, and other kernel-level events are treated as more reliable than system documentation, obscurity, model-generated explanations, or LLM-based verdicts.

### Security tooling must fit existing analyst workflows

The records do not present agent security as requiring an entirely separate operational discipline. Instead, they connect new agent-specific problems to familiar security practices. PowerPwn is positioned as a reconnaissance tool for testing one’s own exposure [record_id:2368] [record_id:3113]. The detonation chamber is intended to generate conventional malware detonation reports and integrate with established analyst workflows and threat-intelligence feeds [record_id:2669].

This points to a pragmatic trend: adapt mature techniques—external reconnaissance, sandbox detonation, kernel telemetry, red teaming, and threat-intelligence integration—to the unusual behavior of AI agents.

### Movement from identifying exposure to testing consequences

The two talk families complement one another in scope. The reconnaissance work asks where agents exist and how attackers may find them. The detonation work asks what happens when an agent interacts with a suspicious artifact and whether harmful behavior can be observed reliably. Although the records do not explicitly present these projects as a unified program, they collectively move from attack-surface discovery toward execution analysis and defensive validation [record_id:2368] [record_id:2669] [record_id:3113].

There are no visible disagreements among the records. Instead, they reinforce a common position: agent deployment and runtime autonomy have outpaced existing security models.

## Methods, Tools, And Approaches Discussed

The **Total Recon** approach appears to involve identifying technical characteristics that make internet-facing agents discoverable and enumerable, using those characteristics to locate exposed deployments, and then measuring their accessibility or permission posture. The records do not disclose the actual fingerprints, search infrastructure, query techniques, endpoints, or validation rules. They do state that the method found thousands of exposed agents of multiple kinds and could help defenders recognize threat-actor reconnaissance before it develops into a more consequential attack [record_id:2368] [record_id:3113].

The associated tool, **PowerPwn**, is described as a reconnaissance utility that defenders can use to test their own exposure. The [un]prompted record says the speakers would “drop” the tool, while the DEF CON description says they would showcase it [record_id:2368] [record_id:3113]. Based on the supplied text, PowerPwn’s exact feature set, target platforms, licensing, release status, and safe-use controls remain unspecified.

The **agent detonation chamber** is a dynamic-analysis architecture modeled on malware sandboxing. Its proposed design contains two agents:

- A **victim agent**, instructed to install a suspicious artifact.
- A **red-teaming agent**, tasked with causing the victim to detonate or exercise the newly acquired skill.

The chamber observes actual system behavior and compares the victim agent’s perceived or reported actions with “kernel-level truths.” This comparison is meant to expose semantic manipulation or compromise that static analysis and LLM judges miss [record_id:2669]. The adversarial second agent is significant because merely installing an artifact may not trigger its malicious path; active prompting or interaction may be necessary to reach the relevant behavior.

The Black Hat description claims that the researchers detonated tens of thousands of skills from public marketplaces and found hundreds of malicious ones. Cryptominers and information stealers are given as representative malware classes [record_id:2669]. The announced workflow aims to preserve established defensive outputs: familiar malware detonation reports, connections to threat-intelligence feeds, and open-source hooks through which agents can submit installed artifacts for remote detonation.

The same briefing announces **Promptware eval**, described as the first open-source benchmark for malicious AI artifacts found in the wild [record_id:2669]. If released with sufficient ground truth, it could support comparative evaluation of static scanners, LLM judges, dynamic chambers, and agent-security products. The record, however, supplies no benchmark schema, sample distribution, labeling procedure, or performance results.

## Notable Talks, Records, And Evidence

The most representative work is **“Total Recon: How We Discovered 1000s of Open Agents in the Wild.”** Its appearance in both the [un]prompted 2026 program and DEF CON 34 indicates repeated dissemination of the same central research: deployed AI agents are externally discoverable, obscurity is ineffective, exposure can be measured, and defenders need to detect agent-focused reconnaissance [record_id:2368] [record_id:3113]. The repeated descriptions provide strong evidence that these are core themes in Ben Chaim’s 2026 speaking activity, though they do not constitute two independent validations of the findings.

The [un]prompted version identifies Ben Chaim as a Staff Engineer at Zenity and Avishai Efrat as a Senior Security Researcher at Zenity. It emphasizes malicious discovery of agents, technical details enabling enumeration, exposure measurement, reconnaissance detection, and the release of PowerPwn [record_id:2368]. The DEF CON version is nearly identical but explicitly mentions exposed agents “of different kinds” and frames PowerPwn as a showcase rather than necessarily a release [record_id:3113]. These minor wording differences do not establish a substantive evolution in the research.

**“Promptware EOD: Skillful Agent Detonation”** is the broader and more technically detailed record. It positions the agent supply chain as a malware distribution environment and proposes dynamic detonation as the corrective to static, build-time security models [record_id:2669]. Its strongest announced empirical evidence is the claimed analysis of tens of thousands of marketplace skills and discovery of hundreds of malicious artifacts. Its most original architectural contribution is the pairing of a victim agent with a red-teaming agent inside a monitored chamber, followed by a comparison between model-level interpretation and kernel-observed behavior.

Evidence strength varies by type:

- **Strong for thematic attribution:** all three conference descriptions clearly associate Ben Chaim with research on practical AI-agent security.
- **Moderate for intended methods and tooling:** the records explain the broad purpose of PowerPwn, the two-agent detonation design, kernel-level observation, and planned analyst integrations.
- **Weak to moderate for empirical claims:** “thousands” of exposed agents, “tens of thousands” of detonated skills, and “hundreds” of malicious skills are asserted, but the records provide no raw data, reproducible methodology, false-positive analysis, or independent corroboration.
- **Weak for tool availability and effectiveness:** releases are announced, but the supplied corpus does not verify that PowerPwn, the free detonation service, its open-source integrations, or Promptware eval were ultimately published or maintained.

## Gaps, Limits, And Open Questions

The main limitation is that these are event abstracts rather than substantive research artifacts. They do not reveal how exposed agents were identified, what counted as an “agent,” how reachability was verified, or whether the researchers interacted with third-party systems beyond passive observation. They also do not distinguish between benign public deployment and unintended exposure. Consequently, the headline count of thousands of open agents cannot be independently assessed from this corpus [record_id:2368] [record_id:3113].

The reconnaissance records leave several operational questions unanswered:

- Which agent frameworks, cloud platforms, middleware products, or deployment patterns were most exposed?
- What specific properties made agents enumerable?
- How was “over-permissioned” defined and measured?
- What telemetry distinguishes malicious reconnaissance from ordinary scanning or legitimate use?
- Can defenders detect reconnaissance without producing excessive false positives?
- Does PowerPwn only inventory exposure, or can it validate permissions and exploit paths?

The detonation work likewise lacks critical evaluation details. The record does not define the collection period, marketplace coverage, maliciousness criteria, labeling process, or prevalence rate behind the claimed hundreds of malicious skills. It is unclear how many findings were conventional malware, prompt injection, policy-violating behavior, or genuinely novel “promptware” [record_id:2669].

Dynamic analysis also raises unresolved technical questions. Malware may detect sandbox conditions, delay execution, require credentials, target specific environments, or activate only after complex multi-step interactions. The red-teaming agent may improve behavioral coverage, but the abstract does not report trigger success, reproducibility, runtime overhead, containment guarantees, or false-negative rates. The phrase “kernel-level truths” signals a strong evidentiary preference but does not identify the operating systems, telemetry sources, isolation mechanisms, or behavioral rules used [record_id:2669].

Another gap concerns safe integration. The Black Hat record says that installed artifacts can be detonated remotely so they have “a chance to infect your systems,” wording that appears to describe giving suspicious artifacts an opportunity to reveal malicious behavior in a controlled environment. The abstract does not explain how artifacts, secrets, network access, or customer data are isolated from the detonation service [record_id:2669]. Those containment and privacy properties would be essential to evaluating the system.

Finally, the corpus is too small and temporally concentrated to establish a long-term evolution in Ben Chaim’s research. All three records are from 2026, and two describe the same talk. There are no blog posts, papers, code repositories, post-release evaluations, prior-year presentations, or incident reports here. Future research should seek those artifacts, verify the announced tool releases, and compare the claims against independent datasets and reproductions.

## Coverage And Evidence Notes

All three expected records are substantively relevant.

- The [un]prompted 2026 record documents Ben Chaim and Avishai Efrat’s external agent-attack-surface research, including the claim of finding thousands of exposed agents and the announced PowerPwn tool [record_id:2368].
- The Black Hat USA 2026 record documents Ben Chaim’s co-authored work on malicious agent artifacts, a two-agent detonation chamber, kernel-based behavioral evidence, public-marketplace skill analysis, and the announced Promptware eval benchmark [record_id:2669].
- The DEF CON 34 record is a second presentation listing for the Total Recon research. It reinforces the themes of reachability, enumeration, excessive permissions, exposure measurement, failure of obscurity, defensive reconnaissance detection, and PowerPwn, but offers little independent evidence beyond the closely matching [un]prompted description [record_id:3113].

No record is merely logistical or unrelated, although the DEF CON entry contains scheduling and venue metadata that adds no technical evidence. Because [record_id:2368] and [record_id:3113] are near-duplicate descriptions of the same work, aggregate conclusions should treat them as repeated coverage rather than separate empirical studies. Similarly, all quantitative and “first” claims in [record_id:2669] should be treated as author assertions pending access to the talk, tooling, benchmark, datasets, or independent validation.