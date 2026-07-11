# Topic: Author: Simon Lermen

## Executive Summary

The two records attributed to Simon Lermen present a focused research thread on AI-enabled phishing and social engineering, co-authored with Fred Heiding. Together, they describe how large language models and AI agents can automate increasingly large portions of the phishing lifecycle: from reconnaissance and psychological targeting to email generation, domain registration, DNS setup, spoofed website deployment, and credential harvesting [record_id:2192] [record_id:2394].

The strongest shared claim is that AI agents reduce the cost, labor, and skill barriers traditionally associated with targeted phishing. One record frames this as “fully automated AI-powered social engineering,” emphasizing OSINT collection, vulnerability profiling, personalized spear phishing, and automated domain purchasing/configuration [record_id:2192]. The other narrows in on phishing infrastructure automation, arguing that prior work has often focused on persuasive phishing text while this project studies back-end tasks such as registering domains, configuring DNS, deploying landing pages, and harvesting credentials [record_id:2394].

Across the records, Lermen’s contribution appears to sit at the intersection of AI security, cybercrime enablement, social engineering, and defensive policy. The work is not merely about LLM-generated phishing emails; it highlights end-to-end automation, measurable operational scaling, and the risk that personalized attacks may become cheap enough to erase the historical cost gap between mass phishing and spear phishing [record_id:2192] [record_id:2394].

## Research Landscape

The topic is represented by two public talk records: one from Prompt||GTFO in 2026 and one from BSidesLV 2025. Both are attributed to Fred Heiding and Simon Lermen, and both concern AI-assisted or AI-agent-driven phishing. The records are not broad biographical materials about Simon Lermen, nor do they document a wide range of unrelated publications. Instead, they provide a compact but coherent view of a specific research program: evaluating how AI agents can automate offensive social engineering and phishing infrastructure workflows.

The 2025 BSidesLV record, “Automating Phishing Infrastructure Development Using AI Agents,” frames the work as a project investigating how attackers can use LLMs and AI agents to create phishing infrastructure autonomously [record_id:2394]. It emphasizes experimental evaluation: comparing frontier and open-source models, including DeepSeek, Claude Sonnet, and GPT-4o, on concrete phishing infrastructure tasks such as domain registration, DNS configuration, landing page deployment, and credential harvesting [record_id:2394]. This record is especially useful for understanding the methodological direction of the work because it mentions planned or performed tests “with and without human intervention” and metrics including task completion rate, cost, time requirements, and amount of human involvement [record_id:2394].

The 2026 Prompt||GTFO record, “Fully Automated AI-Powered Social Engineering,” describes a broader attack-chain demonstration [record_id:2192]. It includes OSINT gathering, target profiling, persuasive email generation, and purchasing/configuring phishing domains [record_id:2192]. Compared with the BSidesLV record, this source broadens the scope from back-end infrastructure automation to full-spectrum social engineering, including psychological persuasion and defensive implications such as training people against their specific persuasion vulnerabilities [record_id:2192].

Overall, the research landscape is dominated by conference-style demonstrations and talk abstracts rather than papers, datasets, implementation repositories, or peer-reviewed empirical studies. The records offer strong evidence about the stated topics and claims of the talks, but thin evidence about exact experimental results, implementation details, reproducibility, legal/ethical safeguards, and measured effectiveness beyond the summarized claims.

## Major Themes And Trends

### End-to-end automation of phishing workflows

The most important theme is the expansion of AI use from isolated phishing email generation to complete phishing campaign automation. The BSidesLV record explicitly states that earlier research had explored LLM-generated persuasive phishing emails, while this project shifts attention to “back-end automation of the phishing lifecycle” [record_id:2394]. The listed tasks include registering phishing domains, configuring DNS records, deploying landing pages, and harvesting credentials [record_id:2394].

The Prompt||GTFO record takes this further by describing an AI-powered phishing agent that automates “the entire attack chain” [record_id:2192]. That chain includes gathering OSINT on targets, building vulnerability profiles, crafting personalized spear phishing emails using psychological persuasion techniques, and purchasing/configuring phishing domains [record_id:2192]. Together, the records suggest a progression from infrastructure automation in 2025 to a more comprehensive social engineering demonstration in 2026, although the available evidence is too sparse to confirm a chronological research evolution beyond the dates and described scopes.

