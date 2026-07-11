# Topic: Author: Paul Miller

## Executive Summary

The two records attributed to Paul Miller show a compact but wide-ranging profile: one co-authored DEF CON 33 presentation on privacy-preserving infrastructure and user-owned data, and one BSidesLV 2025 talk on threat intelligence applied to a high-consequence operational technology incident involving nuclear reactor control systems. Together, the records place Paul Miller at the intersection of privacy engineering, decentralized or user-controlled computation, and defensive security work around critical infrastructure.

The evidence base is small—only two records—and consists of talk abstracts rather than full transcripts or slide decks. Even so, the records suggest two clear areas of contribution. First, Miller is associated with Veilid, a framework presented as part of a broader movement to restore digital privacy, shift control over computation and data back to users, and support applications built on a new technology stack [record_id:2043]. Second, Miller is associated with applied threat intelligence in a serious operational technology context, specifically an alleged March 2022 attack aimed at backdooring or incapacitating nuclear reactor control systems [record_id:2544].

The records do not provide implementation details, technical indicators, adversary attribution, architectural diagrams, or operational lessons in depth. They do, however, identify the talks’ thematic centers: privacy/data ownership through Veilid, and high-impact incident response or threat intelligence in nuclear control-system security.

## Research Landscape

The available research landscape for “Author: Paul Miller” is narrow but notable. Both records are conference talks from 2025 security events. One comes from DEF CON 33 and is co-authored by Katelyn Bowden and Paul Miller, titled “Veilid la revoluçion : Your data is yours to own” [record_id:2043]. The other comes from BSidesLV 2025, titled “Stopping the Nuclear Apocalypse with Threat Intel (Token 11),” authored by Paul Miller [record_id:2544].

The DEF CON record is situated in the Crypto and Privacy Village and frames Veilid as a continuation of a project previously revealed at DEF CON 31. Its raw abstract says Veilid was “revealed to the world as a part of the Bovine Resurrection,” generated worldwide press coverage, and helped move “the window” on how the press discussed digital privacy [record_id:2043]. This talk appears to be outreach-oriented: it promises to explain the “whys and hows” of the Veilid Framework, discuss a “combined technology stack,” cover fundamentals, report progress, and describe apps released on the framework [record_id:2043].

The BSidesLV record is much shorter and more incident-centered. It describes a March 2022 event in which Miller’s team allegedly uncovered an attack against a customer “specifically targeted at backdooring/incapacitating nuclear reactor control systems” [record_id:2544]. The framing is narrative—“This is our story”—and the title emphasizes threat intelligence as the means by which a potential catastrophe was addressed [record_id:2544].

Overall, the records do not represent a dense publication trail. They instead capture two public presentations that place Miller in two different but security-relevant domains: privacy infrastructure and critical infrastructure defense. The contrast between the two talks is important. One is forward-looking and movement-oriented, focused on building frameworks and applications for user-controlled data [record_id:2043]. The other is retrospective and incident-oriented, focused on a specific attack scenario involving nuclear reactor control systems [record_id:2544].

## Major Themes And Trends

### User ownership of data and computation

The most explicit theme in the DEF CON record is user ownership. The title itself, “Your data is yours to own,” establishes a rights-oriented and autonomy-oriented framing [record_id:2043]. The abstract expands this into a broader technical and political claim: Veilid is presented as part of “restoring the future we were promised,” and the talk says it will explain how people can “seize the means of computation” [record_id:2043].

This language suggests that the talk is not merely about a privacy tool in isolation. It positions Veilid as a framework for changing how computation, applications, and data ownership are structured. The abstract implies that the authors see privacy failures as connected to centralized control over infrastructure and data. The promised focus on “fundamentals of Veilid,” “progress made,” and “apps that have been released” suggests the project is intended to be practical and ecosystem-based rather than purely conceptual [record_id:2043].

Because the record is an abstract, the evidence is strong for the talk’s intended themes but thin on technical specifics. It establishes that Miller is connected to a privacy framework and to advocacy around user data ownership, but it does not specify cryptographic protocols, network design, application APIs, identity models, metadata protections, or threat models [record_id:2043].

