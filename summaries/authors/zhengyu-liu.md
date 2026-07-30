# Topic: Author: Zhengyu Liu

## Meta-Summary

The three records attributed to Zhengyu Liu describe coauthored DEF CON research on discovering and operationalizing previously underexplored vulnerability classes. Across web applications, Python packages, and desktop software, the work follows a consistent pattern: formalize an attack surface into a taxonomy or staged model, build an automated analysis tool, scan a large ecosystem, and demonstrate end-to-end exploitation rather than stopping at isolated bug detection.

The subjects are DOM clobbering and HTML injection on the web, Python class pollution in package and AI-related ecosystems, and browser-triggered exploitation of desktop applications through custom URI schemes. The records report hundreds of findings collectively, including 497 DOM-clobbering gadgets, 47 exploitable Python class-pollution zero-days, and 18 LaunchBreak zero-days. They also claim substantial remediation or disclosure outcomes, including acknowledged patches, CVE assignments, and a bug bounty [record_id:1947] [record_id:2922] [record_id:2955].

A recurring contribution is the conversion of fragmented security knowledge into reusable detection frameworks: Hulk for dynamic detection and exploit generation, Pyrl for static operational taint analysis, and Proton for agent-guided segmented fuzzing. The evidence in the records is compelling in scale and specificity, but it consists of talk descriptions rather than full technical papers, datasets, or independently reproduced evaluations.

## Research Landscape

The corpus contains three conference-talk records: one DEF CON 33 talk from 2025 and two DEF CON 34 talks from 2026. All three are collaborative. The DOM-clobbering talk is credited to Zhengyu Liu and Jianjia Yu [record_id:1947], while the two DEF CON 34 talks are credited to Gavin Zhong, Zhengyu Liu, and Jianjia Yu [record_id:2922] [record_id:2955]. The records do not specify how responsibilities were divided among the authors, so individual contributions by Liu cannot be isolated from the joint work.

Exploit development, vulnerability discovery, and application security dominate the landscape. The research moves across three layers of modern software:

- Browser-side JavaScript and DOM behavior, including client-side libraries and HTML-injection triggers [record_id:1947].
- Python’s object and reflection mechanisms, with emphasis on packages used in LLM applications and agent frameworks [record_id:2922].
- Electron-like or desktop application flows in which browser links invoke privileged local behavior through custom URI schemes [record_id:2955].

The talks are not merely conceptual overviews. Each claims a new systematization, an automated tool, ecosystem-scale testing, and practical exploit demonstrations. The targets include prominent libraries, package ecosystems, AI applications, developer tools, terminals, learning platforms, and collaborative applications. This breadth suggests a research program concerned with security boundaries that become dangerous when dynamic language or application features implicitly convert names, objects, links, or configuration data into privileged behavior.

Chronologically, the records indicate a progression from a browser-specific code-reuse attack in 2025 toward broader software and AI-adjacent exploitation in 2026. The later work concentrates especially on attack surfaces created or amplified by LLM tools, agent frameworks, and one-click application onboarding [record_id:2922] [record_id:2955]. Three records are too few to establish a durable longitudinal shift, but the movement toward AI and agentic software is explicit.

## Major Themes And Trends

### Systematizing poorly understood vulnerability classes

All three talks begin from the premise that an attack class is fragmented, underestimated, or incompletely modeled. The DOM-clobbering work organizes exploitation into four stages, integrates known techniques, and adds new clobbering primitives [record_id:1947]. The Python class-pollution work claims the first complete taxonomy, deriving six types from two object-resolution primitives and three object-assignment primitives; according to the record, only one of those six types had previously been recognized [record_id:2922]. LaunchBreak organizes browser-to-desktop exploitation along payload sources, cross-process flows, and security-sensitive sinks [record_id:2955].

This is more than a shared presentation style. Taxonomy construction is the bridge between isolated vulnerability examples and automated discovery. By identifying reusable primitives and data-flow stages, the researchers make it possible to search for variants beyond already documented bug patterns.

### End-to-end exploitability as the standard of significance

