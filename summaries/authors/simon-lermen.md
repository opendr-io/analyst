# Topic: Author: Simon Lermen

## Executive Summary

The three records attributed to Simon Lermen, all co-authored or co-presented with Fred Heiding, form a focused body of work on AI-enabled social engineering and the automation of phishing operations. Across BSidesLV 2025, Prompt||GTFO 2026, and BSidesLV 2026, the records describe a progression from automating phishing infrastructure, to end-to-end AI-powered spear phishing, to empirical measurement of AI-enabled voice phishing. The dominant research concern is that large language models, AI agents, and voice synthesis systems reduce the labor, cost, and skill barriers that historically constrained targeted phishing and vishing attacks.

The strongest through-line is scalability. In the email and web-phishing records, Lermen and Heiding emphasize that AI agents can perform tasks previously requiring human operators: OSINT collection, victim profiling, personalized persuasion, domain purchasing, DNS configuration, landing page deployment, and credential harvesting [record_id:2192] [record_id:2394]. In the voice-phishing record, the same scaling argument appears in a different medium: high-quality AI voice systems and LLMs reduce dependence on human callers, making some vishing models economically profitable where U.S.-wage human-operated scams may not be [record_id:2736].

The records also indicate a shift from speculative concern to operational and empirical evaluation. The BSidesLV 2025 record proposes measuring AI agents’ ability to register domains, configure DNS, deploy landing pages, and harvest credentials using frontier and open-source models [record_id:2394]. The Prompt||GTFO 2026 record describes a demonstration of a fully automated phishing agent spanning the attack chain [record_id:2192]. The BSidesLV 2026 record reports a large-scale survey experiment with 4,100 U.S. adults and qualitative interviews, measuring susceptibility to AI-generated voice scams, model realism, detection difficulty, and economics [record_id:2736].

Collectively, these records present Lermen’s contribution as part of a research program investigating how modern AI systems change the economics and operational feasibility of social engineering. The emphasis is not primarily that AI produces unprecedented “superhuman” persuasion, but that it enables low-cost, scalable, personalized attack execution and infrastructure development [record_id:2192] [record_id:2394] [record_id:2736].

## Research Landscape

The topic contains three records: two BSidesLV conference talks and one Prompt||GTFO talk or demonstration. All three are attributed jointly to Fred Heiding and Simon Lermen, and all concern AI-powered phishing or social engineering. The records are not general-purpose AI security discussions; they are specifically about attacker workflows, economic incentives, automation of cybercrime infrastructure, and human susceptibility to AI-mediated scams.

The records cover three related but distinct areas:

1. **AI-powered phishing infrastructure automation.**  
   The BSidesLV 2025 record focuses on using LLMs and AI agents to create the back-end infrastructure for phishing campaigns. It explicitly shifts attention away from phishing email generation alone and toward domain registration, DNS setup, hosting spoofed websites, deploying landing pages, and credential harvesting [record_id:2394].

2. **Fully automated spear-phishing attack chains.**  
   The Prompt||GTFO 2026 record describes a demonstration of an AI-powered phishing agent that automates the full attack chain: OSINT collection, vulnerability profiling, persuasive email generation, and phishing domain purchasing/configuration [record_id:2192].

3. **AI-powered voice phishing and detection.**  
   The BSidesLV 2026 record examines vishing using large AI voice models and LLMs. It reports an empirical study with 4,100 survey participants and 12 qualitative interviews, covering generated scam audio, transcripts, susceptibility, human recognition, automated classification, and economic analysis [record_id:2736].

The record set is small but coherent. It does not represent a broad survey of Simon Lermen’s entire possible publication history; rather, it captures a concentrated set of talks on AI-enabled phishing and social engineering. The sources are conference or event records and summaries, not full papers. As a result, they provide strong signals about research direction and claims, but limited methodological detail except in the voice-phishing record, which includes more explicit study design, sample size, model names, success rates, and findings [record_id:2736].

The overall research area is AI-enabled cybercrime, with particular attention to phishing, spear phishing, vishing, scam economics, infrastructure automation, and defensive implications. The records repeatedly frame AI as changing the cost structure of attacks. They suggest that tools such as LLMs, AI agents, and voice models can collapse distinctions between low-cost mass phishing and expensive personalized social engineering by enabling personalization and operational execution at scale [record_id:2192] [record_id:2394] [record_id:2736].

