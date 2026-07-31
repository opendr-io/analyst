# Topic: Author: Katie Paxton-Fear

## Meta-Summary

The three records attributed to Katie Paxton-Fear span insider-threat analysis, bug-bounty triage, and consumer-device hacking. Collectively, they show a practical security-research orientation: turning ambiguous narratives or noisy reports into actionable evidence, and exposing the security-relevant complexity hidden beneath familiar systems and devices.

The 2021 CAMLIS presentation proposes using natural-language processing (NLP), topic modeling, and graph visualization to reconstruct insider-threat incidents from news articles and witness reports [record_id:201]. Two DEF CON 34 records from 2026 move into more directly operational areas. One, co-authored with Max vonBlankenburg, introduces “Slop Spotting,” a method that uses static application security testing (SAST) rule generation to test whether apparently AI-generated bug reports correspond to code actually present in a target repository [record_id:3044]. The other surveys the vulnerabilities, jailbreaks, custom firmware, and broader hackability of eReaders [record_id:3049].

Across this small corpus, the strongest recurring theme is evidence validation: finding structured, testable signals in environments where surface appearances can be misleading. Insider activity can resemble legitimate work, fabricated vulnerability reports can cite real code concepts and CVEs, and minimalist reading appliances can conceal flexible and vulnerable computing platforms.

## Research Landscape

The collection consists of three conference-session descriptions rather than full papers, transcripts, demonstrations, or empirical result sets. CAMLIS provides the earliest and most detailed record: a research-oriented proof of concept for modeling insider incidents from textual narratives [record_id:201]. The two later records are DEF CON 34 creator-stage talks, one associated with the Bug Bounty Village and the other with the IoT Village [record_id:3044] [record_id:3049].

The represented research landscape is consequently broad:

- **Human-centered threat analysis:** The insider-threat work integrates organizational, technical, psychological, and social perspectives rather than treating the problem solely as network anomaly detection [record_id:201].
- **Application-security operations:** “Slop Spotting” addresses the burden that plausible but invalid AI-generated vulnerability submissions place on open-source maintainers and bug-bounty teams [record_id:3044].
- **IoT and consumer hardware security:** The eReader presentation treats Kindles, Kobos, Boox devices, and BigMes as general-purpose, modifiable attack surfaces rather than single-purpose appliances [record_id:3049].

No one source type dominates numerically beyond conference descriptions, but the CAMLIS record contains substantially more methodological detail than either DEF CON abstract. The corpus therefore supports a richer interpretation of the insider-threat project than of the later talks. It also suggests widening topical breadth over time—from an interdisciplinary NLP research prototype in 2021 to operational application-security and device-hacking subjects in 2026—but three records are too few to establish a firm longitudinal shift.

## Major Themes And Trends

### Converting ambiguous evidence into structured security judgments

The clearest common thread is the challenge of deciding what is real, relevant, or malicious when the available evidence is ambiguous.

In the insider-threat setting, malicious actions are difficult to distinguish from normal work because insiders possess legitimate credentials, understand organizational processes, and may access sensitive files as part of their jobs. Their attack behavior can be both co-spatial and co-temporal with legitimate activity, and changes in access patterns may reflect either malicious conduct or benign changes in duties [record_id:201]. The proposed response is not merely more alerting, but the organization of narrative evidence into themes, relationships, and incident graphs that investigators can explore.

In bug bounty, ambiguity arises from reports that appear technically credible but allegedly describe code that is not present in the project. The reports may refer to real vulnerability classes, source lines, or previously resolved CVEs, forcing maintainers to spend time establishing that the submissions are invalid [record_id:3044]. “Slop Spotting” converts this uncertain judgment into a more constrained test: formulate the reported issue as a SAST rule and determine whether the rule matches the actual codebase.

The eReader talk is less directly about evidence processing, but it also challenges surface-level assumptions. Devices marketed around a single, simple task—reading—may support jailbreaks, Android applications, custom firmware, and vulnerability research [record_id:3049]. Across all three records, apparently straightforward objects or activities conceal more complicated security realities.

### Supporting human investigators rather than simply replacing them

The insider-threat system is explicitly framed as supporting existing practices, not supplanting them. Its purpose is to help an investigator ask questions about motive, targeted assets, attack methods, existing controls, and how those controls were bypassed [record_id:201]. The resulting visualization is intended to aid reflection and inform organizational changes, such as restricting access or deploying additional controls.

