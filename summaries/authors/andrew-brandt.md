# Topic: Author: Andrew Brandt

## Executive Summary

The two records attributed to Andrew Brandt describe what appears to be the same 2025 research presentation delivered or listed in two major security venues: Black Hat USA 2025 and DEF CON 33. Both records focus on a “China-based adversary” conducting a more-than-five-year campaign against enterprise firewall and perimeter network defenses, using custom exploits and bespoke malware to compromise firewalls in customer environments [record_id:56] [record_id:1998].

The central contribution of these records is not a broad survey of Andrew Brandt’s work, but a focused account of one major research topic: long-running exploitation of firewall vendors and their customers by a well-resourced state-aligned or state-associated adversary. The records emphasize exploit development against specific firewalls, post-compromise malware deployed inside firewall operating systems, the operational cycle of repeated targeting, and the need for collective defense among network security vendors [record_id:56] [record_id:1998].

Across the records, Brandt’s recurring message is that perimeter security devices are not merely defensive infrastructure; they are themselves high-value attack surfaces. The talks frame the campaign as industry-wide rather than isolated to a single firewall vendor, warning that “most of the large network security providers” have been targeted repeatedly using overlapping tactics and tools [record_id:56] [record_id:1998]. The evidence base in the records is strong for identifying the presentation’s stated scope and themes, but thin for technical specifics because the supplied raw text is an abstract-level description rather than a transcript, paper, or slide deck.

## Research Landscape

The topic corpus contains two records, both from 2025 security conferences and both attributed to Andrew Brandt. One is a Black Hat USA briefing titled “Firewalls Under Fire: China’s 5+ Year Campaign to Penetrate Perimeter Network Defenses” [record_id:56]. The other is a DEF CON 33 video entry titled “China’s 5+ year campaign to penetrate perimeter network defenses” [record_id:1998]. The texts are highly similar, suggesting that the DEF CON appearance is either the same talk, a closely related version of the same talk, or a derivative presentation with nearly identical abstract language.

The records sit at the intersection of network security, threat hunting and incident response, exploit development, vulnerability discovery, malware analysis, and reverse engineering. Although the metadata places both under network security and NDR as the primary topic, the raw text makes clear that the research is also heavily concerned with offensive exploitation of perimeter devices and malware deployed into firewall operating systems [record_id:56] [record_id:1998].

The overall research area is the compromise of enterprise firewalls and perimeter network defense products by a persistent China-based adversary. The records describe a multi-year, cyclical struggle between firewall vendors and the adversary, with attackers investing resources in custom exploit development and malware tailored to firewall platforms [record_id:56]. The campaign is framed not as a single intrusion set against one product, but as a broader pattern affecting “most of the large network security providers in the industry” through repeated targeting and reuse of tactics and tools [record_id:56] [record_id:1998].

Because there are only two records and both cover the same topic, the landscape is narrow but coherent. There is no evidence here of unrelated Andrew Brandt posts, publications, or talks. The corpus should therefore be treated as a small but thematically concentrated set of records about one major presentation topic rather than a comprehensive bibliography of Brandt’s research output.

## Major Themes And Trends

### Firewalls as high-value offensive targets

The strongest theme is that enterprise firewalls, traditionally considered core defensive infrastructure, have become direct targets for advanced adversaries. The raw text states that firewall vendors have faced a “persistent, cyclical struggle” against a China-based adversary seeking to compromise “enterprise firewalls in customer environments” [record_id:56]. The DEF CON record repeats this framing, describing attackers who develop “custom exploits and bespoke malware” for the purpose of compromising enterprise firewalls [record_id:1998].

This theme matters because it reframes perimeter devices as both controls and liabilities. Firewalls are strategically positioned in enterprise networks, often trusted, externally reachable, and deeply integrated into traffic flows. Although the records do not spell out every consequence, the emphasis on malware deployed inside firewall operating systems implies that compromising these devices can provide attackers with privileged network footholds, stealthy persistence, and visibility into protected environments [record_id:56] [record_id:1998].

### Long-running, cyclical adversary operations

