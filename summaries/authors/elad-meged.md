# Topic: Author: Elad Meged

## Meta-Summary

The four records attributed to Elad Meged describe offensive security research into systems that mistakenly treat intermediate state, internal interfaces, or startup inputs as trusted. Three records focus on AI coding agents—Anthropic Claude Code, Google Gemini CLI, and OpenAI Codex CLI—and argue that important vulnerabilities arise beneath or before the prompt layer, in workflow orchestration, sandbox enforcement, configuration loading, environment handling, and trust handoffs [record_id:2644] [record_id:2887] [record_id:2939]. The remaining record, coauthored with Lidor Ben Shitrit and Assaf Levkovich, applies a closely related line of reasoning to enterprise Java middleware, tracing unauthenticated paths through routing, authentication glue, unsafe deserialization, token trust, template expansion, and dynamic evaluation [record_id:2589].

Across the corpus, Meged’s recurring contribution is a methodology for deconstructing security boundaries rather than merely testing their stated policies. The records recommend identifying where a system declares data or state safe, following it through the actual runtime, and determining whether later components interpret it with greater authority. The reported consequences include pre-authentication remote code execution, shell execution, secret disclosure, persistence, policy bypass, and sandbox escape or circumvention [record_id:2589] [record_id:2644] [record_id:2887] [record_id:2939].

## Research Landscape

The corpus consists entirely of 2026 conference-talk descriptions: two Black Hat USA Briefings and two DEF CON 34 talks. These are presentation abstracts rather than full papers, source-code analyses, advisories, or independently reproduced technical reports. Consequently, they provide strong evidence of the researchers’ stated findings, targets, and methods, but limited detail with which to verify individual exploit chains.

AI-agent security dominates the collection. Three of the four records examine official coding-agent products or workflows. They deliberately shift attention away from prompt injection, jailbreaking, and model persuasion toward conventional software-security concerns: inconsistent parsing, unsafe startup inputs, environment propagation, trusted state reuse, enforcement-code assumptions, and execution paths outside the model [record_id:2644] [record_id:2887] [record_id:2939]. The named products recur across the records: Claude Code, Gemini CLI, and Codex or Codex CLI appear in both the cross-vendor workflow and sandbox discussions [record_id:2644] [record_id:2887], while Gemini CLI receives a dedicated pre-task remote-code-execution case study [record_id:2939].

The enterprise Java record is distinct in target technology but not in analytical style. It examines middleware as a hidden bridge from exposed, unauthenticated interfaces to privileged internal execution mechanisms. Its examples include permissive XStream configuration, an `ObjectInputStream` path without JEP-290 filtering, and Groovy evaluation reached through token-trust and template-expansion failures [record_id:2589]. Taken together, the records place Meged’s work at the intersection of exploit development, application security, platform security, and AI-agent infrastructure.

## Major Themes And Trends

### Trust decisions fail across component boundaries

The strongest recurring theme is that a security decision made by one component does not necessarily remain valid when another component consumes the resulting state. The Black Hat AI-agent briefing names this a “trust-handoff failure”: a product marks state as approved, sanitized, or safe, but a later component interprets it more powerfully than the approving component anticipated [record_id:2644]. Its examples span differential interpretation of shell arguments in Claude Code, incomplete or reversible environment sanitization in Gemini CLI, and attacker-written state later loaded as trusted instructions or execution context in Codex [record_id:2644].

The enterprise Java briefing presents a comparable pattern in middleware. Publicly exposed interfaces can be routed or dispatched toward internal-only execution surfaces; authentication glue and object-construction paths can transform apparently constrained input into unsafe deserialization or evaluation [record_id:2589]. Although the Java record does not use the same “trust-handoff” terminology, its exploit chains likewise depend on authority increasing as attacker-controlled data crosses internal layers.

### Security claims must be tested against actual runtime semantics

The records repeatedly distinguish intended containment from actual execution. In the sandbox talk, each vendor uses a different enforcement model—permission-based access control, process-level environment sanitization, or kernel-level filesystem enforcement—but each model allegedly depends on a structural assumption that the runtime violates [record_id:2887]. The research approach is therefore not to accept policy descriptions at face value, but to inspect enforcement code and compare its assumptions with real runtime behavior.

The same concern appears in the workflow briefing. Claude Code’s validation and execution stages interpret the same attacker-controlled argument differently, while Gemini CLI’s sanitized environment does not remain sanitized along the real execution path [record_id:2644]. These are forms of semantic mismatch: the security layer validates one representation or lifecycle stage, while the execution layer acts on another.

### AI-agent security extends beyond prompts and models

A major trend across the AI records is an explicit rejection of prompt-centric security analysis as sufficient. The sandbox research says its exploits do not require prompt injection or model persuasion and instead arise from architectural gaps in containment [record_id:2887]. The dedicated Gemini CLI talk moves even earlier, examining configuration files, environment variables, startup parameters, and protocol handshakes processed before the model receives its first task [record_id:2939].

This pre-task framing is especially consequential for CI/CD. According to the record, headless execution, automatic workspace trust, and the absence of a human approval loop can allow startup inputs to reach shell execution or disable controls before the sandbox begins [record_id:2939]. The resulting thesis is that prompt guardrails are irrelevant if the surrounding agent process is already compromised.

### Deterministic exploit paths are emphasized over probabilistic model behavior

The AI talks stress deterministic, implementation-level exploits. The sandbox talk characterizes every demonstrated exploit as deterministic and based on containment design rather than persuading a model to behave unpredictably [record_id:2887]. The Gemini CLI case similarly claims that its flagship exploit requires no model interaction and executes before sandbox startup [record_id:2939]. This positions AI-agent exploitation as conventional systems and application security applied to AI-enabled products, rather than as a problem dependent on uncertain language-model outputs.

### Cross-vendor repetition suggests a systemic design class

Meged’s records do not present the agent findings merely as isolated product bugs. The workflow briefing says that the same trust-handoff failure recurs across Anthropic, Google, and OpenAI [record_id:2644]. The sandbox talk argues that independently designed products make structurally similar mistakes despite using different containment models [record_id:2887]. The Gemini CLI talk adds that a separate case from another, unnamed vendor supports the broader pre-task-input pattern [record_id:2939].

The collective claim is therefore taxonomic: official agent workflows share predictable failure modes because they must bridge untrusted workspaces, model-driven actions, local runtimes, credentials, and unattended automation. The evidence is suggestive across three prominent vendors, though the abstracts do not establish prevalence beyond the examined products.

### Pre-authentication execution is a concern across different technology domains

Two records foreground code execution before a conventional trust gate has taken effect. The Java briefing describes multiple pre-authentication RCE chains that traverse middleware to reach privileged internal endpoints and dangerous execution sinks [record_id:2589]. The Gemini CLI talk describes “pre-task” RCE that triggers before model processing and before sandbox startup [record_id:2939]. These are not the same vulnerability class, but both focus on execution occurring earlier than defenders expect: before authentication in enterprise middleware or before prompt and sandbox protections in an AI-agent lifecycle.

## Methods, Tools, And Approaches Discussed

The records advocate a trace-based audit methodology. For official agent workflows, researchers should locate the point at which a product labels input or state as approved, sanitized, or otherwise trusted; follow that exact state into later stages; and test whether later consumers can turn it into execution, secret disclosure, persistence, or policy bypass [record_id:2644]. This method focuses on the lifecycle of state rather than evaluating each component in isolation.

For sandbox analysis, the proposed workflow is to identify the containment mechanism, read its enforcement code, determine the structural assumption on which enforcement depends, and test that assumption against real runtime behavior [record_id:2887]. The records identify three broad containment architectures: permission-based access control, process-level environment sanitization, and kernel-level filesystem enforcement [record_id:2887]. The abstract does not map each architecture explicitly to a named product, so that association should not be inferred without the full talk.

For pre-task agent analysis, the method begins by enumerating all inputs accepted before normal work starts. Examples include configuration files, environment variables, startup parameters, and protocol handshakes. The researcher then maps the authority carried by each input and checks whether it can reach command execution or alter policy controls [record_id:2939]. This approach is particularly relevant to CI/CD and other headless environments where workspaces may be automatically trusted.

The agent records also point to several concrete failure mechanisms:

- Differential parsing or interpretation between an approval rule and the eventual command executor, enabling arbitrary shell command execution [record_id:2644].
- Environment sanitization that fails to persist through the actual execution path, allowing secrets to remain reachable or stripped state to be reintroduced [record_id:2644].
- Attacker-controlled workflow state that is later reloaded as trusted instructions or context, creating persistence and policy loss [record_id:2644].
- Containment systems whose runtime behavior violates assumptions embedded in their enforcement design [record_id:2887].
- Startup or pre-task inputs that reach shell execution or disable controls before prompt-time and sandbox defenses activate [record_id:2939].

The enterprise Java research uses exploit-chain reconstruction through middleware internals. Its flagship case follows an unauthenticated request from an exposed API surface through routing and dispatch behavior into privileged internal endpoints, then toward multiple unsafe deserialization sinks. Named mechanisms include permissive XStream configuration and a separate `ObjectInputStream` path lacking JEP-290 filtering [record_id:2589]. A second chain combines token-trust failure with template expansion and Groovy evaluation to achieve direct code execution [record_id:2589]. The multiplicity of sinks matters because it suggests that fixing one deserialization route may not remove the broader reachability or trust-boundary defect.

Coordinated disclosure is also part of the reported research practice. The sandbox talk says every exploit was reported through coordinated disclosure [record_id:2887]. The Gemini CLI record says its flagship vulnerability was publicly disclosed and patched, received a CVSS 10.0 score from Google’s security team, and links to a GitHub security advisory [record_id:2939]. These statements strengthen the evidence that at least some vendor validation and remediation occurred, although the corpus does not include the advisory’s technical contents.

## Notable Talks, Records, And Evidence

“Trusted Enough to Run: Breaking AI Agents in Official Workflows” is the clearest statement of Meged’s cross-product trust-handoff thesis. It compares official workflows from Anthropic, Google, and OpenAI and identifies distinct consequences in each: shell execution in Claude Code, secret exposure and state reintroduction in Gemini CLI, and persistence or policy loss through trusted state loading in Codex [record_id:2644]. Its importance lies less in any single exploit than in the proposed general audit question: after a component declares state safe, what can downstream components actually do with it?

“The Sandbox is a Suggestion: Deconstructing AI Agent Sandboxes” broadens this thesis into a comparative analysis of containment architecture. It claims that three different sandbox models fail because of incorrect structural assumptions and emphasizes deterministic exploitation grounded in implementation behavior rather than prompt manipulation [record_id:2887]. This is the most direct record for understanding Meged’s view that AI-agent security should be studied as runtime and systems security.

“No Prompt Required: Pre-Task RCE in Google Gemini CLI” supplies the corpus’s most concrete AI-agent vulnerability claim. The talk describes a publicly disclosed and patched Gemini CLI exploit rated CVSS 10.0 by Google’s security team. It allegedly requires no model interaction, executes before the sandbox starts, and exploits authority available through inputs processed before the first task [record_id:2939]. The linked advisory offers a potential path for downstream researchers to corroborate the abstract, but the present report treats only the supplied raw record text as evidence.

“Pre-auth RCE in Enterprise Java: When Middleware Becomes the Exploit” demonstrates that Meged’s trust-path analysis is not limited to AI systems. Coauthored with Lidor Ben Shitrit and Assaf Levkovich, it reports multiple real-world pre-authentication RCE chains in widely deployed enterprise Java platforms [record_id:2589]. It is technically notable for identifying multiple deserialization sinks and a separate Groovy-evaluation chain, while framing middleware routing, dispatch, and authentication integration as part of the exploitable attack surface rather than as neutral plumbing [record_id:2589].

Evidence strength varies by claim. The conference records provide direct evidence that these talks and assertions were scheduled or described, and several abstracts identify products and mechanisms precisely. The Gemini CLI record adds a claim of vendor scoring, public disclosure, and patching [record_id:2939], while the sandbox record claims coordinated disclosure across all demonstrated exploits [record_id:2887]. Nevertheless, no exploit code, patch diff, affected-version range, reproduction procedure, or vendor response is contained in the four raw records. Detailed technical conclusions should therefore be checked against the talks, advisories, or product repositories.

## Gaps, Limits, And Open Questions

The largest limitation is source type. All four records are abstracts for future or scheduled 2026 conference presentations, not complete technical publications. They describe results and methodologies but omit enough implementation detail to prevent independent reproduction from this corpus alone. It is unclear which exact product versions were affected, what prerequisites each exploit required, how the vendors patched the issues, and whether related weaknesses remain.

The relationship among the three AI-agent talks is also not fully resolved. They share products and concepts, and the Gemini CLI findings in the workflow and sandbox talks may overlap with the dedicated pre-task RCE case [record_id:2644] [record_id:2887] [record_id:2939]. The records do not specify whether these are separate vulnerabilities, different stages of one exploit chain, or alternative presentations of the same research. Downstream work should compare vulnerability identifiers, advisories, timelines, and patch commits.

The abstracts provide little information about threat models. Questions remain about whether exploitation requires a malicious repository, control of configuration or workflow files, compromised dependencies, access to CI inputs, or another foothold. The Gemini record notes automatically trusted workspaces in headless CI/CD [record_id:2939], but it does not define the exact attacker capabilities. Similarly, the Java record does not name affected platforms or clarify whether default configurations were exploitable [record_id:2589].

The proposed mitigations remain high-level. The Java talk promises practical guidance for finding and fixing hidden pre-authentication execution paths, but the abstract does not state that guidance beyond identifying relevant middleware layers and unsafe sinks [record_id:2589]. The AI talks provide strong audit heuristics but do not specify robust architectural remedies for preserving trust labels, canonicalizing arguments, preventing environment reintroduction, authenticating persisted state, or sequencing sandbox initialization safely [record_id:2644] [record_id:2887] [record_id:2939].

Open research questions include:

- How should agent platforms represent provenance and trust so that later components cannot silently reinterpret earlier-approved state?
- Can approval, sanitization, and execution be made to use one canonical representation and parser?
- Which security controls must initialize before configuration, workspace discovery, or protocol negotiation?
- How can CI/CD agents avoid automatically granting authority to repository-controlled startup state?
- Are similar trust-handoff and pre-task vulnerabilities present in other coding agents, autonomous workflow systems, or plugin ecosystems?
- In enterprise Java, how widely do middleware dispatch and authentication layers expose internal deserialization, template, or evaluation surfaces?
- Do fixes address only individual sinks, or do they remove the routing and authority escalation that make those sinks reachable?

## Coverage And Evidence Notes

All four expected records materially contribute to the topic.

The enterprise Java record is the only non-AI item and the only coauthored work. It supports findings about pre-authentication RCE, hidden middleware reachability, unsafe deserialization through XStream and `ObjectInputStream`, absent JEP-290 filtering, token-trust failures, template expansion, and Groovy evaluation [record_id:2589].

The Black Hat AI-agent workflow briefing is the central source for the cross-vendor “trust-handoff” framing and provides named examples involving Claude Code, Gemini CLI, and Codex [record_id:2644].

The DEF CON sandbox talk supplies the comparative containment analysis, the emphasis on deterministic non-prompt exploitation, and the methodology of inspecting enforcement mechanisms and their structural assumptions [record_id:2887].

The dedicated Gemini CLI talk supplies the pre-task-input model, the CI/CD context, and the strongest disclosure claim: a patched, publicly disclosed exploit reportedly rated CVSS 10.0 by Google’s security team [record_id:2939].

Because the records are presentation abstracts, claims about successful exploitation, severity, disclosure, and vendor impact are best treated as author-reported evidence pending review of full talks, advisories, patches, and independent reproductions. Even with that limitation, the corpus consistently portrays Elad Meged’s research as focused on tracing attacker-controlled state through real execution paths and finding the point where an internal trust assumption becomes executable authority.