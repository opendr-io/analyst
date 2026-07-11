# Topic: Author: m0nkeydrag0n

## Executive Summary

The available records attributed to **m0nkeydrag0n / M0nkeyDrag0n** are a very small DEF CON 33-centered corpus consisting of two 2025 records. One is a substantive RF Village talk on **in-flight WiFi security, Evil Twin attacks, aviation connectivity infrastructure, and SOC/threat-hunting workflows** [record_id:1892]. The other is a brief, co-authored Q&A-style record about **Hard Hat Brigade creations**, described as covering “hard hats, construction, and all the hackery things people have done with them” [record_id:2135].

Collectively, the records position m0nkeydrag0n at the intersection of **RF/security-community experimentation**, **field-oriented infrastructure analysis**, and **defensive investigation**. The strongest evidence comes from the “Airborne WiFi” abstract, which lays out a clear scenario: passengers connecting to airline internet services, suspected Evil Twin access points on commercial aircraft, and a SOC analyst correlating logs and external telemetry such as ADS-B and satellite-related data to assess what happened [record_id:1892]. The Hard Hat Brigade record is much thinner, but it suggests participation in a maker/hacker community context involving modified construction hard hats and physical/RF-adjacent creativity [record_id:2135].

Because there are only two records, the evidence base is narrow. The corpus supports identifying recurring interests in **RF environments, unconventional or mobile infrastructure, hands-on hacker culture, and practical defensive analysis**, but it does not support a broad career profile, chronology, or detailed technical taxonomy of m0nkeydrag0n’s work.

## Research Landscape

The research landscape represented here is limited to **DEF CON 33 records from 2025**. Both records appear to be conference-session metadata or abstracts rather than full transcripts, papers, slides, or code repositories. That means the corpus captures presentation topics and intended takeaways, but not necessarily the full technical depth of the talks.

The dominant substantive source is the RF Village talk titled **“Airborne WiFi: Rogue Waves in the Sky”** [record_id:1892]. It is framed around commercial airline in-flight internet, the discovery of Evil Twins “in the wild on commercial airlines,” and the analytical burden placed on a SOC analyst trying to “unravel the truth” from infrastructure knowledge and telemetry [record_id:1892]. This record sits across several research areas: wireless network security, aviation connectivity, detection engineering, SOC workflows, and threat hunting.

The second source, **“Hard Hat Brigade Creations Q&A,”** is co-authored by MrBill, M0nkeyDrag0n, and CoD_Segfault [record_id:2135]. Its abstract is only one sentence: “HHB goes over hard hats, construction, and all the hackery things people have done with them” [record_id:2135]. It appears more community- or maker-oriented than the Airborne WiFi session. Its inclusion broadens the landscape from formal threat hunting into **physical objects, convention culture, hardware/RF-adjacent hacking, and creative modification**.

Overall, the records suggest that m0nkeydrag0n’s DEF CON 33 presence spanned both a focused security research talk and a collaborative community Q&A. The corpus is not dominated by academic-style research, exploit disclosure, malware analysis, or vulnerability writeups. Instead, it is dominated by **conference presentations about applied security contexts**: one operational/defensive and one creative/community-oriented.

## Major Themes And Trends

### 1. Security in unusual RF and connectivity environments

The clearest theme is interest in security problems outside traditional enterprise networks. In “Airborne WiFi,” the core environment is **commercial aircraft in-flight internet** [record_id:1892]. The talk asks whether travelers have used airline internet services and then asserts that “Evil Twins have been discovered in the wild on commercial airlines” [record_id:1892]. This moves WiFi threat modeling into a constrained, mobile, high-trust environment where users are likely rushing to connect and may accept captive portals or network prompts without scrutiny.

The aviation setting matters because the infrastructure is not simply a local access point in a café or hotel. The abstract refers to “on-wing infrastructure” and emphasizes that analysts must understand “the relationships of the pieces” and how those pieces relate to passengers as they journey through the skies [record_id:1892]. This suggests a layered environment: onboard passenger WiFi components, captive portal behavior, aircraft connectivity systems, and upstream communications paths potentially involving satellite or other telemetry.