Both records emphasize duration and recurrence. The campaign is described as extending for “more than five years” and as a continuing struggle rather than a single burst of exploitation [record_id:56] [record_id:1998]. The Black Hat abstract uses the phrase “persistent, cyclical struggle,” suggesting repeated waves of attack, vendor response, countermeasure development, and renewed adversary activity [record_id:56].

The trend implied by the records is that perimeter-device exploitation is not episodic. Instead, the adversary is portrayed as making sustained investments in exploit development and malware engineering over multiple years. That long horizon also suggests that defensive efforts by individual vendors may temporarily derail operations but not end the campaign altogether [record_id:56].

### Custom exploits and bespoke malware

A second major theme is adversary engineering capability. The records do not merely claim opportunistic exploitation of known vulnerabilities. They describe a “well-resourced and relentless China-based adversary” that has invested in “custom exploits and bespoke malware” specifically designed for compromising enterprise firewalls [record_id:56]. The DEF CON record similarly highlights “custom exploits and bespoke malware” and says the talk includes details on “the exploits targeting specific firewalls” and malware deployed inside those firewalls [record_id:1998].

This points to an operational model in which attackers understand firewall internals well enough to develop platform-specific exploitation paths and post-exploitation implants. The records imply that malware analysis and reverse engineering are necessary parts of the defensive response, since the malware exists inside firewall operating systems rather than on ordinary endpoints [record_id:56] [record_id:1998].

### Industry-wide targeting rather than a single-vendor incident

Both records stress that the adversary has not focused on only one firewall vendor. The Black Hat abstract says “most of the large network security providers in the industry have been targeted multiple times, using many of the same tactics and tools” [record_id:56]. The DEF CON abstract repeats the same point, stating that “most of the large network security providers” have been targeted repeatedly [record_id:1998].

This is one of the most important claims in the corpus. It shifts the presentation from a vendor-specific incident report to an industry-wide warning. If multiple vendors face similar tactics and tooling, then isolated response practices are likely insufficient. The records advocate a collective understanding of shared adversary methods and shared defensive requirements [record_id:56] [record_id:1998].

### Collective defense and cross-vendor collaboration

The talks’ concluding message is explicitly collaborative. The Black Hat record says the presentation is “an urgent call” for companies in the security industry to “collectively combat this ongoing problem,” adding that “we all face the same threat” and “cannot hope to withstand the tempo and volume of these attacks alone” [record_id:56]. The DEF CON record preserves essentially the same wording and ends with “We must work together” [record_id:1998].

This gives Brandt’s presentation a strategic policy and coordination dimension in addition to its technical content. The records suggest that individual countermeasures by one firewall vendor may help, but broader industry coordination is necessary because the adversary reuses tactics and tools across providers [record_id:56] [record_id:1998].

## Methods, Tools, And Approaches Discussed

The records are abstract-level descriptions, so they do not enumerate specific CVEs, malware families, detection rules, reverse-engineering tools, or incident response playbooks. However, they do identify several categories of methods and approaches.

First, the adversary’s methods include custom exploit development targeting specific firewall products. The Black Hat record says the presentation will provide “rich detail into the exploit development targeting specific firewalls” and how those exploits were deployed and used to compromise customers [record_id:56]. The DEF CON record similarly says the talk includes “detail into the exploits targeting specific firewalls” [record_id:1998]. This suggests research coverage of vulnerability discovery, exploit construction, deployment infrastructure, and operational use of exploits against perimeter appliances.

Second, the adversary’s post-exploitation approach involves malware deployed inside firewall operating systems. The Black Hat description refers to “characteristics of the malware deployed inside the firewall’s operating system” [record_id:56]. The DEF CON entry describes “malware deployed inside the firewalls as a result of these attacks” [record_id:1998]. This implies a need for specialized forensic and reverse-engineering workflows adapted to embedded or appliance-like network security platforms, rather than standard workstation or server malware analysis.

Third, the defensive approach includes countermeasures developed by at least one firewall vendor. The Black Hat record says Brandt will describe “the countermeasures one firewall vendor developed to derail the threat actors” [record_id:56]. The DEF CON record also mentions “the countermeasures one firewall vendor developed to derail the threat actors” [record_id:1998]. The raw text does not specify what these countermeasures are, but the phrasing suggests a case study in detection, mitigation, hardening, disruption, or incident response by a vendor targeted during the campaign.