The records repeatedly distinguish between finding a suspicious pattern and demonstrating a complete attack. Hulk is described as generating working DOM-clobbering exploits end to end, while the surrounding research connects clobbering gadgets with HTML injection to construct full chains in Jupyter Notebook/JupyterLab, HackMD.io, and Canvas LMS [record_id:1947].

Likewise, the Python work does not treat class pollution as an abstract mutation issue. It reports weaponization into token exfiltration, authentication bypass, stored cross-site scripting, sandbox escape, and remote code execution. The talk particularly emphasizes that even the “weakest” newly identified class-pollution type can produce critical practical impact [record_id:2922].

LaunchBreak is itself defined as a multi-stage exploit model. A crafted browser link launches a desktop application and introduces attacker-controlled input into a chain spanning application processes and dangerous sinks. Seventeen of the 18 reported zero-days allegedly resulted in full remote code execution [record_id:2955].

Collectively, this focus guards against equating syntactic matches with vulnerabilities. The research aims to establish reachable triggers, attacker-controlled flows, exploitable sinks, and real security consequences.

### Dangerous interactions between convenient abstractions and privileged behavior

Each vulnerability class arises from legitimate convenience features:

- DOM elements and JavaScript variables share naming behavior that can create exploitable collisions [record_id:1947].
- Python’s uniform object model and dynamic reflection enable flexible programming but also class-pollution behavior [record_id:2922].
- Custom URI schemes make MCP installation, plugin setup, configuration import, and prompt-driven actions easy, but permit a browser click to reach privileged desktop logic [record_id:2955].

The common security problem is implicit resolution. A name resolves to an unexpected DOM object; an assignment reaches a class or object structure with broader consequences; or a URI-supplied value crosses application processes and reaches command execution, dynamic evaluation, or module loading. The work therefore highlights risks at abstraction boundaries where convenience obscures the actual trust transition.

### Ecosystem-scale measurement and prevalence claims

The records use large scans to argue that these are systemic vulnerability classes rather than isolated implementation mistakes. Hulk was applied in a study of the Tranco Top 5,000, yielding 497 reported zero-day DOM-clobbering gadgets. The same project separately found more than 200 websites vulnerable to HTML injection [record_id:1947].

Pyrl was applied to more than 600,000 GitHub and PyPI packages, reportedly finding 47 exploitable zero-days in projects including Azure CLI, Taipy, ComfyUI, Google Mesop, and HuggingFace Smolagents [record_id:2922]. LaunchBreak reports a smaller but still broad set of 18 zero-days across AI assistants, music players, terminals, and developer tools [record_id:2955].

These figures support the contention that the studied patterns recur across software ecosystems. Nevertheless, the abstracts do not provide denominators for every result category, duplicate-handling rules, selection criteria, or precision and recall measurements, so prevalence comparisons should remain cautious.

### AI and agentic software as an expanding attack surface

The two 2026 records explicitly connect conventional software-security mechanisms to AI-oriented ecosystems. Python class pollution is framed as especially relevant because Python is widely used in LLM applications and agent frameworks [record_id:2922]. LaunchBreak focuses in part on agentic desktop applications and onboarding mechanisms such as MCP installation and prompt-driven actions [record_id:2955].

Importantly, the described vulnerabilities are not attacks on model inference itself. They concern traditional software features—reflection, object mutation, URI dispatch, dynamic evaluation, module loading, and cross-process messaging—embedded in new AI products. The emerging trend is therefore the reappearance of established trust and data-flow problems within rapidly assembled AI application stacks.

### No documented disagreement, but distinct analysis strategies

The records do not contain explicit disagreements between the authors or with other researchers. They instead identify limitations in prior coverage: DOM-clobbering techniques had not been integrated into an end-to-end detector; Python class pollution was represented by one CVE and synthetic examples; and prior Electron research allegedly assumed that an attacker was already inside the application rather than beginning with a browser-triggered link [record_id:1947] [record_id:2922] [record_id:2955].

The approaches differ according to the target. DOM clobbering is addressed through dynamic analysis, Python class pollution through static analysis, and LaunchBreak through segmented fuzzing guided by an agent. This variation indicates that the common methodology is not allegiance to one analysis paradigm, but adaptation of analysis to the relevant runtime and data-flow structure.

