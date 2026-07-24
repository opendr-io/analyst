# Topic: Author: Kane Narraway

## Executive Summary

The available corpus for **Kane Narraway** consists of a single BSidesLV 2026 talk proposal or abstract: **“Paved Roads, AI Potholes: Security Platform Engineering in 2026”** [record_id:2713]. The record presents Narraway as focused on the intersection of **security platform engineering**, **AI-assisted security tooling**, and the operational realities of building security development functions. The talk is framed as a practical and opinionated guide for security engineers and leaders deciding how to build, staff, maintain, or retire internal security tooling in an era where AI has changed both development velocity and the threat landscape [record_id:2713].

The central contribution of the record is its pragmatic stance: AI is neither treated as purely transformative nor dismissed as hype. Instead, the abstract emphasizes evaluating where AI helps, where its benefits are marginal, and where it creates new security burdens. Specific concerns include **agent sandboxing**, **AI access control**, and features being shipped before they are adequately secured [record_id:2713]. The talk also highlights faster prototyping techniques, specifically “ralph loops,” while cautioning that faster shipping does not remove long-term maintenance costs [record_id:2713].

Because there is only one record, the evidence base is narrow. It supports a clear but limited view of Narraway’s public-facing research themes: practical security engineering, platform-building decisions, AI-enabled prototyping, and the governance challenges introduced by AI agents and AI-assisted development workflows.

## Research Landscape

The topic set contains one record attributed to Kane Narraway: a BSidesLV 2026 session titled **“Paved Roads, AI Potholes: Security Platform Engineering in 2026”** [record_id:2713]. The source is the BSidesLV talk listing, with the event identified as **BSidesLV 2026** and the talk scheduled in the **Tuscany** track on **Monday, 17:00–17:30** [record_id:2713]. Its tags include **“[un]prompted”**, suggesting placement within a program area concerned with AI, prompting, or related security implications [record_id:2713].

The record’s topic classification places it primarily under **AI applications, agents, and workflow automation**, with secondary topics of **AI security, prompt injection, and jailbreaking**, and **AI-assisted software development and developer tooling**. The raw abstract supports those classifications insofar as it discusses AI’s impact on security platform engineering, agent sandboxing, AI access control, rapid prototyping of security tooling, and AI-created operational problems [record_id:2713].

The research landscape represented by the record is therefore not broad or archival; it is a single contemporary talk abstract. However, it offers a useful snapshot of a particular 2026 security concern: how organizations should build internal security platforms and developer-facing security functions when AI accelerates prototyping while also introducing new classes of control, access, and assurance problems [record_id:2713].

## Major Themes And Trends

### Security platform engineering as a mature but changing discipline

Narraway’s talk begins from the premise that **security platform engineering is not new**, but that “doing it well in 2026 looks very different than it did two years ago” [record_id:2713]. This implies a theme of continuity and disruption: the core problem of building scalable security infrastructure for developers remains, but the operating environment has changed significantly because of AI.

The abstract frames security platform engineering as a function that must be intentionally built. It mentions “building a security development function from scratch,” including identifying worthwhile problems, shipping MVPs, hiring appropriate staff, and deciding when internal work should be abandoned in favor of vendor solutions [record_id:2713]. This positions Narraway’s contribution less as a narrow technical exploit talk and more as a strategic engineering and organizational framework.

### Practicality over hype

A recurring stance in the record is practical evaluation. Narraway’s abstract promises an “honest look” at how AI has reshaped the landscape and says the talk will be “real about where AI genuinely helps, where it’s marginal” [record_id:2713]. This suggests a deliberate attempt to separate useful AI applications from overclaims.

The framing is important: AI is presented as both an accelerant and a source of risk. The abstract says techniques such as “ralph loops” allow teams to prototype security tooling faster than before, but it immediately balances that benefit against “the flood of new problems AI has created” [record_id:2713]. The trend identified here is not simply AI adoption; it is the tension between AI-driven development speed and the unresolved responsibilities of security design, governance, and maintenance.

### Build-versus-buy decision-making

Another strong theme is the lifecycle of internal security tooling. The talk is described as a guide to “identifying problems worth solving, shipping MVPs, hiring the right people, and knowing when to throw your work away and hand it to a vendor” [record_id:2713]. This reflects a mature platform-engineering concern: internal tools should not be built merely because they can be built quickly, especially when AI lowers the cost of prototyping.

The record suggests that one of Narraway’s distinctive angles is not just how to build, but how to decide whether continued ownership is justified. This includes recognizing when an MVP should become a maintained platform, when it should be retired, and when a vendor product is a better long-term answer [record_id:2713].

### AI as both development accelerator and security burden

The record emphasizes that AI can accelerate security tooling development, but that acceleration creates its own risks. “Ralph loops” are cited as a way to prototype security tooling faster than ever, yet the abstract states that “shipping faster doesn’t eliminate the maintenance burden” [record_id:2713]. This theme is likely central to the talk’s title: paved roads are intended to make secure development easier, but AI creates “potholes” in the form of new security, access-control, and operational problems.

The talk specifically names **agent sandboxing**, **AI access control**, and prematurely shipped features as examples of AI-driven issues [record_id:2713]. These concerns map to broader trends in AI security: agentic systems need boundaries, AI-mediated workflows need permission models, and rapid feature delivery can outpace assurance processes.

### Security leadership and staffing

The record also addresses organizational design. It is aimed both at “a security engineer thinking about building your first tool” and “a leader deciding whether to staff a dedicated team” [record_id:2713]. This dual audience suggests that Narraway’s work bridges hands-on engineering and management decision-making. The talk appears to treat security platform engineering as a function requiring appropriate people, staffing models, and strategic choices, not merely individual technical implementation.

## Methods, Tools, And Approaches Discussed

The record does not provide detailed technical procedures, but it names several methods and approaches that shape the talk’s likely content.

One key approach is building a **security development function from scratch**. The abstract breaks this down into several practical steps: identifying problems worth solving, shipping MVPs, hiring the right people, and deciding when to stop maintaining internally built tools and transfer responsibility to a vendor product [record_id:2713]. This can be understood as a lifecycle model for security platform engineering: problem selection, prototype, team formation, maintenance evaluation, and possible vendor handoff.

Another method discussed is the use of **“ralph loops”** for faster prototyping of security tooling [record_id:2713]. The raw record does not define the term, so downstream researchers should avoid assuming a precise technical meaning without additional sources. In context, however, the abstract presents ralph loops as an AI-era technique that speeds up prototyping. The important evidence-supported claim is that Narraway associates this technique with faster creation of security tools, while also warning that speed does not remove maintenance obligations [record_id:2713].

The talk also foregrounds **agent sandboxing** as an area of concern [record_id:2713]. In the context of AI agents and workflow automation, sandboxing generally refers to constraining an agent’s actions, resources, environment, or permissions. The record does not specify a particular sandbox architecture, but it clearly identifies agent containment as one of the new problems that AI has created for security teams [record_id:2713].

A related approach is **AI access control** [record_id:2713]. Again, the record does not specify an implementation model, but the mention indicates concern with authorization, privilege boundaries, identity, or policy enforcement around AI-enabled systems. This is especially relevant to agentic workflows, where AI systems may act on behalf of users or services and therefore need well-defined permissions.

Finally, the record emphasizes decision frameworks. The talk promises that attendees will leave with “a practical framework” for deciding whether to build a first security tool or staff a dedicated team [record_id:2713]. While the abstract does not enumerate the framework, its components are implied: evaluate problems worth solving, determine MVP viability, consider hiring needs, assess vendor alternatives, and account for AI’s real benefits and costs [record_id:2713].

## Notable Talks, Records, And Evidence

The sole record, **“Paved Roads, AI Potholes: Security Platform Engineering in 2026,”** is the representative and defining evidence for this topic [record_id:2713]. It matters because it places Kane Narraway within an emerging conversation about how AI changes security platform engineering. The talk is not described as a pure AI safety talk, a prompt injection demonstration, or a tool-release presentation. Instead, it appears to be a practical strategy talk about building security tooling and teams under new AI-driven conditions [record_id:2713].

Several elements make the record notable:

- It explicitly contrasts security platform engineering in 2026 with the state of the field two years prior, indicating a focus on recent change [record_id:2713].
- It combines hands-on engineering topics, such as MVPs and prototyping, with leadership concerns, such as hiring and build-versus-buy decisions [record_id:2713].
- It treats AI as both useful and problematic, naming faster prototyping alongside agent sandboxing, AI access control, and insecurely shipped features [record_id:2713].
- It is positioned as “practical” and “opinionated,” suggesting that the talk likely prioritizes lessons learned, decision criteria, and operational judgment over abstract theory [record_id:2713].

The evidence strength for the content of this talk is moderate for identifying intended themes, because the raw record is a conference abstract and provides the speaker’s own description of scope. However, it is weak for determining what was actually said during the session, whether specific tools were demonstrated, or how detailed the proposed framework was. No slides, transcript, video, or post-talk materials are included in the provided corpus.

## Gaps, Limits, And Open Questions

The most important limitation is that the topic corpus includes only one record. As a result, it is not possible to identify long-term trends in Kane Narraway’s work across multiple years, venues, publications, or talk formats. The record provides a snapshot of one BSidesLV 2026 talk, not a full author profile [record_id:2713].

Several specific gaps remain:

1. **No detailed definition of “ralph loops.”**  
   The abstract names ralph loops as a technique for faster security-tooling prototyping, but it does not define the workflow, tooling, or methodology [record_id:2713]. Downstream researchers would need slides, recordings, or related posts to understand whether this refers to a known development loop, an internal practice, or a term coined by the speaker.

2. **No implementation detail for agent sandboxing or AI access control.**  
   The record identifies these as AI-created problems, but it does not explain specific architectures, controls, threat models, or failures [record_id:2713]. Further research would be needed to determine whether Narraway advocates particular sandboxing models, policy engines, isolation mechanisms, or governance practices.

3. **No case studies or examples are provided.**  
   The abstract suggests practical advice on building security development functions, but does not include concrete organizational examples, tool examples, or vendor handoff scenarios [record_id:2713].

4. **No evidence of reception or impact.**  
   The record does not show whether the talk was delivered, how it was received, whether materials were published, or whether it influenced other work [record_id:2713].

5. **No broader author corpus.**  
   Since only one attributed record is available, downstream researchers cannot yet determine whether Narraway consistently works on AI security, platform engineering, developer tooling, or organizational security strategy, or whether this talk is an isolated contribution [record_id:2713].

Open research questions include:

- What exactly are “ralph loops,” and how do they apply to security tooling?
- What practical framework does Narraway propose for deciding when to build, buy, staff, or retire security platforms?
- How does the talk define AI access control in agentic or developer-tooling contexts?
- What specific maintenance burdens arise when AI accelerates security-tool prototyping?
- Does Narraway provide concrete patterns for securing AI-enabled features before they ship?

## Coverage And Evidence Notes

This report covers the full provided corpus: one record attributed to Kane Narraway.

The included record is **[record_id:2713]**, a BSidesLV 2026 talk titled **“Paved Roads, AI Potholes: Security Platform Engineering in 2026.”** It is the only evidence for the topic and supports the report’s conclusions about Narraway’s focus on practical security platform engineering, AI-assisted prototyping, AI-created security problems, agent sandboxing, AI access control, MVP development, hiring, and build-versus-buy decision-making [record_id:2713].

Because there are no additional records, no minor, ambiguous, or weakly tied records are omitted. The analysis should be treated as a focused summary of a single conference abstract rather than a comprehensive account of Kane Narraway’s broader body of work.