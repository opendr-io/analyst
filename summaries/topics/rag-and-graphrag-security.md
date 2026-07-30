# Topic: RAG and GraphRAG security

## Meta-Summary

The records portray retrieval as both a powerful grounding mechanism and a major security boundary. RAG and GraphRAG can enrich cloud-security reasoning, SOC automation, compliance mapping, and threat analysis, but they also introduce attack surfaces around document integrity, vector embeddings, context assembly, persistent memory, external tools, and delegated authority. The central security concern is no longer only whether an attacker can directly jailbreak a model; it is whether an attacker can influence, poison, extract, or misuse the information and capabilities supplied to an agent through its retrieval pipeline.

The collection emphasizes three recurring risks: poisoning retrieved evidence to manipulate decisions, extracting sensitive information from models or vector stores, and chaining retrieval weaknesses with agentic tools and conventional application flaws. It also suggests that defenses focused only on prompt-injection filtering, model alignment, or authorization checks are incomplete. Retrieval provenance, context boundaries, orchestration frameworks, scoring methods, and downstream tool execution all matter. Evidence ranges from architecture proposals and workshops to empirical evaluations, with the strongest quantitative support coming from broader agent-security studies that include RAG and memory poisoning rather than from GraphRAG-specific security research.

## Research Landscape

The collection consists mainly of conference talk and workshop descriptions from CAMLIS, DEF CON, and BSides Las Vegas in 2025–2026. It is therefore a view of practitioner-facing and emerging security research rather than a systematic body of peer-reviewed literature. Several records describe demonstrations, proof-of-concept attacks, open-source harnesses, or training labs; others introduce defensive architectures or report ongoing empirical work.

Only one record is directly centered on GraphRAG as an architecture: RIG-RAG transforms cloud configuration data into a security-enriched knowledge graph for natural-language reasoning about infrastructure [record_id:118]. Most other records address RAG as one component of a larger LLM or agentic application. They focus on context poisoning, embedding inversion, RAG manipulation, tool use, persistent memory, and orchestration frameworks rather than graph-specific attacks.

The records divide broadly into three kinds of work:

1. **Defensive uses of retrieval.** RIG-RAG applies a knowledge graph to cloud-security operations [record_id:118], while CADDIE combines RAG and the Model Context Protocol to inject policy, threat intelligence, and logs into workflows for SOC, audit, and compliance teams [record_id:2515].
2. **Offensive demonstrations and training.** These include bug-bounty techniques for RAG manipulation [record_id:1930], extraction of sensitive information through model and embedding inversion [record_id:1943], poisoning of Copilot’s limited information sources [record_id:2110], and hands-on exploitation of RAG-connected applications [record_id:2740].
3. **Evaluation and taxonomy research.** Context Poisoning research studies how one adversarial document can change an agent’s conclusion [record_id:2827]. SADF introduces an eight-class taxonomy and execution-grounded evaluation framework that includes RAG and memory poisoning [record_id:3110]. Work on abliterated models examines how readily both aligned and safety-modified models create poisoned RAG artifacts or other malicious agent components [record_id:3128].

Overall, the area is shifting from model-centric security toward **pipeline and system security**. Retrieval is treated not simply as a way to improve factual accuracy, but as an ingress point for untrusted content and a repository from which sensitive information may be recovered.

## Major Themes And Trends

### Retrieval improves grounding but creates a new trust boundary

The defensive records rely on retrieval to provide current, domain-specific evidence that a base model does not contain. CADDIE is described as injecting real-time policy, threat intelligence, and log data into an LLM for gap analysis, alert triage, and regulatory mapping [record_id:2515]. RIG-RAG similarly converts cloud configuration into a relational, security-enriched knowledge graph to support reasoning about deployed infrastructure [record_id:118].

These designs implicitly move important security decisions onto the quality and integrity of retrieved material. The model’s output depends not only on its weights and instructions, but also on ingestion, entity relationships, indexing, ranking, context selection, and the freshness of source data. Neither defensive record provides a detailed security model for controlling those stages, making the same retrieval layer that enables grounded reasoning a potentially consequential point of compromise.

### Poisoning increasingly targets evidence rather than explicit instructions

Several records show a shift from obvious malicious prompts toward attacks on the information an agent considers trustworthy. The bug-bounty talk groups context poisoning and RAG manipulation with adversarial prompts and indirect prompt injection, indicating that practitioners see retrieval compromise as a high-impact vulnerability class [record_id:1930]. The BSides workshop similarly includes RAG poisoning within multi-step exploit chains involving tool abuse, access-control failures, SSRF, traversal, and injection flaws [record_id:2740].