## Major Themes And Trends

### AI lowers the cost and skill barriers for social engineering

The most consistent theme is that AI reduces the marginal cost of social engineering. In the Prompt||GTFO record, Lermen and Heiding are described as demonstrating an agent that automates the entire phishing attack chain, from target research to domain configuration. The record states that this “eliminates the cost difference between spray-and-pray and spear phishing,” enabling high click-through rates at near-zero cost [record_id:2192]. This is a central claim: AI allows attackers to combine mass scale with individualized targeting.

The BSidesLV 2025 infrastructure talk reinforces this by focusing on back-end automation. Earlier work had explored LLM-generated persuasive phishing emails, but this project examines whether LLMs and AI agents can autonomously create phishing infrastructure, including domain registration, DNS records, spoofed websites, landing pages, and credential harvesting [record_id:2394]. That shift matters because scalable phishing requires more than convincing text; it also requires reliable operational infrastructure.

The BSidesLV 2026 vishing record extends the cost-barrier argument to phone scams. Traditional voice phishing is described as limited by the need for human operators. AI voice synthesis and LLMs reduce that bottleneck, enabling scalable automated scams [record_id:2736]. The economic analysis reportedly finds that human-operated vishing is unprofitable at U.S. wages, while AI-powered vishing is already profitable for several models [record_id:2736]. This directly links model capability to attacker incentives.

### Automation expands from content generation to full lifecycle execution

A second recurring theme is that the relevant risk is not just AI-generated phishing content but lifecycle automation. The BSidesLV 2025 record explicitly says prior research had examined persuasive phishing emails, while this study shifts focus to the “back-end automation of the phishing lifecycle” [record_id:2394]. It evaluates agents on registering phishing domains, configuring DNS, deploying landing pages, and harvesting credentials [record_id:2394].

The Prompt||GTFO 2026 record appears to broaden this lifecycle further into a fully automated agentic workflow. It includes OSINT gathering, building vulnerability profiles, crafting personalized spear-phishing emails using psychological persuasion techniques, and purchasing/configuring phishing domains [record_id:2192]. This suggests a movement from isolated LLM outputs toward multi-step autonomous cybercrime workflows.

The vishing work similarly treats social engineering as a lifecycle problem, though in a different medium. The BSidesLV 2026 talk includes generation of scam scenarios using voice models, assessment of susceptibility, detection strategies, human recognition, automated classification, and economic analysis [record_id:2736]. Rather than only asking whether AI voices sound realistic, it asks whether they change scam success, detectability, and profitability.

### The main risk is scalability, not necessarily superhuman persuasion

The records collectively suggest a nuanced position: AI is dangerous not only because it can persuade better than humans, but because it can operate cheaply and at scale. The BSidesLV 2026 record is explicit: “the primary risks of present-day AI-vishing lie in improved scalability, not in novel or ‘superhuman’ persuasion techniques” [record_id:2736]. In that study, caller persuasiveness was the strongest predictor of compliance regardless of whether the caller was believed to be human or machine [record_id:2736]. Some models, especially Sesame, achieved ratings comparable to human voices or slightly surpassed them, but the record frames the core risk as scalable profitability rather than magical persuasive superiority [record_id:2736].

This framing also fits the email and infrastructure records. The Prompt||GTFO record emphasizes near-zero cost and elimination of the difference between mass phishing and spear phishing [record_id:2192]. The BSidesLV 2025 record emphasizes task completion rate, cost, time requirements, and human intervention required [record_id:2394]. The recurring metric is operational efficiency.

### Personalization and psychological targeting remain central

Although scalability is the dominant concern, the records also highlight personalization. The Prompt||GTFO demonstration includes OSINT gathering, vulnerability profiles, and personalized spear-phishing emails using psychological persuasion techniques [record_id:2192]. The defensive implication mentioned in that record is training people against their “specific persuasion vulnerabilities” [record_id:2192]. This implies a model of phishing in which individual susceptibility varies and attackers can tailor messages to exploit those differences.