## Methods, Tools, And Approaches Discussed

The DOM-clobbering project introduces **Hulk**, characterized as the first dynamic-analysis tool able to identify DOM-clobbering gadgets and generate working exploits end to end. Its conceptual basis is a four-stage systematization of exploitation that combines existing techniques with newly introduced clobbering primitives [record_id:1947]. Although the record does not name all four stages, it makes clear that gadget discovery alone is insufficient. The researchers separately analyze HTML injection as the trigger needed to place malicious markup and then combine injection flaws with gadgets to form complete exploit chains.

This decomposition is significant because the gadget and its trigger can reside in different parts of an application or software stack. The work reportedly found vulnerable behavior in Google Client API, Webpack, Vite, Rollup, and Astro, followed by acknowledgment and patching. It then demonstrated complete chains in applications such as Jupyter Notebook/JupyterLab, HackMD.io, and Canvas LMS [record_id:1947].

The Python project introduces **Pyrl**, an automated class-pollution detector based on a new static-analysis method called **operational taint analysis**. Its taxonomy combines two object-resolution primitives with three object-assignment primitives to derive six vulnerability types [record_id:2922]. The record does not define the primitives in sufficient detail to reconstruct the analysis, but the design appears intended to model how attacker-controlled data resolves to objects and how assignments mutate security-relevant state.

Pyrl’s scan of more than 600,000 GitHub and PyPI packages reportedly identified 47 exploitable zero-days. Case studies then traced pollution to concrete effects such as credential or token loss, authorization failures, web injection, sandbox escape, and code execution [record_id:2922]. This method represents the corpus’s clearest example of taxonomy-driven static analysis at software-supply-chain scale.

The LaunchBreak project introduces **Proton**, described as an agent-guided segmented fuzzing framework [record_id:2955]. Its attack-surface model has three dimensions:

1. Payload sources: custom URI input, attacker-controlled servers, and local files.
2. Cross-process paths: main, utility, and renderer processes.
3. Sinks: command execution, dynamic evaluation, and module loading.

Segmenting the problem appears intended to make long, cross-process exploit chains tractable. Instead of treating a desktop application as a single input-output target, the method follows attacker-controlled material through multiple stages and process boundaries. The record promises release of Proton and proof-of-concept exploits for every reported vulnerability, although it does not establish within the source text whether those releases ultimately occurred [record_id:2955].

Across all three tools, the workflow is broadly consistent: define primitives, map their composition, automate candidate discovery, validate exploitability, and use concrete chains to demonstrate impact. This compositional approach is arguably the most distinctive methodological feature of the corpus.

## Notable Talks, Records, And Evidence

The 2025 talk, **“AutoDetection & Exploitation of DOM Clobbering Vuln at Scale,”** is the foundational record in this small corpus. It combines conceptual systematization, dynamic tooling, a Top 5,000-site measurement study, disclosure outcomes, and application-level exploitation. Its headline evidence includes 497 zero-day gadgets, more than 200 sites with HTML injection, affected mainstream client-side libraries, complete chains against well-known applications, and 19 assigned CVEs [record_id:1947]. It is particularly representative of the authors’ emphasis on joining separate weaknesses into an actionable chain.

The 2026 talk, **“Get Set, Exploit! Unveiling Python Class Pollution In-the-Wild,”** broadens the research from browser object-name collisions to dynamic object mutation in Python. Its major claimed contributions are a six-type taxonomy, operational taint analysis, the Pyrl framework, a scan of over 600,000 packages, and 47 exploitable zero-days [record_id:2922]. The affected projects named in the record—such as Azure CLI, ComfyUI, Google Mesop, and HuggingFace Smolagents—indicate relevance to cloud tools, AI interfaces, and agent frameworks. The range of demonstrated impacts also supports the argument that class pollution is a vulnerability-enabling primitive rather than a single fixed exploit.