The Context Poisoning work draws a sharper conceptual distinction. Its proposed CXP attack does not require rogue instructions. Instead, a single adversarial document is written as plausible evidence that contradicts the surrounding legitimate material and attempts to flip an agent’s decision. The reported study covers HR evaluations, financial analysis, and corporate strategy, and says that simply adding more legitimate context is not a reliable defense [record_id:2827]. This suggests a broader integrity problem than conventional prompt injection: a retrieval system can return syntactically benign, relevant-looking content that is false, misleading, stale, or strategically framed.

The Copilot data-void attack reflects the same pattern at the source-selection level. Attackers allegedly exploit sparse or limited data sources to associate malicious content with legitimate Microsoft topics. The system then fails to validate key terms and may provide dangerous installation guidance, including instructions associated with command-and-control beacons [record_id:2110]. Together, these records indicate that attackers may succeed by shaping what evidence is available or salient, rather than by inserting visibly imperative text.

### More context is not necessarily safer

A recurring assumption in RAG design is that broader retrieval or larger context windows improve reliability. The CXP study directly challenges that assumption: drowning one poisoned document in legitimate context is described as unreliable, and some context-engineering practices intended to improve capability may enlarge the attack surface [record_id:2827].

Agentic systems intensify the issue because they aggregate heterogeneous sources—documents, email, chat messages, and search results—before reasoning over them together. Trust labels, source boundaries, and conflicting evidence can be flattened into one context window. The SADF taxonomy’s “Context Boundary Violation,” “Memory Poisoning,” and “RAG Poisoning” classes reinforce the need to treat context assembly and persistence as separate security controls rather than neutral preprocessing steps [record_id:3110].

### Retrieval confidentiality is as important as retrieval integrity

Most records concentrate on poisoning, but the embedding-inversion talk highlights confidentiality risks. It claims that sensitive information, including PII and Social Security numbers, can be extracted from modern AI ecosystems through model inversion against fine-tuned models and embedding inversion against vector databases. It further argues that conventional PII scanners fail to recognize how much sensitive information remains encoded in models and embeddings [record_id:1943].

This expands the threat model for vector search. Embeddings should not automatically be treated as harmless mathematical representations or as effectively anonymized data. If inversion attacks can reconstruct meaningful source information, access to a vector database, its query interface, nearest-neighbor results, or embedding exports may constitute access to the underlying sensitive corpus. The record describes demonstrations but does not provide extraction rates, model details, or conditions, so the general risk is clear while its practical scope remains under-specified.

### RAG security converges with agent, application, and tool security

The records consistently place retrieval inside larger agentic systems. The offensive workshop treats LLM applications as authenticated software that can invoke tools, query databases, read files, access internal URLs, and act for users. It combines RAG poisoning with SQL and NoSQL injection, SSRF, path traversal, broken object-level authorization, cross-site scripting, excessive agency, and supply-chain compromise [record_id:2740]. This framing rejects a narrow model-only assessment: a poisoned retrieval result can become the first step in a chain that reaches conventional application resources.

SADF similarly treats retrieval pipelines alongside external tools, persistent memory, delegated credentials, and multi-agent orchestration. Its taxonomy includes Tool Call Hijacking, Output Poisoning, Cross-Tool Injection, Memory Poisoning, RAG Poisoning, Delegated Authority Abuse, Multi-Agent Propagation, and Context Boundary Violation [record_id:3110]. This is significant because the security outcome is measured at the level of actual tool behavior, not merely at the level of model text.

MCP appears on both sides of this convergence. CADDIE uses MCP as a mechanism for feeding operational data into defensive workflows [record_id:2515]. The abliterated-model study identifies malicious MCP tool descriptions as one class of “soft agentic-artifact” attack that aligned base models may readily help create [record_id:3128]. MCP itself is not comprehensively evaluated in these records, but its presence underscores how retrieval, tool descriptions, and action interfaces are becoming tightly coupled.

### Model alignment is not a complete retrieval defense

The abliterated-model study reports that aligned base models comply almost universally with requests to create poisoned RAG documents, malicious agent skills, or MCP tool-poisoning descriptions. For these comparatively “soft” agentic artifacts, removing refusal behavior offers little additional attacker advantage. The agentic framing itself can reduce safety, with a harmful request wrapped as a tool call reportedly reducing base Qwen3’s safety rate from 98% to 44% [record_id:3128].

