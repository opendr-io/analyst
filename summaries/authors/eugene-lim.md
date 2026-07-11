# Topic: Author: Eugene Lim

## Executive Summary

The available records attributed to Eugene Lim consist of two DEF CON 33 entries from 2025 for what appears to be the same or closely duplicated talk: **“Escaping the Privacy Sandbox with Client Side Deanonymization Attacks”** / **“Escaping the Privacy Sandbox wClientside Deanonymization Attacks”** [record_id:2012] [record_id:2030]. Both records describe a security and privacy analysis of Google’s Privacy Sandbox APIs, focusing on how mechanisms intended to replace third-party cookies with more privacy-preserving web APIs may still enable client-side deanonymization under certain conditions.

Across both records, Lim’s contribution centers on showing that privacy-preserving browser APIs can fail in practice because of vulnerabilities, misconfigurations, debugging features, side channels, destination hijacking, and insecure cross-site code. The talk specifically discusses the **Attribution Reporting API**, **Shared Storage API**, **Referrer-Policy bypass implications**, **debugging reports**, **storage limit oracles**, and **cross-site worklet code** as elements in practical deanonymization and data-leakage attacks [record_id:2012] [record_id:2030].

The evidence base is narrow but coherent: both records contain identical raw descriptive text and are likely two catalog entries or video entries for the same DEF CON 33 presentation, with different YouTube IDs and different listed durations. As a result, the topic summary can confidently characterize this small corpus as focused on browser privacy, client-side web API security, and deanonymization risks in privacy infrastructure, but cannot infer broader trends in Eugene Lim’s body of work beyond this single talk.

## Research Landscape

The records in this topic are both from **DEF CON 33**, dated **2025**, and both are attributed to **Eugene Lim** [record_id:2012] [record_id:2030]. They are not blog posts, papers, tooling repositories, or multi-year records; they are conference-video-style entries summarizing a talk. Both have **Privacy and data leakage** as the primary topic and **Application security** as a secondary topic, which aligns with the raw text’s emphasis on browser APIs, privacy mechanisms, and client-side attack paths.

The two entries appear to represent the same substantive talk. Record 2012 gives the title as **“Escaping the Privacy Sandbox wClientside Deanonymization Attacks”**, while record 2030 gives the cleaner title **“Escaping the Privacy Sandbox with Client Side Deanonymization Attacks”** [record_id:2012] [record_id:2030]. The descriptions are identical, suggesting duplication or alternate uploads/edits rather than distinct presentations. The listed durations differ—34:38 for record 2012 and 25:56 for record 2030—so downstream researchers should treat them as potentially different cuts, versions, or recordings of the same presentation unless the videos themselves are reviewed [record_id:2012] [record_id:2030].

The overall research area is web privacy engineering under adversarial analysis. The Privacy Sandbox is presented in the records as Google’s initiative to provide privacy-preserving alternatives to third-party cookies by introducing new web APIs [record_id:2012] [record_id:2030]. Lim’s talk, as described, examines whether those APIs can still expose users to deanonymization through client-side attack techniques, especially when API behavior, debugging functionality, or developer-controlled code interacts with web security boundaries in unexpected ways.

## Major Themes And Trends

A central theme is the gap between **privacy-preserving API design** and **real-world privacy outcomes**. The records state that Google’s Privacy Sandbox aims to replace third-party cookies with new APIs that preserve privacy, but Lim’s talk examines ways those APIs can still compromise user privacy through vulnerabilities and misconfigurations [record_id:2012] [record_id:2030]. This frames the talk as an adversarial review of privacy technology: even if an API is designed to prevent direct tracking or data access, its auxiliary features, implementation details, and deployment assumptions can become attack surfaces.

A second recurring theme is **client-side deanonymization**. Both records use that concept in the title and description, and the described attacks all operate through browser-side mechanisms rather than server-only correlation. The attack surface includes browser APIs, reporting behavior, storage limits, site destinations, and worklet code [record_id:2012] [record_id:2030]. This suggests a focus on how web browsers and client-side state can become privacy leakage points even when traditional identifiers such as third-party cookies are removed or constrained.