Fourth, the presentation appears to use historical reconstruction as a method. Both records say Brandt will walk attendees through “the complete history of the campaign” and detail “the full scope of attacks” [record_id:56] [record_id:1998]. This indicates a longitudinal analysis rather than a point-in-time technical disclosure. The value of such an approach is that it can connect individual exploit chains, malware samples, and vendor incidents into a broader adversary campaign.

Finally, the records advocate industry collaboration as a defensive architecture. The call for vendors to “work together” is not a tool in the narrow technical sense, but it is a strategic approach to security response [record_id:56] [record_id:1998]. The records imply that shared intelligence about tactics, tools, exploited product classes, and appliance malware could improve resilience across vendors facing the same adversary.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 record is the more detailed of the two and provides the clearest articulation of the talk’s framing. Its title, “Firewalls Under Fire: China’s 5+ Year Campaign to Penetrate Perimeter Network Defenses,” explicitly emphasizes firewalls as embattled security infrastructure [record_id:56]. The abstract presents the talk as “first-of-its-kind” and promises a complete campaign history, the scope of attacks, countermeasures by one firewall vendor, exploit development details, deployment and compromise pathways, and malware characteristics inside firewall operating systems [record_id:56]. For downstream researchers, this record is the best evidence for the intended depth and scope of Brandt’s presentation.

The DEF CON 33 record appears to represent the same research in a public conference-video context. Its title, “China’s 5+ year campaign to penetrate perimeter network defenses,” is nearly identical in substance, and the raw text repeats the core claims about a long-running China-based campaign, custom exploits, bespoke malware, vendor countermeasures, repeated targeting of large network security providers, and a call for collective action [record_id:1998]. The DEF CON record includes a video URL and a tag indicating “35:12,” likely a runtime or duration marker, but the raw description itself remains abstract-level rather than transcript-level [record_id:1998].

Together, the two records reinforce the same narrative: Brandt’s 2025 conference work centers on a multi-year adversary campaign against firewall vendors and enterprise perimeter defenses. The evidence is strongest where the two records repeat the same claims: duration of the campaign, China-based attribution, use of custom exploits and bespoke malware, targeting of multiple firewall vendors, and the need for collective industry response [record_id:56] [record_id:1998].

The evidence is weaker for operational specifics. The abstracts promise details about exploit development, malware characteristics, and countermeasures, but the supplied records do not provide those details directly. Researchers seeking technical indicators, vulnerability identifiers, malware names, timelines, affected vendors, or detection strategies would need the full talk video, slides, transcript, or related publication, not just these records.

## Gaps, Limits, And Open Questions

The main limitation is corpus size. Only two records are included, and both appear to describe the same presentation topic. This means the topic summary cannot infer a broad evolution of Andrew Brandt’s research career, writing style, publication history, or recurring interests beyond this 2025 firewall-campaign presentation.

The second limitation is lack of technical detail in the raw records. The abstracts say the talk covers exploit development, malware deployed inside firewall operating systems, and countermeasures by one vendor, but they do not identify the firewall vendor, affected products, vulnerabilities, exploit chains, malware families, indicators of compromise, persistence mechanisms, command-and-control methods, forensic artifacts, or detection logic [record_id:56] [record_id:1998].

The third limitation is attribution specificity. The records describe the adversary as “China-based,” “well-resourced,” and “relentless,” but do not provide a named threat group, attribution methodology, confidence level, or evidence basis [record_id:56] [record_id:1998]. Downstream researchers should avoid overclaiming beyond the wording in the records unless they consult the full presentation or corroborating sources.

The fourth limitation is uncertainty about the relationship between the two talks. The Black Hat and DEF CON records have highly similar abstracts, both in 2025, and both attributed to Brandt, but the records alone do not state whether the DEF CON talk is identical to the Black Hat briefing, a modified version, a public reprise, or an independent delivery of the same research [record_id:56] [record_id:1998].

Open questions for future research include:

-