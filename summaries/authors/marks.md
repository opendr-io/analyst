# Topic: Author: Marks

## Executive Summary

The two records attributed in part to Marks are both DEF CON 33 Voting Village sessions from 2025, and both focus on election-system security. Together, they frame election risk around two linked concerns: technically simple manipulation of ballot-marking-device behavior, and governance failures created by insider or politically motivated access to voting equipment and software. The records do not present a broad portfolio of Marks’s work; instead, they show a narrow but coherent cluster of Voting Village contributions centered on voting technology, election integrity, recoverability after compromise, and the risks posed by both design weaknesses and unauthorized access.

One record describes a technical demonstration involving a Dominion touchscreen ballot-marking device, emphasizing how changes to an election definition—without malware injection—could affect what voters see, how they make selections, and ultimately how votes are counted or interpreted [record_id:1855]. The other record shifts from device-level manipulation to insider-threat and supply-chain/governance concerns, discussing alleged or reported efforts to gain access to voting equipment and copies of voting-system software in several U.S. states [record_id:1867]. Across both, the dominant theme is that election security is not only a matter of preventing sophisticated malware; relatively simple manipulations, access abuses, and institutional failures may create serious risks that are hard to detect, attribute, or recover from.

## Research Landscape

The records in this topic are both talks from DEF CON 33’s Voting Village, a setting focused on hands-on and policy-relevant exploration of election technology security. Marks appears as a co-author or co-speaker rather than as sole author in both records. The records are categorized primarily or secondarily around operational technology / IoT security and governance, risk, and compliance, but the raw text places them specifically in the domain of voting systems and election infrastructure.

The source set is small: only two records. Both are abstracts or descriptions of talks rather than full transcripts, slide decks, papers, or post-event technical writeups. As a result, the evidence is strongest for identifying the topics Marks participated in, the claims the sessions intended to make, and the kinds of demonstrations or discussions planned. The evidence is weaker for reconstructing the full technical details, empirical results, or the speakers’ precise conclusions.

The landscape represented here is highly election-specific. It includes:

- A technical Voting Village demonstration on manipulating ballot displays and voter instructions on a Dominion touchscreen ballot-marking device [record_id:1855].
- A policy and threat discussion about alleged or reported extralegal access to voting equipment, multistate acquisition of voting-system software, and possible implications for future elections [record_id:1867].

Together, the records suggest that Marks’s DEF CON 33 contributions were concentrated on the intersection of voting-machine security, election administration, insider or authorized-access abuse, and resilience after compromise.

## Major Themes And Trends

### Election-security risk can arise without sophisticated malware

A central theme in the Dominion ICX talk is that impactful attacks may be technically simple. The abstract states that “simple ‘hacks’” to the ballot displayed on a voter’s touchscreen could directly affect the vote count or influence voter decisions, and it specifically notes that these do not require injecting malware [record_id:1855]. This is significant because it shifts attention away from only high-complexity software exploitation and toward configuration, election-definition integrity, display logic, and usability manipulation.

The record identifies several possible manipulations: altering how candidate choices are displayed, silently removing candidates from the display, and presenting false touchscreen instructions that misinform voters about candidates or ballot questions [record_id:1855]. These examples suggest a threat model in which the voting device’s interaction with the voter becomes an attack surface. The risk is not limited to changing stored votes invisibly; it also includes manipulating the voter’s perception and decision-making at the point of ballot marking.

### Recoverability is a major concern, not just prevention

The Dominion ICX record emphasizes that determining or recovering from such hacks “can range from difficult to impossible” [record_id:1855]. This makes recovery and forensic confidence a recurring concern. The talk’s framing suggests that election-system design decisions may enable manipulations that are easy to perform but hard to unwind after the fact.

This theme connects naturally with the insider-threat record. If voting-system software has been copied or distributed outside normal controls, future trust and recoverability questions become harder: election officials and researchers may need to understand what was accessed, whether systems were altered, whether vulnerabilities were discovered by unauthorized parties, and how long-term exposure affects future elections [record_id:1867]. The record explicitly says the discussion would outline what is known and not known about the “status” of the “purloined software” and what it could mean for future elections [record_id:1867].

### Design choices and governance failures both matter

The first talk attributes the feasibility of the described hacks to “underlying system design decisions” that made them “technically simple, feasible, and easily executable” [record_id:1855]. That indicates a design-security critique: the system architecture, election-definition handling, or ballot-display mechanisms may create unnecessary opportunities for manipulation.

The second talk focuses less on device design and more on governance, legality, chain of custody, and insider or politically motivated access. It describes reported attempts by representatives of the Trump administration to obtain “extralegal access to voting equipment,” and compares that to a multistate scheme from 2020–2022 that allegedly accessed voting machines in Colorado, Georgia, Michigan, and Pennsylvania and obtained copies of voting-system software [record_id:1867]. The concern here is not simply that systems may contain vulnerabilities, but that unauthorized access to equipment and software can alter the threat environment for future elections.

Together, the records show an integrated view of election security: technical weaknesses are dangerous, but they become more consequential when institutional controls fail or when insiders and politically connected actors obtain access to machines, software, or election definitions.

### Public availability and scalability of knowledge are treated as part of the risk

The Dominion ICX abstract states that the knowledge and tools used or discussed were obtained through public means and public websites and were available to an unlimited number of people [record_id:1855]. This is an important framing. The talk appears to argue that the barrier to entry for certain election-definition or ballot-display manipulations may be low because relevant knowledge and tooling are publicly accessible.

The same record says the talk would focus on “general methodology and ease,” “range of impacts,” “feasibility,” and “scalability” [record_id:1855]. That language suggests the authors were not merely presenting a one-off laboratory trick; they wanted to evaluate whether these manipulation methods could plausibly scale or be repeated across contexts. The abstract does not provide the full methodology, but it clearly identifies scalability and ease of execution as central questions.

### Insider threat is framed as a future-election issue, not only a past incident

The insider-threat talk is rooted in recent and historical events, but its forward-looking emphasis is explicit. It says the discussion will cover what the alleged multistate access plot and the status of copied voting-system software “could mean for elections in the future” [record_id:1867]. This positions insider access not as a closed historical controversy, but as an ongoing security concern.

The record’s mention of what is known and “don’t know” also signals uncertainty as a key part of the threat landscape [record_id:1867]. If copies of voting-system software were obtained by unauthorized parties, open questions include who has the software, whether it has been analyzed, whether vulnerabilities have been found, whether exploit knowledge has spread, and what mitigations are sufficient. The abstract does not answer these questions, but it identifies them as central.

## Methods, Tools, And Approaches Discussed

The methods and approaches in the records fall into two broad categories: hands-on technical manipulation of voting-system artifacts, and investigative/policy analysis of unauthorized access incidents.

In the Dominion ICX session, the described method centers on manipulating the election definition or ballot presentation rather than deploying malware [record_id:1855]. The abstract names several manipulation approaches: changing the display of candidate choices, silently removing candidates from the touchscreen display, and inserting false instructions that misinform voters about candidates or ballot questions [record_id:1855]. These are presented as real-time demonstrations using a Dominion touchscreen ballot-marking device that had debuted at Voting Village 2023 [record_id:1855]. The record also states that a deeper technical dive would follow in the Voting Village lab room, implying a combination of public presentation and hands-on technical exploration [record_id:1855].

The approach in that record is notable because it treats user-interface integrity as a security property. The attack surface is not described as remote code execution or malware persistence; it is the content and structure of what the voter sees and follows. The talk’s planned focus on methodology, ease, impacts, feasibility, and scalability suggests a risk-assessment approach that considers not just whether a manipulation is possible, but whether it could be reproduced and what consequences it could have [record_id:1855].

The insider-threat session uses a different method: synthesis of reported events and known/unknown status of compromised or copied voting-system software [record_id:1867]. It references “recent news accounts” and a “multi-state scheme” from 2020–2022 involving access to voting machines in Colorado, Georgia, Michigan, and Pennsylvania and acquisition of copies of voting-system software [record_id:1867]. The described approach is analytical and investigative rather than a hands-on exploit demonstration. It aims to outline what is known, what remains unknown, and what implications unauthorized access may have for future elections [record_id:1867].