The Hard Hat Brigade Q&A also hints at nonstandard security and hacker environments, though with much less detail. It centers on “hard hats, construction, and all the hackery things people have done with them” [record_id:2135]. While the raw text does not specify RF implants, sensors, badges, or other technical details, the record’s context implies a maker-style exploration of physical objects as hacking platforms or community artifacts.

### 2. Defensive investigation and SOC analyst perspective

The Airborne WiFi record is framed not only around an attack possibility but around the **analyst’s investigative workflow**. It presents “a tale of two people”: the passenger rushing to connect and the SOC analyst “charged with the task of unraveling the truth” [record_id:1892]. This dual framing is important: the talk appears to contrast the user experience of suspicious in-flight connectivity with the defender’s need to validate, correlate, and explain the event.

The abstract repeatedly emphasizes preparation and evidence handling. It says the analyst must tie together “logged events,” understand “what the infrastructure is on-wing,” and piece together a “bigger puzzle” using “other telemetry provided by ads-b, satellite or more” [record_id:1892]. The stated takeaways include what an analyst should do “to prepare themselves to hunt in this arena,” how to process evidence to support a hypothesis, and how to “unlock the truth” behind a browser portal that “didn’t feel right” [record_id:1892].

This gives the record a strong detection-engineering and threat-hunting orientation. The suspected Evil Twin is not treated merely as a wireless attack demonstration; it is treated as an incident requiring telemetry, infrastructure literacy, and hypothesis-driven analysis.

### 3. Evil Twin attacks and user trust in captive portals

A specific recurring concern in the substantive record is the **Evil Twin** problem: fraudulent wireless networks or access points that impersonate legitimate services. The record explicitly says “Evil Twins have been discovered in the wild on commercial airlines” and concludes by inviting the audience to a talk about “Evil Twins in the sky” [record_id:1892].

The talk appears especially interested in the passenger’s interaction with an airline WiFi portal. The abstract refers to “that pesky browser portal that didn’t feel right” [record_id:1892]. This suggests attention to the ambiguity of captive portals: users expect redirects, login pages, payment flows, airline branding, and unusual network behavior during in-flight WiFi onboarding. Those normal frictions can make malicious imitation harder for passengers to distinguish.

This theme connects human behavior with infrastructure. The passenger is “in a rush to connect to in-flight services,” creating a plausible social-engineering or usability weakness [record_id:1892]. Meanwhile, the defender needs to validate whether the odd portal was benign, misconfigured, or malicious.

### 4. Correlation of heterogeneous telemetry

Another major theme is correlation across different kinds of data. The Airborne WiFi talk mentions “logged events” and “other telemetry provided by ads-b, satellite or more” [record_id:1892]. That phrasing indicates that investigating in-flight wireless events may require combining conventional security logs with aviation-specific or communications-specific data sources.

ADS-B, in particular, is associated with aircraft position and movement broadcasting. The record does not explain exactly how ADS-B would be used in the investigation, but its inclusion implies that location, route, timing, aircraft identity, or flight context may help analysts reconstruct the incident environment [record_id:1892]. Satellite-related telemetry could potentially help relate onboard connectivity state to upstream links, though the abstract does not provide details.

This theme is important because it shows m0nkeydrag0n’s contribution, at least in this record, as not merely identifying a wireless risk but mapping how defenders might investigate it in a real operational environment.

### 5. Hacker-maker culture and physical artifacts

The Hard Hat Brigade record introduces a different but related theme: security-community creativity around physical artifacts. The record describes HHB as going over “hard hats, construction, and all the hackery things people have done with them” [record_id:2135]. The term “Creations Q&A” and the co-presenter list suggest a collaborative, informal, audience-facing session rather than a single-researcher technical talk.

Because the raw abstract is sparse, it should not be overinterpreted. However, within the two-record corpus it is the only evidence of m0nkeydrag0n’s participation in a **community creation / physical object hacking** context [record_id:2135]. This complements the RF Village talk by placing the author within DEF CON’s hands-on, artifact-oriented subculture as well as its technical research programming.

## Methods, Tools, And Approaches Discussed

