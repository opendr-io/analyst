# Topic: Author: Qidan He

## Executive Summary

The available records attributed to Qidan He consist of two DEF CON 33 entries from 2025 for the same talk, **“Bypassing Intent Destination Checks, LaunchAnyWhere Privilege Escalation”** [record_id:1982] [record_id:2138]. The raw text is identical across both records, suggesting duplicate or parallel catalog entries rather than distinct works. The talk focuses on Android security, specifically the revival of the historically significant **LaunchAnywhere** class of vulnerabilities, in which unprivileged applications can invoke protected activities and potentially gain access to system-level functionality.

Across the records, Qidan He’s contribution is framed around showing that prior mitigations—especially **destination component checks** added by Google and device vendors before launching Android Intents—remain bypassable. The talk introduces a new exploitation technique called **BadResolve**, which reportedly bypasses these checks through multiple methods and enables a **zero-permission app** to regain LaunchAnywhere-style privilege escalation capability [record_id:1982] [record_id:2138]. The records also state that the identified high-severity vulnerabilities affected all Android versions, including Android 16 at the time of writing, and had been confirmed and patched by Google [record_id:1982] [record_id:2138].

A notable secondary contribution is methodological: the talk claims to address the challenge of finding exploitable methods in large Android codebases, including both AOSP and vendor-specific closed-source implementations, using **LLM Agents and MCP** [record_id:1982] [record_id:2138]. However, the records provide only abstract-level detail; they do not include technical exploit steps, patch details, evaluation data, tool architecture, or concrete examples of affected components.

## Research Landscape

The research landscape represented by these records is narrow but technically significant. Both records are DEF CON 33 entries from 2025 and appear to describe the same presentation, with the same title, abstract, event, year, duration tag, and author attribution [record_id:1982] [record_id:2138]. The source material is therefore best understood as a single talk represented twice in the dataset.

The talk sits primarily within **Android exploit development and vulnerability discovery**, with a strong application security focus. Its central concern is Android’s Intent-based activity launching model and the potential for unauthorized activity invocation when privileged components mishandle destination resolution. The raw records describe LaunchAnywhere as a long-standing Android security concern that has been “actively exploited in the wild in the past” [record_id:1982] [record_id:2138]. This situates the work not merely as theoretical vulnerability research but as a continuation of a known, historically exploited weakness class.

The records also point to a modern vulnerability-research workflow that combines traditional exploit analysis with automated code discovery. The abstract says the work addresses the difficulty of efficiently and accurately identifying exploitable methods across “the vast codebases of AOSP and vendor-specific closed-source implementations” using **LLM Agents and MCP** [record_id:1982] [record_id:2138]. This suggests that Qidan He’s talk bridges mobile platform security research with emerging AI-assisted analysis methods. Still, the evidence for the AI-assisted component is limited to a single sentence in the abstract, and no operational details are provided in the records.

## Major Themes And Trends

### Re-emergence of a supposedly mitigated Android vulnerability class

The dominant theme is the claim that **LaunchAnywhere-style privilege escalation has not been fully eliminated** despite vendor patches. The records describe LaunchAnywhere as a vulnerability class where “unprivileged applications” can “invoke protected activities, even with system-level privileges” [record_id:1982] [record_id:2138]. Google and device vendors reportedly attempted to mitigate this by introducing destination component checks in privileged code before launching Intents [record_id:1982] [record_id:2138].

The talk’s core research claim is that these defenses are “insufficient” and that LaunchAnywhere has been “reborn” through the new BadResolve technique [record_id:1982] [record_id:2138]. This creates a recurring security pattern: a vulnerability class is believed to be patched through local checks, but researchers later find that the underlying trust boundary or resolution mechanism remains exploitable. The records frame the research as a reassessment of whether patch strategies actually address root causes or only block known exploit paths.

### Android Intent resolution and destination checking as a fragile security boundary

The records repeatedly emphasize **Intent destination checks** as the key mitigation under scrutiny. Android Intents are a central inter-component communication mechanism, and the abstract suggests that privileged code attempts to defend itself by checking destination components before launching Intents [record_id:1982] [record_id:2138]. BadResolve is presented as a technique for bypassing those checks “through multiple methods” [record_id:1982] [record_id:2138].