Across both records, the implied defensive approaches include stronger controls over election definitions and ballot displays, improved system design to prevent easy manipulation, better forensic and recovery capabilities, and stricter governance over access to voting equipment and software [record_id:1855; record_id:1867]. The abstracts do not list specific defensive tools, but their risk framing points toward election-definition validation, chain-of-custody controls, access governance, post-compromise assessment, and independent review.

## Notable Talks, Records, And Evidence

The most technically focused record is “Voting Village - Dominion ICX Simple Hacks Daunting Recoveries,” co-authored by Springall, Davis, and Marks [record_id:1855]. It matters because it presents a concrete device and scenario: a Dominion touchscreen ballot-marking device, a real-time demonstration, and specific types of ballot-display manipulation. Its key contribution is the assertion that technically simple changes to election definitions can manipulate candidate displays, remove candidates, or mislead voters through false instructions, potentially affecting vote counts or voter decisions without malware injection [record_id:1855]. The talk also foregrounds the recovery problem, arguing that determining or recovering from such manipulation may be difficult or impossible [record_id:1855].

The most governance- and threat-actor-focused record is “Voting Village - When Insiders Are the Threat,” co-authored by Burbank, Greenhalgh, Marks, and Jefferson [record_id:1867]. It matters because it connects election security to allegations of extralegal access and prior multistate efforts to access voting equipment and obtain voting-system software [record_id:1867]. The record specifically references Colorado, Georgia, Michigan, and Pennsylvania as states where voting machines were accessed during a 2020–2022 scheme, according to the abstract’s framing [record_id:1867]. Its contribution is to treat insider or politically motivated access as an ongoing threat with uncertain future consequences.

The two records complement one another. Record 1855 shows why access to voting-system configuration, election definitions, or device behavior can be dangerous even in the absence of malware [record_id:1855]. Record 1867 explains why unauthorized access to equipment and software could matter at a systemic level, especially when software copies circulate outside official controls [record_id:1867]. Together, they support a combined technical-governance interpretation: election security depends on both robust system design and strong institutional controls over who can access systems and software.

## Gaps, Limits, And Open Questions

The evidence base is thin because there are only two records, both of which are talk abstracts rather than full proceedings. They identify topics and planned demonstrations or discussions, but they do not provide full technical details, experimental data, mitigation recommendations, or final conclusions.

For the Dominion ICX record, major unanswered questions include:

- What exact components of the election definition were modified?
- What access level was required to perform the described manipulations?
- How would standard pre-election logic and accuracy testing interact with these manipulations?
- What audit mechanisms, voter-verifiable paper records, or canvass procedures might detect or limit the effects?
- Under what conditions would recovery be “difficult” versus “impossible”?
- How scalable are the techniques in practice across jurisdictions or ballot styles?

The abstract says the talk would discuss methodology, impact, feasibility, and scalability, and that a deeper technical dive would occur in a lab room, but the record itself does not include those details [record_id:1855].

For the insider-threat record, major unanswered questions include:

- What is the current status and distribution of the allegedly obtained voting-system software?
- Which parties possess copies, and whether those copies have been shared further?
- Whether vulnerabilities have been found or exploited as a result of that access?
- What remediation actions election officials, vendors, or federal authorities have taken?
- How current reported efforts compare legally and operationally to the 2020–2022 incidents?
- What concrete policy controls would reduce future insider or extralegal access risk?

The record explicitly notes that the discussion would address what is known and “don’t know” about the status of the “purloined software,” indicating that uncertainty is part of the evidence landscape [record_id:1867].

Another limitation is attribution. Marks is one of several named authors or speakers in each record, so the records do not isolate Marks’s individual contributions, views, or technical findings. Downstream researchers should avoid attributing every claim in the abstracts solely to Marks. The safest characterization is that Marks participated in or was credited on two DEF CON 33 Voting Village sessions about voting-system security, one technical and one governance/insider-threat