### Collapse of the cost distinction between mass phishing and spear phishing

A central claim in the 2026 record is that AI-enabled automation may eliminate “the cost difference between spray-and-pray and spear phishing” [record_id:2192]. Traditionally, spear phishing has required more manual effort because it depends on target-specific research, tailored messaging, and custom infrastructure. The records argue that AI agents can automate many of these labor-intensive steps, potentially making individualized attacks scalable.

The BSidesLV record supports this theme from an infrastructure perspective. It emphasizes measuring cost and time requirements, task completion rate, and human intervention required when AI agents perform phishing infrastructure tasks [record_id:2394]. Its stated goal is to demonstrate how “easy and low-cost” it has become to scale phishing infrastructure with AI [record_id:2394]. The Prompt||GTFO record extends that cost-reduction argument to the social engineering side, noting “high click-through rates at near-zero cost” in the context of personalized spear phishing [record_id:2192].

### AI agents as operational actors, not just content generators

Both records foreground AI agents as actors capable of executing workflows, not merely language models producing text. In the BSidesLV record, agents are tasked with operational steps: domain registration, DNS configuration, hosting personalized spoofed websites, deploying landing pages, and harvesting credentials [record_id:2394]. The Prompt||GTFO record similarly describes an “AI-powered phishing agent” that gathers OSINT, builds profiles, writes persuasive messages, and purchases/configures domains [record_id:2192].

This distinction matters because the risk model is different. A text-generation risk centers on malicious or deceptive content. An agentic workflow risk includes tool use, account creation, infrastructure orchestration, credential collection, and campaign management. The records collectively suggest that Simon Lermen’s work with Fred Heiding is concerned with this broader agentic threat model.

### Personalization and psychological persuasion

The Prompt||GTFO record emphasizes target personalization. It says the agent gathers OSINT, builds vulnerability profiles, and crafts spear phishing emails using “psychological persuasion techniques” [record_id:2192]. It also mentions defensive training tailored to people’s “specific persuasion vulnerabilities” [record_id:2192]. This indicates an interest not only in whether AI can automate phishing, but also in whether AI can adapt persuasion strategies to individual targets.

The BSidesLV record is less focused on persuasion, but it does mention “hosting personalized spoofed websites” [record_id:2394]. This suggests that personalization may extend beyond email copy into landing pages and phishing infrastructure. Across both records, personalization is treated as a key mechanism by which AI-powered phishing could become more effective and scalable.

### Comparative evaluation of model capabilities

The BSidesLV record explicitly names model families and providers, including Chinese models such as DeepSeek and Western models such as Claude Sonnet and GPT-4o [record_id:2394]. This implies a comparative model evaluation agenda: assessing how different modern frontier and open-source models perform on cybercrime-relevant operational tasks.

The evidence does not include the outcome of those comparisons, such as which model performed best, what failure modes appeared, or how safeguards affected results. Still, the inclusion of multiple model categories is significant. It suggests that the work is not limited to one vendor’s model or one prompt-engineering setup, but considers the broader ecosystem of frontier and open-source LLM capability [record_id:2394].

### Defensive, regulatory, technical, and policy implications

The records do not only describe offensive capability; they also gesture toward defense and governance. The BSidesLV record says the work “highlights the urgent need for regulatory, technical, and policy countermeasures” [record_id:2394]. The Prompt||GTFO record mentions defensive implications, including training people against their specific persuasion vulnerabilities [record_id:2192].

The defensive discussion appears less developed in the supplied texts than the offensive demonstration. The records identify the need for countermeasures but do not provide detailed defensive architectures, regulatory proposals, phishing-resistant identity systems, model governance frameworks, or empirical evidence about training effectiveness. This is an important gap for downstream researchers.

## Methods, Tools, And Approaches Discussed

The records describe several methods and workflows associated with AI-powered phishing research.

One method is agentic OSINT-driven targeting. In the Prompt||GTFO record, the AI-powered phishing agent gathers OSINT on targets and builds vulnerability profiles [record_id:2192]. The raw text does not specify which OSINT sources, APIs, data brokers, social platforms, or enrichment tools are used. However, the described workflow indicates an approach in which AI systems collect or process target-specific information before generating outreach.

