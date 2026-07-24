# Topic: Author: Stav Cohen

## Executive Summary

The five records attributed to Stav Cohen describe a focused body of offensive AI-security research centered on agentic systems: LLM-powered assistants, workspace agents, browser agents, and always-on autonomous agents that consume untrusted content while acting with user permissions. Across the records, Cohen appears as a coauthor or speaker on work arguing that the security risks of AI agents are not merely speculative prompt-injection curiosities, but practical attack surfaces enabling zero-click or low-interaction compromise, data exfiltration, account takeover, persistence, lateral movement, and even physical-world effects through connected devices.

The strongest recurring claim is that modern AI agents collapse traditional security boundaries by combining untrusted inputs, user intent, privileged integrations, browser or OS access, and model-driven planning. The 2025 Gemini Workspace records describe “Targeted Promptware Attacks” in which a Google Calendar invite, email, or shared Google Doc can carry an indirect prompt injection that hijacks Gemini agents and abuses their permissions [record_id:53] [record_id:1965]. The 2026 agentic-browser records extend this argument to browsers, asserting that vendors intentionally relax longstanding browser security assumptions—Same-Origin Policy, filesystem isolation, localhost restrictions, script execution boundaries—to support agentic functionality, and that model safety training is an inadequate primary mitigation [record_id:2667] [record_id:3117]. A further DEF CON 34 record broadens the scope to “always-on agents” and agent networks, describing zero-click backdoors in OpenClaw and large-scale prompt-injection effects across MoltBook’s agent ecosystem [record_id:3125].

Collectively, the records position Cohen’s work around a central thesis: when AI agents are empowered to act, retrieve, browse, execute, integrate, remember, and coordinate, prompt injection becomes closer to a general exploitation primitive than a chatbot nuisance. The proposed defensive lesson is also consistent: soft controls such as model alignment, “vibes,” or safety training are portrayed as insufficient, while deterministic, code-level, hard security boundaries are repeatedly identified as the defenses that meaningfully constrained attacks [record_id:2667] [record_id:3117] [record_id:3125].

## Research Landscape

The records are conference-talk abstracts from major security venues, primarily Black Hat and DEF CON, spanning 2025 and 2026. They are not blog posts, papers, or implementation documentation; they are talk descriptions that summarize planned demonstrations, claims, and findings. As a result, the evidence base is strong for identifying the public themes and stated contributions of Cohen-attributed talks, but thinner for independently verifying technical details, exploit reliability, vendor status, or exact mitigations.

Two records describe essentially the same 2025 Gemini Workspace work: a Black Hat US 2025 briefing and a DEF CON 33 presentation, both titled around invoking Gemini agents with a Google Calendar invite [record_id:53] [record_id:1965]. These records introduce “Promptware” and “Targeted Promptware Attacks,” focusing on indirect prompt injection delivered via everyday collaboration artifacts such as calendar invites, emails, or shared documents. The abstracts are nearly identical and emphasize practicality: the attacker does not require white-box access, specialized adversarial ML expertise, or expensive compute; instead, a meeting subject can carry the malicious instruction [record_id:53] [record_id:1965].

Two 2026 records address “PleaseFix,” a vulnerability class for agentic browsers. The Black Hat US 2026 record is multi-authored and frames the work as a broad critique of security boundary dismantling in agentic browsers [record_id:2667]. The DEF CON 34 record lists Stav Cohen as author and provides a more compressed but detailed version, naming five platforms—ChatGPT Atlas, Perplexity Comet, Claude in Chrome, Gemini in Chrome, and Microsoft Copilot Actions—and claiming a first cross-platform analysis of all five [record_id:3117]. These records move the research landscape from workspace assistants to browser agents and from individual prompt-injection incidents to browser-wide exploitation patterns, including drive-by exploitation, account takeover, persistence, data theft, and remote code execution [record_id:2667] [record_id:3117].

