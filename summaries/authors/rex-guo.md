# Topic: Author: Rex Guo

## Executive Summary

The two records attributed to Rex Guo both come from 2025 security conference talks and center on a consistent research concern: attackers do not always need exotic exploits or full security-tool bypasses to succeed; they can often exploit weaknesses in defender visibility, alert prioritization, logging, and investigation workflows. One talk, co-authored with Khang Nguyen, focuses on endpoint detection and response environments and argues that adversaries can “blend into the noise” by causing security activity to appear as medium- or low-severity alerts that SOC teams routinely deprioritize [record_id:59]. The other, co-authored with Shuyang Wang, focuses on Google Workspace and describes “silent” attacks that exploit logging gaps to escalate privileges, exfiltrate data, and evade detection, while also discussing investigation techniques when logs are insufficient [record_id:2312].

Collectively, the records position Rex Guo’s work around detection engineering, SOC operations, cloud and endpoint visibility, and practical adversary tradecraft. The strongest shared theme is that detection is not simply a matter of having tools or alerts. Both records emphasize that defenders must understand how adversaries manipulate operational assumptions: alert severity in EDR/SOC settings [record_id:59] and logging or monitoring gaps in SaaS/cloud identity environments [record_id:2312]. The evidence base is narrow—only two abstracts are available—but the records are thematically coherent and suggest a research profile focused on real-world bypasses of monitoring workflows and improving investigations through better custom detections, automation, and compensating techniques.

## Research Landscape

The available Rex Guo-attributed records consist of two conference presentation abstracts from 2025. One is a Black Hat USA briefing titled “Death by Noise: Abusing Alert Fatigue to Bypass the SOC (EDR Edition),” authored by Rex Guo and Khang Nguyen [record_id:59]. The other is a BSidesSF 2025 talk titled “THE SILENT BREACH: SECURITY THREATS IN GOOGLE WORKSPACE,” authored by Rex Guo and Shuyang Wang [record_id:2312].

Both records belong primarily to the detection engineering, SOC, SIEM, and threat hunting domain. However, they approach that domain through different technical surfaces. The Black Hat talk is framed around endpoint security and EDR products, specifically naming CrowdStrike, SentinelOne, and Microsoft Defender for Endpoint as environments in which the presenters target endpoints and cloud workloads [record_id:59]. The BSidesSF talk is framed around Google Workspace, with emphasis on cloud productivity infrastructure, identity-related privilege escalation, data exfiltration, and insufficient logs [record_id:2312].

The records are not full papers, slide decks, transcripts, or tool repositories. They are presentation descriptions. As a result, they provide high-level claims and thematic direction rather than detailed experimental evidence, code, detection logic, or step-by-step methodology. Still, the abstracts are specific enough to identify a coherent research landscape: practical adversary behavior against enterprise monitoring systems, especially where defenders rely on alert severity, default detections, cloud logs, or SaaS audit trails.

The overall research area reflected in these records is operational detection failure. Rex Guo’s talks, as represented here, are less about bypassing a single technical control in isolation and more about bypassing the human and procedural systems wrapped around those controls. In the EDR-focused talk, attackers succeed because the right alerts are generated but ignored or deprioritized [record_id:59]. In the Google Workspace talk, attackers succeed because monitoring and logging gaps prevent defenders from seeing or reconstructing critical actions [record_id:2312]. Together, these suggest a research agenda concerned with the gap between theoretical detection capability and practical SOC effectiveness.

## Major Themes And Trends

### Alert Fatigue As An Attack Surface

The most explicit theme appears in the Black Hat record: alert fatigue is treated not merely as a defender inconvenience but as an attacker-abusable condition. The abstract argues that many incidents do not happen because alerts are absent; they happen because “the right ones are ignored” [record_id:59]. This reframes SOC overload as a security weakness that adversaries can intentionally exploit.

The talk’s central claim is that attackers can achieve objectives while triggering only medium- and low-severity alerts, which the abstract says make up the majority of SOC alerts and are “often overlooked or not thoroughly investigated” [record_id:59]. The implication is that adversaries can avoid noisy high-severity indicators not by becoming invisible, but by becoming operationally ordinary. This is a practical and important shift: the bypass target is the SOC’s prioritization model rather than only the EDR sensor or detection engine.