Also in 2026, **“LaunchBreak: a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover”** studies an external entry point that previous Electron-oriented work allegedly neglected: a browser click that activates a custom URI handler and reaches local application logic. The record reports 18 zero-days, including 17 full-RCE findings, 11 CVEs, and one bug bounty [record_id:2955]. Named affected applications include AFFiNE, Hyper, Cherry Studio, Pinokio, deepchat, and Paperlib. This record is notable for combining browser-originated payload delivery with desktop process boundaries and privileged execution sinks.

The quantitative evidence across the records is unusually concrete for talk descriptions, and the named projects, CVEs, patch acknowledgments, and bounty provide potential avenues for external verification. However, the records remain author-provided summaries. They do not include evaluation tables, false-positive rates, test harnesses, commit-level patch references, disclosure timelines, or independent replication.

## Gaps, Limits, And Open Questions

The central limitation is source depth. Each record is an abstract or conference description rather than a full paper, transcript, code repository, or dataset. Consequently, many technical details needed to evaluate or reproduce the work are absent.

For Hulk, the record does not identify the four exploitation stages, explain the new clobbering primitives, describe browser coverage, or report detection accuracy. It is also unclear how the 497 gadgets map to distinct websites, libraries, or exploitable application states. The relationship between the more than 200 HTML-injection sites and the gadget population is not quantified beyond selected complete chains [record_id:1947].

For Pyrl, the two object-resolution and three object-assignment primitives are not defined in the record. Operational taint analysis is named but not technically explained, and the source does not state how the scan handled package versions, forks, unreachable code, framework conventions, or false positives. It also leaves open how many of the 600,000 packages were analyzable and how the 47 exploitable zero-days were validated or disclosed [record_id:2922].

For LaunchBreak, the source provides the clearest high-level attack-surface dimensions but little information about Proton’s implementation, agent model, seed generation, process instrumentation, or success rate. It promises a tool and proof-of-concept release, but the record itself does not confirm release status. It also says that a related CCS paper would exist only if a then-pending submission were accepted, making that publication status explicitly uncertain [record_id:2955].

Several broader questions remain:

- How effectively do the tools generalize beyond the ecosystems and application architectures tested?
- What false-positive and false-negative rates do Hulk, Pyrl, and Proton exhibit?
- Which findings were independently confirmed, fixed, disputed, or found to be duplicates?
- Can the proposed taxonomies inform preventive engineering, such as framework-level defenses, safer APIs, or automated code transformations?
- How should custom URI handlers authenticate intent and constrain imported configuration or installation actions?
- Can operational taint analysis be generalized to other reflective languages and prototype- or class-mutation problems?
- To what degree do AI applications introduce genuinely new vulnerability mechanisms, as opposed to exposing conventional application-security failures through faster integration and broader privilege?
- What was Zhengyu Liu’s specific role in each project, given that all three records describe coauthored work?

There is also no record here of defensive deployment, longitudinal remediation, or measurements after patches. The corpus is therefore strongest on vulnerability discovery and exploit demonstration, but thin on prevention, durable mitigation, and real-world post-disclosure outcomes.

## Coverage And Evidence Notes

All three expected records are substantively relevant and none is merely logistical.

- The DEF CON 33 DOM-clobbering record establishes the earliest work in the set and supplies the strongest evidence for large-scale web measurement, dynamic exploit generation, and the joining of gadget and injection findings into complete attack chains [record_id:1947].
- The DEF CON 34 Python class-pollution record supplies the largest software-corpus scan and the clearest static-analysis contribution, while extending the work into Python, LLM applications, and agent frameworks [record_id:2922].
- The DEF CON 34 LaunchBreak record covers browser-to-desktop exploitation, custom URI schemes, cross-process chains, and agent-guided segmented fuzzing. It also contains an explicit uncertainty about whether a related CCS paper would follow [record_id:2955].

Evidence strength is highest for identifying the authors’ stated topics, tools, taxonomies, target classes, headline finding counts, and intended demonstrations. Evidence is moderate for broader conclusions about a recurring research methodology because the same systematize–automate–scan–exploit pattern appears in all three records. Evidence is weaker for comparative tool effectiveness, prevalence rates, independent confirmation, release status, and attribution of individual contributions, because those matters are not documented in the raw records.