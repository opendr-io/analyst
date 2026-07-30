# Topic: Digital forensics preservation and cyber history

## Meta-Summary

The records portray digital forensics and preservation as a continuum extending from historical recovery to active incident investigation. At one end, researchers recover deleted communications from hundreds of thousands of Commodore 64 disk images, revisit foundational network investigations, and preserve community artifacts such as laptop stickers. At the other, practitioners reconstruct malware state from memory, decode data from damaged accident equipment, preserve evidence of online harassment, and analyze cryptocurrency thefts through frontend and blockchain artifacts.

A recurring principle is that valuable evidence often survives outside its obvious or intended location: deleted files remain in unallocated disk sectors; runtime artifacts exist only in memory; aircraft logs hide within gigabytes of apparently random data; and cryptocurrency incidents leave evidence across clients, compromised frontends, and public ledgers. Several records also point to growing automation and AI assistance in forensic work, although the evidence for its reliability and safeguards is preliminary. Collectively, the material emphasizes preservation before loss, reconstruction across heterogeneous sources, and conversion of obscure technical artifacts into intelligible historical or investigative accounts.

## Research Landscape

The collection consists predominantly of 2025–2026 security-conference talk descriptions from DEF CON, BSidesLV, and UNPROMPTED. It is therefore a map of practitioner interests and proposed demonstrations rather than a body of peer-reviewed findings. Most records provide abstracts rather than full methodologies, datasets, validation results, or post-talk evaluations.

The research landscape has four overlapping areas:

1. **Historical computing and hacker history.** The strongest example is large-scale forensic processing of Commodore 64 floppy-disk images to recover traces of 1980s and 1990s hacker activity [record_id:1937]. A retrospective by Cliff Stoll revisits a landmark investigation that began with a small Unix accounting discrepancy and developed into international hacker attribution [record_id:2913].

2. **Cultural and community preservation.** Emergency web archiving appears through the title and the speaker’s role as a co-founder of Saving Ukrainian Cultural Heritage Online, although the supplied text is principally a biography and does not explain the archival workflow [record_id:2006]. Sticker preservation broadens the definition of hacker heritage from digital files to material objects carrying community identity [record_id:2477].

3. **Contemporary forensic analysis.** Records cover memory forensics for Go malware [record_id:2752], AI-assisted use of a DFIR workstation [record_id:2340], forensic reconstruction of a major cryptocurrency theft [record_id:3016], and the recovery and decoding of data from damaged transportation equipment [record_id:3086].

4. **Evidence in operational and social investigations.** Digital forensics is combined with HUMINT, OSINT, AI, and traditional intelligence tradecraft in a claimed counterespionage operation [record_id:2386]. Evidence preservation also appears as part of the legal and technical response to cyber harassment [record_id:2705].

The records consequently treat “preservation” broadly. It includes byte-for-byte imaging, recovery of deleted material, emergency archiving, preservation of physical hacker culture, volatile-memory acquisition and interpretation, evidentiary retention for legal disputes, and extraction from damaged embedded systems. Historical research and present-day response are connected by the same underlying challenge: artifacts are incomplete, fragile, undocumented, distributed, or difficult to interpret.

## Major Themes And Trends

### Latent evidence is often more valuable than the visible artifact

The clearest recurring theme is that investigators should not limit analysis to what a system overtly exposes. In the Commodore 64 project, enthusiasts originally created byte-for-byte disk copies to preserve games, applications, and demos. Because users reused disks and deleted files, unallocated sectors retained less obvious material, including online-session logs and hacker text files. The proposed research processed more than 650,000 unique images and indexed recovered content for search and analysis [record_id:1937].

The same logic appears in modern malware analysis. Static reverse-engineering tools can inspect compile-time artifacts, but they cannot necessarily recover execution state or data that exists only in memory. The Go-malware work therefore examines internal runtime structures, heaps, strings, call sites, and goroutine stacks to reveal evidence absent from conventional static analysis and, reportedly, from published threat intelligence [record_id:2752].

Aircraft and maritime accident recovery presents an even more physically demanding version of the problem. NTSB specialists recover data from broken or damaged equipment, search gigabytes of apparently random bytes for logs, decode undocumented binary formats, and transform the results into graphs and charts useful to investigators [record_id:3086]. Across these records, preservation is not passive storage: it is the recovery of context and meaning from residual data.

### Forensics is becoming more cross-layer and multidisciplinary

Several records reject single-source investigation. The alleged counterespionage operation combines human intelligence, open-source intelligence, digital forensics, AI, and “old-school” open-source tradecraft to identify and remove foreign actors with physical and virtual access to infrastructure [record_id:2386]. The abstract offers few reproducible details, but its framing reflects a broader movement toward joining technical telemetry with human and organizational information.

