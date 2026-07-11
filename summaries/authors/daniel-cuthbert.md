# Topic: Author: Daniel Cuthbert

## Executive Summary

The available record for Daniel Cuthbert consists of a single 2026 Prompt\|\|GTFO presentation, **“Adventures in Cryptographic Discovery,”** describing a two-year project that combines CodeQL, software supply-chain style inventorying, graph visualization, and large language models to identify and reason about cryptographic behavior in applications and binaries [record_id:2186]. The central contribution described by the record is a workflow for tracing cryptographic flows, extracting crypto-relevant paths with CodeQL, converting those findings into SBOM-like cryptographic bills of materials, visualizing cryptographic operations as graphs, and using GPT-based analysis to flag weak cryptography from normalized scanner output [record_id:2186].

Because the corpus contains only one record, the evidence base is narrow. Still, the record points to several clear themes: crypto discovery as an application-security and software-supply-chain problem; the use of static analysis and query languages to extract security-relevant program behavior; graph-based representations for understanding complex cryptographic usage; and LLM-assisted interpretation of scanner output [record_id:2186]. The presentation appears to sit at the intersection of application security, cryptographic inventory, supply-chain transparency, and AI-augmented security analysis.

## Research Landscape

The research landscape represented here is highly concentrated: there is one source record, a conference-style talk attributed to Daniel Cuthbert at Prompt\|\|GTFO in 2026, titled **“Adventures in Cryptographic Discovery”** [record_id:2186]. The raw record text characterizes it as a presentation of a “two-year project” focused on tracing and mapping cryptographic flows in applications and binaries using CodeQL queries and LLMs [record_id:2186].

The dominant source type is therefore not a blog series, paper collection, or multi-talk career survey, but a single technical presentation. It appears to cover a research-and-engineering system rather than a purely conceptual argument. The record describes specific components: CodeQL, SBOM-like output, D3-based graph visualization, demonstrations on OpenSSL and BoringSSL, and GPT-based analysis of normalized scanner output [record_id:2186]. The metadata also associates the record with tools and platforms such as CodeQL, an SBOM Graph Explorer, a CodeQL-to-SBOM tool, a CodeQL Helper using ChatGPT, D3.js, Neo4j, GitHub Advanced Security, GitHub Copilot, and ChatGPT/GPT-5, but the raw text itself specifically supports CodeQL, LLMs/GPT, D3 visualizations, OpenSSL, BoringSSL, and SBOM-like cryptographic bills of materials [record_id:2186].

The overall research area is best understood as **cryptographic discovery and inventory**: finding where and how cryptography is used inside software, mapping the flow of cryptographic operations, and representing those findings in ways that are useful for security review, modernization, or weakness detection [record_id:2186]. The record also places the work in the broader area of **application security** and, secondarily, **software supply chain security**, because the project generates SBOM-like artifacts for cryptographic components and behaviors [record_id:2186].

## Major Themes And Trends

### Cryptography as Discoverable Application Behavior

The central theme is that cryptographic use inside applications and binaries can be systematically discovered, traced, and mapped [record_id:2186]. Rather than treating cryptographic assessment as a manual code review problem alone, the project described in the record uses CodeQL queries to extract “crypto paths” from software [record_id:2186]. This suggests a model in which cryptographic APIs, operations, and flows are treated as queryable program facts.

This is significant because cryptographic risk often depends not only on the presence of a library or algorithm but on how cryptography is invoked, configured, chained, and exposed through application behavior. The record’s emphasis on “flows” and “paths” indicates an attempt to move beyond simple dependency inventory toward behavioral mapping of cryptographic usage [record_id:2186].

### From SBOMs to Cryptographic Bills of Materials

Another major theme is the adaptation of SBOM concepts to cryptographic discovery. The record says the system generates “SBOM-like cryptographic bills of materials” [record_id:2186]. This implies a specialized inventory that captures cryptographic operations or paths rather than only software packages, libraries, and versions.

