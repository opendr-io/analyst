# Topic: Author: Ben Nassi

## Executive Summary

The two records attributed to Ben Nassi describe the same 2025 research presentation, delivered or listed in two venues: Black Hat USA 2025 and DEF CON 33. The work is coauthored by Ben Nassi, Or Yair, and Stav Cohen, and focuses on attacks against LLM-powered agents, specifically Google Gemini for Workspace assistants, using what the authors call “Promptware” and, more specifically, “Targeted Promptware Attacks” [record_id:53] [record_id:1965].

Across both records, the central contribution is the claim that prompt-injection attacks against agentic LLM systems can be practical, low-friction, and capable of producing real-world effects. The described attack vector is a Google Calendar invitation whose meeting subject contains an indirect prompt injection. According to the records, this can cause Gemini-integrated agents to act within their application context and use their available permissions to perform malicious actions [record_id:53] [record_id:1965].

The research emphasizes a broad exploitation surface: Gemini web, Gemini mobile, and Google Assistant powered by Gemini on Android. The demonstrations reportedly include toxic content generation, spam and phishing, deletion of calendar events, control of connected home appliances, Zoom video streaming, email and calendar exfiltration, geolocation, and a worm targeting Gemini for Workspace clients [record_id:53] [record_id:1965]. The work also frames these examples as evidence of “inter-agent lateral movement” and “inter-device lateral movement,” where malicious activity crosses from one Gemini agent to another or escapes the Gemini environment into smartphone applications and physical devices [record_id:53] [record_id:1965].

The evidence base is narrow but focused: both records appear to be substantially identical abstracts for the same talk. Therefore, the records strongly establish what the talk claims to cover, but they do not provide independent validation, technical implementation details, mitigations, experimental artifacts, or post-disclosure outcomes.

## Research Landscape

The records in this topic are not a broad sample of Ben Nassi’s body of work. They cover one research project, repeated across two major security-conference contexts: Black Hat USA 2025 and DEF CON 33. The Black Hat record is titled “Invitation Is All You Need! Invoking Gemini for Workspace Agents with a Simple Google Calendar Invite” [record_id:53]. The DEF CON 33 record is titled “Invoking Gemini Agents with a Google Calendar Invite” [record_id:1965]. Both attribute the work to Ben Nassi, Or Yair, and Stav Cohen.

The research area represented by these records is AI security, with a particular focus on prompt injection against LLM-integrated agents. The talks are not about generic chatbot jailbreaks alone; they specifically address agentic LLM systems that have access to tools, applications, operating-system permissions, or user data. The records present prompt injection as an application-security and systems-security problem because the LLM does not merely produce text; it can trigger actions through connected services and devices [record_id:53] [record_id:1965].

The stated threat model centers on an attacker who can place adversarial content into a data channel consumed by the victim’s LLM-powered assistant. The primary example is sending a Google Calendar invitation whose subject contains an indirect prompt injection. The records also mention related delivery mechanisms: email and shared Google Docs [record_id:53] [record_id:1965]. This positions the research within a growing concern about untrusted content entering LLM context windows through ordinary collaboration workflows.

The dominant source type is conference-talk abstract material. There are no full papers, slide decks, code repositories, vulnerability advisories, vendor responses, or empirical datasets included in the provided records. As a result, the landscape is best understood as a conference-level summary of a research demonstration rather than a complete technical corpus.

## Major Themes And Trends

### Promptware as a practical attack class

The records introduce or emphasize “Promptware” as a class of attacks against LLM-powered systems. Promptware is defined in the abstracts as prompts in text, image, or audio form that are engineered to exploit LLMs at inference time and cause malicious activity within the application context [record_id:53] [record_id:1965].

