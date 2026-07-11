# Topic: Author: Juanma

## Executive Summary

The two records attributed to Juanma describe closely related BSidesLV 2025 talks about **Have I Been Ransomed? (HIBR)**, a toolchain and public search engine intended to identify personally identifiable information (PII) inside ransomware leak dumps. Both records focus on the modern ransomware ecosystem’s shift from file encryption alone to **large-scale data exfiltration and public leakage**, and both frame the resulting dumps as chaotic, unstructured collections of sensitive corporate and personal documents. Juanma’s contribution, as represented in these records, is a practical and ethical exploration of how to crawl ransomware gang leak sites, process leaked files using **OCR and large language models**, detect PII in formats such as scanned IDs, HR documents, contracts, passports, insurance records, PDFs, and image scans, and make breach-awareness tooling without directly exposing the sensitive data being discovered [record_id:2470] [record_id:2471].

The strongest common theme is the tension between **visibility and harm reduction**: HIBR aims to make ransomware-leaked PII discoverable enough to alert or inform affected people, while avoiding the creation of a new privacy risk or search interface for abuse. The records repeatedly emphasize ethical, legal, and operational constraints, including GDPR concerns, “blurry legal zones,” and design choices meant to avoid becoming “a privacy nightmare” or “getting sued” [record_id:2470] [record_id:2471]. The evidence base is narrow—only two records, both apparently describing variants of the same talk—but it is thematically coherent and gives downstream researchers a clear view of Juanma’s stated area of work: responsible processing and indexing of ransomware leak data for PII detection and breach awareness.

## Research Landscape

The available corpus for “Author: Juanma” consists of two BSidesLV 2025 records, both centered on the same core project and talk concept: **“Indexing the Chaos”**, with one title phrased as “Extract PII from Ransomware Leaks” and the other as “Extracting PII from Ransomware Leaks (Token 06)” [record_id:2470] [record_id:2471]. The records appear to represent two scheduled or venue-specific versions of a talk at the same event rather than two distinct research lines. One is associated with BSidesLV’s Ground Truth track/location metadata and tagged for Tuesday 18:00–18:45, while the other is associated with Skytalks/Misora and tagged for Monday 18:00–18:45 [record_id:2470] [record_id:2471]. The raw text, however, shows substantial overlap in subject matter and project framing.

The dominant research area is at the intersection of:

- **Ransomware leak analysis**
- **Data loss detection and prevention**
- **Privacy and data leakage**
- **PII extraction from unstructured documents**
- **Responsible disclosure and harm-minimizing breach-awareness systems**
- **Legal and ethical handling of illicitly published datasets**

The records describe ransomware leaks as containing “terabytes of internal corporate documents” and “unstructured chaos,” including scanned passports, HR forms, insurance records, contracts, HR PDFs, scanned IDs, and similar documents [record_id:2470] [record_id:2471]. Juanma’s work is presented as addressing a gap in breach-checking: existing tools often focus on credential dumps or structured breach datasets, while ransomware leak archives may contain sensitive data hidden inside PDFs, scans, images, ZIP files, and other messy document formats [record_id:2470].

The talk descriptions are practical rather than purely theoretical. They promise a walkthrough of a working pipeline: crawling ransomware leak sites, downloading leaked materials, applying OCR and LLM-based analysis, identifying the presence and location of PII, and doing so without showing or exposing the PII itself [record_id:2470] [record_id:2471]. At the same time, the records frame the project as ethically precarious. The tool is not merely a technical achievement; it is described as “half tool, half moral panic generator,” and the talks explicitly address legal constraints and the “fine art of not getting sued” [record_id:2471].

## Major Themes And Trends

### Ransomware has evolved into mass data exposure

Both records begin from the premise that ransomware is no longer only about encryption. Juanma’s talk frames the modern ransomware problem as one of **exfiltration and public leakage**, with attackers publishing large quantities of internal corporate data when victims do not pay [record_id:2470]. This makes ransomware leaks not just an availability or extortion issue, but a privacy and identity-risk problem affecting employees, customers, and third parties whose documents may be buried in leaked archives.