The record further claims that attackers can adapt common tactics, techniques, and procedures across platforms to bypass SOC operations and that default critical or high-severity alerts can be “consistently downgraded to medium/low or suppressed” while attack effectiveness remains intact [record_id:59]. This suggests a trend toward adversary tradecraft that manipulates detection semantics—what severity an alert receives, whether it is suppressed, and whether it will be investigated—rather than only manipulating whether telemetry exists.

### Detection Gaps In SaaS And Cloud Productivity Platforms

The Google Workspace record extends the same operational-detection concern into SaaS and identity-heavy cloud environments. It states that Google Workspace enables productivity but that attackers exploit “logging gaps” to escalate privileges, exfiltrate data, and evade detection [record_id:2312]. Whereas the EDR talk focuses on alert severity and SOC prioritization, the Google Workspace talk focuses on insufficient monitoring and incomplete logs.

This record’s title, “THE SILENT BREACH,” reinforces the idea that successful attacks may be quiet not because no malicious action occurred, but because defenders lack adequate telemetry or investigation paths [record_id:2312]. The talk promises to reveal real-world attacks that bypass monitoring and to share techniques for investigating these threats “even without sufficient logs” [record_id:2312]. That framing indicates a concern with post-facto investigation under degraded visibility conditions, a common challenge in SaaS environments where audit data may be limited by product tier, retention settings, API coverage, event schema limitations, or administrative configuration.

### Practical Bypass Of Defender Workflows Rather Than Pure Exploit Research

Neither record is primarily about novel memory corruption, vulnerability exploitation, malware development, or cryptographic weakness. Instead, both are about abusing how enterprise defense is implemented and operated.

In the EDR record, the attackers do not need to disable EDR or rely on “highly complex techniques”; they can “blend into the noise” [record_id:59]. That line is central to the apparent research contribution. It suggests that many organizations may have invested in endpoint security tools but remain vulnerable because their SOC workflows cannot reliably distinguish important medium/low signals from benign or routine background activity.

In the Google Workspace record, attackers exploit monitoring gaps rather than necessarily exploiting a conventional software flaw [record_id:2312]. The focus is on privilege escalation, exfiltration, and evasion in the context of incomplete logging. This implies a practical understanding of enterprise SaaS attack paths and the investigative problems they create.

Across both records, the recurring pattern is: attackers use ordinary or plausible activity paths; defenders technically have some tooling or data; but monitoring, prioritization, or logging limitations allow the attack to proceed.

### Need For Better Custom Detection, Investigation, And Automation

The Black Hat record explicitly argues for rethinking how alerts are created, prioritized, and investigated [record_id:59]. It notes that even custom detections that might close critical gaps can be deprioritized because they add to the volume of low- and medium-severity alerts [record_id:59]. This is an important nuance: simply adding more detections can worsen the operational problem if the SOC cannot scale triage and investigation.

The same abstract states that the presenters will discuss custom detections for the demonstrated TTPs and that “automation is the key to scale the investigations” [record_id:59]. This points toward a defensive approach combining detection engineering with automated enrichment, correlation, triage, and response workflows. The emphasis is not merely on producing more alerts, but on making investigations scalable enough that lower-severity signals can still receive meaningful scrutiny.

The Google Workspace record similarly promises investigation techniques for threats “even without sufficient logs” [record_id:2312]. While it does not specify tools or methods, this suggests compensating investigative workflows: using alternate data sources, correlating partial evidence, reconstructing activity from administrative state, or looking for indirect indicators of abuse. The exact techniques are not described in the abstract, so downstream agents should treat this as a lead rather than a fully evidenced method.

### Endpoint And Cloud/SaaS Convergence

The two records cover different surfaces—EDR-protected endpoints/cloud workloads and Google Workspace—but both are enterprise security domains where identity, telemetry, and SOC processes intersect. The EDR talk explicitly mentions endpoints and cloud workloads protected by major endpoint platforms [record_id:59]. The Google Workspace talk addresses a SaaS productivity suite where attackers can escalate privileges and exfiltrate data [record_id:2312].

Together, the records suggest that Rex Guo’s work is not confined to one control plane. Instead, it spans endpoint telemetry, cloud workloads, SaaS logging, and SOC investigation. The common thread is adversary success through visibility and workflow gaps. This is useful for downstream research agents because questions about Guo’s work should not be routed only to endpoint security or only to cloud identity; the stronger organizing concept is detection failure across enterprise environments.

## Methods, Tools, And Approaches Discussed

