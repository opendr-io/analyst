# Topic: Author: Adam Crosser

## Executive Summary

The two records attributed to Adam Crosser describe the same 2025 research theme and likely the same talk presented in two venues: Black Hat USA 2025 and DEF CON 33. Both records focus on “Ghost Calls,” a technique for abusing web conferencing infrastructure as a short-term, high-bandwidth command-and-control channel. The central idea is that traditional covert C2 channels may be stealthy and persistent but often lack the responsiveness needed for interactive operations such as SOCKS proxying, pivoting, relaying attacks, or hidden VNC. Crosser’s work proposes using real-time collaboration and conferencing protocols—especially trusted media relay infrastructure such as TURN servers—to temporarily route interactive traffic in a way that resembles ordinary enterprise meeting activity [record_id:33] [record_id:1913].

The records identify an open-source tool called TURNt as the practical implementation of this approach. TURNt is described as enabling covert traffic routing through media servers hosted by web conferencing providers, taking advantage of the fact that enterprises often whitelist conferencing IP ranges and may exempt them from TLS inspection [record_id:33]. The DEF CON record specifically frames these as commonly trusted TURN servers from services like Zoom and says the resulting sessions can look like legitimate Zoom meeting traffic [record_id:1913].

Across both records, the contribution is dual-use: it is presented as a red-team operational capability and as an emerging defensive concern. The talks promise to explain how operators can integrate “ghost calls” into existing workflows while also covering detection risks, trade-offs, and countermeasures for defenders [record_id:33] [record_id:1913]. The evidence base is narrow but consistent: both records provide abstracts for talks rather than detailed technical papers, code, measurements, or independent validation.

## Research Landscape

The record set contains two conference-style descriptions from major security venues in 2025. One is a Black Hat USA briefing titled “Ghost Calls: Abusing Web Conferencing for Covert Command & Control” [record_id:33]. The other is a DEF CON 33 talk titled “Ghost Calls - Abusing Web Conferencing for Covert Command & Control,” associated with a YouTube video and a listed runtime of 42:04 [record_id:1913]. Both are attributed to Adam Crosser and both use nearly identical framing, indicating that the records cover one research project disseminated across multiple venues rather than a broad portfolio of unrelated work.

The dominant research area is network security, with strong overlap into red-team tradecraft, command-and-control design, network detection and response, SOC visibility, SIEM/threat hunting, and collaboration-platform abuse. The records are not about generic malware persistence or endpoint compromise. Instead, they concentrate on network transport: how an operator can move interactive traffic through infrastructure that enterprises already trust, and how defenders might distinguish this activity from normal conferencing behavior.

The landscape represented here is therefore specialized and tactical. It sits at the intersection of three trends:

1. Enterprise dependence on real-time collaboration suites.
2. Defensive monitoring focused on known C2 infrastructure and suspicious outbound channels.
3. Offensive interest in short-lived, high-bandwidth interactive tunnels that can blend into legitimate traffic.

The Black Hat abstract is somewhat more detailed in describing the operational problem and emphasizing globally distributed media servers as “natural traffic relays” [record_id:33]. The DEF CON abstract is shorter and more direct, naming “services like Zoom” and emphasizing trusted TURN servers as the mechanism [record_id:1913]. Together, they suggest that Crosser’s contribution is not merely the observation that conferencing traffic is trusted, but the construction of a repeatable tool-supported workflow for exploiting that trust boundary.

## Major Themes And Trends

### Web Conferencing As Trusted Network Infrastructure

The most important theme is the abuse of ordinary collaboration infrastructure as an implicit trust channel. Both records argue that web conferencing platforms are designed for low-latency, real-time media exchange and therefore provide properties attractive to interactive C2. The Black Hat record states that web conferencing protocols operate through “globally distributed media servers” that act as natural traffic relays [record_id:33]. The DEF CON record similarly describes using “whitelisted media servers from services like Zoom” to create short-term high-speed C2 channels [record_id:1913].

This reflects a broader security concern: infrastructure that is essential to business operations can become difficult to inspect or block. The Black Hat abstract notes that vendors may recommend whitelisting conferencing provider IP addresses and exempting them from TLS inspection, which can “significantly” reduce detection likelihood [record_id:33]. The DEF CON abstract repeats this point in condensed form, saying many enterprises whitelist conferencing IPs and exempt them from TLS inspection, allowing sessions to resemble legitimate Zoom meetings [record_id:1913].

