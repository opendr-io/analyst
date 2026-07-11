# Topic: Author: Olivier Bilodeau

## Executive Summary

The two records attributed to Olivier Bilodeau focus on the modern information stealer malware ecosystem, especially how stealers capture sensitive victim material and how defenders can transform that material into detection, threat intelligence, and countermeasures. Both records are 2025 conference talks, and both treat infostealers as a major, underestimated cybercrime problem rather than a narrow malware-analysis niche.

The strongest shared theme is that information stealers produce artifacts that can be used defensively. In one talk, Bilodeau and Estelle Ruellan propose using screenshots embedded in stealer logs, together with large language models, to identify infection vectors and extract indicators of compromise at scale [record_id:26]. In the other, Bilodeau presents a broader ecosystem-level deep dive into what stealers capture, including screenshots, password vaults, browser extensions, and MFA-bypass material, while also discussing the Redline takedown and defensive countermeasures with code and samples [record_id:2253].

Taken together, the records position Bilodeau’s contribution around practical malware ecosystem analysis: understanding what infostealers collect, how they spread, how attackers monetize or operationalize stolen material, and how defenders can use stealer artifacts to detect campaigns and reduce further compromise. The evidence base is narrow—only two records, both abstracts rather than full papers or slide decks—but coherent. It suggests a focused 2025 research agenda around infostealers, threat intelligence extraction, and countermeasure development.

## Research Landscape

The record set consists of two conference presentation abstracts from 2025. One is a Black Hat USA 2025 briefing co-authored by Estelle Ruellan and Olivier Bilodeau, titled “Hackers Dropping Mid-Heist Selfies: LLM Identifies Information Stealer Infection Vector and Extracts IoCs” [record_id:26]. The other is a BSidesSF 2025 talk by Olivier Bilodeau, titled “Inside the Information Stealer Ecosystem: From Compromise to Countermeasure” [record_id:2253].

The overall research area is malware analysis and reverse engineering, with strong overlap into detection engineering, threat hunting, endpoint security, identity compromise, and access-token abuse. Both records treat information stealers as an operational threat with downstream consequences beyond initial infection. The Black Hat abstract emphasizes scale, automation, and extraction of indicators of compromise from infostealer logs using large language models [record_id:26]. The BSidesSF abstract emphasizes ecosystem understanding and defensive response, including what data is captured by stealers and what countermeasures can be implemented [record_id:2253].

The sources are talk abstracts, not complete technical artifacts. They provide enough detail to infer key research directions and claims, but they do not include implementation specifics, datasets, evaluation metrics, code repositories, or full methodology. As a result, the records are best used as evidence of Bilodeau’s public speaking and research focus, rather than as complete technical documentation.

## Major Themes And Trends

### Information stealers as a large-scale and underestimated threat

Both records characterize information stealer malware as a serious and growing problem. The Black Hat abstract states that infostealers are “one of the most prolific and damaging threats” in the cybercrime landscape and claims that more than 30 million stealer logs were traded on underground markets in 2024 [record_id:26]. The BSidesSF abstract makes a similar but more qualitative claim, saying that “information stealer malware is underestimated by our industry” [record_id:2253].

This shared framing is important. The records do not present infostealers merely as commodity malware or simple credential theft tools. Instead, they present them as an ecosystem that captures diverse sensitive material and enables broader compromise. The BSidesSF talk lists captured artifacts such as desktop screenshots, password vaults, browser extensions, and MFA-bypass material [record_id:2253]. The Black Hat talk emphasizes browser-stored credentials, session tokens, and system secrets, then focuses on screenshots captured at the moment of infection [record_id:26].

The trend across the records is a move from treating stealer logs as stolen data dumps toward treating them as structured intelligence sources. Bilodeau’s work, as represented here, appears to ask: if attackers collect massive amounts of victim-side context, can defenders mine that same context to identify how infections happened and prevent the next wave?

### Defensive use of attacker-collected artifacts

