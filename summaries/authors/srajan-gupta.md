# Topic: Author: Srajan Gupta

## Executive Summary

The two records attributed to Srajan Gupta present a focused body of work around the security implications of AI-assisted software development, especially where AI agents connect to external context, tools, data, and workflows. Both records center on the Model Context Protocol, or MCP, but from different angles: one as a defensive mechanism for injecting application-security context into AI coding workflows, and the other as an attack surface that can expose organizations to new classes of agentic AI vulnerabilities.

Collectively, the records suggest that Gupta’s work emphasizes a practical security-engineering view of AI developer tooling. The 2026 UNPROMPTED talk, “Injecting Security Context During Vibe Coding,” frames AI coding assistants such as Cursor as productivity accelerators that may bypass traditional application-security controls unless security context is brought directly into the coding loop [record_id:2373]. The 2025 BSidesLV talk, co-authored with Vinay Kumar, examines MCP itself as a protocol layer that enables AI agents to interact with tools, data, and services, while also creating risks such as tool poisoning, shared-memory exploits, version drift, and line-jumping attacks [record_id:2554].

The strongest theme across the records is that AI-assisted development and agentic workflows require security controls to move closer to the AI interaction layer. Instead of relying only on post-hoc code review, static analysis, or conventional AppSec gates, these talks point toward security-aware context injection, validation before and after generation, and careful threat modeling of the protocols that connect AI systems to tools and services [record_id:2373], [record_id:2554].

## Research Landscape

The available corpus is small, consisting of two conference-style records. Both are talks, not blog posts, papers, code repositories, or long-form technical writeups. One record comes from UNPROMPTED2026 and lists Srajan Gupta as the sole author/speaker [record_id:2373]. The other comes from BSidesLV 2025 and lists Srajan Gupta together with Vinay Kumar [record_id:2554]. Because both records are abstracts or talk descriptions rather than full transcripts, the evidence is useful for identifying themes and intended contributions, but it is limited for reconstructing detailed technical implementations.

The records sit at the intersection of three overlapping research areas:

1. **AI-assisted software development and developer tooling.**  
   The UNPROMPTED2026 record explicitly discusses “vibe coding with AI tools like Cursor” and the way such workflows can bypass established AppSec processes [record_id:2373].

2. **Application security for AI-generated code.**  
   Gupta’s 2026 talk proposes injecting threat models, security requirements, and OWASP guidance into the AI coding loop before code generation, then verifying generated output afterward for vulnerabilities and compliance with security standards [record_id:2373].

3. **AI-agent protocol security.**  
   The BSidesLV 2025 talk focuses on MCP as a protocol for connecting AI agents to tools, data, and services, and argues that its integration model exposes critical vulnerabilities [record_id:2554].

The overall landscape is therefore not general AI safety or broad model-alignment research. It is more specifically about securing the operational layer where AI systems become useful to developers: the agent, protocol, tool, memory, and code-generation interfaces. The records portray Gupta’s contributions as practical and demonstration-oriented. Both descriptions refer to demos or examples: the UNPROMPTED talk says it will “demo an MCP server” that injects security context into AI coding workflows [record_id:2373], while the BSidesLV abstract says attendees will learn through “real-world examples and demonstrations” [record_id:2554].

## Major Themes And Trends

### Security controls must move into the AI coding loop

A central theme is that traditional AppSec controls may be poorly aligned with AI-assisted coding practices. The UNPROMPTED record states that “vibe coding with AI tools like Cursor is fast,” but that it “quietly bypasses traditional AppSec controls” [record_id:2373]. This identifies a process-level security problem: if developers increasingly rely on AI assistants to generate code rapidly, then security checks that assume slower, more deliberate development workflows may be skipped, delayed, or rendered ineffective.

Gupta’s proposed response is not simply to warn developers against AI coding. Instead, the talk describes an MCP server that inserts security guidance directly into the workflow. Before code is generated, the system “pulls threat models, security requirements, and OWASP guidance for your task”; after generation, it “verifies the output for vulnerabilities and if it meets the security standards” [record_id:2373]. This reflects a trend toward embedded, workflow-native security: bringing controls to the developer and the AI assistant at the moment of generation.