The final record, a DEF CON 34 AI Village session coauthored by João Maria Campos Donato and Stav Cohen, shifts from agentic browsers to always-on agents and networked agent ecosystems [record_id:3125]. It describes OpenClaw as an always-on agent embedded in chat, browser, and Google Workspace, and MoltBook as an “Internet of Agents” where many agents reread a shared feed every 30 minutes [record_id:3125]. This record broadens the research area toward agent botnets, agent-to-agent propagation, and ecosystem-level measurement.

Overall, the corpus is narrow but coherent: it is almost entirely about offensive security for LLM-powered agents, especially prompt injection and agent hijacking in environments where agents act with delegated user authority. It does not present Cohen as working broadly across unrelated security domains; rather, these records show a concentrated contribution to emerging AI agent exploitation research.

## Major Themes And Trends

### From Prompt Injection To Agent Hijacking

A major trend across the records is the reframing of prompt injection from a text-generation problem into an agent-hijacking problem. In the Gemini Workspace records, “Promptware” is defined as prompts in text, images, or audio engineered to exploit LLMs at inference time inside an application context [record_id:53] [record_id:1965]. The key shift is that the malicious prompt does not merely cause undesirable text output. It hijacks an integrated agent that has permissions and tools, allowing the attacker to induce actions such as spamming, phishing, calendar deletion, email and calendar exfiltration, geolocation, and even remote control of smart-home appliances [record_id:53] [record_id:1965].

The same conceptual move appears in the later records. Agentic browsers are described as systems where traditional exploit classes return because agents can browse, execute, access files, interact with accounts, and act across sites [record_id:2667] [record_id:3117]. OpenClaw is described as an always-on agent that “swallow[s] untrusted content” with no reliable wall between data and commands, then acts with the user’s permissions [record_id:3125]. Across all records, the problem is not only that the model can be tricked; it is that the model is attached to capabilities.

### Zero-Click And Low-Interaction Attack Delivery

Another recurring theme is the use of ordinary user-facing content as an attack delivery vehicle. The 2025 Gemini work centers on a Google Calendar invite whose subject contains an indirect prompt injection [record_id:53] [record_id:1965]. The abstracts also mention email and shared Google Docs as possible delivery paths [record_id:53] [record_id:1965]. In the agentic-browser work, weaponized calendar invites again appear as targeted payloads, while social media interaction can lead to drive-by exploitation [record_id:2667]. The DEF CON 34 browser abstract lists “poisoned tweet” and “calendar invite” as zero-click vectors [record_id:3117]. The OpenClaw/MoltBook record describes a zero-click prompt injection buried in a shared document, plus posts in an agent network that induce agents to follow a link and phone home [record_id:3125].

This repeated emphasis suggests that Cohen-attributed work is especially concerned with content-mediated exploitation: attackers do not necessarily need to exploit memory corruption or trick a human into approving a suspicious action. Instead, they place adversarial instructions in content that an agent will read as part of its ordinary workflow.

### Delegated Permissions As The Core Risk Amplifier

The records repeatedly stress that agents act with user, browser, workspace, or OS permissions. In the Gemini talks, the attacker hijacks the “application context” and exploits the permissions of integrated Gemini agents [record_id:53] [record_id:1965]. Google Assistant is singled out as powered by Gemini and running with OS permissions on Android devices, enabling outcomes that include smartphone-mediated activity and physical effects through home appliances [record_id:53] [record_id:1965].

The browser-agent records similarly focus on agents with access to accounts, browser state, local files, localhost, scripts, and possibly sandbox escape paths [record_id:2667] [record_id:3117]. The OpenClaw record states that always-on agents live in chat, browser, and Google Workspace and “act with your permissions,” then describes file theft, file wiping, command execution, persistence, and C2 deployment [record_id:3125].

The common pattern is clear: delegated authority transforms instruction-following failures into security incidents. The agent becomes an ambient deputy for the attacker.

### Collapse Or Relaxation Of Traditional Security Boundaries