The bug-bounty method similarly responds to a human workload problem. The abstract emphasizes that triage is expensive, slow, and demoralizing for maintainers, especially when an apparently credible submission requires careful examination but yields no valid issue [record_id:3044]. Its proposed SAST-based signal is lightweight and designed to produce a rapid yes-or-no result even across large repositories.

Thus, the records do not primarily present autonomous security decision systems. Instead, they describe methods that reduce the search space or provide additional evidence to human analysts, investigators, and maintainers.

### Security consequences of privileged or highly capable actors and tools

The insider-threat work focuses on people who already possess access and contextual knowledge. Their privileges, awareness of controls, and ability to blend into ordinary operations make conventional outsider-oriented detection less effective [record_id:201].

“Slop Spotting” describes a different asymmetry: generative systems can produce large volumes of convincing reports much more cheaply than small security teams can validate them. The cited case says curl ended its HackerOne program in January 2026 after AI-generated reports overwhelmed a seven-person team; in some weeks it received seven reports in sixteen hours, with none valid [record_id:3044]. Whether viewed as abuse, low-quality automation, or an incentive problem, the effect is to transfer substantial verification costs to maintainers.

The eReader record highlights capability hidden in consumer devices. Jailbreaking, sideloaded Android applications, and firmware modification can turn a reading appliance into a research platform, while the same extensibility implies opportunities for vulnerability discovery and exploitation [record_id:3049].

### Interdisciplinary and cross-layer analysis

The insider-threat presentation is explicitly interdisciplinary. It combines organizational mitigation, network-oriented technical detection, and psychological or social inquiry into motivation and behavioral change [record_id:201]. It also proposes mapping “organic narratives” onto existing frameworks rather than requiring witnesses to structure their accounts according to a predetermined model.

The later talks operate at other layers: source-code analysis and bug-bounty workflows in one case [record_id:3044], and operating systems, firmware, and consumer hardware in the other [record_id:3049]. Taken together, the records portray security as a cross-layer discipline in which human behavior, text analysis, software verification, platform policy, firmware, and physical devices all matter.

## Methods, Tools, And Approaches Discussed

The insider-threat project begins with a corpus of publicly available news articles concerning insider incidents. It applies **topic modeling** to identify recurring themes through word associations, with the goal of extracting attributes such as attack methods, motivations, the insider’s organizational role, and weaknesses in the affected organization [record_id:201]. Those themes form a custom insider-threat model that can be updated with new documents.

The model is then applied to witness reports. Temporal, causal, and narrative clues are combined so that the incident can be represented as a graph resembling existing insider-threat models [record_id:201]. Investigators can use the graph to explore questions such as:

- What motivated the insider?
- Which assets were targeted?
- How were they targeted?
- Which controls existed?
- Were those controls bypassed?

The work remains a proof of concept rather than a described production system. The record identifies co-reference resolution and improved entity or graph merging as possible enhancements, especially for creating graphs at a broader or “macro” level [record_id:201]. A distinctive methodological contribution is its use of reports already produced after incidents. Rather than forcing witnesses to adapt their accounts to a formal framework, the system attempts to preserve natural narratives and map them into that framework afterward.

“Slop Spotting” uses a much narrower and more directly testable workflow. The analyst takes the vulnerability described in a bug-bounty report and attempts to express it as a **SAST rule**. The proposal rests on two linked assumptions: a genuine and sufficiently well-specified flaw should be expressible as a static-analysis rule, and the rule should produce a result if the relevant code pattern is actually present [record_id:3044]. A report that sounds convincing but refers to absent code should fail this validation quickly. The output is presented as a validity signal rather than a complete replacement for vulnerability assessment.

The eReader talk describes several classes of hands-on device-security activity: **Kindle jailbreaking, running Android applications, flashing custom firmware, vulnerability exploration, and device customization** [record_id:3049]. The abstract does not identify specific exploits, hardware-debug interfaces, reverse-engineering suites, firmware extraction methods, or affected versions. It nevertheless frames unused consumer eReaders as accessible lab platforms for IoT and embedded-device experimentation.

## Notable Talks, Records, And Evidence

The most substantively detailed record is **“Visualising an insider threat incident from witness reports using natural language processing,”** presented at CAMLIS in 2021 [record_id:201]. It matters because it provides a full problem formulation as well as a proposed analytical pipeline. The record explains why insiders are difficult to detect, distinguishes unintentional from malicious incidents, identifies organizational, technical, psychological, and social approaches to risk, and describes how topic modeling and graph visualization might combine these perspectives. It also carefully limits its claim by calling the implementation a proof of concept and naming technical areas that require improvement.