### Privacy as public narrative and movement-building

The DEF CON abstract also emphasizes communications strategy and public discourse. It says the DEF CON 31 reveal generated press coverage worldwide and “managed to drag the window over on how the press talked about digital privacy” [record_id:2043]. This phrasing suggests a recurring concern beyond engineering: shaping the social, media, and cultural framing of privacy.

The talk’s promised aim to “spread the good word of the future restored” and explain “HOW YOU CAN HELP” also suggests community-building and recruitment [record_id:2043]. The Veilid presentation appears to combine technical explanation, project update, and movement rhetoric. For downstream researchers, this means Miller’s contribution in this record should be understood as partly technical and partly advocacy-oriented.

### Threat intelligence for high-consequence infrastructure defense

The BSidesLV record centers on threat intelligence in a critical infrastructure scenario. Its title, “Stopping the Nuclear Apocalypse with Threat Intel,” is deliberately dramatic, but the raw abstract gives a concrete claim: in March 2022, Miller’s team uncovered an attack on a customer that was “specifically targeted at backdooring/incapacitating nuclear reactor control systems” [record_id:2544].

This record indicates a theme of applied threat intelligence in operational technology or industrial control system contexts. The abstract implies that threat intelligence was not merely a background function but a decisive investigative or defensive capability. The phrase “my team and I uncovered an attack” suggests active detection, analysis, or incident response work [record_id:2544]. The targeted systems—nuclear reactor control systems—make the stakes unusually high.

However, the evidence is limited to an abstract. It does not identify the customer, country, reactor type, threat actor, malware family, intrusion vector, timeline, indicators of compromise, mitigation steps, or whether the attack achieved any operational effect [record_id:2544]. The record is therefore strong evidence that Miller presented on such a case, but not enough to independently evaluate the attack’s details or broader significance.

### Dual emphasis on empowerment and protection

Across the two records, one broad synthesis is that Miller-associated work is framed around control: users controlling their own data and computation in the Veilid talk [record_id:2043], and defenders detecting or preventing malicious control over nuclear reactor systems in the BSidesLV talk [record_id:2544]. These are very different domains, but both involve adversarial relationships around who controls technical systems.

In the Veilid record, the adversary is implied to be the current privacy-hostile or centralized computing environment, though the abstract does not name specific companies, governments, or surveillance systems [record_id:2043]. In the nuclear-control-system record, the adversary is an attacker seeking to backdoor or incapacitate industrial control systems, though the abstract does not name an actor [record_id:2544]. In both cases, the talks appear to advocate technical work that restores or preserves legitimate control.

## Methods, Tools, And Approaches Discussed

The records provide only high-level descriptions of methods and tools, but several approaches can be identified.

The most concrete tool or framework named is Veilid. The DEF CON abstract says the talk will cover “the whys and hows of the Veilid Framework,” the “fundamentals of Veilid,” progress since its earlier reveal, and applications released on the framework [record_id:2043]. This establishes Veilid as a core technical object in Miller’s co-authored work. The record describes it as a “combined technology stack” tied to data ownership and restored digital privacy [record_id:2043]. It does not provide specifics on the stack’s components, programming model, networking approach, cryptographic design, or deployment model.

The DEF CON record also implies an ecosystem-development approach. Rather than presenting only a protocol or isolated proof of concept, the abstract refers to “apps that have been released on our framework” [record_id:2043]. This suggests an approach based on building usable applications atop privacy-preserving infrastructure. For researchers, the key lead is not just Veilid as a framework but Veilid as an application platform.

The BSidesLV record’s primary method is threat intelligence. The title directly frames the story as “Stopping the Nuclear Apocalypse with Threat Intel” [record_id:2544]. The abstract says Miller’s team uncovered an attack targeting nuclear reactor control systems [record_id:2544]. This suggests an approach involving intelligence collection, analysis, detection, or correlation sufficient to identify the attack’s intent or target. But the abstract does not explain whether the team used network telemetry, malware reverse engineering, log analysis, industrial protocol monitoring, customer incident-response data, external intelligence feeds, human sources, or any other method.