A recurring and distinctive theme is the inversion of infostealer telemetry. Stealer logs are normally harmful because they contain credentials, secrets, tokens, and other victim data. However, record 26 argues that buried within these logs are “screenshots captured at the precise moment of infection,” which the authors describe as a “crime scene” snapshot and an “underexplored goldmine” [record_id:26]. The presentation proposes using those screenshots to identify infection vectors, extract IoCs, and track campaigns.

This theme also appears in the BSidesSF abstract, although in broader terms. That talk promises a deep dive into what stealers capture and then offers defensive countermeasures, including code and samples [record_id:2253]. The connection between the two records is that understanding the contents of stealer logs is not only an exercise in victim-impact assessment; it is also a path toward practical defense.

This is one of the clearest unique contributions in the record set. The Black Hat talk’s framing—“Hackers Dropping Mid-Heist Selfies”—captures the idea that attackers inadvertently create evidence that can be exploited by defenders [record_id:26]. The method appears to involve analyzing infection-time screenshots to infer whether a victim downloaded malware through cracked software, malicious ads, fake AI tools, or other lures.

### Campaign tracking and infection-vector reconstruction

The Black Hat briefing is specifically about reconstructing infection vectors and extracting IoCs from infostealer screenshots [record_id:26]. It says the approach found “several hundred potential IoCs” in the form of URLs leading to malware-laden payloads. It also claims that applying the method to “fresh” stealer logs could allow defenders to detect and mitigate infection vectors “almost instantaneously,” reducing further infections [record_id:26].

The same abstract identifies three campaign categories used to illustrate attacker tactics: cracked versions of popular software, ads pointing to popular software, and free AI image generators [record_id:26]. These examples suggest that the research is concerned with social engineering, lure infrastructure, and malware distribution, not just post-infection forensic analysis.

The BSidesSF talk appears to operate at a higher level of abstraction, moving “from compromise to countermeasure” and covering the overall stealer ecosystem [record_id:2253]. It does not list specific infection vectors, but it likely provides context for why reconstructing the chain of compromise matters. Together, the records imply a workflow from understanding what stealers collect, to identifying how infections happen, to implementing defensive mitigations.

### Identity, session, and MFA compromise

Although the primary topic is malware analysis, the records also highlight identity security implications. The Black Hat abstract mentions browser-stored credentials, session tokens, and system secrets as data siphoned by infostealers [record_id:26]. The BSidesSF abstract expands this with password vaults, browser extensions, and “MFA bypass material” [record_id:2253].

This theme matters because it places infostealers in the broader context of account takeover and access delegation. The records imply that modern infostealer compromise is not limited to password theft. Session tokens and MFA-bypass material can allow attackers to bypass traditional authentication controls, making endpoint infection a direct route to identity compromise. The BSidesSF record’s secondary association with endpoint security and identity is consistent with the raw text’s emphasis on password vaults, browser extensions, and MFA-bypass material [record_id:2253].

### Practical countermeasures and operationalization

Both records emphasize practical defense. The Black Hat talk promises a live demonstration and discusses implementation challenges and costs of using LLMs to extract IoCs at scale [record_id:26]. The BSidesSF talk promises defensive countermeasures, “including code and samples” [record_id:2253].

This indicates an operational orientation. Bilodeau’s talks, as represented in these abstracts, are not purely descriptive. They aim to give defenders methods they can use: mine stealer artifacts, extract indicators, understand captured materials, and apply countermeasures. The explicit mention of live demonstration, code, samples, and implementation costs makes this a practical research strand rather than a purely conceptual one [record_id:26; record_id:2253].

## Methods, Tools, And Approaches Discussed

The most concrete method appears in the Black Hat record: using large language models to analyze screenshots taken by information stealers at the moment of infection [record_id:26]. The proposed workflow is to leverage infection screenshots and LLMs to identify infection vectors, extract indicators of compromise, and track campaigns at scale. The abstract states that this method found several hundred potential IoCs, especially URLs leading to malware-laden payload downloads [record_id:26].

The method is notable because screenshots are semi-structured visual evidence. They may show browser pages, search results, download prompts, websites, ads, fake software portals, cracked-software pages, or other lure content. The abstract does not describe the exact technical pipeline, but it implies a combination of screenshot ingestion, LLM-based interpretation, extraction of URLs or other indicators, and campaign clustering or tracking [record_id:26]. It also explicitly states that the presentation addresses “challenges and costs of implementation,” suggesting attention to practical scaling constraints such as model cost, accuracy, data sensitivity, triage volume, or integration with threat-intelligence workflows [record_id:26].