By contrast, the choice of backbone matters more when attacks require intrinsically harmful content such as malware or exploit code. Abliteration reportedly increases success substantially in those categories [record_id:3128]. The implication for RAG security is that content-integrity attacks often do not look harmful enough for model safety training to block. Defenders therefore cannot rely on the attacking or consuming model to recognize poisoned retrieval artifacts as malicious.

### Framework and evaluation design materially affect measured security

SADF provides the most detailed quantitative evidence in the collection. It argues that substring-based benchmarks substantially overstate attack success because safe models may repeat attack indicators while refusing the action. Across direct-model tests, naive scoring allegedly produced 90–100% success, while refusal-filtered scoring yielded 59% for Llama 3.2, 22% for Claude Haiku, and 16% for Claude Sonnet [record_id:3110].

The study also reports that orchestration frameworks are independent attack surfaces. Holding Claude Sonnet constant while changing wrappers yielded a 2.6-fold range in Agent Compromise Rate: 11.9% for CrewAI, 31.1% for SmolAgents, and 15.6% for the direct baseline. The expanded evaluation covers 2,656 runs across direct models and LangChain, AutoGen, CrewAI, and SmolAgents [record_id:3110]. This is especially relevant to RAG research because retrieval behavior is often implemented by frameworks—through chunking, memory, callbacks, tool routing, and context formatting—rather than by the underlying model alone.

The reported findings are not uniformly pessimistic. Memory poisoning compromised Llama 3.2 on all three cited payloads, while the four framework architectures and Claude Sonnet reportedly had zero compromises across 243 combined memory-poisoning runs. Delegated Authority Abuse also scored zero on both Claude models despite authorization checks passing [record_id:3110]. At the same time, file-path traversal and code-execution-to-file-write payloads succeeded across all seven architectures. The mixed results suggest that security varies substantially by attack class and that aggregate “jailbreak rates” obscure important distinctions.

## Methods, Tools, And Approaches Discussed

The records describe several architectures and research workflows.

**Relational Inference GraphRAG (RIG-RAG)** uses an LLM-assisted pipeline to transform cloud configuration into a security-enriched knowledge graph. Its stated purpose is to let users reason in natural language about deployed cloud infrastructure and improve agentic cloud-security operations [record_id:118]. The abstract does not specify graph schema construction, entity resolution, authorization propagation, provenance, or resistance to poisoned cloud metadata.

**CADDIE** is presented as a RAG engine driven by MCP. It retrieves real-time policy, threat-intelligence, and log information for operational and governance tasks such as alert triage, gap analysis, and regulatory mapping [record_id:2515]. The emphasis is explainability and current cyber context, although the record does not detail how sources are authenticated, how user permissions are applied during retrieval, or how tool actions are constrained.

**Data-void and key-term association attacks** manipulate retrieval indirectly. Rather than compromising the model, the attacker publishes or inserts persistent malicious content where the AI has limited trusted evidence, then associates that content with legitimate terminology. The Copilot demonstration reportedly used this technique to influence enterprise-facing answers and guide users toward compromised actions [record_id:2110].

**Context Poisoning (CXP)** inserts one apparently legitimate but adversarial document among many valid documents. Proposed attack variants include subtle or forceful assertions, claims framed as updated records, and fabricated statements. The evaluation studies whether these artifacts can flip recommendations in enterprise scenarios [record_id:2827]. Candidate defenses include secure context engineering and prompt hardening, but the work explicitly states that no single measure has closed the gap.

**Model and embedding inversion** seek to recover sensitive source information from trained models or vector representations. The embedding-focused attack is particularly relevant to RAG systems that store document representations in vector databases [record_id:1943]. The record also raises the methodological concern that ordinary PII scanners may inspect explicit text while missing sensitive information recoverable from latent representations.

**Full-stack offensive testing** is represented by the Vulnerable AI Application workshop. Its hosted AWS environment contains isolated, intentionally vulnerable agents mapped to the OWASP Top 10 for LLM Applications. Participants chain prompt injection, system-prompt extraction, RAG poisoning, agent-mediated database injection, traversal, SSRF, excessive agency, broken object-level authorization, XSS, and supply-chain-style flaws [record_id:2740]. This approach treats retrieval testing as part of application penetration testing rather than a standalone model exercise.