The records use vivid language to emphasize the scale and disorder of the problem. Leaked datasets are described as “terabytes of internal corporate documents” and “unstructured chaos” [record_id:2470]. The second record similarly describes ransomware gang outputs as “the chaos” left behind by “digital hyenas,” including scanned IDs, contracts, HR PDFs, and sensitive documents in archives with names such as “pay_or_we_leak.zip” [record_id:2471]. These descriptions point to a core trend: ransomware leak sites have become informal, hostile data repositories containing PII that may not be captured by conventional breach-monitoring systems.

### Existing breach-checking tools may miss unstructured ransomware leaks

A recurring claim is that “most breach-checking tools ignore” ransomware leak data because it is messy and unstructured [record_id:2470]. Traditional breach search systems often work best with structured datasets such as email/password dumps, but ransomware leaks may involve scanned documents, image-based PDFs, handwritten or low-quality records, insurance forms, identification documents, contracts, and HR material. Juanma’s talk positions HIBR as an answer to that gap: a system that can process the document-heavy formats where PII may be present but not trivially searchable [record_id:2470] [record_id:2471].

This is an important contribution because it reframes breach awareness from “Has my email appeared in a database?” to “Is my personal data somewhere inside a leaked corporate document dump?” The records suggest that the latter is more complex technically and legally, because the system needs to inspect sensitive leaked content while ensuring it does not become a channel for further disclosure [record_id:2470].

### OCR and LLMs are presented as enablers for finding hidden PII

Both records identify **OCR plus LLMs** as central to the HIBR pipeline [record_id:2470] [record_id:2471]. OCR allows the system to extract text from image scans, scanned IDs, PDF images, and other non-text-native files. LLMs are described as enabling detection of personal data “buried deep inside PDFs and image scans” and helping sift through the disorganized mix of documents found in ransomware dumps [record_id:2470].

The records do not provide implementation details such as model selection, prompt structure, validation metrics, data schemas, or false positive/false negative rates. However, they strongly indicate that Juanma’s work is not simply keyword search over leaked data. It is a pipeline for extracting meaning from complex, noisy document collections. This is particularly relevant for downstream researchers studying applied LLM use in security operations, privacy engineering, or cybercrime data analysis.

### Responsible design is treated as central, not incidental

The strongest non-technical theme is **responsible handling of dangerous data**. Both records repeatedly stress that the system is designed to identify sensitive information without exposing it. The first record says the talk will explain how HIBR “safely extract[s] identifiers without exposing PII” and will address “ethical landmines,” GDPR, and design decisions to avoid becoming “a privacy nightmare” [record_id:2470]. The second record says, “No, we don’t show you the PII. But we know where it is,” and frames the work as navigating “uncomfortable data,” “blurry legal zones,” and avoiding legal trouble while examining ransomware leaks [record_id:2471].

This gives Juanma’s work a distinctive emphasis: the technical pipeline is inseparable from its governance model. HIBR is presented as a tool that must balance public benefit—helping people know whether their data has been leaked—against the risk that indexing ransomware dumps could increase harm by making sensitive documents more discoverable. The records do not resolve all of these tensions, but they make them explicit and central [record_id:2470] [record_id:2471].

### The talk tone combines technical realism with moral discomfort

The first record is relatively formal and conference-abstract-like, describing a “toolchain and public search engine,” “practical understanding,” and “live examples” [record_id:2470]. The second record is more provocative and informal, describing the pipeline as “half tool, half moral panic generator” and ransomware data as “the internet’s open wound” [record_id:2471]. Despite stylistic differences, both converge on a shared message: processing ransomware leak data is technically possible and socially useful, but also ethically unsettling.

This tonal contrast may reflect different venues or audiences within BSidesLV 2025: one record is associated with Ground Truth, the other with Skytalks [record_id:2470] [record_id:2471]. Downstream researchers should treat the two records as complementary descriptions of the same project rather than as separate evidence of multiple distinct talks unless additional scheduling or archival material confirms that they were delivered independently.

