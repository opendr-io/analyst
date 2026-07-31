# Topic: Author: Yarden Porat

## Meta-Summary

The three records attributed to Yarden Porat are Black Hat Briefing descriptions coauthored with Shahar Tal. They present offensive security research focused on breaking high-value trust boundaries: enterprise secret vaults, same-process cloud isolation, and the internal control planes of AI-agent frameworks. Across the corpus, the recurring contribution is not merely identifying unsafe input handling, but tracing attacker-controlled input through privileged software layers until it enables remote code execution, native code execution, cross-tenant disclosure, or access to protected secrets.

The work progresses from two remote code execution chains against HashiCorp Vault and CyberArk Conjur in 2025 [record_id:88] to two related 2026 investigations into agentic and cloud infrastructure. One follows prompt injection through Cloudflare CodeMode, the workerd runtime, and its JSG C++ binding layer to an isolate escape and alleged production impact on Cloudflare Workers [record_id:2630]. The other generalizes prompt injection into a framework-exploitation problem across six widely used AI-agent frameworks, reporting 11 CVEs and three recurring attack classes [record_id:2648].

Collectively, the records argue that systems fail when security reviews focus on the most visible boundary—the vault login, the LLM’s behavior, its external tools, or the V8 engine—while overlooking privileged glue, orchestration, state management, parsing, and framework logic beneath it. The evidence is technically specific but limited to conference abstracts: it reports vulnerability counts, affected products, exploit stages, and intended demonstrations, yet provides no CVE identifiers, patches, code, reproduction instructions, or independent validation.

## Research Landscape

The corpus consists entirely of Black Hat US Briefing listings. It contains one 2025 session and two 2026 sessions, and every record names Porat together with Shahar Tal. Consequently, the material supports conclusions about their joint research program, but it does not isolate Porat’s individual role or distinguish which findings, methods, or implementation work should be attributed specifically to either coauthor.

The 2025 record is centered on established enterprise security infrastructure. “Vaulted Severance: Your Secrets Are Now Outies” targets HashiCorp Vault and CyberArk Conjur, products entrusted with secrets, credentials, and encryption keys. The abstract claims two novel and confirmed RCE chains, including a full HashiCorp Vault chain and a pre-authentication CyberArk Conjur chain, both demonstrated against default configurations [record_id:88].

The two 2026 records shift toward AI-agent and cloud-runtime security. “When Agentic Glue Melts” begins with Cloudflare CodeMode, an experimental LLM tool-orchestration layer, but expands into the shared workerd runtime and the production Cloudflare Workers environment [record_id:2630]. “No Tools Required” surveys six agent frameworks—LangChain, LangGraph, CrewAI, AutoGen, Microsoft Agent Framework, and Google ADK—and claims a cross-framework architectural pattern in which prompt-controlled content can influence trusted orchestration and framework state [record_id:2648].

Despite differing product categories, exploit development and vulnerability discovery dominate the landscape. These are not policy-oriented discussions of abstract AI risk. The descriptions emphasize concrete exploit chains, memory-safety flaws, pre-authentication attack surfaces, heap manipulation, read/write primitives, native execution, and demonstrations ending in stolen secrets or a shell. Application security, cloud security, identity and access infrastructure, reverse engineering, and AI security converge around a common question: where does untrusted input cross into privileged execution or control?

## Major Themes And Trends

### Security failures beneath the obvious interface

The strongest recurring theme is that the most consequential attack surface lies beneath the interface defenders are likely to inspect first. In the vault research, the security premise of a hardened repository is challenged by attacks that allegedly reach code execution remotely, including without authentication in the Conjur case. If the vault itself is compromised, the secrets it protects become part of the impact rather than a defense [record_id:88].

The same reasoning appears more explicitly in the 2026 work. Cloudflare CodeMode’s model-generated TypeScript is confined by V8 isolates, but the research focuses on JSG, the C++ “JavaScript Glue” connecting JavaScript to native workerd APIs. The authors’ central lesson is that the engine is not the entire sandbox boundary: binding and glue code on that boundary must receive equivalent scrutiny [record_id:2630].

The agent-framework survey makes a parallel distinction between the “data plane” and trusted framework logic. It argues that prompt-controlled content should remain data, yet can instead affect system instructions, routing, memory, state, and control flow. Under this model, the framework internals—not only the model or attached tools—become the exploit surface [record_id:2648].

