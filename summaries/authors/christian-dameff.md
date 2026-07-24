# Topic: Author: Christian Dameff

## Executive Summary

The three records attributed to Christian Dameff show a research and public-speaking profile centered on security’s real-world effects on human behavior, healthcare operations, and crisis resilience. Although the dataset is small, it spans two adjacent domains: first, empirical critique of phishing training and security-awareness metrics; second, cybersecurity risks to hospitals, trauma centers, urgent care, and continuity of care during infrastructure crises.

The strongest evidence comes from two fuller abstracts. One 2025 Black Hat briefing, coauthored with Ariana Mirian, describes an 8-month real-world phishing-training study across more than 20,000 employees and argues that conventional phishing training may fail to meaningfully improve behavior, while click-rate metrics can mislead defenders because lure design itself strongly affects outcomes [record_id:91]. A 2025 BSidesLV panel with Beau Woods and Dina Carlisle frames healthcare cybersecurity as a patient-safety, public-health, and national-security issue, emphasizing ransomware, phishing, supply-chain disruption, legacy medical devices, unsegmented networks, third-party dependencies, and resilience measures such as zero trust, incident response planning, workforce training, policy, and cross-sector collaboration [record_id:2434].

The third record is much thinner: a 2026 BSidesLV entry with Jeff Tully titled “No Water: No Hospitals : Continuity of Care under Crisis,” whose raw text contains only the title [record_id:2846]. Even so, it reinforces the broader pattern: Dameff’s work, at least in these records, repeatedly connects cybersecurity and crisis management to direct operational consequences in healthcare and safety-critical environments.

Overall, the records suggest Christian Dameff’s recurring contribution is not merely technical vulnerability analysis, but security research framed around operational reality: how organizations measure human security behavior, how hospitals continue care under cyber or infrastructure disruption, and how policy, technology, and preparedness intersect when failures can affect lives.

## Research Landscape

The dataset contains three attributed records from conference-style sources: one Black Hat briefing and two BSidesLV entries. All are recent, covering 2025 and 2026. They are not blog posts, papers, or code repositories; they are talk or panel abstracts. This means the evidence is mostly descriptive: the records tell us what the talks intended to cover, but not the full empirical results, methodology details, slides, transcripts, audience Q&A, or subsequent publications.

The Black Hat record is the most research-study oriented. “Pwning User Phishing Training Through Scientific Lure Crafting” is explicitly framed around an “8-month, real-world study across 20,000+ employees” and claims the study was embedded “in the wild” rather than run as a controlled lab test [record_id:91]. It is attributed to Christian Dameff and Ariana Mirian. The talk’s focus is human factors, phishing training, security metrics, and the possibility that internal phishing programs can create misleading or manipulable results.

The BSidesLV 2025 record is a panel rather than a narrowly scoped research presentation. “Emergency & Urgent Care Remains in Critical Condition,” attributed to Beau Woods, Christian Dameff, and Dina Carlisle, discusses cybersecurity threats to hospitals and trauma centers, especially where outages can disrupt emergency care [record_id:2434]. It takes a broad, policy-and-operations view, covering ransomware, phishing, supply-chain risks, medical devices, network segmentation, third-party dependencies, federal funding, regulatory frameworks, zero-trust architectures, incident response planning, workforce training, and cross-sector collaboration [record_id:2434].

The BSidesLV 2026 record is minimal but points toward continuity-of-care concerns during crisis. “No Water: No Hospitals : Continuity of Care under Crisis,” attributed to Christian Dameff and Jeff Tully, contains no abstract beyond the title itself [record_id:2846]. The title indicates a focus on hospitals’ dependence on water infrastructure and the implications for care continuity when that dependency fails, but the record does not provide enough detail to infer specific methods, claims, or recommendations beyond that general framing.

Across the records, the research landscape is therefore concentrated in applied security and resilience rather than exploit development or malware reverse engineering. The recurring setting is organizational security under real constraints: employees confronting phishing simulations, hospitals facing cyber disruptions, emergency care systems dependent on technology and infrastructure, and policy or operational mechanisms intended to reduce harm.

## Major Themes And Trends

### 1. Skepticism toward simplistic security metrics