The Black Hat record also describes applying the approach to “fresh” stealer logs to detect and mitigate infection vectors quickly [record_id:26]. This suggests a near-real-time or rapid-response workflow in which newly acquired logs are processed to identify active distribution infrastructure before more users are infected. The method’s stated outputs include IoCs, infection-vector identification, campaign tracking, and analysis of distribution strategies, lure themes, and social engineering techniques [record_id:26].

The BSidesSF record is less specific about the mechanics but broader in defensive scope. It says the talk examines what infostealers capture, including desktop screenshots, password vaults, browser extensions, and MFA-bypass material [record_id:2253]. It also covers the Redline takedown and offers defensive countermeasures with code and samples [record_id:2253]. The raw text does not specify the code, tooling, or countermeasure categories, but it implies hands-on defensive guidance for reducing risk from infostealer compromise.

Across both records, the approaches include:

- Artifact analysis of stealer logs and captured victim data [record_id:26; record_id:2253].
- Screenshot-based infection reconstruction [record_id:26].
- LLM-assisted extraction of IoCs and campaign intelligence [record_id:26].
- Study of lure themes and social engineering tactics [record_id:26].
- Defensive countermeasure development, with code and samples promised in the BSidesSF talk [record_id:2253].
- Ecosystem analysis, including discussion of Redline and its takedown [record_id:2253].

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 briefing is the more technically detailed and methodologically distinctive record. “Hackers Dropping Mid-Heist Selfies: LLM Identifies Information Stealer Infection Vector and Extracts IoCs,” co-authored by Estelle Ruellan and Olivier Bilodeau, presents a novel defensive use of infection-time screenshots captured in infostealer logs [record_id:26]. Its importance lies in the combination of a large-scale threat problem, an overlooked artifact class, and a modern analysis technique. The abstract claims that over 30 million stealer logs were traded in 2024 and that screenshots within those logs can reveal infection vectors [record_id:26]. It further claims that the proposed LLM-based approach found several hundred potential IoCs, especially malware-download URLs, and can be applied to fresh logs to reduce further infections [record_id:26].

This record also provides the clearest examples of attacker distribution strategies: cracked versions of popular software, ads pointing to popular software, and free AI image generators [record_id:26]. These examples are useful for downstream researchers because they show the types of lures Bilodeau and Ruellan planned to analyze in the presentation. The mention of a live demonstration and implementation costs also suggests that the work was intended for practitioners building detection or threat-intelligence systems [record_id:26].

The BSidesSF 2025 talk, “Inside the Information Stealer Ecosystem: From Compromise to Countermeasure,” is important because it frames Bilodeau’s broader view of infostealers [record_id:2253]. The abstract states that infostealer malware is underestimated and promises a deep dive into what these tools capture, including screenshots, password vaults, browser extensions, and MFA-bypass material [record_id:2253]. It also says the talk covers the Redline takedown and offers defensive countermeasures, including code and samples [record_id:2253].

While the BSidesSF record has fewer technical specifics than the Black Hat record, it is valuable because it situates the narrower LLM-and-screenshot technique inside the larger infostealer ecosystem. It suggests that Bilodeau’s research interest includes not only extraction of IoCs but also the full path from compromise to countermeasure: what is stolen, how that stolen material changes defender priorities, how major stealer operations such as Redline fit into the ecosystem, and what defenders can implement in response [record_id:2253].

## Gaps, Limits, And Open Questions

The evidence is coherent but limited. There are only two records, and both are short conference abstracts from 2025. They do not provide enough detail to fully evaluate the technical claims. For example, record 26 says the LLM-based approach found several hundred potential IoCs, but it does not specify the dataset size, ground truth, false-positive rate, model type, prompt strategy, evaluation process, or validation method for the extracted URLs [record_id:26]. It also does not explain how sensitive victim data in stealer logs is handled, anonymized, minimized, or legally obtained.