### From behavioral manipulation to software exploitation

The records describe a widening conception of prompt injection. The framework study supplies the clearest progression: prompt injection was initially treated as a way to induce model misbehavior or expose hidden context, then as a means to abuse connected tools, and finally as a primitive that can compromise trusted framework logic and potentially reach memory corruption and a shell [record_id:2648].

The Cloudflare research demonstrates a closely related escalation path. It starts from “a basic prompt injection entry point,” proceeds through a JSG use-after-free, escapes a V8 isolate, establishes read/write primitives, and reaches native code execution in the host process. The asserted final impact is extraction of a private key belonging to another worker [record_id:2630]. This turns prompt injection from the endpoint of an AI-security finding into the first stage of a conventional memory-corruption and cloud-isolation exploit chain.

This trend links the AI-focused records to the earlier vault work. All three treat input-driven compromise as a chain leading to traditional high-impact outcomes: RCE, native execution, cross-tenant disclosure, shell access, or exposure of credentials and keys [record_id:88] [record_id:2630] [record_id:2648].

### Trust-boundary analysis as the organizing principle

Across the corpus, the research is organized around finding where a system’s architectural trust assumptions do not match actual data flow.

For vaults, the boundary is the remotely reachable surface protecting the organization’s most sensitive assets, with particular concern around unauthenticated access and default deployment conditions [record_id:88]. For workerd, it is the in-process V8 isolate and the native JSG layer surrounding it [record_id:2630]. For agent frameworks, it is the separation between untrusted prompt content and trusted instructions, orchestration, memory, state, and routing [record_id:2648].

A recurring analytical move is therefore to ask not only whether input is malicious, but where it changes status: from remote request to privileged vault behavior, from model output to executable TypeScript, from JavaScript to native C++, or from prompt data to framework control state. This is the most coherent methodological thread across the otherwise different technologies.

### High-value secrets as both target and proof of impact

Secrets and private keys recur as concrete impact markers. The vault talk directly concerns repositories for secrets, credentials, and encryption keys [record_id:88]. The Cloudflare talk culminates in a claimed cross-worker extraction of a sensitive private key, using that result to demonstrate failure of same-process multi-tenant isolation [record_id:2630]. The framework study does not focus specifically on secret theft, but its system-prompt overwrite class includes compromise of trusted instructions, and its end-to-end demonstration allegedly ends in a shell [record_id:2648].

This use of secret access or host execution as proof distinguishes the records from findings limited to output manipulation. The presentations frame exploitability in terms familiar to enterprise and cloud defenders: control of a process, violation of tenant isolation, or loss of privileged material.

### Broadening scope from products to architectural classes

There is a visible expansion in research scope. The 2025 work names two vault products and two exploit chains [record_id:88]. One 2026 investigation begins with a single experimental Cloudflare feature but traces the affected layer into a production multi-tenant service, reporting five vulnerabilities and broader Workers impact [record_id:2630]. The other audits six frameworks and claims 11 CVEs, then abstracts the findings into three cross-framework attack classes [record_id:2648].

This suggests movement from product-specific exploitation toward reusable architectural models. Nevertheless, the records do not show that vault exploitation and agent-framework exploitation share specific vulnerable code patterns. Their connection is conceptual—misplaced trust and boundary failure—rather than evidence of a single technical root cause.

### No documented disagreement, but different defensive emphasis

The abstracts do not disagree with one another. Each favors deep technical review of layers assumed to be trusted. Their defensive emphasis differs according to subject matter: the vault briefing promises detection and prevention guidance [record_id:88]; the workerd briefing emphasizes reviewing native glue as part of the isolation boundary [record_id:2630]; and the framework briefing emphasizes keeping untrusted content in the data plane and protecting framework-managed logic, state, and instructions [record_id:2648].

## Methods, Tools, And Approaches Discussed

The vault research uses end-to-end exploit-chain construction against HashiCorp Vault and CyberArk Conjur. The abstract stresses remote code execution under default, out-of-the-box conditions and distinguishes a first claimed full RCE chain for HashiCorp Vault from a pre-authentication RCE chain for Conjur. It also promises live demonstrations and discussion of detection and prevention, although the raw record does not identify the component flaws, exploit prerequisites, instrumentation, indicators, or mitigations [record_id:88].