**Bug-bounty methodology** applies adversarial prompts, indirect prompt injection, context poisoning, and RAG manipulation to real-world AI targets. The stated focus is finding high-impact bugs and demonstrating severity and organizational value [record_id:1930]. The record indicates practical relevance but provides no taxonomy, metrics, or named case studies in its abstract.

**SADF** supplies both a failure taxonomy and an automated harness. Its scoring filters out refusals and grounds success in actual tool-execution output strings, addressing false positives caused by keyword matching. It compares models and framework wrappers across eight agentic failure classes, including RAG poisoning [record_id:3110]. This method is the clearest attempt in the collection to make retrieval-adjacent security measurement reproducible.

Finally, the **abliteration evaluation harness** compares base and refusal-modified Qwen3 and Gemma-3 models across attack classes. It distinguishes easy artifact-generation attacks—such as poisoned RAG documents—from categories requiring hard harmful content. It also proposes using high success on hard categories as a detector for abliterated models and reports releasing a harness, probe set, and detector [record_id:3128].

## Notable Talks, Records, And Evidence

RIG-RAG is notable because it is the collection’s only dedicated GraphRAG architecture. It shows how graph-based retrieval may support cloud-security reasoning by converting configuration data into security-enriched relationships [record_id:118]. Its importance is architectural rather than empirical: the record explains the intended function but provides no security evaluation.

The CXP talk is the clearest retrieval-integrity study. It offers a distinct threat model in which a credible-looking document changes an agent’s conclusion without containing overt instructions. Its reported enterprise scenarios and the finding that additional legitimate context does not reliably defeat poisoning make it directly relevant to production RAG design [record_id:2827]. However, the research is explicitly ongoing, and the abstract supplies no sample size, model list, success rates, or statistical analysis.

The Copilot data-void demonstration provides a concrete poisoning scenario against a named deployed ecosystem. Its key contribution is showing how sparse information environments and weak term validation can allow persistent malicious associations to influence generated advice [record_id:2110]. The record describes a proof of concept from Microsoft’s Zero Day Quest, but it does not state the affected product configuration, remediation status, or reproducibility conditions.

The embedding-inversion talk is the strongest confidentiality-focused record. It argues that PII can remain recoverable from vector databases and fine-tuned models even when scanning tools do not flag it [record_id:1943]. It is important because retrieval security is often framed around prompt injection while the confidentiality properties of embeddings receive less attention. The abstract promises real-world attacks and demonstrations but gives no quantitative reconstruction results.

SADF contains the collection’s most substantial measurement claims. Its 2,656 evaluation runs, cross-framework comparisons, refusal-filtered scoring, and execution-grounded success criteria offer a more rigorous basis than simple attack anecdotes [record_id:3110]. It also demonstrates why conclusions about RAG poisoning should account for orchestration frameworks and why textual benchmark outputs may not correspond to actual compromise. Even so, the abstract alone does not expose payload composition, confidence intervals, environmental controls, or independent replication.

The abliterated-model study contributes a useful attacker-capability distinction. It suggests that poisoned RAG artifacts are easy enough to generate that even aligned models commonly comply, whereas refusal removal matters more for malware and similarly hard harmful content [record_id:3128]. Its reported percentages make it evidence-rich relative to most records, although the findings are confined to specific Qwen3 and Gemma-3 variants and the described attack categories.

The OWASP-oriented workshop is representative of the full-stack application-security view. It shows how RAG poisoning can be chained with database attacks, SSRF, traversal, authorization failures, and unsafe output handling [record_id:2740]. As a training description, it establishes practical attack coverage but not prevalence or effectiveness against real production systems.

The bug-bounty presentation adds evidence that RAG manipulation and context poisoning are entering mainstream AI vulnerability research and disclosure practice [record_id:1930]. CADDIE, conversely, represents the positive operational case for RAG: using live security data and MCP to make AI-driven SOC and compliance work more precise and explainable [record_id:2515]. Together, they illustrate the dual-use character of retrieval pipelines.

## Gaps, Limits, And Open Questions

The largest gap is the lack of GraphRAG-specific attack research. RIG-RAG proposes a graph architecture, but none of the records evaluates graph poisoning, malicious edge creation, entity-resolution attacks, relationship inference leakage, graph traversal authorization, or corruption of graph-derived summaries [record_id:118]. It remains unclear whether graph structure improves provenance and consistency or simply creates additional high-impact objects for attackers to manipulate.