The records do not provide code, step-by-step procedures, or tool names beyond telemetry categories. However, they do describe several approaches and workflows.

The most concrete method is **hypothesis-driven SOC investigation in an aviation WiFi context**. In the Airborne WiFi talk, the analyst is tasked with “unraveling a tip” and must process evidence “to support their hypothesis” [record_id:1892]. This implies an investigative workflow: receive a report or observation, understand the relevant infrastructure, identify available telemetry, correlate events, and decide whether the suspicious portal or network behavior reflects an Evil Twin or another cause.

A second approach is **infrastructure mapping**. The talk promises to introduce “the many components that comprise the on-wing infrastrucutre” and explain how they relate to passengers during flight [record_id:1892]. The method here is not just packet capture or WiFi scanning; it is learning the system architecture well enough to interpret logs and anomalies. For downstream researchers, this suggests looking for details about aircraft cabin WiFi architecture, onboard access points, network controllers, satellite or air-to-ground links, captive portals, and airline service providers.

A third approach is **multi-source telemetry correlation**. The abstract names “logged events” and “other telemetry provided by ads-b, satellite or more” as pieces of a larger puzzle [record_id:1892]. This indicates a defensive analysis style that combines internal security data with external or domain-specific signals. The record does not say whether these are open-source feeds, vendor logs, aircraft system records, or SOC-integrated telemetry, so that remains an open detail.

A fourth approach is **user-experience-informed threat analysis**. The passenger is described as rushing to connect, and the suspicious indicator is a browser portal that “didn’t feel right” [record_id:1892]. This suggests attention to how normal in-flight WiFi workflows may obscure malicious behavior. The method is partly behavioral: evaluate how user expectations, portal design, and connection urgency influence detection or reporting.

The Hard Hat Brigade Q&A likely discusses **creative modification or hacking of hard hats**, but the raw text does not specify tools, electronics, RF techniques, fabrication methods, or safety practices [record_id:2135]. The only defensible statement is that the session concerns “hard hats, construction,” and “hackery things people have done with them” [record_id:2135]. Downstream researchers should treat this as a pointer to possible physical/maker methods, not as evidence of any particular technical implementation.

## Notable Talks, Records, And Evidence

The most important record is **“RF Village - Airborne WiFi: Rogue Waves in the Sky”** [record_id:1892]. It is notable because it provides a clear topic, scenario, threat model, and analytical frame. The talk focuses on in-flight internet services and specifically claims that Evil Twin attacks have been found “in the wild on commercial airlines” [record_id:1892]. It also introduces two personas—the rushed passenger and the SOC analyst—which makes the talk both user-facing and defender-facing [record_id:1892].

Its strongest contribution is the framing of aircraft WiFi security as a **threat-hunting problem requiring aviation-aware context**. The analyst must understand on-wing infrastructure, tie logged events together, and use additional telemetry such as ADS-B and satellite-related data to build a larger evidentiary picture [record_id:1892]. The talk appears to be designed to help analysts prepare to hunt in this environment and process evidence to support or refute a hypothesis [record_id:1892]. For downstream research, this is the key record to consult for m0nkeydrag0n’s substantive security content.

The second notable record is **“Hard Hat Brigade Creations Q&A”** [record_id:2135]. It matters because it shows m0nkeydrag0n as one of several speakers in a Hard Hat Brigade context, alongside MrBill and CoD_Segfault [record_id:2135]. The record is much less detailed than the Airborne WiFi talk, but it points to a different mode of contribution: community discussion around physical creations and “hackery” involving hard hats [record_id:2135]. It may be relevant for questions about DEF CON culture, hacker fabrication, physical objects as community platforms, or the Hard Hat Brigade specifically.

In terms of evidence strength, [record_id:1892] is strong for identifying topic, setting, and intended analytical takeaways, but weak for implementation details because it is an abstract rather than a transcript. [record_id:2135] is weak for technical detail but useful for attribution and community-context coverage.

## Gaps, Limits, And Open Questions

The largest limitation is the size of the corpus: only two records are available. This prevents confident claims about long-term trends in m0nkeydrag0n’s work, evolution over time, preferred tools, recurring collaborators beyond the single Q&A,