The record does not specify the exact schema, fields, or output format of these cryptographic bills of materials, but the concept is important. It aligns with a broader industry trend toward making software composition and security posture machine-readable. In this case, Cuthbert’s project appears to extend that trend into cryptographic transparency: identifying what crypto is present, where it occurs, and potentially whether it is weak or acceptable [record_id:2186].

### Graph-Based Understanding of Crypto Operations

The system also creates “D3-based graph visualizations of crypto operations,” demonstrated on OpenSSL and BoringSSL [record_id:2186]. This highlights a recurring challenge in security analysis: raw static-analysis output can be difficult to interpret, especially when dealing with large codebases or complex libraries. Graphs can help analysts understand relationships among functions, call paths, cryptographic primitives, and data flows.

The choice of OpenSSL and BoringSSL as demonstration targets is representative because they are widely used cryptographic libraries with large and complex codebases [record_id:2186]. The record does not provide details about what specific OpenSSL or BoringSSL flows were found, but their mention suggests the project was tested or demonstrated against mature, security-critical cryptographic software rather than only small toy examples [record_id:2186].

### LLM-Assisted Security Analysis

The presentation also includes the use of GPT to analyze and flag weak cryptography from normalized scanner output [record_id:2186]. This shows an AI-augmented workflow where LLMs are not necessarily the primary scanner but are used after normalization to interpret, triage, or classify findings. The raw record text frames GPT as part of a pipeline that processes scanner output and identifies weak cryptography [record_id:2186].

This theme matters because it positions LLMs as analytical helpers in a structured security workflow. The record does not claim that GPT directly discovers vulnerabilities from source code alone; rather, it describes GPT analyzing normalized scanner output [record_id:2186]. That distinction suggests a more controlled use of LLMs: first obtain structured evidence from static analysis or scanners, then use the model to assist with interpretation and weakness identification.

### Bridging Application Security and Software Supply Chain Security

The record’s topic classification places the work primarily under application security and secondarily under software supply chain security, and the raw text supports that bridge through its combination of CodeQL path extraction and SBOM-like cryptographic inventories [record_id:2186]. The project appears to address questions relevant to both domains: What cryptography is present in an application? Where does it flow? Is any of it weak? Can it be represented in a portable artifact for later analysis or visualization? [record_id:2186]

This bridging is a distinctive feature of the record. Traditional application security may focus on defects in code, while software supply chain security often focuses on components and dependencies. Cuthbert’s described work connects those concerns by treating cryptographic behavior as something that can be extracted, inventoried, visualized, and evaluated [record_id:2186].

## Methods, Tools, And Approaches Discussed

The primary method described is the use of **CodeQL queries** to trace and extract cryptographic paths in applications and binaries [record_id:2186]. CodeQL is presented not merely as a vulnerability query tool but as a mechanism for discovering crypto-relevant flows and producing structured outputs that can feed later stages of analysis [record_id:2186].

A second approach is the creation of **SBOM-like cryptographic bills of materials** [record_id:2186]. The record does not specify whether these artifacts follow an established SBOM standard or a custom format, so the safest conclusion is that they are “SBOM-like” rather than necessarily formal SPDX or CycloneDX documents. Their purpose appears to be documenting cryptographic usage or operations extracted from code and analysis results [record_id:2186].

A third method is **graph visualization**, specifically D3-based graph visualizations of crypto operations [record_id:2186]. These visualizations are described as being demonstrated on OpenSSL and BoringSSL [record_id:2186]. The record does not give full architectural details, but the likely role of the visualization layer is to make cryptographic paths and relationships easier to inspect than raw query output.

A fourth approach is **LLM-assisted analysis**, where GPT analyzes normalized scanner output and flags weak cryptography [record_id:2186]. This suggests a workflow in which scanner findings are first normalized into a consistent form, then passed to GPT for interpretation or classification [record_id:2186]. The record does not provide evaluation metrics, false-positive rates, prompt design, or model-comparison results, so the evidence supports the presence of this approach but not its measured effectiveness.