Although the records do not explain the mechanics of BadResolve, the naming implies that the exploitation may involve manipulating or abusing how Android resolves Intent destinations. The security theme is that a check performed before Intent launch may not be equivalent to the actual resolution or dispatch behavior that occurs later. The records do not provide enough detail to confirm that interpretation, but they clearly identify destination resolution and pre-launch validation as the vulnerable area.

### Zero-permission exploitation and privilege boundary collapse

Another key theme is the severity of exploitation from a low-privilege starting point. The records state that BadResolve can enable “a zero-permission app to achieve LaunchAnywhere once again” [record_id:1982] [record_id:2138]. This is important because Android’s security model depends heavily on app sandboxing and permission declarations. A vulnerability that allows an app with no permissions to trigger protected or privileged activity behavior represents a substantial privilege boundary failure.

The raw text further claims that the resulting vulnerabilities are “high-severity” and affect “all Android versions, including the latest Android 16” at the time of writing [record_id:1982] [record_id:2138]. If taken at face value, this indicates broad platform exposure rather than a narrow vendor-specific misconfiguration. However, because the records are abstract-level only, they do not specify CVEs, affected components, proof-of-concept constraints, exploit reliability, or required device configurations.

### Coordinated vulnerability confirmation and patching

The records state that the vulnerabilities were “confirmed and patched by Google” [record_id:1982] [record_id:2138]. This provides stronger evidence than a purely speculative conference abstract because it implies vendor validation and remediation. Still, the records do not include patch references, Android Security Bulletin identifiers, bug IDs, CVEs, or timelines. The claim is therefore useful as a signal of credibility but insufficient for detailed vulnerability tracking without external corroboration.

### AI-assisted vulnerability discovery in large mobile codebases

A secondary but notable theme is the use of **LLM Agents and MCP** to identify exploitable methods in large codebases [record_id:1982] [record_id:2138]. The talk claims to address both AOSP and vendor-specific closed-source implementations, which implies a hybrid analysis problem: open-source platform code can be inspected directly, while vendor-specific behavior may require reverse engineering, firmware analysis, or other techniques.

The records do not define MCP or explain how LLM agents are integrated into the workflow. They also do not specify whether the agents perform code search, semantic analysis, exploit-path ranking, patch-diffing, decompilation assistance, or test generation. Still, the inclusion of this method suggests that Qidan He’s work is not limited to a single exploit, but also concerns scalable vulnerability discovery across fragmented Android ecosystems.

## Methods, Tools, And Approaches Discussed

The central technical approach discussed is the introduction of **BadResolve**, described as a “new exploitation technique” for bypassing destination component checks [record_id:1982] [record_id:2138]. The records state that BadResolve uses “multiple methods,” but they do not enumerate them. Its reported effect is to allow a zero-permission Android application to obtain LaunchAnywhere behavior despite the presence of mitigations [record_id:1982] [record_id:2138].

The defensive mechanism being bypassed is also described at a high level: Google and device vendors patched prior LaunchAnywhere issues “primarily by introducing destination component checks within privileged code before launching Intents” [record_id:1982] [record_id:2138]. The research therefore appears to compare intended destination validation with actual Intent resolution or launch behavior. The records do not say whether the bypasses depend on implicit Intents, aliases, exported components, package visibility, resolver behavior, pending intents, chooser flows, mutable fields, race conditions, confused deputy patterns, or vendor modifications.

For vulnerability discovery, the records mention a workflow using **LLM Agents and MCP** to efficiently and accurately identify methods that could be exploited by BadResolve in “the vast codebases of AOSP and vendor-specific closed-source implementations” [record_id:1982] [record_id:2138]. This is the only explicit tooling or automation reference. The records do not provide tool names, prompts, agent architecture, data sources, model types, evaluation metrics, false positive rates, or reproducibility guidance.

The methods discussed can therefore be summarized as:

