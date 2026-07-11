# Topic: Author: Peter Smith

## Executive Summary

The available records attributed to Peter Smith consist of two closely related entries from [un]prompted 2026 for the same talk, **“Beyond the Chatbot: Delivering an Agentic SOC for Real-World Defense,”** co-presented by **Peter Smith**, identified in the raw text as **Director, Agentic SOC Product Management, Salesforce**, and **Ravi Kiran Sharma / RK**, identified as **Lead Security Engineer, Salesforce** [record_id:2380] [record_id:2381].

Across both records, the central contribution is a security-operations vision that moves beyond AI as a simple chatbot or “copilot” for question-answering. The talk frames the next stage of security operations as an **Agentic SOC**, where autonomous agents can **plan, reason, and act** in real-world defense workflows [record_id:2380] [record_id:2381]. The records also emphasize an architectural position: building such systems requires moving away from monolithic “black box” models and toward a **Polyphonic, Supervisor-Worker architecture** [record_id:2380] [record_id:2381].

The evidence base is narrow but consistent. Both records describe the same topic, speakers, event, year, and conceptual framing. One record appears to be a shorter or alternate listing that points to the “full video including demo,” while the other is explicitly titled as the version “including demo” [record_id:2380] [record_id:2381]. As a result, the strongest conclusions concern Peter Smith’s association with agentic SOC product thinking, AI-driven security operations, and multi-agent workflow architecture. The records do not provide detailed implementation specifics, evaluation results, demo contents, deployment lessons, or independent validation.

## Research Landscape

The topic collection contains only two records, and both are from **UNPROMPTED2026**. They are not a broad sample of Peter Smith’s work across many venues, formats, or years; instead, they document a single co-authored/co-presented conference talk, represented in two related source entries [record_id:2380] [record_id:2381].

The records sit at the intersection of:

- **Detection engineering, SOC, SIEM, and threat hunting**, listed as the primary topic area in the metadata;
- **AI applications, agents, and workflow automation**, listed as a secondary topic area;
- Practical security operations product architecture, given Smith’s described role in “Agentic SOC Product Management” at Salesforce [record_id:2380] [record_id:2381].

The raw text positions the talk as a contribution to the evolution of AI in security operations. Rather than presenting AI as a passive assistant, the talk is framed around autonomous systems that can participate in SOC workflows by planning, reasoning, and acting [record_id:2380] [record_id:2381]. The term **“Beyond the Chatbot”** signals a deliberate shift away from chat-based interfaces and simple Q&A toward operationally embedded agents.

The two records appear to be highly overlapping. Record 2380 is titled **“Beyond the Chatbot”** and includes a note that the “Full video including demo” is available at another video link [record_id:2380]. Record 2381 is titled **“Beyond the Chatbot (including demo)”** and gives the full talk title with the parenthetical “including demo” [record_id:2381]. This suggests the collection contains both a talk listing or excerpt-style record and a fuller demo-inclusive record, but the raw descriptions are otherwise substantively the same.

## Major Themes And Trends

### 1. Moving beyond chatbot-style AI in the SOC

The clearest recurring theme is the claim that security operations should move beyond the “copilot” era of simple question-answering. Both records state that the talk is about **“Moving beyond the ‘copilot’ era of simple Q&A”** toward an Agentic SOC [record_id:2380] [record_id:2381]. This framing implies that chatbot interfaces are treated as an earlier or limited stage in the adoption of AI for SOC work.

The records do not dismiss AI assistance outright. Rather, they suggest that chatbots and copilots are insufficient for the next generation of operational defense because they remain largely reactive and conversational. The proposed direction is a system capable of autonomous contribution to workflows.

### 2. The Agentic SOC as the next frontier in security operations

Both records describe the **Agentic SOC** as “the next frontier in security operations” [record_id:2380] [record_id:2381]. In the raw text, this concept is defined by systems “where autonomous agents plan, reason, and act” [record_id:2380] [record_id:2381].

This is the primary substantive idea associated with Peter Smith in the records. The talk appears to argue that future SOC systems will not merely surface information or respond to analyst prompts; they will coordinate actions, make plans, reason through tasks, and execute or assist in defensive operations. Because the records are brief descriptions rather than transcripts, they do not specify exactly which SOC tasks are delegated to agents, how much autonomy is granted, or what safeguards are used.

### 3. Architectural shift away from monolithic black-box models

A second major theme is architectural. The records state that building an Agentic SOC “requires moving away from monolithic ‘black box’ models” [record_id:2380] [record_id:2381]. This suggests concern with opaque, single-model AI systems that attempt to handle many tasks without modular structure, orchestration, or role separation.

The talk’s alternative is described as a **“Polyphonic (Supervisor-Worker) architecture”** [record_id:2380] [record_id:2381]. The word “Polyphonic” implies multiple voices, roles, or agents operating together, while “Supervisor-Worker” suggests hierarchical coordination: one component or agent supervises or orchestrates tasks, while worker components or agents perform specialized subtasks. The records do not give detailed diagrams, implementation components, or design patterns, but the repeated wording makes this architectural distinction central to the talk.

### 4. Practical orientation toward real-world defense

The full title, **“Beyond the Chatbot: Delivering an Agentic SOC for Real-World Defense,”** indicates a practical emphasis [record_id:2380] [record_id:2381]. The phrase “delivering” suggests productization or deployment rather than purely conceptual research, and “real-world defense” suggests applicability to operational environments.

This practical orientation is reinforced by the roles of the speakers in the raw text: Peter Smith is described as Director of Agentic SOC Product Management at Salesforce, while RK Sharma is described as Lead Security Engineer at Salesforce [record_id:2380] [record_id:2381]. Together, those roles suggest a combined product-management and engineering perspective, although the records do not provide enough detail to evaluate how much of the talk is strategic, technical, demo-driven, or case-study-based.

### 5. Co-presented work rather than solo authorship

Both records attribute the talk to **Peter Smith & RK Sharma** [record_id:2380] [record_id:2381]. Therefore, downstream researchers should treat the ideas in these records as co-presented and not solely attributable to Peter Smith. The records support Peter Smith’s involvement in the talk and its themes, but they do not separate which claims, sections, or technical details came from Smith versus Sharma.

## Methods, Tools, And Approaches Discussed

The records do not provide a detailed technical walkthrough, tool list, or implementation plan. However, they do identify several methods and approaches at a conceptual architecture level.

The most important approach is the **Agentic SOC** model. In the raw descriptions, this is a SOC system where autonomous agents can “plan, reason, and act” [record_id:2380] [record_id:2381]. This implies a workflow in which AI agents are not limited to answering analyst questions but participate in multi-step security operations. The records do not specify whether these agents perform triage, investigation, detection engineering, enrichment, response, reporting, or threat hunting, even though the topic metadata places the records in detection engineering, SOC, SIEM, and threat hunting.

The second key approach is a **Polyphonic architecture**, clarified parenthetically as **Supervisor-Worker** [record_id:2380] [record_id:2381]. From the record wording, the architecture is presented as the necessary alternative to monolithic black-box models. The evidence supports the conclusion that Smith and Sharma advocate multi-agent or multi-component orchestration for SOC automation. However, the records do not define the supervisor’s responsibilities, worker specialization, communication model, control boundaries, memory handling, auditability, or human-in-the-loop mechanisms.

The third implied method is use of a **demo**. Record 2380 explicitly says “Full video including demo” and points to another video, while record 2381’s title includes “including demo” [record_id:2380] [record_id:2381]. This indicates that the talk likely included a demonstration of the Agentic SOC concept or architecture. The raw text does not describe what was demonstrated, so any detailed claims about the demo would require reviewing the source video or additional records.

## Notable Talks, Records, And Evidence

The two records are best understood as different entries for the same notable talk.

**Record 2380** documents **“Beyond the Chatbot”** at UNPROMPTED2026, presented by Peter Smith and RK Sharma [record_id:2380]. It gives the speakers’ Salesforce roles and frames the talk around the transition from simple AI Q&A to an Agentic SOC. It also notes that a “Full video including demo” is available at a separate video link [record_id:2380]. This record matters because it establishes the talk topic, the speakers, the event, and the high-level thesis.

**Record 2381** appears to be the full/demo-inclusive version: **“Beyond the Chatbot (including demo)”** [record_id:2381]. It repeats the same core description: the talk concerns delivering an Agentic SOC for real-world defense, moving beyond the copilot era, and adopting a Polyphonic Supervisor-Worker architecture rather than monolithic black-box models [record_id:2381]. This record matters because it confirms that the demo-inclusive version belongs to the same conceptual package and reinforces the central claims from record 2380.

Together, the records provide strong evidence that Peter Smith is associated, in this dataset, with the topic of **agentic AI for security operations**. They provide weaker evidence about the specific technical implementation, because the raw text is a short abstract-style description rather than a transcript, paper, slide deck, or detailed technical write-up.

## Gaps, Limits, And Open Questions

The biggest limitation is the small and duplicative evidence base. There are only two records, and both describe essentially the same UNPROMPTED2026 talk [record_id:2380] [record_id:2381]. This means the collection can support a focused summary of one presentation, but not a comprehensive profile of Peter Smith’s broader body of work.

Important open questions include:

- **What did the demo show?** The records indicate that there was a demo or a demo-inclusive video, but they do not describe its contents, workflow, interface, or technical outcome [record_id:2380] [record_id:2381].
- **How is the Supervisor-Worker architecture implemented?** The phrase appears in both records, but the raw text does not define the architecture beyond naming it as “Polyphonic” and contrasting it with monolithic black-box models [record_id:2380] [record_id:2381].
- **What SOC tasks are in scope?** The records refer broadly to security operations and real-world defense but do not list specific use cases such as alert triage, incident response, detection tuning, threat hunting, or SIEM query generation [record_id:2380] [record_id:2381].
- **What are the safety, governance, and control mechanisms?** Autonomous agents that “plan, reason, and act” raise questions about permissions, approvals, audit trails, error handling, rollback, and human oversight. The records do not address these issues directly [record_id:2380] [record_id:2381].
- **What evidence validates effectiveness?** The records do not provide metrics, case studies, benchmark results, analyst productivity data, detection-quality improvements, or comparisons to chatbot/copilot systems [record_id:2380] [record_id:2381].
- **Which contributions are Peter Smith’s versus RK Sharma’s?** Both records identify the talk as co-presented, but neither separates the speakers’ individual contributions [record_id:2380] [record_id:2381].

For downstream research agents, the main follow-up should be to inspect the linked video material, especially the demo-inclusive version, and extract concrete examples of workflows, architecture diagrams, terminology, product claims, evaluation evidence, and any stated design constraints.

## Coverage And Evidence Notes

This report covers all two expected records.

- **[record_id:2380]** is a UNPROMPTED2026 record for **“Beyond the Chatbot”** by Peter Smith and RK Sharma. It identifies Smith as Director, Agentic SOC Product Management at Salesforce and Sharma as Lead Security Engineer at Salesforce. It describes the talk as moving beyond simple copilot-style Q&A toward an Agentic SOC where autonomous agents plan, reason, and act, and it emphasizes a Polyphonic Supervisor-Worker architecture rather than monolithic black-box models. It also points to a full video including a demo.
- **[record_id:2381]** is the demo-inclusive UNPROMPTED2026 record for **“Beyond the Chatbot (including demo)”** by the same speakers. It repeats the same core framing around Agentic SOC, autonomous agents, and Polyphonic Supervisor-Worker architecture.

No record in this topic is minor in the sense of being unrelated, but the two records are highly overlapping. The evidence is therefore coherent but narrow: it strongly supports the existence and theme of one