Another method is personalized persuasive message generation. The Prompt||GTFO record says the agent crafts personalized spear phishing emails using psychological persuasion techniques [record_id:2192]. The exact taxonomy of persuasion techniques is not provided, but the record implies that the system chooses or applies persuasion strategies based on target profiles.

A third approach is automated phishing infrastructure provisioning. Both records discuss purchasing or registering domains and configuring them for phishing use [record_id:2192] [record_id:2394]. The BSidesLV record provides the clearest breakdown: domain registration, DNS configuration, hosting personalized spoofed websites, deploying landing pages, and harvesting credentials [record_id:2394]. These are practical operational steps that move the topic beyond text generation into end-to-end campaign deployment.

The BSidesLV project also uses comparative model evaluation. It names “modern frontier and open-source models,” including DeepSeek, Claude Sonnet, and GPT-4o, and evaluates them on infrastructure tasks [record_id:2394]. It also indicates tests both “with and without human intervention,” which suggests a spectrum from fully autonomous operation to human-assisted agent workflows [record_id:2394].

The evaluation metrics mentioned in the BSidesLV record include task completion rate, cost and time requirements, and amount of human intervention required [record_id:2394]. These metrics are notable because they focus on operational scalability and attacker economics rather than only content quality or persuasion effectiveness. The Prompt||GTFO record similarly emphasizes economics and effectiveness by claiming high click-through rates at near-zero cost and the elimination of the cost difference between broad phishing and spear phishing [record_id:2192].

The records mention specific model names but do not mention codebases, tools, frameworks, orchestration libraries, browsers, domain registrars, hosting providers, anti-abuse bypass techniques, or credential-harvesting implementations. Downstream agents should therefore treat the described methods as high-level evidence of research scope rather than as a reproducible technical recipe.

## Notable Talks, Records, And Evidence

The most comprehensive record is the 2026 Prompt||GTFO talk “Fully Automated AI-Powered Social Engineering,” by Fred Heiding and Simon Lermen [record_id:2192]. It matters because it describes an AI-powered phishing agent that automates the “entire attack chain,” including OSINT, vulnerability profiling, personalized phishing emails, and domain purchasing/configuration [record_id:2192]. It also contains the strongest claim about the strategic impact of AI on phishing economics: that automation can remove the cost difference between “spray-and-pray” phishing and spear phishing, producing high click-through rates at near-zero cost [record_id:2192]. This record is especially representative of the broader social engineering angle of Lermen’s attributed work.

The 2025 BSidesLV talk “Automating Phishing Infrastructure Development Using AI Agents,” also by Fred Heiding and Simon Lermen, is important because it gives a more specific research design for the infrastructure side of the problem [record_id:2394]. It frames the work as a shift from LLM-generated phishing emails to the automation of back-end phishing lifecycle tasks [record_id:2394]. It also names the types of models being evaluated, including DeepSeek, Claude Sonnet, and GPT-4o, and the operational metrics used to judge performance: task completion rate, cost, time, and human intervention [record_id:2394]. This record is the strongest evidence for a comparative, measurement-oriented approach.

Taken together, the two talks show a coherent contribution: Simon Lermen is associated here with research demonstrating that AI agents can lower the operational burden of phishing campaigns across both social and infrastructure layers. The records also suggest that this work is intended to raise awareness of AI-powered cybercrime risk and motivate defenses, training, regulation, and policy responses [record_id:2192] [record_id:2394].

## Gaps, Limits, And Open Questions

The evidence base is small: only two records. Both are conference or talk descriptions rather than full papers, transcripts, slide decks, code releases, datasets, or independent evaluations. As a result, the records are strong evidence for what the talks claimed to cover, but weaker evidence for the empirical validity, reproducibility, or generality of the findings.

Several open questions remain:

- **Experimental results are not detailed.** The BSidesLV record lists metrics such as task completion rate, cost, time, and human intervention, but does not provide actual measured values or comparative outcomes across DeepSeek, Claude Sonnet, GPT-4o, or other models [record_id:2394].
- **Implementation details are absent.** The records do not describe the agent architecture, tools, prompts, APIs, browser automation, registrar interactions, hosting setup, or safeguards used in the demonstrations [record_id:2192] [record_id:2394].
- **Ethical and safety controls are unclear.** The records describe phishing infrastructure and credential harvesting as evaluation tasks, but the raw text does not explain containment, consent, test environments, synthetic targets, or legal review processes [record_id: