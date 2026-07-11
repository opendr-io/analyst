# Topic: Author: Philip Young

## Executive Summary

The two records attributed to Philip Young form a tightly focused mini-corpus on mainframe security, specifically the security implications of IBM z/OS Unix System Services, also referred to as OMVS. Both records describe 2025 conference talks that argue the “UNIX side” of z/OS can expose serious attack paths comparable to, and potentially more dangerous than, better-known MVS/ISPF or TSO-oriented mainframe attack surfaces. The records emphasize practical penetration-testing experience, live demonstrations, privilege escalation, database compromise, file-permission weaknesses, Enterprise Security Manager resource misunderstandings, APF-authorized dataset exploitation, open-source testing tools, and partial detection opportunities [record_id:27] [record_id:1949].

The central contribution across the records is the reframing of mainframe exploitation: not as a niche limited to traditional mainframe interfaces, but as a broader attack surface where Unix concepts—files, permissions, superuser privileges, privileged command execution, and buffer overflows—interact with z/OS-specific security models in dangerous ways. The evidence base is narrow but consistent: both records contain nearly identical abstracts for talks delivered at major security venues in 2025, one at Black Hat USA with Chad Rikansrud as coauthor, and one at DEF CON 33 attributed to Philip Young alone [record_id:27] [record_id:1949].

## Research Landscape

The included records are conference-talk abstracts rather than full papers, slides, transcripts, or technical writeups. They come from two prominent security conferences: Black Hat USA 2025 and DEF CON 33 in 2025. The Black Hat record is titled “Unix Underworld: Tales from the Dark Side of z/OS” and is attributed to Philip Young and Chad Rikansrud [record_id:27]. The DEF CON record is titled “SSH-nanigans - Busting Open the Mainframes Iron Fortress through Unix” and is attributed to Philip Young [record_id:1949].

The research area represented by these records is mainframe penetration testing and exploit development, with a strong platform-security angle. Both records situate themselves against prior “tales of mainframe pentesting and exploitation” that focused on “the MVS/ISPF side of the IBM z/OS,” then pivot to the lesser-known Unix System Services side of z/OS [record_id:27] [record_id:1949]. This indicates that Young’s contribution, at least in these records, is not generic Unix exploitation and not purely traditional mainframe security, but the intersection between the two.

The landscape is also explicitly practitioner-driven. Both abstracts state that the talks will present “live demos of real-world scenarios” encountered during mainframe penetration tests [record_id:27] [record_id:1949]. That framing matters: the records are not merely theoretical vulnerability taxonomies. They claim to be based on offensive security assessments and practical attack paths discovered over time.

At the same time, the corpus is small and abstract-level. The records do not provide exploit code, vulnerability identifiers, tool names, logs, architectures, or detailed remediation steps. They do, however, define a coherent agenda: demonstrate why z/OS Unix System Services deserves serious attention from mainframe defenders, penetration testers, detection engineers, and organizations that may underestimate the risk of granting Unix superuser access on mainframes.

## Major Themes And Trends

### z/OS Unix System Services as an underestimated mainframe attack surface

The dominant theme is that many defenders and practitioners may not realize z/OS includes a Unix environment, or may not understand its security implications. Both records use similar language: “I bet you didn’t even know z/OS had a UNIX side!” [record_id:27] [record_id:1949]. This is rhetorical, but it conveys a clear research claim: z/OS Unix System Services is underrecognized compared with the traditional MVS/ISPF side of mainframe security.

The talks position OMVS as a place where “all those same tricks” associated with mainframe pentesting can be performed, with “and more” added to emphasize that Unix services introduce additional pathways [record_id:27] [record_id:1949]. The trend suggested here is a shift from mainframe security being treated as a specialized legacy discipline toward a more hybrid model where Unix-like behavior, permissions, filesystems, privileged execution, and classic exploitation techniques matter alongside mainframe-native controls.

### Practical attack paths from weak hygiene and misconfiguration