A prominent theme in the 2026 records is that AI agents are not merely creating new bugs; they are causing vendors to relax old boundaries by design. The Black Hat 2026 PleaseFix abstract claims that “decades of isolation techniques and exploit mitigations” are being intentionally dismantled for agentic browsers, giving examples such as Atlas breaking Same-Origin Policy, Gemini and Edge adding localhost access, Comet opening the filesystem, and Claude executing scripts on any website [record_id:2667]. The DEF CON 34 version makes the same point: vendors “intentionally relax thirty years of browser security” and rely primarily on model safety training [record_id:3117].

This theme is important because it frames the vulnerability class as architectural rather than incidental. The records argue that these are “design choices, not vulnerabilities” in the usual sense, and that those choices revive XSS, sandbox escapes, and drive-by exploitation [record_id:2667] [record_id:3117]. The OpenClaw/MoltBook record expresses a parallel concern in agent infrastructure: agents consume untrusted content without a hard boundary separating data from orders, trusting the model to distinguish the two [record_id:3125].

### Lateral Movement, Persistence, And Worm-Like Behavior

The records also show a progression from single-agent compromise to propagation and persistence. The Gemini work claims demonstrations of both inter-agent lateral movement and inter-device lateral movement: malicious activity can move between different Gemini agents and escape Gemini’s boundaries by leveraging applications installed on a victim’s smartphone [record_id:53] [record_id:1965]. It also claims the ability to launch a worm targeting Gemini for Workspace clients [record_id:53] [record_id:1965].

The browser-agent work describes long-term persistence through agent memory, drive files, and browser history [record_id:2667]. The DEF CON 34 browser record adds “HistoryFixing,” a technique that poisons browsing history trusted by agents as ground truth [record_id:3117]. The OpenClaw/MoltBook record similarly describes persistence by rewriting the agent’s SOUL.md on a timer, and states that the same trick used for harmless pings in MoltBook could ship a worm [record_id:3125].

This suggests an evolution in the research from prompt injection as immediate command hijacking to prompt injection as a basis for durable compromise, memory poisoning, and network-scale spread.

### Physical And Real-World Consequences

The Gemini records are notable for explicitly connecting promptware to physical-world consequences. They claim that an attacker could remotely control home appliances such as connected windows, a boiler, and lights, and could activate lights or open a window in a victim’s apartment via inter-device lateral movement [record_id:53] [record_id:1965]. These examples expand the risk model beyond data leakage and account compromise.

The other records focus more on digital assets—Slack, X, 1Password, Claude, Gmail, Google Drive, local files, GitHub, Amazon, and host takeover—but still include real-world financial or operational consequences such as unauthorized Amazon purchases and use of WhatsApp for phishing [record_id:2667] [record_id:3117]. Across the corpus, the broader implication is that agentic systems bridge online inputs and offline consequences.

### Hard Boundaries Versus Model Safety

The strongest defensive theme is skepticism toward model safety training as a primary security control. The PleaseFix records explicitly state that model safety training is the main mitigation in agentic browsers, then argue that this is insufficient in the face of revived XSS, sandbox escapes, and drive-by exploitation [record_id:2667] [record_id:3117]. The Black Hat 2026 abstract says some browser agents made attacks harder with “creative engineering,” including “hard boundaries” such as deterministic filters and human reviews, while also noting bypasses and vendor collaboration [record_id:2667]. The DEF CON 34 browser abstract states more bluntly that “only deterministic, code-level defenses stopped us” [record_id:3117].

The OpenClaw/MoltBook abstract echoes the same conclusion: “only a hard, code-level boundary, not alignment, would have stopped us” [record_id:3125]. This creates a clear recurring defensive recommendation across the records: AI-agent security should not rely solely on alignment, safety training, or model judgment; it needs enforceable code-level separation of untrusted content, user intent, tools, memory, and permissions.

## Methods, Tools, And Approaches Discussed

The records describe several named methods or approaches, though mostly at abstract level rather than implementation detail.

The earliest method is “Targeted Promptware Attacks,” introduced in the Gemini Workspace talks [record_id:53] [record_id:1965]. The approach is to place an indirect prompt injection in a medium a target’s agent will ingest, especially a Google Calendar meeting subject. Once the victim receives the invitation, the attacker can invoke Gemini