## Methods, Tools, And Approaches Discussed

Juanma’s records describe a pipeline centered on **Have I Been Ransomed? (HIBR)**. In the first record, HIBR is described as “a toolchain and public search engine designed to extract meaningful PII” from ransomware leaks using OCR and LLMs [record_id:2470]. In the second, HIBR is described as “a system that crawls ransomware gang leak sites, downloads the chaos, and uses OCR + LLMs to sift through scanned IDs, contracts, HR PDFs,” and other materials [record_id:2471].

The implied workflow has several stages:

1. **Crawling ransomware leak sites**  
   HIBR is said to crawl ransomware gang leak sites and collect leaked datasets [record_id:2470] [record_id:2471]. The records do not specify whether this crawling is manual, automated, continuous, selective, or limited to particular gangs. They also do not describe infrastructure, storage controls, or deconfliction procedures.

2. **Downloading and ingesting leaked archives**  
   The second record explicitly says the system “downloads the chaos,” while the first describes processing “terabytes of internal corporate documents” leaked by ransomware actors [record_id:2470] [record_id:2471]. The data types include scanned passports, HR forms, insurance records, scanned IDs, contracts, HR PDFs, PDFs, image scans, and other corporate documents [record_id:2470] [record_id:2471].

3. **Optical character recognition**  
   OCR is used to extract text from scanned documents and image-based files [record_id:2470] [record_id:2471]. This is necessary because many ransomware leaks contain documents that are visually readable but not text-indexable by conventional search.

4. **LLM-based PII detection and interpretation**  
   LLMs are presented as helping detect personal data that may be buried inside complex documents [record_id:2470]. The records suggest that LLMs are used for more than simple pattern matching; they help interpret messy, heterogeneous documents such as PDFs, scans, contracts, and HR files [record_id:2470] [record_id:2471]. However, the records do not provide technical detail on how LLM outputs are verified or constrained.

5. **Identifier extraction without exposing PII**  
   The first record emphasizes safe extraction of identifiers “without exposing PII” [record_id:2470]. The second similarly says that the system does not show users the PII, even though it can determine where it is [record_id:2471]. This implies some kind of minimization, hashing, redaction, location-based indexing, or controlled search mechanism, but the records do not specify the exact design.

6. **Public search or awareness interface**  
   The first record explicitly calls HIBR a “public search engine” and says attendees will learn how to build “awareness tools responsibly” [record_id:2470]. This suggests a user-facing component, probably intended to let people or organizations determine whether their information appears in ransomware leaks. The second record stresses that it is “not a product demo,” but rather a deep dive into the pipeline and its implications [record_id:2471]. Together, the records indicate both a practical system and a broader research/ethics discussion.

7. **Legal and ethical constraint management**  
   GDPR, ethical landmines, privacy nightmare avoidance, legal ambiguity, and liability avoidance are explicit parts of the methodology [record_id:2470] [record_id:2471]. Juanma’s approach appears to treat compliance and harm reduction as design requirements rather than afterthoughts.

## Notable Talks, Records, And Evidence

The most representative record is **“Indexing the Chaos: Extract PII from Ransomware Leaks”**, a BSidesLV 2025 talk attributed to Juanma [record_id:2470]. This record provides the clearest formal statement of the project’s purpose: ransomware leaks contain sensitive unstructured documents, existing breach-checking tools often ignore them, and HIBR uses OCR and LLMs to extract meaningful PII while avoiding direct exposure of that PII [record_id:2470]. It also explicitly mentions legal and ethical concerns such as GDPR and design decisions to avoid creating a privacy nightmare [record_id:2470]. For downstream researchers, this record is the strongest evidence for HIBR as a privacy/security toolchain and public search engine.

The second notable record, **“Indexing the Chaos: Extracting PII from Ransomware Leaks (Token 06)”**, appears to cover the same project in a more informal and rhetorically intense style [record_id:2471]. It is