The EDR-focused Black Hat record gives the clearest methodological detail. The talk claims to demonstrate how attackers can achieve goals while triggering only medium- and low-severity alerts [record_id:59]. It describes adapting common TTPs across platforms to bypass SOC operations, rather than depending on disabling EDRs or using highly complex techniques [record_id:59]. The named target environments include endpoints and cloud workloads protected by CrowdStrike, SentinelOne, and Microsoft Defender for Endpoint [record_id:59]. The claimed method is to cause default critical/high-severity alerts to be downgraded to medium/low severity or suppressed, while still preserving attack effectiveness [record_id:59].

From the defensive side, the same talk says it will discuss custom detections for these TTPs and emphasizes automation as necessary to scale investigations [record_id:59]. The implied defensive workflow is: identify attacker behaviors that are hidden among lower-severity alerts, create custom detection logic for those behaviors, and automate investigation sufficiently that low- and medium-severity alerts do not remain effectively invisible. The abstract does not provide detection rules, data schemas, automation playbooks, or implementation details, so the evidence supports the existence of these proposed approaches but not their exact design.

The Google Workspace talk discusses a different set of methods at a high level. It says attackers exploit logging gaps to escalate privileges, exfiltrate data, and evade detection [record_id:2312]. It also says the talk shares techniques to investigate these threats even when logs are insufficient [record_id:2312]. The abstract does not identify specific Google Workspace logs, APIs, privilege paths, OAuth flows, admin roles, or investigation artifacts. Nevertheless, the described approach is clear at a conceptual level: investigate cloud/SaaS attacks under conditions of incomplete telemetry by using methods beyond straightforward log review.

Across both records, the methods and approaches can be summarized as follows:

- Offensive simulation or demonstration of realistic enterprise attacks that do not depend on complete invisibility [record_id:59; record_id:2312].
- Abuse of defender assumptions, including alert severity thresholds and monitoring coverage [record_id:59; record_id:2312].
- Cross-platform adaptation of common TTPs in EDR/SOC environments [record_id:59].
- Investigation of SaaS/cloud threats despite insufficient logs [record_id:2312].
- Defensive emphasis on custom detections and automation to make investigation scalable [record_id:59].

The records do not provide enough detail to assess the novelty or reproducibility of the techniques. They do, however, indicate that the talks are practical and demonstration-oriented rather than purely theoretical.

## Notable Talks, Records, And Evidence

The most detailed and representative record is the Black Hat USA 2025 briefing “Death by Noise: Abusing Alert Fatigue to Bypass the SOC (EDR Edition),” by Rex Guo and Khang Nguyen [record_id:59]. It matters because it provides a concrete thesis: SOCs may fail not because alerts are absent, but because meaningful alerts are drowned among low- and medium-severity noise [record_id:59]. It also gives concrete product context by naming CrowdStrike, SentinelOne, and Microsoft Defender for Endpoint as the EDR platforms involved in the demonstrations [record_id:59]. This record is the strongest evidence for Guo’s interest in EDR bypasses, SOC alert prioritization, threat hunting, custom detections, and automation-assisted investigation.

The Black Hat record is also notable for its operational framing. It says attackers can “blend into the noise” instead of disabling EDRs or relying on highly complex techniques [record_id:59]. That makes the talk relevant to detection engineers and SOC leaders because it challenges common prioritization practices. The record’s claim that default critical/high-severity alerts can be downgraded to medium/low or suppressed while maintaining attack effectiveness is especially significant, though it remains an abstract-level claim without supporting experimental detail in the provided material [record_id:59].

The BSidesSF 2025 talk “THE SILENT BREACH: SECURITY THREATS IN GOOGLE WORKSPACE,” by Rex Guo and Shuyang Wang, is the second important record [record_id:2312]. It matters because it expands the research scope from endpoint/SOC alerting into SaaS/cloud productivity security. The talk claims that attackers exploit Google Workspace logging gaps to escalate privileges, exfiltrate data, and evade detection [record_id:2312]. It also promises investigative techniques for cases where logs are insufficient [record_id:2312]. This record is less detailed than the Black Hat abstract, but it is important because it shows Guo addressing cloud identity and workspace monitoring problems, not just endpoint alerts.

Together, the two records offer evidence of a coherent contribution: examining how enterprise attacks succeed in the gray areas of detection operations. The Black Hat talk emphasizes excessive noisy telemetry and severity downgrade/suppression