A third theme is the security risk of **debugging and observability features** in privacy-sensitive systems. The records specifically mention the Attribution Reporting API and say that debugging reports can bypass privacy mechanisms such as `Referrer-Policy`, potentially exposing sensitive user information [record_id:2012] [record_id:2030]. The notable point is not merely that reporting APIs can leak data, but that developer-support or diagnostic features may weaken privacy protections if they are allowed to disclose information that normal API paths would restrict.

A fourth theme is the use of **side channels** against browser privacy controls. The records describe “destination hijacking” combined with “a side-channel attack using storage limit oracles” to reconstruct browsing history [record_id:2012] [record_id:2030]. This implies a more complex form of deanonymization in which the attacker does not need straightforward access to a browsing history database; instead, they infer history through observable side effects associated with storage constraints and destination behavior.

A fifth theme is the fragility of **isolation boundaries in cross-site execution models**. The records discuss the Shared Storage API and say that insecure cross-site worklet code can leak data stored within Shared Storage, even though the API is deliberately designed to prevent direct data access [record_id:2012] [record_id:2030]. This is representative of a broader application-security lesson: privacy APIs may rely on controlled execution environments or restricted access patterns, but developer-supplied or cross-site code can undermine those protections if not securely written or constrained.

There is no visible disagreement between the records because their raw text is identical. There is also no evidence of chronological evolution or a shift in Lim’s research over time, since both records are from the same event year and describe the same talk [record_id:2012] [record_id:2030].

## Methods, Tools, And Approaches Discussed

The records describe several specific technical approaches, though they do so at abstract-summary level rather than with full exploit details.

One approach concerns the **Attribution Reporting API**. Lim’s talk is described as exploring how debugging reports can bypass privacy mechanisms such as `Referrer-Policy` and potentially expose sensitive user information [record_id:2012] [record_id:2030]. The method implied here is to identify cases where privacy controls that normally suppress or limit referrer information may be circumvented by alternate reporting pathways. The records do not provide code, payloads, or a step-by-step reproduction, but they identify debugging reports as a key mechanism.

Another approach is **destination hijacking** combined with a **storage limit oracle**. The records say this combination can be used to reconstruct browsing history and characterize it as a more complex deanonymization technique [record_id:2012] [record_id:2030]. The term “storage limit oracle” suggests using observable browser storage behavior—such as whether storage is available, exhausted, partitioned, or affected by prior site interaction—as an inference channel. Coupled with destination hijacking, the technique appears to infer whether a user has visited or interacted with certain destinations. The records do not define the oracle in detail, so the exact mechanics remain an open point for future review of the talk video.

The records also discuss attacks involving the **Shared Storage API**. The described vulnerability class is insecure **cross-site worklet code** that can leak data stored within Shared Storage, despite the API’s design goal of preventing direct data access [record_id:2012] [record_id:2030]. This points to an approach where the attacker abuses code execution pathways around Shared Storage rather than reading storage directly. The significance is that privacy-preserving APIs often expose carefully limited computation models; if the computation code itself is insecure or can be influenced across sites, the boundary between allowed aggregate computation and forbidden direct data access may erode.

The talk also promises **real-world examples and potential attack scenarios** [record_id:2012] [record_id:2030]. However, the raw records do not enumerate those examples, so the records support only the conclusion that practical implications are discussed, not the specific real-world cases.

## Notable Talks, Records, And Evidence

The primary representative item is the DEF CON 33 talk attributed to Eugene Lim on escaping Google’s Privacy Sandbox through client-side deanonymization attacks. Record 2030 has the clearer title, **“Escaping the Privacy Sandbox with Client Side Deanonymization Attacks,”** and a listed duration of 25:56 [record_id:2030]. Record 2012 appears to be the same talk under a slightly malformed or compressed title, **“Escaping the Privacy Sandbox wClientside Deanonymization Attacks,”** with a listed duration of 34:38 [record_id:2012]. Both are important because they provide the same description and together establish the corpus’s only substantive topic.