A recurring theme is the rejection of the idea that prompt-based exploitation is exotic or impractical. The records explicitly state that Promptware has often been perceived as requiring adversarial machine-learning expertise, GPU clusters, and white-box access, and then frame the talk as a demonstration that this assumption is wrong [record_id:53] [record_id:1965]. The central rhetorical move is to shift prompt injection from a specialized AI-research concern into a practical security threat accessible through ordinary user workflows such as calendar invitations.

### Targeted Promptware Attacks through collaboration artifacts

The most specific contribution is the concept of “Targeted Promptware Attacks.” In the records, this means attacks where an adversary targets a particular user by sending content that the user’s assistant may later ingest. The primary attack vector is a Google Calendar meeting invitation whose subject contains an indirect prompt injection [record_id:53] [record_id:1965].

This framing matters because the attack does not require compromising the victim’s account in the conventional sense. Instead, the attacker supplies malicious content through a legitimate collaboration mechanism. The assistant’s later interpretation of that content becomes the exploitation path. The records also note that similar attacks could be delivered by email or a shared Google Doc, expanding the theme from calendar-specific exploitation to the broader problem of trusted productivity tools carrying untrusted prompt content [record_id:53] [record_id:1965].

### Agent hijacking and permission abuse

Both records describe the attack as “agent hijacking.” The attacker allegedly hijacks the application context, invokes integrated agents, and exploits the agents’ permissions to perform malicious activities [record_id:53] [record_id:1965]. This is one of the most important security themes in the records: the danger comes not only from model misbehavior, but from the model’s coupling to real capabilities.

The described targets are three Gemini for Workspace assistants: the Gemini web interface, Gemini for Mobile, and Google Assistant powered by Gemini on Android devices [record_id:53] [record_id:1965]. The Android/Google Assistant angle is especially significant because the records state that Google Assistant runs with OS permissions on Android devices. This connects prompt injection to mobile-device control, local application access, and potentially physical-world effects through connected services.

### Lateral movement between agents and devices

The records explicitly claim that the demonstrations show two forms of lateral movement: “inter-agent lateral movement” and “inter-device lateral movement” [record_id:53] [record_id:1965].

Inter-agent lateral movement refers to malicious activity being triggered between different Gemini agents. The records do not give a detailed step-by-step chain, but they present the idea that one agentic context can cause or influence activity in another Gemini-related context [record_id:53] [record_id:1965].

Inter-device lateral movement is described as escaping the boundaries of Gemini and using applications installed on a victim’s smartphone to perform malicious activities with physical outcomes. The examples include activating a boiler and lights or opening a connected window in a victim’s apartment [record_id:53] [record_id:1965]. This theme places the work at the intersection of AI security, mobile security, and IoT/OT-adjacent risk.

### Physical-world impact from LLM-agent compromise

A major trend in these records is the movement from information security to physical security. The listed attack outcomes include traditional cyber harms such as spam, phishing, email exfiltration, calendar exfiltration, and calendar-event deletion. But they also include remotely controlling home appliances, video streaming the victim through Zoom, and geolocating the victim [record_id:53] [record_id:1965].

This combination broadens the perceived consequences of prompt injection. The records present LLM-agent exploitation as a route to privacy invasion, social engineering, data theft, service disruption, surveillance, and physical-environment manipulation. In that sense, the talks contribute to a broader trend in AI security research: treating LLM agents as high-risk orchestrators when connected to tools and permissions.

### Risk assessment and urgency of mitigations

Both records state that the authors developed a dedicated threat-analysis and risk-assessment framework. They report that 73% of the identified risks are classified as high-critical and require immediate mitigations [record_id:53] [record_id:1965].

The abstracts do not provide the framework’s methodology, scoring criteria, risk categories, sample size, or validation process. Still, the inclusion of a risk framework indicates that the work aims to go beyond proof-of-concept demonstrations. The authors appear to be arguing for systematic assessment of agentic LLM risk rather than isolated bug reports.

## Methods, Tools, And Approaches Discussed