The operational technology context is also important. The record’s primary topic classification points to OT and IoT security, while the raw text specifically says “nuclear reactor control systems” [record_id:2544]. Based on the raw text, the relevant approach is threat intelligence applied to industrial control systems with potential physical consequences. Researchers should avoid inferring detailed nuclear safety or reactor operations claims beyond what the abstract states.

## Notable Talks, Records, And Evidence

The DEF CON 33 talk “Veilid la revoluçion : Your data is yours to own” is notable because it connects Miller to Veilid, privacy advocacy, data ownership, and a broader technology-stack narrative [record_id:2043]. The talk appears to be both a status update and a call to action. Its abstract references a prior DEF CON 31 reveal, worldwide press coverage, and a desire to change public discourse on digital privacy [record_id:2043]. It also promises technical coverage of the Veilid Framework and applications released on it [record_id:2043]. This makes the record representative of Miller’s association with privacy-preserving infrastructure and community-oriented technical movements.

The BSidesLV 2025 talk “Stopping the Nuclear Apocalypse with Threat Intel (Token 11)” is notable because it is the only record in this set focused on operational technology, threat intelligence, and high-consequence cyber-physical systems [record_id:2544]. The abstract’s claim that Miller’s team uncovered an attack “specifically targeted at backdooring/incapacitating nuclear reactor control systems” makes it potentially significant for research into critical infrastructure threats [record_id:2544]. It is also a much more incident-specific record than the Veilid abstract. Where the Veilid talk appears to present a framework and movement, the BSidesLV talk appears to recount a particular investigation or defensive episode.

In evidentiary terms, both records are useful but limited. They are strong evidence for what talks were advertised to cover. They are weak evidence for the underlying factual details of the technologies or incidents because no full talk content, slides, code, indicators, or supporting documentation are included. The Veilid record supports claims about Miller’s co-authorship and association with privacy/data-ownership messaging [record_id:2043]. The BSidesLV record supports claims about Miller presenting a threat-intelligence story involving a nuclear reactor control-system attack [record_id:2544].

## Gaps, Limits, And Open Questions

The largest limitation is the size and form of the evidence base. There are only two records, and both are abstracts. The records do not include transcripts, slide decks, Q&A, whitepapers, source code, incident reports, or independent validation. As a result, the report can identify themes and likely areas of expertise, but it cannot reconstruct detailed arguments or technical methods.

For the Veilid talk, several important questions remain open. What exactly is the Veilid Framework’s architecture? What privacy guarantees does it claim? What adversaries does it defend against? How does it handle identity, routing, storage, metadata leakage, trust, abuse, moderation, or denial-of-service? What applications have been released on the framework, and how mature are they? The abstract says the talk covers fundamentals, progress, and released apps, but the record itself does not name those apps or describe the design [record_id:2043].

For the threat-intelligence talk, the gaps are even more consequential. The abstract does not identify the victim, attacker, campaign, malware, intrusion vector, evidence basis, or mitigation path [record_id:2544]. It does not explain how Miller’s team determined that the attack was specifically aimed at “backdooring/incapacitating nuclear reactor control systems” [record_id:2544]. It also does not clarify whether the attack targeted a real plant environment, a vendor, an engineering workstation, a customer network related to nuclear operations, or some other asset. Future research would need the full talk or corroborating materials before treating the incident as a detailed case study.

Another gap is continuity. The two records do not show whether Miller’s work consistently bridges privacy engineering and critical infrastructure defense, or whether these are separate episodes in a broader career. There is no record here that links Veilid to operational technology, or threat intelligence to privacy-preserving infrastructure. The thematic bridge around control of systems is interpretive and should be treated as a synthesis, not as an explicit claim made in the records.

Finally, because one record is co-authored, attribution should be handled carefully. “Veilid la revoluçion” is credited to Katelyn Bowden and Paul Miller, so specific claims about that talk should not be assigned solely to Miller without qualification [record_id:2043]. The BSidesLV talk is authored by Paul Miller alone in the provided metadata