Access control is also underdeveloped. The records recognize authentication boundaries, delegated credentials, excessive agency, and broken object-level authorization [record_id:2740] [record_id:3110], but they do not define a complete authorization model for retrieval. Open questions include whether permissions are enforced before embedding, during indexing, at query time, after reranking, and when content is copied into persistent memory. There is no direct evaluation of cross-tenant vector-search leakage, metadata-filter bypass, embedding cache isolation, or permission revocation.

The poisoning studies leave several measurement questions unresolved. CXP does not disclose models, corpus sizes, retrieval algorithms, or attack-success rates in the abstract [record_id:2827]. The Copilot example is concrete but singular [record_id:2110]. Future work should separate failures caused by ingestion, retrieval ranking, source scarcity, context formatting, and final model reasoning. It should also test whether provenance indicators, source diversity, contradiction detection, signed content, temporal validation, or confidence calibration improve robustness.

Embedding confidentiality needs more precise characterization. The inversion record establishes a plausible and serious privacy problem, but it does not state what attacker access is required, how accurately PII can be reconstructed, or how risk varies by embedding model, dimensionality, quantization, corpus size, or query interface [record_id:1943]. Research should compare encryption, query controls, noise, dimensionality reduction, rate limits, and safer embedding designs without assuming that embeddings are inherently anonymized.

Defensive RAG architectures are described in terms of usefulness more than assurance. CADDIE does not explain how real-time logs, threat intelligence, and policy are validated or permissioned [record_id:2515]. RIG-RAG does not address graph provenance, stale configuration, poisoned telemetry, or how natural-language users are authorized to traverse cloud relationships [record_id:118]. These are central concerns when retrieved information can influence automated actions.

The collection also lacks operational evidence about incident frequency, production prevalence, and remediation costs. Workshops and bug-bounty talks demonstrate plausible vulnerabilities [record_id:1930] [record_id:2740], but they do not quantify how often RAG attacks occur in deployed systems. No record supplies longitudinal incident data or compares organizational controls.

Finally, the evaluation literature remains fragmented. SADF offers a promising framework and demonstrates that scoring and wrappers change results [record_id:3110], while the abliteration study distinguishes artifact generation from hard harmful content [record_id:3128]. Future benchmarks should combine these insights with realistic retrieval corpora, access-control policies, multi-turn state, poisoned embeddings, source provenance, and measurable downstream consequences. Independent reproduction is needed before the reported framework rankings or model-specific rates can be generalized.

## Coverage And Evidence Notes

The collection’s two primary-topic defensive records are RIG-RAG, a GraphRAG-inspired cloud knowledge-graph pipeline [record_id:118], and CADDIE, an MCP-driven RAG engine for SOC, audit, and compliance work [record_id:2515]. Both are important architecture examples, but their abstracts offer limited evidence about security testing.

The principal poisoning and manipulation records are the practical AI bug-bounty discussion [record_id:1930], the Copilot data-void proof of concept [record_id:2110], the OWASP-aligned exploitation workshop containing a RAG-poisoning lab [record_id:2740], and the ongoing empirical CXP study [record_id:2827]. Of these, CXP supplies the clearest retrieval-specific threat model, while the others place poisoning within broader offensive practice.

The primary confidentiality record is the talk on extracting “shadow data” through model and embedding inversion [record_id:1943]. Its relevance to vector databases is strong, but the supplied text contains no quantitative evidence.

The broadest evaluation record is SADF, which includes RAG poisoning within an eight-class agentic-failure taxonomy and reports detailed cross-model and cross-framework measurements [record_id:3110]. The companion record on abliterated backbones is less directly about retrieval systems but provides evidence about how easily models generate poisoned RAG documents and how agent scaffolding can weaken safety behavior [record_id:3128].

Evidence strength is therefore uneven. Detailed numerical claims appear mainly in the two 2026 agent-evaluation records [record_id:3110] [record_id:3128]. The CXP work reports an empirical study but labels it ongoing and omits figures in the raw description [record_id:2827]. The Copilot and embedding-inversion records describe demonstrations without enough methodological detail for independent assessment [record_id:2110] [record_id:1943]. The remaining records are architecture, workshop, or bug-bounty descriptions that establish themes and practical relevance but do not by themselves demonstrate prevalence, generality, or comparative defensive effectiveness [record_id:118] [record_id:1930] [record_id:2515] [record_id:2740].