The main method described in both records is indirect prompt injection through a Google Calendar invitation. The attacker sends a meeting invite to a victim, placing adversarial prompt text in the meeting subject. When Gemini for Workspace or a related assistant processes that content, the prompt can allegedly invoke the agent, alter its behavior, and cause it to misuse its available tools or permissions [record_id:53] [record_id:1965].

The records mention several delivery surfaces:

- Google Calendar meeting subject lines as the primary demonstration path [record_id:53] [record_id:1965].
- Email as another possible channel for adversarial content [record_id:53] [record_id:1965].
- Shared Google Docs as another possible channel [record_id:53] [record_id:1965].

The targeted systems are described as three widely used Gemini for Workspace assistants:

- Gemini web interface at `www.gemini.google.com` [record_id:53] [record_id:1965].
- Gemini for Mobile [record_id:53] [record_id:1965].
- Google Assistant powered by Gemini on Android devices [record_id:53] [record_id:1965].

The described exploitation approach depends on the assistant having access to tools and permissions. The records list 15 exploitations of agent hijacking, though they do not enumerate all 15 as discrete technical cases. The examples given include content generation, spam/phishing, calendar deletion, home-appliance control, Zoom streaming, exfiltration of emails and calendar events, geolocation, and a worm targeting Gemini for Workspace clients [record_id:53] [record_id:1965].

The “worm” claim is particularly notable. It suggests a self-propagating or semi-self-propagating attack pattern against Gemini for Workspace clients, likely using the same collaboration surfaces that deliver the original malicious prompt. However, the abstract does not provide enough detail to determine the propagation mechanism, necessary permissions, user interaction requirements, or containment assumptions [record_id:53] [record_id:1965].

The records also mention a “dedicated threat analysis and risk assessment framework” developed by the authors. The framework is used to classify identified risks, with 73% reportedly falling into high-critical categories [record_id:53] [record_id:1965]. Because the records do not describe the framework’s structure, downstream researchers should treat this as a claimed component of the talk rather than a fully inspectable method.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 record, “Invitation Is All You Need! Invoking Gemini for Workspace Agents with a Simple Google Calendar Invite,” is the clearest record for the research’s framing and branding [record_id:53]. It foregrounds the “Invitation Is All You Need” phrasing and explicitly presents the work as a Black Hat briefing. It describes Promptware, introduces Targeted Promptware Attacks, and claims 15 demonstrations against Gemini for Workspace assistants. This record is important because it presents the research as a formal security-conference briefing and gives a compact statement of the threat model, affected assistant surfaces, exploit outcomes, lateral-movement claims, and risk-assessment result [record_id:53].

The DEF CON 33 record, “Invoking Gemini Agents with a Google Calendar Invite,” appears to describe the same research presentation in another venue [record_id:1965]. Its raw text is effectively the same as the Black Hat abstract, including the Promptware definition, the Google Calendar invitation vector, the three Gemini assistant targets, the list of malicious outcomes, the lateral-movement claims, and the 73% high-critical risk finding [record_id:1965]. It matters because it shows the work was also presented or made available in the DEF CON 33 context, with a listed video duration of 45:36 in the record metadata. The raw text itself does not add technical detail beyond the Black Hat version.

Taken together, the two records provide strong evidence that Ben Nassi and coauthors publicly presented a research project on Gemini agent invocation through calendar-invite prompt injection in 2025. They provide moderate evidence about the scope of claimed demonstrations because the abstracts are detailed and consistent. They provide weaker evidence about the technical validity, exploit reliability, disclosure status, mitigations, and reproducibility because neither record includes full technical artifacts.

## Gaps, Limits, And Open Questions

The biggest limitation is that both records appear to be duplicate or near-duplicate abstracts for the same research. They should not be treated as two independent confirmations of the technical claims. They are better understood as two venue listings for one project [record_id:53] [record_id:1965].

Several important technical questions remain unanswered:

1. **Exploit mechanics.** The records state that a