The clearest theme in the dataset is skepticism toward simple metrics used as proxies for real security improvement. The Black Hat phishing-training talk directly challenges the idea that awareness training and fake-email exercises are a “silver bullet” [record_id:91]. It argues that current phishing training “doesn't move the needle” and that phishing-training metrics can be a “dangerous mirage” when used as security theater or as a flawed defense strategy [record_id:91].

The record’s most important conceptual point is that click rates may reflect the qualities of the lure more than the qualities of the user. The abstract says lures “behave chaotically” and that some bait, such as “urgent dress code updates,” consistently outperformed others in ways that did not align with conventional wisdom [record_id:91]. This suggests a broader critique of organizational security dashboards: numbers that appear to measure user susceptibility may instead measure novelty, context, copywriting, or incentive structures inside the phishing program.

This theme is significant because it reframes human-factors security from a compliance exercise into a measurement-science problem. Rather than asking only “Did users click?”, the talk appears to ask what the click rate actually measures and whether internal phishing metrics can be manipulated “for good—or evil” [record_id:91].

### 2. Human behavior as an operational security variable

Human behavior appears in both the phishing-training record and the healthcare-security panel. In the Black Hat talk, employees are the subject of a large real-world study, but the abstract resists the simplistic interpretation that employees are simply careless or in need of more training [record_id:91]. It instead highlights the interaction between lure design, novelty, context, gamified lure creation, and organizational measurement practices [record_id:91].

In the healthcare panel, “workforce training” is listed as one operational mitigation among many, alongside zero-trust architectures and incident response planning [record_id:2434]. This places training in a broader socio-technical system rather than treating it as a standalone fix. Taken together, the records suggest a recurring concern with how people, incentives, institutions, and technical controls interact.

### 3. Healthcare cybersecurity as patient-safety risk

The BSidesLV 2025 panel makes healthcare cybersecurity a central theme. It states that hospitals and trauma centers face sophisticated cyber threats that jeopardize patient safety, disrupt critical care, and compromise sensitive health data [record_id:2434]. The record emphasizes that these risks are especially acute in trauma centers, where even brief system outages can create life-threatening delays [record_id:2434].

This framing moves beyond confidentiality or compliance to operational safety. Ransomware, phishing, and supply-chain disruptions are described as daily risks to clinical operations [record_id:2434]. Vulnerabilities such as legacy medical devices, unsegmented networks, and third-party software dependencies are presented as high-impact because they can cascade into emergency-care disruption [record_id:2434].

The 2026 “No Water: No Hospitals” title extends this patient-safety and continuity theme from cyber systems to physical infrastructure dependency [record_id:2846]. Although the record is sparse, the phrase “Continuity of Care under Crisis” strongly aligns with the 2025 panel’s concern for emergency care resilience during outages and disruptions [record_id:2846].

### 4. Resilience and continuity rather than prevention alone

The healthcare records emphasize resilience: how hospitals continue functioning when systems or infrastructure fail. The 2025 panel explicitly includes incident response planning, zero-trust architectures, workforce training, and cross-sector collaboration as mitigations [record_id:2434]. It also references policy challenges, federal funding, regulatory frameworks, and public-health or national-security implications [record_id:2434]. This indicates an approach that combines technical controls, organizational preparedness, and governance.

The 2026 title “No Water: No Hospitals” points toward a continuity-of-care lens: hospitals depend on external utilities, and loss of water can threaten their ability to operate [record_id:2846]. The record does not specify whether the crisis is cyber-induced, natural, political, infrastructural, or some combination, but the phrasing suggests that resilience must account for non-digital dependencies as well as networked systems.

This is a notable trend across the records: Dameff-attributed work appears interested in what happens after assumptions fail. Phishing training fails to reliably produce behavior change or meaningful metrics [record_id:91]. Emergency care systems face outages, ransomware, supply-chain issues, and legacy-device weaknesses [record_id:2434]. Hospitals may face continuity crises when foundational services such as water are unavailable [record_id:2846].

### 5. Cross-sector policy and governance as part of security practice

The healthcare panel explicitly connects operational cybersecurity with policy, funding, regulation, public health, and national security [record_id:2434]. It promises to discuss “new federal funding and regulatory frameworks” and to highlight cross-sector collaboration as a way to strengthen resilience [record_id:2434]. This is consistent with the topic metadata placing some records in governance, risk, and compliance, but the raw evidence itself supports the conclusion that policy and governance are part of the discussed security response.