The Cloudflare work combines architecture analysis, native-code auditing, and exploit engineering. The researchers map CodeMode’s path from LLM-generated TypeScript into workerd and then identify JSG as the C++ bridge between JavaScript and native runtime APIs. They report five vulnerabilities, including two rated Critical by Cloudflare, and describe exploiting a use-after-free to escape the V8 isolate. The chain includes constructing read/write primitives, manipulating or “shaping” the heap for reliability, reaching native execution in the host, and using that access for cross-tenant private-key extraction [record_id:2630]. This record provides the corpus’s most detailed exploit-development workflow, though it still omits the vulnerable APIs, object lifetimes, affected versions, and technical artifacts required for reproduction.

The agent-framework investigation uses comparative auditing across LangChain, LangGraph, CrewAI, AutoGen, Microsoft Agent Framework, and Google ADK. It reports 11 responsibly disclosed CVEs, several described as Critical, and groups the findings into three attack classes:

1. **System-prompt overwrite**, in which attacker-controlled content rewrites trusted instructions.
2. **Orchestration compromise**, in which injected content corrupts framework routing, state, or control flow.
3. **Prompt-to-native exploitation**, in which prompt-driven logic reaches native parsing and causes memory corruption.

The authors’ proposed analytical model is to identify where untrusted content escapes the data plane and begins influencing framework-managed logic. Their stated demonstration moves from an initial prompt, across the framework boundary, to shell access [record_id:2648]. Importantly, this approach claims not to depend on a particular external tool, Model Context Protocol server, shell integration, browser, database, or filesystem API. The finding is framed as intrinsic to framework architecture rather than contingent on a dangerous tool configuration.

Across all three records, live or end-to-end demonstrations are an important communication method. The abstracts use full-chain outcomes to establish severity rather than stopping at isolated bugs: RCE in vaults [record_id:88], isolate escape and another tenant’s private key in Workers [record_id:2630], and prompt-to-shell compromise in agent frameworks [record_id:2648].

## Notable Talks, Records, And Evidence

“Vaulted Severance: Your Secrets Are Now Outies” is the earliest record and establishes the authors’ focus on compromising security-critical infrastructure itself. Its significance lies in the asserted combination of novelty, high-value targets, unauthenticated reachability, default configurations, and full-chain RCE. The HashiCorp Vault result is described as the first full RCE chain for the product, while the CyberArk Conjur result is presented as pre-authentication RCE [record_id:88]. If substantiated, these are high-impact findings because successful exploitation would place centralized credentials and keys at direct risk. However, the abstract alone does not reveal the two chains or substantiate the “first” claim.

“When Agentic Glue Melts: Exploiting Cloudflare CodeMode and Workers” is the most technically detailed record. It matters because the investigation reportedly expanded from an experimental LLM feature into production cloud infrastructure sharing the same runtime. The identification of JSG as an under-scrutinized isolation-boundary component is a distinctive contribution: it redirects scrutiny from V8 itself toward the native binding code around it. The record claims five vulnerabilities, two rated Critical, and describes a use-after-free chain involving isolate escape, heap shaping, native code execution, and cross-tenant key disclosure [record_id:2630]. Its broader security proposition is that same-process multi-tenancy can only be as strong as every native layer reachable across the isolate boundary.

“No Tools Required: Post-Injection Exploitation Across AI Agent Frameworks” offers the broadest comparative evidence and the clearest attempt at taxonomy. It claims an audit of six production-oriented frameworks and 11 disclosed CVEs, then distills the findings into system-prompt overwrite, orchestration compromise, and prompt-to-native exploitation. Its unique contribution is to argue that tool abuse is not required for serious post-injection impact: prompt-controlled content may compromise trusted framework internals directly [record_id:2648]. This reframes AI-agent defense away from merely restricting tools and toward enforcing integrity boundaries around orchestration, state, routing, memory, and system instructions.

The strongest evidence within the supplied material is descriptive specificity: named affected platforms, reported vulnerability counts, exploit stages, claimed severity ratings, and precise end-state demonstrations. The weakest aspect is verification. All three sources are promotional conference descriptions written in the voice of the presenters. None includes advisories, CVE numbers, vendor statements, patches, slides, recordings, proof-of-concept code, or independent technical analysis. Claims such as “novel,” “first,” “confirmed,” and “Critical” should therefore be treated as reported claims rather than independently established facts.

