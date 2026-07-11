# Topic: Author: Joshua Saxe

## Executive Summary

The available record set for “Author: Joshua Saxe” is very small: two records, one with substantive raw text and one with no raw text. The strongest evidence comes from a 2026 [un]prompted talk, “The Hard Part Isn’t Building the Agent: On Measuring Agent Effectiveness to Improve It,” attributed to Joshua Saxe, identified in the raw text as “AI Security Technical Lead, Meta” [record_id:2322]. That record centers on a clear research and practice theme: as AI coding tools make it increasingly cheap to build security agents, the difficult and strategically important problem becomes evaluating whether those agents work against real, novel attacks and vulnerabilities [record_id:2322].

Across the records, the identifiable Joshua Saxe research profile is therefore thin but suggestive: he is associated with forward-looking AI-for-security questions, especially practical measurement, evaluation, and improvement of AI security agents [record_id:2322]. The second record is a 2024 CAMLIS keynote entry, but its raw record text is empty, so it cannot support substantive claims about the talk’s arguments, methods, or conclusions beyond noting its presence in the corpus and the supplied record metadata [record_id:143].

## Research Landscape

The corpus contains two attributed records. The substantive landscape is dominated by one conference-style talk description from [un]prompted 2026 [record_id:2322]. That description frames the topic around AI agents for security work, particularly security agents built with AI coding tools. The talk is not primarily about how to build an agent; instead, it argues that agent construction is becoming easier and cheaper, while evaluation remains the bottleneck [record_id:2322].

The other included record is a CAMLIS 2024 keynote entry titled in the supplied metadata as “You’ll Never Guess What Happens Next: Acting to Ensure AI Benefits Cyber Defense in a Decade of Technological Surprise,” attributed to Joshua Saxe [record_id:143]. However, the raw record text for this entry is empty. Because the instructions require raw text to be treated as authoritative evidence, this report treats that record as coverage evidence only, not as support for any detailed claim about Saxe’s 2024 arguments [record_id:143].

Overall, the research landscape represented here is narrow but coherent: Joshua Saxe is represented as a speaker on AI and cyber defense, with the strongest documented emphasis on measurement frameworks for security AI agents [record_id:2322]. The records do not provide papers, slide text, transcripts, implementation details, benchmark data, or empirical results; they provide talk-level descriptions.

## Major Themes And Trends

### Measuring AI security agents becomes harder and more important than building them

The central theme in the available substantive record is a shift from agent construction to agent evaluation. Record 2322 states that “AI coding tools drive the cost of building security agents toward zero,” making the “hard problem” determining whether those agents “actually work in the wild against real attacks and vulnerabilities we haven’t seen before” [record_id:2322]. This positions Saxe’s talk within a broader trend in AI security engineering: as generative and coding tools accelerate prototyping, the bottleneck moves from implementation to validation.

The language of the record suggests concern with generalization and operational reliability. It is not enough for an agent to perform on known examples or retrospective datasets. The talk description explicitly foregrounds “real attacks and vulnerabilities we haven’t seen before,” implying that security-agent evaluation must test performance under novelty, ambiguity, and adversarial conditions [record_id:2322].

### Movement beyond naive precision and recall

A second theme is dissatisfaction with simple metrics. The talk description describes a “practical journey from naive precision/recall metrics on old data toward multi-dimensional evaluation” [record_id:2322]. This is important because precision and recall are common evaluation measures in detection and classification tasks, but the record indicates that Saxe’s talk treats them as insufficient for evaluating complex AI agents.

The critique appears to be not that precision and recall are useless, but that they are too narrow when used alone, especially on historical data. The talk’s framing suggests that security agents need to be evaluated on process quality as well as outcome quality. In other words, it matters not only whether an agent flags the right item, but how it reasons, what evidence it gathers, and whether it uses tools appropriately [record_id:2322].

### Multi-dimensional evaluation of reasoning, evidence, and tool use

The record identifies three dimensions of evaluation: “reasoning quality, evidence gathering, and tool-calling logic” [record_id:2322]. These dimensions suggest a model of agent effectiveness that is closer to assessing an analyst workflow than scoring a simple classifier.

Reasoning quality concerns whether the agent draws justified conclusions. Evidence gathering concerns whether the agent obtains and uses relevant supporting information. Tool-calling logic concerns whether the agent invokes available tools appropriately and in the right sequence [record_id:2322]. Together, these dimensions reflect the needs of AI agents operating in security contexts, where a good answer often depends on investigation, context assembly, and careful procedural choices rather than a single prediction.

### Measurement as a path to automated improvement

The final major theme is that evaluation is not just a reporting activity; it enables optimization. The talk description says that “proper measurement unlocks automated agent improvement using genetic algorithms and AI coding tools” [record_id:2322]. This is a notable contribution because it links evaluation infrastructure to iterative agent development.

The implied workflow is: define meaningful measurements, evaluate agents along multiple dimensions, identify weaknesses, and then use automated methods to improve the agent. Genetic algorithms are specifically named as one mechanism for automated improvement, alongside AI coding tools [record_id:2322]. The record does not provide implementation details, but it does indicate that Saxe’s talk treats measurement as the foundation for closed-loop improvement rather than as an after-the-fact scorecard.

### Forward-looking AI and cyber defense concerns

The CAMLIS 2024 keynote record cannot be used for substantive evidence because its raw text is empty [record_id:143]. However, its presence in the attributed corpus alongside the [un]prompted 2026 talk suggests that the dataset associates Saxe with high-level AI-and-cyber-defense discussions as well as practical agent-evaluation work. Any stronger claim about the 2024 keynote’s content would require the missing abstract, transcript, slides, or other raw source material [record_id:143].

## Methods, Tools, And Approaches Discussed

The substantive methodological content appears in record 2322. The described approach begins with an evaluation problem: determining whether AI-built security agents will work “in the wild” against unseen attacks and vulnerabilities [record_id:2322]. This requires moving beyond “naive precision/recall metrics on old data” toward a broader assessment framework [record_id:2322].

The record names several evaluation dimensions:

- **Reasoning quality**: assessing whether the agent’s reasoning process is sound, not merely whether its final output is correct [record_id:2322].
- **Evidence gathering**: evaluating how well the agent collects, selects, and uses relevant evidence in support of its conclusions [record_id:2322].
- **Tool-calling logic**: measuring whether the agent uses external tools appropriately, presumably including when to call tools and how to integrate their outputs [record_id:2322].

The record also names two improvement mechanisms:

- **Genetic algorithms**, presented as part of automated agent improvement once proper measurement is available [record_id:2322].
- **AI coding tools**, which are described both as driving down the cost of building security agents and as part of the improvement loop [record_id:2322].

The talk description also notes that a “Live demo” was included [record_id:2322]. That suggests the methods were not purely conceptual, but the raw text does not describe the demo’s contents, datasets, tools, architecture, or results. Downstream researchers should therefore treat the presence of a demo as evidence of practical orientation, but not infer the technical implementation without additional source material.

No methods can be extracted from record 143 because the raw record text is empty [record_id:143].

## Notable Talks, Records, And Evidence

The most important record is the 2026 [un]prompted talk, “The Hard Part Isn’t Building the Agent: Measuring Effectiveness,” because it contains the only substantive raw description in the corpus [record_id:2322]. It identifies Joshua Saxe as “AI Security Technical Lead, Meta” and frames his talk around measuring AI security-agent effectiveness [record_id:2322]. Its importance lies in three linked claims: AI coding tools are making agent construction cheap; old-data precision/recall evaluations are inadequate; and multi-dimensional measurement can support automated improvement via genetic algorithms and AI coding tools [record_id:2322].

This record is representative of a practical AI-security engineering perspective. It addresses not just whether agents can be built, but whether they can be trusted to operate against unfamiliar real-world threats [record_id:2322]. It also bridges evaluation and optimization by arguing that good measurement enables agent improvement [record_id:2322].

The CAMLIS 2024 keynote record is notable mainly because it indicates another attributed Joshua Saxe appearance in the corpus, but the raw text field is empty [record_id:143]. The supplied metadata names the talk as “Keynote - You’ll Never Guess What Happens Next: Acting to Ensure AI Benefits Cyber Defense in a Decade of Technological Surprise” at CAMLIS in 2024 [record_id:143]. Because no raw abstract or description is available, this report cannot summarize its substantive content or connect it evidentially to the themes in record 2322 beyond noting that both records are attributed to Joshua Saxe in the provided dataset [record_id:143].

## Gaps, Limits, And Open Questions

The largest limitation is evidence volume. There are only two records, and one has no raw text [record_id:143]. As a result, the synthesis depends heavily on a single talk description [record_id:2322]. The conclusions should be treated as a preliminary profile rather than a comprehensive account of Joshua Saxe’s work.

Several important questions remain unanswered:

1. **What specific evaluation framework was proposed?**  
   Record 2322 mentions multi-dimensional evaluation but does not provide scoring rubrics, benchmark construction methods, task suites, datasets, or validation procedures [record_id:2322].

2. **How were reasoning quality, evidence gathering, and tool-calling logic measured?**  
   The record names these dimensions but does not specify whether they were measured by human evaluators, automated judges, trace analysis, ground-truth comparison, or other methods [record_id:2322].

3. **What agents or security tasks were evaluated?**  
   The record refers broadly to “security agents,” “real attacks,” and “vulnerabilities,” but does not specify whether the agents performed triage, vulnerability discovery, detection engineering, incident response, malware analysis, threat hunting, code review, or another task [record_id:2322].

4. **How were genetic algorithms used?**  
   The record says measurement unlocks improvement using genetic algorithms and AI coding tools, but it does not explain the representation, fitness function, mutation strategy, selection process, or what aspects of the agent were evolved [record_id:2322].

5. **What happened in the live demo?**  
   The talk description notes a live demo, but the raw text gives no details about the demonstration scenario, tooling, outcome, or reproducibility [record_id:2322].

6. **What was the substance of the 2024 CAMLIS keynote?**  
   Record 143 has empty raw text, so its arguments, examples, and recommendations are unknown from the authoritative record content available here [record_id:143]. The title metadata suggests a relationship to AI and cyber defense, but downstream researchers should obtain the original CAMLIS page, abstract, slides, or transcript before drawing conclusions [record_id:143].

A broader open question is whether Saxe’s work, as represented here, is primarily about AI governance for cyber defense, operational evaluation of AI systems, automated security-agent development, or some combination. The existing evidence supports the evaluation-and-improvement theme most strongly [record_id:2322], while the governance or long-term cyber-defense theme cannot be substantiated from raw text in this record set [record_id:143].

## Coverage And Evidence Notes

This report covers both expected records.

Record 2322 is the primary evidence source. Its