The phishing-training record also has governance implications. If click-rate metrics are misleading, then organizations may be making risk, compliance, training, and accountability decisions based on weak indicators [record_id:91]. The abstract’s language about “security theater” and “flawed defense strategy” suggests concern that organizations may overvalue visible programs that produce metrics while undervaluing actual behavior change or structural controls [record_id:91].

## Methods, Tools, And Approaches Discussed

The records discuss methods and approaches at different levels of specificity.

The most concrete method is the real-world phishing-training study described in the Black Hat record. The abstract says the authors conducted an 8-month study across more than 20,000 employees, not in a controlled lab environment but “in the wild” [record_id:91]. The study appears to compare how different phishing lures perform, with attention to lure content, novelty, context, and conventional assumptions about what makes a lure effective [record_id:91]. It also raises the possibility of “scientific lure crafting,” suggesting a more systematic or experimental approach to designing phishing simulations [record_id:91]. However, the raw record does not provide statistical methods, sampling details, organizational context, baseline training conditions, or outcome measures beyond discussion of click rates.

The same record discusses gamified lure creation inside organizations and warns that it can backfire [record_id:91]. This suggests an operational workflow in which employees or security teams compete or collaborate to create phishing lures, potentially optimizing for clicks rather than learning outcomes. The abstract’s concern is that such systems may reward deceptive creativity while producing misleading metrics [record_id:91].

The healthcare panel discusses a broad set of security and resilience approaches. It identifies zero-trust architectures, incident response planning, and workforce training as operational mitigations [record_id:2434]. It also points to network segmentation indirectly by identifying “unsegmented networks” as a high-impact vulnerability [record_id:2434]. Legacy medical devices and third-party software dependencies are described as major areas of concern, implying the need for asset management, compensating controls, vendor-risk management, dependency mapping, and resilience planning, though those specific terms are not all present in the raw text [record_id:2434].

Policy and collaboration are also described as approaches. The panel highlights federal funding, regulatory frameworks, and cross-sector collaboration as part of strengthening healthcare resilience [record_id:2434]. This indicates that the discussed solutions are not purely technical. They likely involve hospital leadership, clinical operations, cybersecurity teams, government agencies, vendors, and public-health stakeholders.

The 2026 continuity-of-care record provides only the title, so methods cannot be reliably extracted [record_id:2846]. The title nevertheless signals a scenario-based or crisis-continuity approach: examining what happens to hospitals when water is unavailable and how care continues under crisis [record_id:2846]. Future research agents should avoid inferring detailed recommendations from this record unless more source material, such as a full abstract, slides, or recording, becomes available.

## Notable Talks, Records, And Evidence

The most evidence-rich record is “Pwning User Phishing Training Through Scientific Lure Crafting,” a Black Hat US 2025 briefing by Christian Dameff and Ariana Mirian [record_id:91]. It is notable because it presents a specific empirical claim: an 8-month real-world study across more than 20,000 employees found that current phishing training “doesn't move the needle” [record_id:91]. It is also notable for its critique of click rates and phishing-training metrics. The record argues that lure performance can be chaotic, that certain lures outperform expectations, and that click metrics may say more about bait than users [record_id:91]. For downstream researchers, this record is the strongest starting point for questions about Dameff’s work on human factors, security awareness, phishing simulations, and measurement validity.

The BSidesLV 2025 panel “Emergency & Urgent Care Remains in Critical Condition” is the strongest record for Dameff’s healthcare-security focus [record_id:2434]. It presents hospitals and trauma centers as targets of sophisticated cyber threats, with ransomware, phishing, and supply-chain disruption posing daily risks to clinical operations [record_id:2434]. It identifies high-impact vulnerabilities including legacy medical devices, unsegmented networks, and third-party software dependencies [record_id:2434]. It also emphasizes that outages in trauma centers can create life-threatening delays, making this record important for patient-safety and critical-infrastructure research [record_id:2434].

The 2026 BSidesLV record “No Water: No Hospitals : Continuity of Care under Crisis,” by Christian Dameff and Jeff Tully, is notable mainly as a directional signal rather than a source of detailed evidence [record_id:2846]. Its title suggests a continuation or expansion