### MCP appears both as an enabler and as an attack surface

The two records treat MCP in complementary ways. In the 2026 talk, MCP is part of the solution architecture: an MCP server is used to inject security context into the coding loop [record_id:2373]. In the 2025 BSidesLV talk, MCP is itself the subject of scrutiny: it is described as “rapidly becoming the standard for connecting AI agents to tools, data, and services,” but also as exposing “critical security vulnerabilities” beneath its “streamlined facade” [record_id:2554].

This dual framing is important. Gupta’s work does not present MCP as inherently good or bad. Instead, the records suggest that MCP is a powerful integration layer whose security properties must be understood. It can be used to deliver security context and enforce standards [record_id:2373], but it can also introduce new attack vectors through malicious tool descriptions, unsafe shared context, unversioned tools, and attacks that occur before explicit tool invocation [record_id:2554].

### Context is both a defensive asset and a liability

Both records revolve around context. In the UNPROMPTED talk, context is defensive: threat models, requirements, and OWASP guidance are supplied to the AI system so that generated code is informed by the relevant security constraints [record_id:2373]. In the BSidesLV talk, context can be dangerous: “Shared Memory Exploits” are described as arising from “unvalidated context sharing among agents” [record_id:2554].

This creates a recurring tension. AI agents and coding assistants need context to perform useful work, but context channels can become avenues for manipulation, leakage, or unintended behavior. The records therefore point to a security model in which context must be curated, validated, scoped, and monitored. Context injection is not automatically safe; it depends on the trustworthiness of the inputs and the integrity of the protocol and tools through which that context is delivered.

### Agentic systems introduce pre-invocation and indirect attack paths

The BSidesLV record highlights attacks that do not map neatly to older security models. “Tool Poisoning” involves malicious tool descriptions that manipulate AI behavior [record_id:2554]. “Line Jumping Attacks” are described as exploits that occur “before any tool is explicitly invoked” [record_id:2554]. These examples imply that agentic AI systems may be influenced not only by direct user prompts or explicit tool calls, but also by metadata, descriptions, memory, and protocol interactions that shape model behavior before conventional execution boundaries are crossed.

This theme complements the 2026 record’s concern that AI-assisted development bypasses traditional AppSec controls [record_id:2373]. Both records suggest that new security boundaries are forming around agent orchestration, tool metadata, and model context rather than only around application code, APIs, or infrastructure.

### Practical mitigation is emphasized, though details are limited

Both records promise actionable content. The 2026 talk describes a specific workflow: pull threat models, security requirements, and OWASP guidance before generation; verify generated code afterward [record_id:2373]. The 2025 talk says it will explain the threats and “the steps necessary to mitigate them” [record_id:2554]. However, because the records are abstracts, they do not provide full mitigation catalogs, implementation details, code, test cases, or empirical results. The practical orientation is clear, but the evidence available here is high-level.

## Methods, Tools, And Approaches Discussed

The most concrete method described is the use of an MCP server as a security-context broker inside an AI-assisted coding workflow. In the UNPROMPTED2026 talk, Gupta proposes an MCP server that interacts with the AI coding loop before and after code generation. Before code is produced, it retrieves relevant threat models, security requirements, and OWASP guidance. After code is generated, it checks whether the output contains vulnerabilities and whether it satisfies security standards [record_id:2373].

This approach combines several security practices:

- **Threat-model retrieval.** The system uses existing threat models as input to the AI coding process, implying that threat modeling artifacts can become machine-consumable context rather than static documentation [record_id:2373].
- **Security-requirements injection.** Requirements are supplied before generation, shifting security from a review-only phase to a design-and-generation phase [record_id:2373].
- **Standards-based guidance.** The reference to OWASP guidance suggests use of established application-security knowledge as context for generated code [record_id:2373].
- **Post-generation verification.** The workflow includes checking the generated output for vulnerabilities and conformity with security standards [record_id:2373].

The BSidesLV 2025 record discusses methods more from an offensive and diagnostic perspective. It names several vulnerability classes associated with MCP:

- **Tool poisoning.** Malicious tool descriptions can manipulate AI behavior [record_id:2554].
- **Shared-memory exploits.** Unvalidated context sharing among agents can create security hazards [record_id:2554].
- **Version drift.** Unversioned tools can lead to unexpected behaviors [record_id:2554].
- **Line-jumping attacks.** Some exploits can occur before a tool is explicitly invoked [record_id:2554].

The record does not provide detailed exploit mechanics, but the listed categories indicate an approach centered on protocol analysis, agent-tool interaction testing, and adversarial examination of agent context flows. The mention of “real-world examples and demonstrations” suggests that the talk likely uses concrete scenarios rather than purely theoretical discussion [record_id:2554].

Taken together, the methods point toward a security program for AI developer tooling that includes both defensive integration and adversarial protocol assessment: build mechanisms to inject trusted security context, but also threat model and test the channels through which that context, tools, and memory are exposed [record_id:2373], [record_id:2554].

## Notable Talks, Records, And Evidence

The most directly relevant record for Gupta’s work on AI-assisted secure development is “Injecting Security Context During Vibe Coding,” presented at UNPROMPTED2026. The talk identifies a specific problem: AI coding tools such as Cursor accelerate development but can bypass traditional AppSec controls [record_id:2373]. Its proposed contribution is a demonstrated MCP server that inserts security context before code generation and verifies the generated code afterward [record_id:2373]. This record is important because it frames MCP not merely as infrastructure for AI agents, but as a mechanism for operationalizing application security inside the coding workflow.

The BSidesLV 2025 talk, “The Protocol Behind the Curtain: What MCP Really Exposes,” is important because it broadens the analysis from secure coding assistance to the security of MCP itself [record_id:2554]. The abstract describes MCP as an emerging standard for connecting AI agents to tools, data, and services, and then enumerates concrete risk categories: tool poisoning, shared-memory exploits, version drift, and line-jumping attacks [record_id:2554]. This record is representative of Gupta’s apparent concern with the hidden attack surface created by agent-tool integration layers.

Together, the two records are mutually reinforcing. The 2025 BSidesLV talk helps explain why MCP-enabled systems need threat modeling and mitigation: the protocol can expose subtle vulnerabilities in tool descriptions, memory sharing, tool versioning, and pre-invocation behavior [record_id:2554]. The 2026 UNPROMPTED talk then shows a constructive security use case for MCP: using an MCP server to inject trusted security knowledge and validate AI-generated code [record_id:2373]. The pair gives downstream researchers a coherent view of Gupta’s work as both critical and constructive: identifying risks in agentic protocols while also proposing ways those protocols can be used to improve security outcomes.

## Gaps, Limits, And Open Questions

The main limitation is that the corpus contains only two short records, both of which are talk abstracts rather than full presentations, transcripts, slides, papers, or source code. As a result, the available evidence supports high-level thematic conclusions but not detailed technical claims about implementation, efficacy, or completeness.

Several open questions remain:

- **How exactly does the MCP security-context server work?**  
  The UNPROMPTED record says it pulls threat models, security requirements, and OWASP guidance before generation, then verifies output afterward [record_id:2373]. It does not describe the architecture, data formats, retrieval mechanism, policy language, integration with Cursor, or the vulnerability-detection method.

- **How are threat models and requirements mapped to a coding task?**  
  The 2026 talk implies task-specific retrieval of security context [record_id:2373], but the record does not explain how tasks are classified, how relevant controls are selected, or how stale or conflicting requirements are handled.

- **What verification techniques are used after generation?**  
  The record mentions checking generated output for vulnerabilities and standards compliance [record_id:2373], but it does not specify whether this involves static analysis, LLM-based review, rules engines, tests, policy-as-code, manual review, or a combination.

- **What are the concrete exploit mechanics for MCP attacks?**  
  The BSidesLV record lists tool poisoning, shared-memory exploits, version drift, and line-jumping attacks [record_id:2554], but it does not provide payloads, example protocols, affected implementations, severity ratings, or mitigations in the raw text.

- **How generalizable are