The Web3 workshop similarly divides the attack surface among the client, decentralized-application frontend, and blockchain. Its Bybit case study proposes correlating a malicious transaction, a compromised frontend, and on-chain evidence rather than treating smart-contract auditing as sufficient protection [record_id:3016]. Cyber-harassment research adds legal thresholds, psychological effects, policies, support systems, evidence preservation, and response strategy to the technical problem [record_id:2705].

Historical work is also multidisciplinary. Stoll’s retrospective joins Unix accounting, network tracing, modem infrastructure, improvised electronics, shell scripts, handwritten logbooks, and international espionage context [record_id:2913]. The record suggests that effective cyber investigation has long depended on combining weak clues from multiple technical and human domains.

### Scale and automation are changing preservation practice

The Commodore 64 work moves beyond manual examination of selected artifacts by processing and full-text indexing over 650,000 unique disk images from public archives [record_id:1937]. This makes a large historical corpus searchable and potentially enables aggregate research into hacker language, tools, and daily communication.

A more recent automation trend is agentic AI. One record describes connecting Claude Code to the SIFT digital-forensics workstation through the Model Context Protocol so that an investigator can request timeline generation, memory analysis, and malware sweeps in natural language [record_id:2340]. The speaker characterizes the result as functional only “mostly” and bases the report on more than 40 hours of testing. This is meaningful as an exploratory practitioner account, but the abstract provides no accuracy measurements, benchmark corpus, error taxonomy, or safety architecture.

AI also appears in the counterespionage account alongside HUMINT, OSINT, and digital forensics [record_id:2386]. Taken together, the records suggest that natural-language interfaces and agentic execution are moving into forensic workflows, but they do not yet establish when AI output is dependable, reproducible, or acceptable as legal evidence.

### Preservation serves historical memory as well as adjudication

The collection does not restrict preservation to courtroom evidence or technical incident response. The C64 disk corpus is presented as a way to recover day-to-day communications and tools from formative hacking, phreaking, piracy, and cybercrime subcultures [record_id:1937]. Stoll’s retrospective asks what has changed and what has not in the four decades since a foundational network intrusion investigation [record_id:2913].

Sticker preservation extends this concern to social and material history. Laptop stickers are described as markers of interests, aspirations, and community membership, but laptop upgrades threaten their survival. The talk reports experimentation with ways to remove, retain, and reuse them [record_id:2477]. Although technically modest compared with disk or memory forensics, it highlights that hacker history also resides in ephemeral physical culture.

Emergency web archiving potentially represents preservation under conditions of war or institutional disruption. The title concerns building “onramps” for emergency web archiving in Ukraine and elsewhere, and the biography identifies the speaker as a co-founder of Saving Ukrainian Cultural Heritage Online [record_id:2006]. However, because the supplied raw text contains no description of the talk’s archival methods, outcomes, or challenges, this theme is supported more by context than by substantive evidence.

### Small anomalies remain central to forensic discovery

Several records illustrate the investigative importance of anomalies. Stoll’s case began with a 75-cent Unix accounting glitch, which led to a year-long investigation across networks, modem banks, and national borders [record_id:2913]. In historical disk images, sectors not represented in the active file listing become the source of unexpected evidence [record_id:1937]. In accident investigation, the task can be to locate a meaningful log in a mass of seemingly random data [record_id:3086].

These examples span four decades and different technologies, but they share a common pattern: investigators recognize that a minor inconsistency or residual artifact does not fit the expected state, preserve it, and progressively construct a larger explanation.

## Methods, Tools, And Approaches Discussed

The historical-computing record describes a corpus-scale forensic workflow. Publicly available Commodore 64 disk images are deduplicated into a collection of more than 650,000 unique images, forensically processed, and full-text indexed. Analysis includes material in file-system structures and unallocated sectors, where deleted files and session logs may remain after disk reuse. Search and content analysis then support historical reconstruction of communications and tools [record_id:1937]. The abstract does not identify the software, file-system parser, deduplication algorithm, carving method, or quality-control process, but it clearly presents forensic indexing rather than simple archival cataloging.

For modern malware, the proposed Volatility 3 plugins parse Go runtime internals from memory. They reconstruct type and function metadata, recover heap-allocated and static strings, and classify functions by origin. ABI-aware backward analysis derives execution paths and argument values from call sites, while goroutine-stack analysis identifies active functions and recovers runtime arguments. Demonstrated targets reportedly include BRICKSTORM, Obscura ransomware, and Pantegana RAT, with recovered artifacts such as command-and-control endpoints, persistence mechanisms, encryption keys, ransom notes, attacker commands, and execution state [record_id:2752]. This is the collection’s most technically specific forensic methodology.

