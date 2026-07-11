# Topic: Author: Manish Gupta

## Executive Summary

The records attributed to Manish Gupta consist of four BSidesLV 2025 Training Ground entries for a single repeated or multi-session workshop titled **“Multi-Cloud (AWS, Azure & GCP) Security [25 Edition]”**, co-authored or co-presented with Yash Bharadwaj. The entries cover Day One morning and afternoon sessions and Day Two morning and afternoon sessions, all in the same venue track and all using the same workshop description [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

Collectively, the records portray Gupta’s contribution as centered on **hands-on enterprise cloud security training** across AWS, Microsoft Azure, and Google Cloud Platform. The workshop emphasizes both offensive and defensive security perspectives: red teamers and penetration testers are taught to understand advanced real-world cloud attacks and simulate adversary TTPs, while blue teamers and defenders are taught to identify and defend against emerging threats in multi-cloud infrastructure [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

A distinctive element across all records is the reference to **CyberWarFare Labs** and its **CWL RedCloud OS**, described as a “cloud adversary simulation VM.” The records frame the workshop as being delivered by the creators of that environment and as focused on practical lab-based offensive and defensive operations in enterprise cloud infrastructure [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

Because all four records share identical raw descriptive text, the evidence base is strong for identifying the workshop’s stated scope and positioning, but thin for differentiating individual sessions, specific modules, technical depth, demonstrations, vulnerabilities, tools beyond CWL RedCloud OS, or Manish Gupta’s individual role relative to co-author Yash Bharadwaj.

## Research Landscape

The available material is narrow but coherent. All four records come from **BSidesLV 2025** and are categorized as **Training Ground** sessions. They are not standalone research papers, blog posts, exploit writeups, or traditional conference talks; they are training workshop entries. The records are divided by schedule into:

- Day One AM, Monday 10:30–14:30 [record_id:2489]
- Day One PM, Monday 15:00–19:00 [record_id:2490]
- Day Two AM, Tuesday 10:30–14:30 [record_id:2491]
- Day Two PM, Tuesday 15:00–19:00 [record_id:2492]

The common title, shared description, and sequential scheduling indicate a structured multi-part training program rather than four substantively distinct talks. The raw text does not specify whether each session repeats the same content, advances through different modules, or represents separate registration blocks. However, the naming convention—“Day One, AM,” “Day One, PM,” “Day Two, AM,” and “Day Two, PM”—suggests an extended workshop format spread across two days [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

The dominant research area is **multi-cloud security**, specifically across AWS, Microsoft Azure, and GCP. The records place the workshop at the intersection of cloud infrastructure security, adversary simulation, red team tradecraft, blue team detection and defense, and enterprise-scale compromise scenarios. The raw text explicitly says the workshop aims to provide “practical insights” into offensive and defensive techniques used by red and blue teams in enterprise cloud infrastructure [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

The source material also positions the training as practitioner-oriented. Its intended audiences include:

- Red teamers
- Penetration testers
- Blue teamers
- Defenders

For red team and penetration testing audiences, the records emphasize understanding “advanced real-world cyber attacks” against AWS, Azure, and GCP and simulating TTPs used by APT groups in a practical lab environment [record_id:2489] [record_id:2490]. For blue team and defender audiences, the records emphasize identifying and defending against emerging threats, complex attack vectors, and sophisticated compromise scenarios in multi-cloud infrastructure [record_id:2491] [record_id:2492].

## Major Themes And Trends

### Multi-cloud security as an enterprise problem

The central theme is that modern enterprise cloud security cannot be treated as a single-platform discipline. The workshop explicitly covers **AWS, Microsoft Azure, and GCP**, and frames the problem as “Enterprise Cloud Infrastructure” rather than isolated cloud accounts or individual services [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. This reflects a broader trend in cloud security training: practitioners increasingly need to understand how adversary behavior and defensive controls differ across providers while still applying a unified operational model.

The records do not provide details about provider-specific content, such as IAM exploitation in AWS, Azure AD abuse, GCP service account compromise, cloud logging differences, or cross-cloud identity federation. However, the repeated inclusion of the three major cloud providers suggests the workshop is designed to address the operational reality of organizations using multiple cloud environments at once [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

### Offensive and defensive security treated as complementary

A recurring theme is the pairing of red team and blue team perspectives. The raw text describes “offensive / defensive techniques used by the Red & Blue Teams” and then separately explains what red teamers or penetration testers will learn and what blue teamers or defenders will learn [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

This dual framing is important. The workshop is not presented solely as an attack course, nor solely as a defensive monitoring course. Instead, it uses adversary simulation as a bridge between offensive understanding and defensive readiness. Red teamers are expected to simulate attacks and TTPs, while defenders are expected to recognize and mitigate those same or related techniques. This creates an implied training loop: understand adversary behavior, reproduce it in a lab, and develop defensive reasoning around it.

### Adversary simulation and APT-style TTPs

All four records mention the simulation of “Tactics, Techniques, and Procedures (TTPs) widely used by APT groups” in a practical lab environment [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. This indicates that the workshop is positioned around realistic adversary behavior rather than abstract cloud security concepts alone.

The reference to APT-group TTPs gives the training a threat-informed orientation. However, the records do not name specific APT groups, malware families, intrusion sets, cloud attack paths, MITRE ATT&CK techniques, or campaign examples. The evidence therefore supports the conclusion that adversary simulation is a stated theme, but not the specifics of how APT behavior is modeled.

### Practical lab-based learning

The raw text repeatedly emphasizes practical training. It says the workshop aims to provide “practical insights” and that participants will simulate TTPs “in a practical lab environment” [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. The reference to CWL RedCloud OS, described as a “cloud adversary simulation VM,” further reinforces a hands-on instructional model.

This suggests the records are less about theoretical cloud security architecture and more about operational skill-building. The intended learning outcomes are phrased as things trainees will “understand,” “simulate,” “identify,” and “defend against,” implying active exercises rather than passive lecture content [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

### Emerging threats and complex compromise scenarios

For defenders, the records emphasize “various emerging threats,” “complex attack vectors,” and “sophisticated compromise scenarios” in multi-cloud infrastructure [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. This suggests that the training is oriented toward advanced or evolving cloud threat models rather than basic cloud hygiene alone.

The evidence is not detailed enough to identify which emerging threats are covered. It could include identity compromise, privilege escalation, lateral movement across cloud services, exposed credentials, misconfiguration exploitation, cloud-native persistence, data exfiltration, or control-plane abuse, but these are not stated in the raw records. Downstream researchers should avoid inferring specific attack techniques unless corroborated by additional materials.

## Methods, Tools, And Approaches Discussed

The most concrete tool or platform mentioned across the records is **CWL RedCloud OS**, described as “a cloud adversary simulation VM” [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. The records state that trainees will learn from the creators of this tool how to perform enterprise offensive and defensive operations. This makes CWL RedCloud OS the central named technical artifact in the available evidence.

The methodological approach appears to include:

1. **Cloud adversary simulation**  
   The workshop uses adversary simulation to help participants reproduce attack behavior in a lab. The raw text specifically says trainees will “simulate Tactics, Techniques, and Procedures (TTPs)” used by APT groups [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

2. **Red team / penetration testing workflows**  
   For offensive practitioners, the training promises exposure to “advanced real-world cyber attacks” against AWS, Azure, and GCP [record_id:2489] [record_id:2490]. The records do not enumerate exploitation chains, but they clearly frame the red-team side as attack emulation across major cloud vendors.

3. **Blue team / defensive workflows**  
   For defenders, the course promises instruction on identifying and defending against emerging threats in multi-cloud infrastructure. It also emphasizes understanding compromise scenarios from a “defensive mindset” [record_id:2491] [record_id:2492].

4. **Enterprise cloud infrastructure context**  
   The records repeatedly situate the training in “Enterprise Cloud Infrastructure,” which implies scenarios involving organizational cloud estates rather than isolated personal lab accounts [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

5. **Multi-provider comparative or integrated training**  
   AWS, Microsoft Azure, and GCP are all named in the title and body text. The records do not explain whether the course treats them separately or through unified attack-defense patterns, but multi-cloud coverage is core to the presentation [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

The records do not provide enough information to describe specific lab steps, architectures, cloud services, detection rules, SIEM queries, exploit chains, or defensive controls. They also do not say whether CWL RedCloud OS includes prebuilt scenarios, automated attack modules, telemetry generation, cloud connectors, or reporting capabilities. The only safe conclusion is that CWL RedCloud OS is presented as a VM for cloud adversary simulation and is associated with the workshop’s practical lab environment [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

## Notable Talks, Records, And Evidence

The four records are best interpreted as parts of one workshop offering rather than separate intellectual contributions. Their importance lies in how they collectively define the scope and delivery model of Manish Gupta’s BSidesLV 2025 material.

The Day One AM entry establishes the workshop title and the core description: “Multi-Cloud Security” training by CyberWarFare Labs, covering offensive and defensive techniques for red and blue teams in enterprise cloud infrastructure [record_id:2489]. It identifies the three major cloud platforms—AWS, Microsoft Azure, and GCP—and introduces CWL RedCloud OS as the adversary simulation VM associated with the creators delivering the workshop [record_id:2489].

The Day One PM entry repeats the same workshop description and continues the Day One training block [record_id:2490]. Its metadata includes a secondary topic of exploit development and vulnerability discovery, but the raw text itself does not specifically discuss exploit development or vulnerability discovery. As evidence, the record is strongest for the same multi-cloud red/blue training themes as the other entries, not for detailed exploit-development content [record_id:2490].

The Day Two AM entry indicates that the workshop extends into a second day, again using the same description and emphasizing practical offensive and defensive operations, APT-style TTP simulation, and defender-oriented response to emerging threats [record_id:2491]. This reinforces the interpretation that the material is a substantial training program rather than a brief overview session.

The Day Two PM entry completes the two-day sequence and again repeats the same content description [record_id:2492]. Its presence suggests continuity and depth in the workshop schedule, but because the raw text is identical, it does not provide distinct evidence about what was covered in the final block.

Across all four records, the most representative evidence is the repeated claim that the workshop aims to provide practical insights into offensive and defensive techniques used by red and blue teams in enterprise cloud infrastructure [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492]. The second most representative evidence is the positioning of CWL RedCloud OS as a cloud adversary simulation VM used or discussed by its creators in the context of enterprise offensive and defensive operations [record_id:2489] [record_id:2490] [record_id:2491] [record_id:2492].

## Gaps, Limits