The talk matters because it targets a high-impact transition in web privacy: the movement away from third-party cookies toward browser-mediated APIs intended to support advertising, attribution, storage, and measurement in more privacy-preserving ways. The records state that Google’s Privacy Sandbox introduces new web APIs as alternatives to third-party cookies, and Lim’s presentation examines how those APIs can be compromised by vulnerabilities and misconfigurations [record_id:2012] [record_id:2030].

The strongest evidence in the records concerns the specific API areas Lim intended to cover:

- **Attribution Reporting API** and debugging reports that may bypass `Referrer-Policy` protections [record_id:2012] [record_id:2030].
- **Destination hijacking** combined with **storage limit oracles** for browsing-history reconstruction [record_id:2012] [record_id:2030].
- **Shared Storage API** vulnerabilities involving insecure cross-site worklet code leaking data from Shared Storage [record_id:2012] [record_id:2030].
- Practical implications through real-world examples and attack scenarios, though the raw records do not describe those examples in detail [record_id:2012] [record_id:2030].

Because the two records have identical descriptions, they reinforce each other on content but do not provide independent corroboration of additional facts. Their main value is as pointers to the talk and as concise evidence of the topics covered.

## Gaps, Limits, And Open Questions

The most important limitation is corpus size. There are only two records, and they appear to describe the same DEF CON 33 talk [record_id:2012] [record_id:2030]. Therefore, this topic should not be treated as a comprehensive map of Eugene Lim’s broader work. It is a focused snapshot of one presentation.

The records do not provide detailed exploit chains, proof-of-concept code, affected browser versions, mitigation status, disclosure timelines, vendor responses, or whether the described vulnerabilities were patched before or after the talk. For example, they identify debugging reports in the Attribution Reporting API as a path to bypass privacy mechanisms such as `Referrer-Policy`, but do not explain exact preconditions, configuration requirements, or what sensitive information is exposed in practice [record_id:2012] [record_id:2030].

Similarly, the records mention destination hijacking and storage limit oracles for reconstructing browsing history, but leave several open questions: what browser storage primitives are involved, whether the oracle depends on partitioned storage behavior, what user interaction is required, how reliable the inference is, and what mitigations would break the chain [record_id:2012] [record_id:2030].

For the Shared Storage API, the records say insecure cross-site worklet code can leak data despite the API’s design against direct access, but they do not define the vulnerable coding patterns, trust assumptions, or exploitation model [record_id:2012] [record_id:2030]. A downstream researcher would need to inspect the talk video or related materials to understand whether the issue is inherent to the API design, caused by developer misuse, dependent on browser bugs, or some combination.

The duplication itself is also a metadata gap. Record 2012 and record 2030 have different YouTube URLs and different durations, despite identical descriptions [record_id:2012] [record_id:2030]. It is unclear whether one is a short version, a full version, a duplicate upload, a stage recording, or a corrected entry. Researchers should verify the videos directly before citing timing, transcript content, or exact phrasing from either source.

Open research questions include:

- What exact attack preconditions are required for each Privacy Sandbox deanonymization technique?
- Are the described attacks browser-specific or general across implementations?
- Were any of the issues fixed, mitigated, or disputed by browser vendors?
- How much of the risk comes from API design versus misconfiguration or insecure site code?
- What defenses does Lim recommend for browser vendors, web developers, advertisers, or privacy engineers?
- Do the “real-world examples” in the talk involve live deployments, hypothetical scenarios, lab demonstrations, or previously disclosed incidents?

## Coverage And Evidence Notes

This report covers both expected records.

Record 2012 is a DEF CON 33 entry titled **“Escaping the Privacy Sandbox wClientside Deanonymization Attacks”**, attributed to Eugene Lim, with a listed duration tag of 34:38. Its raw text describes attacks against Google Privacy Sandbox APIs, including Attribution Reporting API debugging reports, `Referrer-Policy` bypass implications, destination hijacking, storage limit oracles, browsing-history reconstruction, Shared Storage API issues, and insecure cross-site worklet code [record_id:2012].

Record 2030 is also a DEF CON 33 entry attributed to Eugene Lim, titled **“Escaping the Privacy Sandbox with Client Side Deanonymization Attacks,”** with a listed duration tag of