- Exploit development against Android Intent launch flows.
- Analysis of privileged code paths that perform destination component checks.
- Identification of bypasses under the BadResolve technique.
- Large-scale codebase triage across AOSP and vendor Android implementations.
- AI-assisted discovery using LLM agents and MCP, at least as described in the abstract [record_id:1982] [record_id:2138].

## Notable Talks, Records, And Evidence

The sole substantive talk represented in the dataset is **“Bypassing Intent Destination Checks, LaunchAnyWhere Privilege Escalation,”** attributed to Qidan He at DEF CON 33 in 2025 [record_id:1982] [record_id:2138]. Both records provide the same abstract and appear to correspond to the same 46:31 presentation, though they have different source record IDs and YouTube URLs [record_id:1982] [record_id:2138].

This talk matters for several reasons. First, it revisits a historically important Android vulnerability class, LaunchAnywhere, and argues that the class remains exploitable despite prior mitigation efforts [record_id:1982] [record_id:2138]. Second, it introduces a named technique, BadResolve, which is presented as a new way to bypass destination component checks [record_id:1982] [record_id:2138]. Third, it claims broad impact across all Android versions, including Android 16 at the time of writing, with confirmation and patches from Google [record_id:1982] [record_id:2138]. Fourth, it includes an AI-assisted discovery component involving LLM Agents and MCP, indicating an attempt to scale vulnerability research across large and fragmented Android codebases [record_id:1982] [record_id:2138].

The evidence strength is moderate at the abstract level. The records make clear claims about technique, impact, and vendor confirmation, but they do not supply technical details. For downstream researchers, this talk should be treated as a strong lead for Android privilege escalation research and AI-assisted vulnerability discovery, but not as a complete technical source by itself. Additional materials—slides, transcript, CVE references, Android Security Bulletin entries, patches, proof-of-concept details, or follow-up writeups—would be needed to validate and operationalize the claims.

## Gaps, Limits, And Open Questions

The primary limitation is that both records contain the same short abstract. There is no independent corroborating record in the dataset, no transcript, no slides, and no detailed technical explanation. As a result, many important research questions remain open.

Key gaps include:

- **BadResolve mechanics:** The records do not explain how BadResolve bypasses destination component checks, what Android APIs are involved, or what assumptions prior patches made [record_id:1982] [record_id:2138].
- **Affected components:** The abstract says all Android versions were affected, including Android 16, but does not identify specific framework services, privileged apps, OEM components, or APIs [record_id:1982] [record_id:2138].
- **Patch details:** The records state that Google confirmed and patched the vulnerabilities, but they do not provide CVEs, bug IDs, commit references, bulletin dates, or patch descriptions [record_id:1982] [record_id:2138].
- **Exploit constraints:** The records say a zero-permission app can achieve LaunchAnywhere, but do not specify user interaction requirements, device state assumptions, target activity properties, Android version differences, or reliability constraints [record_id:1982] [record_id:2138].
- **Vendor ecosystem scope:** The abstract mentions AOSP and vendor-specific closed-source implementations, but does not say which vendors were analyzed or whether vendor bugs differed from AOSP bugs [record_id:1982] [record_id:2138].
- **LLM/MCP workflow:** The records mention LLM Agents and MCP but do not define the architecture, the model’s role, the inputs, the evaluation criteria, or the degree of automation [record_id:1982] [record_id:2138].
- **Security classification ambiguity:** One record’s metadata includes “AI security, prompt injection, and jailbreaking” as a secondary topic, but the raw text only supports an AI-assisted vulnerability discovery angle through “LLM Agents and MCP”; it does not directly discuss prompt injection or jailbreaking [record_id:1982]. The other record lists application security only as a secondary topic and has the same raw text [record_id:2138].

Future research agents should look for the actual DEF CON 33 video, slides, associated blog posts, Android Security Bulletin entries, CVEs, AOSP commits, and any released tooling or MCP/LLM agent workflow materials. The abstract is sufficient to identify the talk’s subject and claimed contributions, but insufficient for reproducing the research.

## Coverage And Evidence Notes

The dataset contains two records