## Gaps, Limits, And Open Questions

The main limitation is source type. Conference abstracts summarize intended presentations but do not provide enough information to reproduce or fully assess the research. It is unclear from the records whether the demonstrations occurred exactly as described, whether disclosure and remediation were complete, or whether the affected systems remained vulnerable at the event dates.

For the vault findings, unanswered questions include:

- Which components and versions of HashiCorp Vault and CyberArk Conjur were affected?
- What primitives or individual vulnerabilities composed each RCE chain?
- Did “default” exploitation require network exposure, a specific deployment mode, or environmental assumptions?
- What CVEs, patches, configuration changes, detections, or indicators resulted?
- Was the HashiCorp chain pre-authentication, or is that property asserted only for Conjur?
- What evidence supports the claim that it was the first full Vault RCE chain? [record_id:88]

For the Cloudflare research, key gaps include:

- Which JSG APIs and object-lifetime errors produced the five vulnerabilities?
- What are their CVE or advisory identifiers, affected versions, and remediation status?
- How did CodeMode’s prompt-injection entry point produce attacker-controlled code, and what permissions or application design did that require?
- Which parts of the chain applied specifically to experimental CodeMode and which applied generally to Cloudflare Workers?
- Under what production conditions was cross-tenant exploitation possible?
- How did Cloudflare assign the two Critical ratings, and what severity did the remaining issues receive?
- What mitigations were added to JSG, workerd, or tenant isolation? [record_id:2630]

For the framework audit, the abstract does not map the 11 CVEs to the six frameworks or to the three attack classes. It also does not state whether every framework exhibited the same architectural failure, whether some findings required unusual application patterns, or which native parser was involved in prompt-to-native memory corruption. Further research should determine what “prompt-controlled” means in each case, whether indirect prompt injection is sufficient, what framework privileges are required, and how proposed data-plane separation can be enforced in practice [record_id:2648].

The corpus also leaves attribution unresolved. All records are coauthored with Shahar Tal, with no indication of Porat’s specific role in vulnerability discovery, exploit construction, disclosure, taxonomy development, or presentation. There are no solo-authored posts, technical papers, repositories, interviews, or biographical records from which to infer an independent research trajectory.

Finally, the apparent chronological trend must be interpreted cautiously. The three records suggest a move from enterprise vault exploitation in 2025 to AI-agent and cloud-runtime research in 2026, but the sample is too small to establish a durable career shift. The 2026 sessions may represent concurrent projects rather than a definitive change in focus.

## Coverage And Evidence Notes

All three expected records are substantive Black Hat Briefing descriptions and fit the topic through explicit authorship attribution to Yarden Porat, always alongside Shahar Tal.

The 2025 vault briefing covers full-chain remote exploitation of HashiCorp Vault and CyberArk Conjur, with emphasis on default configurations, pre-authentication risk in Conjur, live demonstrations, and defensive guidance [record_id:88]. It is the only record focused primarily on mature enterprise secret-management products rather than AI or cloud-agent infrastructure.

The Cloudflare briefing covers CodeMode, workerd, V8 isolates, the JSG native binding layer, five reported vulnerabilities, a use-after-free exploit chain, and alleged cross-tenant private-key disclosure in Cloudflare Workers [record_id:2630]. It provides the richest account of low-level exploit methodology and connects agentic tooling to production cloud isolation.

The cross-framework AI-agent briefing covers LangChain, LangGraph, CrewAI, AutoGen, Microsoft Agent Framework, and Google ADK; reports 11 disclosed CVEs; and proposes three post-injection attack classes reaching from trusted-instruction overwrite to memory corruption and shell access [record_id:2648]. It is the strongest source for the authors’ architectural model of prompt injection as framework exploitation rather than only behavioral manipulation or tool abuse.

No record is merely logistical or too weakly tied to the topic to require separate treatment. Nonetheless, the evidentiary base remains narrow: three coauthored conference abstracts, no full presentation content, and no independent corroboration. Downstream research should use these records as leads to associated advisories, CVE entries, vendor acknowledgments, slides, recordings, and patches rather than as complete technical documentation.