### Short-Term Interactive C2 Versus Long-Term Covert C2

A recurring distinction is made between persistent, low-profile channels and temporary, high-bandwidth channels. Crosser’s framing is that red teams often already have stealthy long-term C2, but those channels are poorly suited for interactive activity. The Black Hat record lists SOCKS proxying, layer-two pivoting, relaying attacks, and hidden VNC sessions as examples of operations requiring responsiveness or bandwidth beyond what traditional covert C2 can comfortably provide [record_id:33]. The DEF CON record echoes this with SOCKS proxying, pivoting, and hidden VNC [record_id:1913].

The proposed model is complementary rather than substitutive: maintain a persistent covert channel, then activate a real-time conferencing-based channel for short operational windows. The Black Hat abstract explicitly describes activating high-bandwidth sessions for “short, one-to-two-hour periods,” mimicking legitimate conferencing activity [record_id:33]. The DEF CON description similarly emphasizes periodically activating higher-bandwidth interactivity for time-sensitive operations [record_id:1913].

This is an important conceptual contribution. The research is not simply about hiding all C2 in conferencing traffic indefinitely. Instead, it proposes a hybrid C2 architecture: low-and-slow channels for persistence and coordination, plus brief “ghost call” channels for interactive tasks.

### Blending Into Normal Enterprise Traffic

Both records emphasize traffic blending. The Black Hat record says the approach allows operators to “blend interactive C2 sessions into normal enterprise traffic patterns,” appearing like a temporarily joined online meeting [record_id:33]. The DEF CON record says TURNt sessions look like a legitimate Zoom meeting [record_id:1913].

The records do not provide raw detection data or packet-level evidence, but the claim is plausible within the abstracts’ own logic: conferencing traffic is common in enterprises, tends to be latency-sensitive, often traverses vendor-operated relays, and may be subject to exceptions in proxying or inspection policies. The talks appear intended to make defenders aware that collaboration traffic should not be treated as inherently benign merely because it terminates at trusted provider infrastructure.

### Dual-Use Framing: Red-Team Capability And Defensive Countermeasure

The work is explicitly dual-use. On the offensive side, attendees are told they will learn how to integrate short-term interactive C2 into red-team operations [record_id:33] [record_id:1913]. On the defensive side, both records promise discussion of detection, mitigation, and countermeasures. The Black Hat record says the presentation will “discuss the trade-offs and detection risks” and “explore countermeasures defenders can implement” [record_id:33]. The DEF CON record similarly says the talk will cover “trade-offs and detection challenges” and defensive countermeasures [record_id:1913].

This balance matters for interpreting the records. The research is not presented solely as an attack demonstration, nor solely as a defensive warning. It is positioned as operational red-team research whose value includes helping blue teams identify a new class of suspicious behavior within collaboration traffic.

### Enterprise Exposure Across Industries

The Black Hat record makes a broad exposure claim: “Any enterprise reliant on collaboration suites could be exposed to these vectors” [record_id:33]. This suggests the issue is not limited to a single sector or a rare configuration. The DEF CON record narrows the example by referencing services like Zoom, but the larger pattern remains collaboration-platform reliance [record_id:1913].

The evidence for this exposure claim is abstract-level rather than empirical. The records do not include statistics on how many organizations whitelist conferencing media servers, exempt them from TLS inspection, or log TURN behavior in a way useful for detection. Nevertheless, the theme is clear: common collaboration platforms may create blind spots when their network paths are treated as special or trusted.

## Methods, Tools, And Approaches Discussed

The key tool discussed is TURNt, described as an open-source tool for covert traffic routing through web conferencing media infrastructure [record_id:33]. In the Black Hat record, TURNt is said to route traffic through media servers hosted by web conferencing providers, leveraging vendor-recommended whitelisting and TLS inspection exemptions [record_id:33]. In the DEF CON record, TURNt is described as automating covert traffic routing through commonly trusted TURN servers, with services like Zoom given as an example [record_id:1913].

The method can be summarized as follows, based strictly on the records:

- An operator maintains a stealthy, persistent C2 channel through traditional means.
- When a high-bandwidth interactive task is needed, the operator activates a short-lived real-time communication channel.
- That channel uses conferencing-related protocols and media relay infrastructure, especially TURN servers or media servers.
- The resulting traffic is intended to blend into normal conferencing behavior, resembling a legitimate online meeting or Zoom session.
- The channel is used only temporarily, such as during one-to-two-hour windows, to reduce anomaly and match plausible business activity [record_id:33].
- The workflow supports interactive operations such as SOCKS proxying, pivoting, relay attacks, layer-two pivoting, or hidden VNC sessions [record_id:33] [record_id:1913].

The records point to several defensive approaches but do not fully specify them. They mention identifying and mitigating the technique, exploring countermeasures, and discussing detection challenges [record_id:33] [record_id:1913]. The abstracts imply that defenders may need to scrutinize conferencing traffic patterns, exceptions to TLS inspection, and trusted media server access. However, the records do not enumerate concrete detections, signatures, telemetry sources, or mitigations in detail.

A notable architectural idea is the separation of persistent and interactive C2 roles. Rather than forcing a covert channel to handle all operator needs, Crosser’s approach uses the persistent channel for stealth and continuity while using conferencing infrastructure for short bursts of responsive, high-throughput activity [record_id:33] [record_id:1913]. This architecture is arguably the main technical framing across the records.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 record is the richer of the two abstracts. It lays out the operational motivation in more detail, explaining that traditional C2 mechanisms can be slow, conspicuous, and detectable when used for bandwidth-intensive interactive tasks in monitored networks [record_id:33]. It also gives the clearest list of use cases: SOCKS proxying, layer-two pivoting, relaying attacks, and hidden VNC sessions [record_id:33]. The Black Hat record is also the strongest source for the claim that media servers are globally distributed natural traffic relays and that vendors may recommend whitelisting or TLS-inspection exemptions [record_id:33].

The DEF CON 33 record is important because it confirms the same research was presented in another major venue and provides a concise version of the same claims. It explicitly mentions trusted TURN servers and services like Zoom, which makes the conferencing mechanism more concrete [record_id:1913]. It also indicates the talk had a recorded video with a 42:04 runtime, suggesting that downstream researchers may be able to extract more detailed technical content from the associated presentation if they consult the source video [record_id:1913].

Together, the two records are mutually reinforcing. They use nearly the same title, describe the same problem, name the same tool, and frame the same red-team/blue-team learning outcomes. The evidence is therefore strong that Adam Crosser’s records in this corpus center on the “Ghost Calls” research project and the TURNt tool. The evidence is weaker for assessing implementation quality, real-world effectiveness, detection feasibility, or adoption, because neither record includes detailed results, code excerpts, packet captures, diagrams, case studies, or post-talk discussion.

## Gaps, Limits, And Open Questions

The largest limitation is that the record set is very small and consists of two abstracts for what appears to be the same talk. It does not show a broad range of Adam Crosser’s work across multiple topics or years. Based on these records alone, downstream researchers should avoid overgeneralizing about Crosser’s entire research profile. The available evidence supports a focused claim: these records attribute to Crosser a 2025 project on abusing web conferencing infrastructure for covert interactive C2 [record_id:33] [record_id:1913].

Several open questions remain:

- **Implementation details of TURNt:** The records name TURNt and describe its purpose, but they do not explain its internals, supported platforms, deployment requirements, authentication model, traffic encapsulation details, or operational limitations [record_id:33] [record_id:1913].
- **Provider specificity:** Zoom is explicitly mentioned in the DEF CON abstract, while the Black Hat abstract speaks more generally about web conferencing providers and collaboration suites [record_id:33] [record_id:1913]. The records do not clarify which providers or protocols are supported beyond that example.
- **Detection engineering specifics:** Both records promise discussion of detection risks, challenges, and countermeasures, but neither abstract provides concrete detection logic, SIEM queries, network indicators, behavioral analytics, or recommended telemetry sources [record_id:33] [record_id:1913].
- **Empirical validation:** The records do not include measurements of bandwidth, latency, detection rates, false positives, operational success, or testing across enterprise environments.
- **Legal and policy constraints:** The records focus on red-team operations and defensive mitigation, but they do not address provider terms of service, consent boundaries, or organizational policy implications in detail.
- **Defender trade-offs:** The abstracts imply that whitelisting and TLS-inspection exemptions create risk, but they do not resolve the operational tension between inspecting collaboration traffic