The metadata associated with the record also lists tools and systems such as a CodeQL-to-SBOM tool, a CodeQL Helper implemented as a ChatGPT custom GPT, an SBOM Graph Explorer, D3.js, Neo4j, GitHub Advanced Security, GitHub Copilot, and ChatGPT/GPT-5 [record_id:2186]. However, the raw record text directly substantiates CodeQL, LLMs/GPT, D3-based graph visualization, SBOM-like crypto bills of materials, OpenSSL, and BoringSSL [record_id:2186]. Downstream researchers should treat the metadata-enumerated tools as useful leads but should verify them against the actual talk or transcript before relying on them as evidence.

## Notable Talks, Records, And Evidence

The sole and therefore most important record is **“Adventures in Cryptographic Discovery,”** a 2026 Prompt\|\|GTFO presentation by Daniel Cuthbert [record_id:2186]. It is notable because it describes a multi-year effort rather than a one-off tool demo: the raw text identifies it as a “two-year project” [record_id:2186]. The project’s purpose is to trace and map cryptographic flows in applications and binaries using CodeQL queries and LLMs [record_id:2186].

The presentation is representative of a practical research direction in modern security engineering. It combines several layers:

- static analysis through CodeQL queries;
- extraction of cryptographic paths;
- generation of SBOM-like cryptographic bills of materials;
- graph visualization of crypto operations;
- demonstrations on OpenSSL and BoringSSL;
- GPT-based analysis to flag weak cryptography from normalized scanner output [record_id:2186].

The evidentiary strength of this record is high for describing what the talk is about, but thin for validating the effectiveness of the system. The raw record provides a compact summary of the project and its components, but it does not include implementation details, examples of queries, sample output, benchmark results, error analysis, or independent evaluation [record_id:2186]. As a result, the record is best used to identify the talk’s scope, themes, and technical direction, not to make strong claims about accuracy, scalability, or production readiness.

## Gaps, Limits, And Open Questions

The largest limitation is corpus size. With only one record, it is not possible to describe Daniel Cuthbert’s broader body of work, long-term evolution of views, recurring talks across multiple events, or changes in emphasis over time. The available evidence supports a focused summary of one 2026 presentation, not a full author profile [record_id:2186].

Several technical gaps remain open:

1. **Exact CodeQL methodology.**  
   The record says CodeQL queries are used to extract crypto paths, but it does not describe the query structure, supported languages, source/sink models, taint tracking configuration, or how cryptographic operations are identified [record_id:2186].

2. **Binary-analysis details.**  
   The raw text says the project traces and maps cryptographic flows in “applications and binaries,” but does not explain how binaries are analyzed, whether CodeQL is applied only to source, or whether other binary-analysis tooling is involved [record_id:2186].

3. **SBOM-like artifact specification.**  
   The record mentions cryptographic bills of materials but does not define their schema, whether they interoperate with existing SBOM standards, or whether they encode algorithms, key sizes, modes, call paths, libraries, versions, or policy results [record_id:2186].

4. **Graph model and visualization semantics.**  
   D3-based graph visualizations are described, but the record does not explain what graph nodes and edges represent, how graphs are generated, whether graph data is stored in a database, or how analysts interact with the visualization [record_id:2186].

5. **LLM evaluation and safety.**  
   GPT is used to analyze normalized scanner output and flag weak cryptography, but the record does not include performance metrics, hallucination controls, reproducibility methods, model choice rationale, or validation against expert labels [record_id:2186].

6. **Results from OpenSSL and BoringSSL demonstrations.**  
   The record says the system was demonstrated on OpenSSL and BoringSSL, but does not state what findings were produced, whether weak cryptography was identified, or how the visualizations improved analyst understanding [record_id:2186].

7. **Operational use cases.**  
   The record implies relevance to application security and software supply chain security, but does not specify whether the system is intended for CI/CD, audit, compliance, cryptographic migration, vulnerability research, or incident response [record_id:2186].

Future research agents should therefore seek the full video, slides, transcript, code repositories, sample artifacts, or follow-up publications connected to the talk. Those materials would be needed to determine the system’s architecture, implementation maturity, supported ecosystems, and empirical performance.

## Coverage And Evidence Notes

This report covers the single expected record: Daniel Cuthbert’s 2026 Prompt\|\|GTFO talk **“Adventures in Cryptographic Discovery”** [record_id: