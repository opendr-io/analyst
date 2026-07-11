# Topic: Author: Michael Bargury

## Executive Summary

The two records attributed to Michael Bargury present a focused body of work around offensive and defensive security for generative AI systems, especially enterprise AI assistants and agentic workflows. Together, they show Bargury concentrating on a rapidly emerging class of AI-enabled enterprise compromise: prompt-injection-driven misuse of assistants and agents, jailbreak transferability across models, and the challenge of building practical defenses when AI systems can read sensitive enterprise context and invoke tools on behalf of users.

The strongest record is a Black Hat USA 2025 briefing abstract co-authored with Tamir Ishay Sharbat, which frames enterprise AI assistants as an attack surface capable of supporting initial access, persistence, data harvesting, exfiltration, and impact with minimal or even zero user interaction. It emphasizes “0click attacks,” vulnerability chains across major enterprise AI assistants, and the need to manage prompt injection as an ongoing security problem rather than treat it as a conventional patchable bug [record_id:71].

The second record, from Prompt||GTFO in 2026, is narrower and more tool-oriented. It describes Bargury demonstrating an open-source tool, “chatbot.ai,” for testing jailbreaks across multiple models and configurations simultaneously. It also highlights his development workflow using Claude for planning, security review, and nightly build prompts [record_id:2212]. This complements the Black Hat record by moving from enterprise attack chains and mitigation frameworks toward repeatable testing infrastructure and AI-assisted development practices.

Collectively, the records position Bargury’s work at the intersection of AI red teaming, enterprise application security, prompt injection, jailbreak evaluation, and practical security engineering for AI agents.

## Research Landscape

The record set is small—only two records—but coherent. Both records concern AI security, with particular emphasis on generative AI systems that interact with enterprise data, user context, tools, and external prompts. The included sources are event/talk descriptions rather than full papers, code repositories, or technical writeups. As a result, the evidence is useful for understanding Bargury’s public research themes and claimed contributions, but limited for independently validating technical details.

The Black Hat USA 2025 record presents a high-level briefing abstract about enterprise AI compromise. It describes an offensive research agenda involving “access-to-impact AI vulnerability chains” in flagship enterprise AI assistants including ChatGPT, Gemini, Copilot, Einstein, and a custom agent [record_id:71]. It also claims demonstrations of attacks requiring either a single bad click or no user interaction at all, framed as “0click attacks” [record_id:71]. This record dominates the research landscape because it covers threat models, attack lifecycle stages, affected platforms, mitigations, and a proposed framework called the “GenAI Attack Matrix” [record_id:71].

The Prompt||GTFO 2026 record is shorter and more practical. It describes a demonstration of “chatbot.ai,” an open-source tool built by Bargury for testing AI jailbreaks across multiple models simultaneously [record_id:2212]. Unlike the Black Hat abstract, which emphasizes enterprise compromise and agentic assistant exploitation, this record emphasizes experimentation infrastructure: configurable API keys, system instructions, temperatures, and models, with the goal of assessing whether jailbreaks transfer across model families [record_id:2212].

Taken together, the records suggest that Bargury’s public work is not limited to one-off prompt injection examples. Instead, it spans attack chains, defensive frameworks, multi-model jailbreak testing, and AI-enabled development workflows. However, because both records are summaries rather than full technical artifacts, downstream researchers should treat them as pointers to talks and demonstrations rather than exhaustive documentation.

## Major Themes And Trends

### Enterprise AI Assistants As High-Impact Attack Surfaces

The central theme in the record set is that AI assistants and agents are becoming embedded in enterprise environments deeply enough to create new compromise paths. The Black Hat record argues that compromising an enterprise “used to require careful planning, proper resources, and the ability to execute,” but that AI changes this dynamic by allowing attackers to operate through AI systems acting on behalf of users [record_id:71]. The abstract frames AI assistants as systems with access to user data, enterprise tools, and operational context.

The record specifically names several stages of an attack lifecycle: initial access, persistence, data harvesting, exfiltration, and impact [record_id:71]. This language suggests an attempt to map AI exploitation into familiar enterprise security concepts rather than treating prompt injection as an isolated application bug. For example, persistence is described as self-replication through corporate documents, data harvesting as enabled by AI’s tendency to collect or access large stores of information, and exfiltration as possible through rendered images [record_id:71].