The BSidesLV 2026 vishing record also investigates variation across scam types and perceived caller persuasiveness. Participants were exposed to five scam scenarios, including password reset scams and relative-in-distress scams, with success rates reaching up to 36% for certain categories [record_id:2736]. The record’s finding that caller persuasiveness was the strongest predictor of compliance suggests that content, delivery, and scenario framing remain important even when the broader risk is scalability [record_id:2736].

### Detection and defense are acknowledged but less developed than offense and measurement

All three records mention defensive or policy implications, but the available text provides less detail about concrete defenses than about attack automation and measurement. The Prompt||GTFO record mentions defensive implications, including training people against their specific persuasion vulnerabilities [record_id:2192]. The BSidesLV 2025 record says the work highlights the need for regulatory, technical, and policy countermeasures [record_id:2394]. The BSidesLV 2026 record discusses detection strategies for AI-generated voice phishing, including human recognition and automated classification, and raises concerns for consumer protection and model release policies [record_id:2736].

However, the records do not provide detailed defensive architectures, implementation guidance, or validated mitigation outcomes. The vishing record provides the richest defensive evidence because it reports that humans struggle to distinguish AI-generated scam calls from human voices and that participants often misidentified human callers as AI, correctly recognizing human voices only 24–45% of the time [record_id:2736]. This finding complicates defenses based on human awareness or simple “spot the AI voice” training.

## Methods, Tools, And Approaches Discussed

The records describe several methods and technical approaches, mostly in the context of evaluating AI-enabled attack automation.

In the phishing infrastructure work, the approach is to task modern frontier and open-source models with operational phishing setup tasks. The BSidesLV 2025 record names Chinese models such as DeepSeek and Western counterparts including Claude Sonnet and GPT-4o [record_id:2394]. The tasks include registering phishing domains, configuring DNS records, deploying landing pages, and harvesting credentials [record_id:2394]. The planned or described evaluation uses metrics such as task completion rate, cost and time requirements, and the amount of human intervention required [record_id:2394]. This suggests a benchmarking-style methodology for measuring how capable AI agents are at cybercrime infrastructure development.

The Prompt||GTFO record describes an integrated phishing agent that performs OSINT, target profiling, persuasive message generation, and domain purchasing/configuration [record_id:2192]. The workflow begins with gathering open-source intelligence on targets, then building vulnerability profiles, then crafting personalized spear-phishing emails using psychological persuasion techniques, and finally purchasing and configuring phishing domains [record_id:2192]. The record does not specify particular models, code, architecture, or evaluation methodology, but it presents the work as a demonstration of end-to-end automation.

The vishing record has the most explicit empirical design. It describes a large-scale survey experiment with N=4100 and qualitative interviews with N=12, assessing U.S. adults’ susceptibility to AI-powered voice phishing [record_id:2736]. Participants were exposed to audio recordings or transcripts of scam scenarios generated by leading voice models, including Llama Full Duplex, Sesame, Gemini, OAI AVM, Play.AI, and ElevenLabs [record_id:2736]. The study tested five scam scenarios, including password reset scams and relative-in-distress scams [record_id:2736]. It measured success rates, perceived persuasiveness, whether callers were believed to be human or machine, human ability to recognize AI-generated voices, automated classification, and economic profitability [record_id:2736].

Several methodological motifs recur:

- **Agentic task execution:** AI is evaluated as an actor that can perform multi-step operational tasks, not merely generate text [record_id:2192] [record_id:2394].
- **Cost/time/human-intervention metrics:** The infrastructure work explicitly measures task completion, cost, time, and required human intervention [record_id:2394], while the vishing work includes an economic analysis comparing human-operated and AI-powered attacks [record_id:2736].
- **Human susceptibility testing:** The vishing work directly measures human compliance under scam scenarios, with reported success rates up to 36% in certain categories [record_id:2736].
- **Detection evaluation:** The vishing work assesses both human recognition and automated classification of AI-generated voice phishing [record_id:2736].
- **Personalization and persuasion modeling:** The fully automated phishing agent uses OSINT and vulnerability profiles to personalize spear-phishing emails with psychological persuasion techniques [record_id:2192].

## Notable Talks, Records,