Both records emphasize operational weaknesses rather than only exotic zero-day exploitation. The abstracts identify “poor file hygiene” leading to database compromise, “inadequate file permissions” enabling privilege escalation, and a “lack of ESM resource understanding” allowing privileged command execution [record_id:27] [record_id:1949]. These examples suggest that many relevant risks may arise from configuration, access control, and governance failures.

This is an important theme because it makes the work relevant not just to exploit developers but also to security administrators, auditors, SOC teams, and mainframe operations teams. The talks appear to argue that organizations can be compromised through mundane but consequential mistakes: files left exposed, permissions too broad, security manager rules misunderstood, and assumptions that dataset protections are sufficient when Unix-layer access creates alternate paths.

### Privilege escalation on z/OS Unix as near-critical mainframe compromise

Both abstracts state that “privesc in UNIX isn’t game over for your mainframe, it’s pretty close” [record_id:27] [record_id:1949]. This frames Unix privilege escalation as an extremely high-impact event in the mainframe context. The talks appear to challenge any security model that treats Unix superuser access as less sensitive than access to traditional mainframe interfaces.

The records sharpen this argument by concluding that granting superuser access to Unix can be “just as dangerous, if not more so, than giving access to TSO on the mainframe” [record_id:27] [record_id:1949]. That is a notable claim because TSO access is often treated as a major mainframe privilege boundary. Young’s records suggest that Unix superuser privileges should be governed with comparable or greater seriousness.

### Dataset protection is not sufficient by itself

A recurring concern is that mainframe defenders may rely too heavily on dataset protections while missing Unix-mediated attack paths. Both records explicitly say the demonstrations will show “how dataset protection won’t save you from these attacks” [record_id:27] [record_id:1949]. This theme indicates that controls need to be evaluated across the full z/OS environment, not just in one security domain.

The records do not explain the exact mechanics of how dataset protections are bypassed or rendered insufficient. However, the repeated claim suggests an architectural lesson: protection models that are effective in traditional z/OS contexts may not fully constrain what can happen through OMVS, APF-authorized datasets, privileged commands, or file permission paths.

### Blending classic Unix issues with mainframe-specific privilege models

The records combine familiar Unix security categories—file permissions, superuser access, privileged command execution, buffer overflow—with mainframe-specific concepts such as z/OS, OMVS, MVS/ISPF, TSO, ESM resources, datasets, and APF authorization [record_id:27] [record_id:1949]. This combination is arguably the most distinctive feature of the corpus.

The result is a research theme around hybrid exploitation. The attack paths are not just “Unix on a mainframe” and not just “mainframe exploitation.” They concern the ways Unix semantics operate inside an environment governed by mainframe security assumptions and resource controls.

### Offensive testing paired with partial detection

Both records indicate that attendees will learn how to test controls “using freely available open-source tools” and how to “partially” detect the attacks [record_id:27] [record_id:1949]. This introduces a defensive and detection-engineering dimension, though the wording is cautious. “Partially” suggests that visibility may be incomplete, detections may be hard to operationalize, or some activity may evade conventional monitoring.

This is a significant trend because it links exploit development and vulnerability discovery with detection engineering. The talks are framed not merely as “here is how to break mainframes,” but also as “here is how to test whether your environment is vulnerable and how to begin detecting the activity.”

## Methods, Tools, And Approaches Discussed

The records describe methods and approaches at a high level. They do not name specific tools, but they repeatedly mention “freely available open-source tools” for testing controls [record_id:27] [record_id:1949]. Downstream researchers should treat the tool evidence as real but underspecified: the abstracts support the claim that open-source testing tools are part of the talks, but they do not identify which tools or provide usage details.

The main methodological approach is live demonstration based on real-world mainframe penetration-test scenarios. Both records say the talks will present “live demos of real-world scenarios” encountered during mainframe penetration tests [record_id:27] [record_id:1949]. These scenarios include:

- Exploiting poor file hygiene to reach database compromise [record_id:27] [record_id:1949].
- Abusing inadequate file permissions to perform privilege escalation [record_id:27] [record_id:1949].
- Taking advantage of insufficient understanding of ESM resources to enable privileged command execution [record_id:27] [record_id:1949].
- Demonstrating why dataset protection alone does not prevent the described attacks [record_id:27] [record_id:1949].
- Triggering or demonstrating the consequences of overflowing a buffer in an APF-authorized dataset [record_id:27] [record_id:1949].
- Testing relevant controls with open-source tools and discussing partial detection methods [record_id:27] [record_id:1949].

The ESM-related material is especially important. ESM likely refers to Enterprise Security Manager controls in the z/OS ecosystem, but the records themselves only say “ESM resource understanding.” The method implied is to find gaps between what administrators believe ESM resource controls enforce and what they actually permit in Unix System Services contexts [record_id:27] [record_id:1949].

The APF-authorized dataset buffer overflow component adds an exploit-development dimension beyond misconfiguration. APF authorization is a mainframe-specific privilege mechanism, and a buffer overflow there suggests a path from memory-safety or input-handling failure into highly privileged execution contexts. The records do not provide enough detail to determine whether this is a known vulnerability class, a specific exploit, a lab demonstration, or a generalized technique, but both records flag it as one of the more technical demonstrations [record_id:27] [record_id:1949].

Finally, the talks appear to include detection guidance, but the record language is deliberately modest: attendees will learn how to “partially” detect the attacks [record_id:27] [record_id:1949]. This likely reflects the difficulty of monitoring OMVS activity, privileged command execution, or cross-domain mainframe activity, but the records do not specify telemetry sources, SIEM logic, audit settings, or detection rules.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 briefing, “Unix Underworld: Tales from the Dark Side of z/OS,” is the strongest record for formal conference positioning. It is categorized as a Black Hat briefing and attributed to both Philip Young and Chad Rikansrud [record_id:27]. The abstract presents a broad technical agenda around z/OS Unix System Services exploitation, real-world penetration-test scenarios, database compromise, privilege escalation, ESM resource issues, privileged command execution, dataset protection limits, APF-authorized dataset buffer overflow, open-source testing tools, and partial detection [record_id:27]. Because Black Hat briefings typically represent curated technical presentations, this record is a key anchor for understanding Young’s 2025 work in platform security and vulnerability discovery.

The DEF CON 33 talk, “SSH-nanigans - Busting Open the Mainframes Iron Fortress through Unix,” appears to cover substantially the same material, using nearly identical abstract language [record_id:1949]. It is attributed to Philip Young and listed as a DEF CON 33 video with a duration tag of 46:24 [record_id:1949]. The title emphasizes “SSH-nanigans” and “through Unix,” implying that Unix-access mechanisms such as SSH may play a role in the presentation’s framing, although the raw abstract itself does not provide specific SSH attack details beyond the broader OMVS theme [record_id:1949]. This record matters because it likely provides a public video presentation of the same or closely related research, which may contain details absent from the abstract.

Together, these records indicate that Young’s public 2025 conference work focused on moving mainframe exploitation discussions into the z/OS Unix System Services domain. The records are mutually reinforcing because their raw text is nearly identical, but that also means they are not independent evidence for separate findings. Rather, they should be treated as two appearances or versions of the same research theme at two major venues [record_id:27] [record_id:1949].

## Gaps, Limits, And Open Questions

The evidence base is narrow. There are only two records, and both are abstract-level descriptions of talks. They do not include full transcripts, slide decks, exploit code, detailed tool lists, detection logic, or remediation guidance. Because the records contain nearly identical descriptions, they provide strong evidence that this was a recurring 2025 presentation theme for Philip Young, but limited evidence about the full depth of the technical content [record_id:27] [record_id:1949].

Several open questions remain for downstream researchers:

- What specific open-source tools were used to test the controls described in the talks? Both records mention freely available tools but do not name them [record_id:27] [record_id:1949].
- What exact telemetry sources support “partial” detection? The records do not identify logs, audit events, SIEM rules, ESM records, OMVS audit settings, or behavioral indicators [record_id:27] [record_id:1949].
- What are the precise mechanics of the database compromise scenario arising from poor file hygiene? The abstracts state the outcome but not the path [record_id:27] [record_id:1949].
- How does inadequate file