This is one of the most important conceptual contributions in the records: Bargury’s work appears to frame enterprise AI assistants not merely as chat interfaces but as active security principals that can be hijacked into performing attacker-directed actions.

### Shift From Assistants To Agents

A second theme is the worsening risk profile as AI assistants become agents. The Black Hat record states that “AI assistants have morphed into agents” and that these agents read search history, emails, and chat messages while wielding tools that can manipulate the enterprise environment on behalf of users—or on behalf of a malicious attacker once hijacked [record_id:71]. This reflects a broader trend in AI security: the move from passive text generation toward tool-using systems with permissions, memory, retrieval, browsing, and workflow automation.

The record implies that the transition to agents increases both reach and impact. If a model can only generate text, prompt injection may cause misleading output. If an agent can read sensitive enterprise context and invoke tools, the same class of manipulation may support compromise chains. The Black Hat abstract explicitly connects this agentic capability to “access-to-impact AI vulnerability chains” across major enterprise AI assistants [record_id:71].

The Prompt||GTFO record also fits this trend, though from a tooling angle. It describes AI jailbreak testing across models and configurations, including control over system instructions, temperatures, and model selection [record_id:2212]. This reflects the need to evaluate behavior not just in one model, but across increasingly diverse AI application stacks.

### Prompt Injection And Jailbreaking As Managed Security Risks

The Black Hat record makes a strong claim: “Prompt injection is not another bug we can fix. It is a security problem we can manage” [record_id:71]. This is a key theme. Rather than presenting prompt injection as a vulnerability class that can be eliminated by patching a model or filtering a string, the record positions it as a persistent risk requiring frameworks, mitigations, detection, and operational management.

The proposed response is the “GenAI Attack Matrix,” described as a security framework to help protect organizations [record_id:71]. The abstract says the presenters will compare mitigations from AI vendors, identify which mitigations prevent the worst 0click attacks, and break down their attacks into basic tactics, techniques, and procedures that can be detected and mitigated [record_id:71]. This suggests a move toward standardization and operationalization: attack taxonomy, mitigation comparison, and detection engineering.

The Prompt||GTFO record complements this by focusing on jailbreak testing infrastructure. Bargury’s “chatbot.ai” tool is described as enabling users to run one prompt against many model configurations to determine if jailbreaks transfer across model families [record_id:2212]. That implies a practical recognition that jailbreak behavior is empirical and variable: defenders and researchers need tooling to test prompts across models, temperatures, system instructions, and providers.

### Multi-Platform And Cross-Model Evaluation

Both records emphasize breadth across AI systems. The Black Hat abstract names multiple enterprise assistants—ChatGPT, Gemini, Copilot, Einstein, and a custom agent—as targets for demonstration [record_id:71]. This suggests the research is not limited to a single vendor implementation. The Prompt||GTFO record similarly describes running prompts across multiple model configurations, including different API keys, system instructions, temperatures, and models [record_id:2212].

The recurring concern is transferability. In the enterprise compromise record, transferability appears as a platform-wide issue: multiple flagship assistants may be susceptible to related classes of vulnerability chains [record_id:71]. In the jailbreak testing record, transferability is explicit: the tool helps determine whether jailbreaks transfer across model families [record_id:2212].

This theme is important for downstream researchers because it suggests Bargury’s work may be useful in comparative AI security evaluation. Rather than asking only whether a single prompt works against one model, the records encourage asking whether an attack pattern generalizes across architectures, vendors, system prompts, tool integrations, and deployment contexts.

### AI-Assisted Security Engineering And “Vibe-Coding”

A smaller but notable theme appears in the Prompt||GTFO record: Bargury’s own development process uses Claude for “vibe-coding,” including automated plan generation, security reviews, and nightly build prompts [record_id:2212]. This differs from the attack-focused material in the Black Hat abstract, but it is still relevant. It shows AI being used not only as a target of security testing but also as part of the development and security review workflow.

The evidence here is thin because the record is a brief description, not a detailed methodology. Still, it points to a possible secondary area of interest: AI-assisted creation of security tooling, with LLMs participating in planning, code generation, review, and iterative builds [record_id:2212].

## Methods, Tools, And Approaches Discussed

The records describe several methods and approaches, though mostly at the level of talk abstracts rather than implementation details.

One major approach is the construction and demonstration of “access-to-impact AI vulnerability chains” against enterprise AI assistants [record_id:71]. The Black Hat record frames these chains in terms familiar to enterprise security: initial access, persistence, data harvesting, exfiltration, and impact [record_id:71]. It claims that some attacks require a victim click while others require no user interaction, described as “0click attacks” [record_id:71]. This suggests a methodology of chaining AI-specific weaknesses into full attack paths rather than demonstrating isolated prompt-injection effects.

Another approach is breaking attacks into basic TTPs for detection and mitigation. The Black Hat abstract says the presenters will dissect their attacks, break them down into basic tactics, techniques, and procedures, and show how they can be detected and mitigated [record_id:71]. This is significant because it links AI exploitation to security operations practices such as detection engineering, threat hunting, and control validation.

The “GenAI Attack Matrix” is the major named framework in the records. It is described as a security framework intended to help organizations protect themselves against AI-related attacks [record_id:71]. The abstract does not provide the matrix contents, categories, or maturity model, so downstream researchers would need the full briefing, slides, or related publications to analyze it in detail. Still, its inclusion indicates an effort to provide structured guidance rather than only offensive demonstrations.

The second record introduces “chatbot.ai,” described as an open-source tool for testing AI jailbreaks across multiple models simultaneously [record_id:2212]. The tool reportedly allows configuration of API keys, system instructions, temperatures, and models, then runs one prompt across many configurations [record_id:2212]. This supports comparative jailbreak testing and transferability analysis. In practical terms, such a tool could help researchers answer questions like whether a jailbreak is model-specific, prompt-template-specific, system-prompt-sensitive, or robust across providers.

The Prompt||GTFO record also describes Bargury using Claude in a development workflow that includes automated plan generation, security reviews, and nightly build prompts [record_id:2212]. This is a method for building or iterating on security tooling with AI assistance. However, the record does not provide enough detail to evaluate reliability, safeguards, or reproducibility.

## Notable Talks, Records, And Evidence

The most substantial record is the Black Hat USA 2025 briefing, “AI Enterprise Compromise - 0click Exploit Methods,” co-authored by Michael Bargury and Tamir Ishay Sharbat [record_id:71]. Its importance lies in its broad enterprise threat model. It claims that external attackers can exploit AI assistants without credentials, phishing, social engineering, or human-in-the-loop interaction, potentially achieving “in-and-out with a single prompt” [record_id:71]. It also claims demonstrations across major enterprise AI assistants and positions 0click prompt-injection-style exploitation as a serious unresolved industry problem [record_id:71].

This record is representative of Bargury’s higher-level security framing: enterprise AI systems are not merely productivity features but attack surfaces with access to sensitive data and tool permissions. The abstract’s reference to previous Black Hat USA work on “living off Microsoft Copilot” suggests continuity from earlier Copilot-focused enterprise AI exploitation toward broader multi-assistant and agent-focused attack chains [record_id:71]. The current record claims that the situation has changed “for the worse” as assistants become agents with deeper access to user history, email, chat, and tools [record_id:71].

The Prompt||GTFO 2026 record, “AI Sandboxing with Agents,” is notable because it shows a more concrete testing-oriented contribution: the “chatbot.ai” open-source tool [record_id:2212]. Its value is in operationalizing jailbreak research. Instead of testing prompts manually against one model at a time, the tool is described as enabling simultaneous multi-model testing with configurable parameters [record_id:2212]. This record also provides insight into Bargury’s development style, noting his use of Claude for planning, security reviews, and nightly build prompts [record_id:2212].

In terms of evidence strength, record 71 is strong for identifying Bargury’s public claims, framing, and intended demonstrations, but not sufficient for independently confirming exploit feasibility or mitigation effectiveness. Record 2212 is strong for identifying a tool and workflow focus, but sparse on technical implementation details.

## Gaps, Limits, And Open Questions

The biggest limitation is the small record set. With only two records, the report can identify recurring