The AI-assisted SIFT workflow connects Claude Code to a DFIR SIFT workstation through Model Context Protocol. Natural-language requests initiate tasks including timeline generation, memory analysis, and malware sweeps [record_id:2340]. The approach may lower the interaction cost of complex tools and coordinate multi-step workflows, but granting an agent high privileges on an analysis workstation raises concerns about contamination, uncontrolled execution, hallucinated conclusions, and chain-of-custody documentation. Those concerns are logical implications of the setup, not issues resolved by the abstract.

The NTSB process focuses on physical recovery and binary interpretation. Investigators extract data from damaged devices, search large volumes of unstructured or random-looking bytes for logs, reverse or decode undocumented formats, and turn results into visual representations that investigators can use [record_id:3086]. The record does not name acquisition hardware or software, but it emphasizes the translation pipeline from damaged media to binary data to human-readable evidence.

Web3 analysis is explicitly cross-layer. Participants review their own wallet approvals with `revoke.cash`, then study the Bybit theft by examining the malicious transaction, compromised frontend, and on-chain evidence [record_id:3016]. This combines a practical exposure-reduction exercise with forensic case reconstruction. The abstract does not describe wallet-acquisition procedures, attribution methods, or standards for preserving off-chain frontend evidence.

Other approaches are less technically specified. The cyber-harassment session addresses legal thresholds, evidence preservation, response strategies, psychological impacts, policy, and support [record_id:2705]. The counterespionage account blends HUMINT, OSINT, digital forensics, AI, and established intelligence tradecraft [record_id:2386]. Sticker preservation involves experimentally comparing methods to remove, retain, and reuse physical stickers when hardware is replaced [record_id:2477]. The emergency-archiving record identifies SUCHO and its cultural-preservation setting but supplies no technical workflow [record_id:2006].

## Notable Talks, Records, And Evidence

The most substantial historical-preservation record is **“Amber64 – Mining Hacker History from Over 500k Commodore 64 Disks.”** It matters because it combines byte-level preservation, deleted-data recovery, large-scale indexing, and historical inquiry. Its corpus size and identification of specific recovered artifact classes make it the strongest evidence in the collection for computational cyber-history research [record_id:1937]. The abstract nevertheless reports intended presentation content rather than independently validated results.

**“Stalking the Wily Hacker … 40 years later”** is the collection’s central retrospective on early network forensics. It ties a tiny accounting anomaly to a year-long pursuit of German hackers associated with East German and Soviet intelligence, emphasizing improvised tools and investigative persistence before contemporary cybersecurity institutions existed. It is especially useful for comparing historical investigative fundamentals with present practice [record_id:2913].

**“Beyond Static Analysis: Memory Forensics for Go Malware”** provides the most detailed contemporary technical contribution. Its claim to present the first memory-forensics framework for runtime analysis of Go binaries, implemented as open-source Volatility 3 plugins, is concrete and potentially testable. It also names malware families and artifact types used in demonstrations [record_id:2752]. Evidence strength is relatively high at the abstract level, though the record gives no repository, evaluation metrics, comparison baseline, or reproducibility results.

**“Hacking Airplanes at the NTSB”** is notable for applying forensic recovery to safety investigations rather than conventional cyber incidents. It highlights the practical difficulties of damaged equipment, undocumented binary formats, and conversion of raw data into investigative visualizations [record_id:3086]. It also broadens the scope from computers and networks to aircraft and a recovered tourist submarine.

**“SIFT – FIND EVIL!!”** represents an emerging workflow trend: granting an agentic coding system access to a mature forensic workstation and using natural language to conduct analysis [record_id:2340]. It is valuable as evidence of experimentation with AI orchestration in DFIR, but weaker as evidence of operational readiness because the abstract provides only a testing-duration claim and a qualified assertion that the system works “mostly.”

**“Web3 Security: Hacks, Scams, and Exploits”** is representative of forensic reconstruction in distributed systems. Its key contribution is the insistence that audited smart contracts do not cover the entire attack surface. Client behavior, frontend compromise, approvals, transactions, and on-chain records must be examined together [record_id:3016].

The remaining records broaden the social and operational boundaries of the topic. Cyber-harassment work treats preservation as necessary to legal and response processes [record_id:2705]. The foreign-espionage account presents digital forensics as one element in a blended intelligence operation [record_id:2386]. Sticker preservation treats community memorabilia as historical evidence [record_id:2477]. The emergency-web-archiving record points toward cultural rescue in Ukraine, although the available source text is too biographical to establish the talk’s actual methods [record_id:2006].

## Gaps, Limits, And Open Questions

The largest limitation is source type. These are conference descriptions, not full talks, papers, datasets, code repositories, or judicial findings. They tell researchers what speakers claim they will present, but usually do not permit verification. Dates also extend into 2026, so some records may describe scheduled or proposed presentations rather than completed work.

Several important questions remain:

- **Validation of historical recovery:** How were the C64 disk images deduplicated, parsed, and searched? How often does recovered unallocated data contain false fragments or material from disk-image processing rather than original use? What ethical controls govern publication of private communications preserved unintentionally [record_id:1937]?
- **Provenance and archival integrity:** The collection rarely discusses cryptographic hashing, metadata standards, storage redundancy, format migration, rights management, or chain of custody. These are core preservation questions but are absent even where byte-for-byte imaging is mentioned.
- **Emergency web archiving:** What are the actual “onramps,” capture tools, volunteer workflows, selection criteria, authentication methods, and sustainability plans for endangered Ukrainian cultural websites? The supplied text does not answer these questions [record_id:2006].
- **AI reliability in DFIR:** What permissions were granted to the agent, how was the test environment isolated, and what errors occurred during the reported 40-plus hours? How are agent actions logged and reproduced? Can resulting findings withstand evidentiary scrutiny [record_id:2340]?
- **Operational counterespionage evidence:** The foreign-actor account makes a consequential claim involving a major portion of US infrastructure but supplies no sector, indicators, chronology, tooling details, or corroboration. The roles of AI and digital forensics cannot be evaluated from the abstract [record_id:2386].
- **Memory-forensics generalizability:** The Go framework is technically detailed, but its performance across compiler versions, architectures, stripped binaries, corrupted captures, and anti-forensic manipulation remains unknown [record_id:2752].
- **Legal preservation standards:** The cyber-harassment record mentions legal thresholds and evidence preservation without identifying jurisdictions, admissibility requirements, platform-retention constraints, or victim-safe collection procedures [record_id:2705].
- **Cross-layer cryptocurrency reconstruction:** The Web3 record does not explain how the compromised frontend was preserved or how off-chain and on-chain evidence was temporally correlated. The description of the Bybit incident as the largest cryptocurrency theft in history is a talk claim, not independently supported within this collection [record_id:3016].
- **Damaged-device recovery:** The NTSB record does not address acquisition repeatability, error correction, validation of undocumented decoders, or how investigators distinguish true logs from coincidental byte patterns [record_id:3086].
- **Material-culture preservation:** Sticker reuse may retain an object but alter its context. Future work could ask how provenance, placement, associated hardware, photography, oral histories, and community meaning should be documented alongside the sticker itself [record_id:2477].
- **Historical continuity:** Stoll explicitly asks what changed and what did not, but the abstract does not give his conclusions. Comparative work could assess which techniques—anomaly detection, logging, patient observation, infrastructure tracing, and international cooperation—remain durable and which are products of an earlier technical environment [record_id:2913].

There is also little discussion of privacy and ethics. Historical disk images may contain personal communications; memory captures can expose secrets unrelated to an incident; public-ledger evidence can be overinterpreted; and harassment records can endanger victims if mishandled. These risks are central to responsible preservation but largely outside the supplied abstracts.

## Coverage And Evidence Notes

All ten records contribute to the topic, but with unequal depth and relevance.

The strongest primary evidence for historical digital forensics is the Commodore 64 corpus, which provides a stated scale, data source, recovery location, workflow concept, and examples of recovered content [record_id:1937]. Stoll’s retrospective is strong as first-person historical testimony and points to contemporaneous publications, though this record itself remains a conference abstract [record_id:2913]. The NTSB talk gives a credible institutional use case for damaged-media recovery and undocumented binary decoding but few technical implementation details [record_id:3086].

The emergency-web-archiving entry is clearly relevant by title and by the speaker’s connection to SUCHO, yet its raw text is almost entirely biographical. It should be treated as evidence of speaker background and thematic intent, not as proof of particular archival methods or outcomes [record_id:2006]. The sticker-preservation talk is a minor but meaningful record on hacker material culture, community identity, and the practical loss caused by hardware replacement [record_id:2477].

Among secondary records, the Go-malware talk offers unusually detailed claims about a Volatility 3 framework and concrete recovered artifacts [record_id:2752]. The SIFT presentation demonstrates interest in agentic AI for timelines, memory analysis, and malware sweeps, but provides no formal evaluation [record_id:2340]. The counterespionage talk is relevant through its use of digital forensics in a blended intelligence operation, although its broad operational claims are weakly substantiated in the abstract [record_id:2386].

The cyber-harassment session is tied to the topic through preservation of evidence for legal and response purposes rather than through archival or technical recovery research [record_id:2705]. The Web3 workshop contributes a current cybercrime-forensics example by correlating wallet approvals, frontend compromise, malicious transactions, and on-chain evidence in the Bybit case [record_id:3016].

Overall, evidence is strongest where the records name a corpus, specific artifacts, an implementation platform, or a reconstruction process. It is weakest where abstracts rely on broad operational claims, titles unsupported by substantive descriptions, or general promises to equip attendees. The collection is best used to identify research directions and representative practitioner concerns, with follow-up to full talks, code, datasets, papers, and archival documentation required before relying on specific technical or historical claims.