**“Slop Spotting, Using Rules to Detect AI Slop for Bug Bounty,”** a DEF CON 34 session attributed to Katie Paxton-Fear and Max vonBlankenburg, is the corpus’s clearest response to generative AI’s operational effects on security work [record_id:3044]. Its unique contribution is not a generic call for better spam filtering, but a concrete validation heuristic tied to the target codebase. The talk’s motivating example is striking: AI-generated reports can include authentic-looking references and plausible vulnerability reasoning while still being wholly inapplicable to the project. The proposed answer is executable or machine-checkable grounding through a SAST rule.

**“Beyond Your Bookshelf: Hackable eReaders”** broadens the corpus from analytical workflows to device exploration [record_id:3049]. Its importance lies in threat-surface reframing. EReaders are presented as modifiable computing systems with jailbreak, application, firmware, and vulnerability-research possibilities—not merely as closed reading devices. Compared with the other records, however, the abstract is introductory and gives little evidence about particular flaws or findings.

## Gaps, Limits, And Open Questions

The corpus is too small and heterogeneous to establish a comprehensive account of Katie Paxton-Fear’s overall research output. It contains only three conference descriptions, two of which are brief. No slides, recordings, code, datasets, evaluation tables, audience questions, or post-talk revisions are included.

For the insider-threat project, several validation questions remain unanswered:

- How accurately does topic modeling recover meaningful insider-threat attributes?
- What corpora, labeling processes, preprocessing steps, or topic-model algorithms were used?
- How are contradictory witness reports handled?
- How are people, assets, motives, and events merged across documents?
- How is uncertainty represented in the resulting graph?
- Did investigators find the visualizations useful or make better decisions because of them?
- What privacy, bias, and evidentiary risks arise when deriving models from news coverage and witness narratives?

The record itself acknowledges that the work is a proof of concept and suggests co-reference resolution and improved merging as future directions [record_id:201]. This makes its conceptual rationale stronger than its empirical support.

For “Slop Spotting,” the main open issue is whether SAST-rule generation is a reliable discriminator. Some real vulnerabilities depend on runtime state, business logic, deployment configuration, data flow across systems, concurrency, or human workflow and may not be readily representable as static rules. Conversely, a generated rule could match code without proving exploitability. The abstract does not explain whether rules are written by humans, generated automatically, or produced with AI assistance; nor does it provide benchmark results, false-positive rates, false-negative rates, or comparisons with ordinary manual triage [record_id:3044]. The curl example is a strong motivating anecdote within the record, but the corpus provides no independent corroboration or broader prevalence data.

For the eReader work, nearly all technical specifics remain open. The record does not distinguish among vulnerabilities that enable jailbreaks, vendor-supported Android extensibility, and customization requiring physical access or firmware flashing. It also does not specify device models, firmware versions, persistence mechanisms, exploit chains, privilege boundaries, or defensive recommendations [record_id:3049]. Future research would need to determine whether the talk is primarily a survey, a tutorial, or a disclosure of original vulnerabilities.

A broader unanswered question is whether there is a direct methodological continuity among these projects. All can be interpreted as efforts to reveal hidden structure and validate security-relevant claims, but the records do not explicitly state that this is an intentional research program.

## Coverage And Evidence Notes

All three expected records are represented in this report.

The CAMLIS 2021 record is the strongest source for methods and research framing. It attributes the insider-threat presentation solely to Katie Paxton-Fear and describes an NLP and visualization proof of concept in considerable detail [record_id:201]. Its evidence is still an abstract-level project description rather than a peer-reviewed evaluation or complete implementation report.

The DEF CON 34 bug-bounty record is jointly attributed to Katie Paxton-Fear and Max vonBlankenburg. Claims or methods from that session should therefore not be attributed exclusively to Paxton-Fear without qualification [record_id:3044]. The abstract provides a concrete operational problem and a succinct proposed method, but no measured evaluation.

The DEF CON 34 eReader record is solely attributed to Katie Paxton-Fear. It offers the broadest device-oriented topic in the collection but the least methodological detail, functioning mainly as a talk preview about jailbreaks, Android applications, custom firmware, vulnerabilities, and eReader customization [record_id:3049].

Overall, the evidence is strongest for identifying topics, motivations, and proposed approaches. It is considerably thinner for establishing effectiveness, novelty relative to prior work, production adoption, or reproducibility.