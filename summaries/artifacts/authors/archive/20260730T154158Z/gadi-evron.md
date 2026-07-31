# Topic: Author: Gadi Evron

## Executive Summary

The five records attributed to Gadi Evron depict a set of 2026 Prompt||GTFO presentations centered on practical, live, often experimental uses of large language models in security research, productivity tooling, and everyday decision support. Across the corpus, Evron appears less as someone presenting polished enterprise systems and more as a practitioner stress-testing what current AI tools can and cannot do in real workflows: manipulating AI notetakers, automating research pipelines, vibe-coding Gmail tools, building browser extensions, analyzing phishing language, and even navigating restaurant menus with AI assistance.

The strongest recurring theme is pragmatic experimentation with AI as a co-worker: Claude, ChatGPT, GPT-5, and related coding/research tools are used to generate code, analyze text, debug applications, automate research, and make recommendations. The records also repeatedly show the limits of these systems. The most security-focused record describes prompt steering and injection against AI meeting notetakers and reports that attempted LLM research automation produced false positives, fabricated statistics, and systemic failures requiring manual oversight [record_id:2179]. Other records show live demos that work but remain brittle, such as a GPT-5-assisted Chrome extension whose on-screen demo partially fails before eventually working [record_id:2189], and a Claude-generated Google Apps Script mail merge tool tested live in Gmail [record_id:2203].

Evron’s unique contribution across these records is a hands-on, adversarial-but-practical view of AI adoption: he demonstrates how LLMs can help build tools quickly and support investigative workflows, while also highlighting unreliability, prompt sensitivity, UI failures, and the need for human supervision. The corpus is small and narrow—five short descriptions, all from Prompt||GTFO in 2026—but it captures a coherent pattern of lightweight AI-enabled workflows spanning security, coding, productivity, and personal decision support.

## Research Landscape

The included records are all Prompt||GTFO presentations from 2026 attributed to Gadi Evron. They are mostly demonstrations rather than formal papers or deeply documented research artifacts. The raw texts describe live or semi-live experiments involving AI tools, with an emphasis on applied workflows:

- AI security and prompt injection against meeting notetakers [record_id:2179].
- AI-assisted browser extension development using GPT-5 [record_id:2189].
- Claude-assisted generation of a Gmail mail merge tool in Google Apps Script [record_id:2203].
- Claude-assisted restaurant menu interpretation and communication support [record_id:2225].
- ChatGPT-assisted linguistic triage of a Hebrew phishing email [record_id:2235].

The research area is therefore not a single technical subfield but an author-centered slice of Evron’s AI experimentation. Security appears in two records most directly: manipulation of AI notetakers and unreliable automated LLM research pipelines [record_id:2179], and linguistic analysis of phishing emails for source-language and dialect inference [record_id:2235]. Developer tooling and workflow automation are also prominent, especially in the records on “Mail Goggles” and mail merge [record_id:2189; record_id:2203]. One record is explicitly lighthearted and consumer-oriented, using Claude for dining recommendations and Portuguese waiter phrases [record_id:2225].

The corpus is dominated by short presentation summaries, not transcripts, code repositories, benchmark results, or detailed technical writeups. As a result, the evidence is best for identifying topics, tools, and high-level claims. It is weaker for validating whether the demonstrated systems were robust, reproducible, secure, or technically novel beyond the live-demo context.

## Major Themes And Trends

### Practical AI experimentation across security, coding, and daily life

The clearest through-line is Evron’s use of LLMs as practical assistants. The records show him applying AI to a wide range of tasks: security research, phishing assessment, software development, Gmail automation, and restaurant menu interpretation. This breadth suggests an exploratory mode: rather than confining AI to one domain, Evron probes how far prompt-based systems can be pushed in ordinary and specialized workflows.

In the security-oriented records, this experimentation has an adversarial character. In the notetaker presentation, Evron researches “manipulating AI meeting notetakers through prompt steering and injection techniques,” while also attempting to automate the research pipeline with Claude Code and ChatGPT Deep Research [record_id:2179]. In the phishing record, he uses ChatGPT to conduct linguistic analysis of a Hebrew phishing email, iteratively prompting for grammar interference patterns, cultural cues, dialect analysis, and likelihood scores for possible source languages [record_id:2235].

In the productivity and developer-tooling records, the experimentation is constructive. Evron builds a Chrome extension called “Mail Goggles” with GPT-5, using specialized developer and tester prompts to work through bugs, UI issues, and Chrome Manifest 3 challenges [record_id:2189]. He also live vibe-codes a Gmail mail merge tool with Claude, generating a Google Apps Script that adds functionality to Google Sheets and sends a six-recipient test email [record_id:2203]. The restaurant-menu demonstration extends the same style into personal productivity, using Claude to tailor Michelin-star dining recommendations to a picky eater and produce Portuguese phrases for communicating with waiters [record_id:2225].

### AI systems are useful but brittle

A second major theme is brittleness. Evron’s demonstrations do not present LLMs as magic automation engines. They repeatedly show failure modes, workarounds, and the need for human judgment.

The most explicit example is the automated LLM research pipeline in the notetaker record. The summary states that the automation “frequently produced false positives, fabricated statistics, and systemic failures requiring significant manual oversight” [record_id:2179]. This is a strong cautionary finding: LLM research agents can accelerate work, but unsupervised outputs may be unreliable, especially when tasked with broad research and evidentiary synthesis.

The “Mail Goggles” record also indicates brittleness in development and demonstration. Evron uses GPT-5 iteratively with specialized developer and tester prompts to overcome bugs, UI issues, and Manifest 3 challenges; even then, the live demo “partially fails on screen but eventually works” [record_id:2189]. That detail is important because it captures a realistic AI-assisted development workflow: the model can help produce working software, but debugging, iteration, and live failure management remain central.

The mail merge record is more successful on the surface: Claude generates Google Apps Script, Evron pastes it into Apps Script, authorizes it, and sends a six-recipient test email live [record_id:2203]. But even here, the description implies a small-scale demo rather than evidence of production readiness. Features such as deduplication, test sends, and randomized pacing to respect Gmail rate limits suggest awareness of operational constraints, but the record does not establish long-term reliability or safety.

### Prompting as workflow design

Another recurring trend is prompt engineering as a practical workflow discipline. Evron does not merely “ask the AI” once; he structures prompts around roles, iteration, and task decomposition.

In the Chrome extension record, he creates “specialized developer and tester prompts” to build and improve the Mail Goggles extension [record_id:2189]. In the phishing investigation, he “iteratively” prompts ChatGPT to examine grammar interference, cultural cues, dialect signals, and possible source languages [record_id:2235]. In the dining demonstration, he gives Claude a screenshot of a menu and frames recommendations around his “simple palate,” asking for items to choose, items to avoid, and useful Portuguese phrases [record_id:2225]. In the mail merge record, Claude is used to generate a complete Google Apps Script with specific workflow features [record_id:2203].

The emphasis is less on model internals and more on how to convert a task into an interaction pattern. The records portray prompting as a way to build software, conduct triage, generate localized advice, or manipulate another AI system.

### Security concerns around AI-mediated communication

The notetaker record raises a security issue specific to AI-mediated communication: if AI meeting notetakers summarize, record, or transmit meeting content, they may be vulnerable to prompt steering and injection embedded in the meeting itself [record_id:2179]. This suggests a risk model where malicious or strategic participants influence not just human listeners but also automated note-taking systems.

That theme connects loosely to the phishing email record, which uses AI not as the target but as the analyst. ChatGPT is applied to infer likely attacker language background from a Hebrew phishing email, including possible Arabic, Farsi, Russian, or Chinese source-language influence and specific Arabic dialect assessment [record_id:2235]. Together, these records show AI on both sides of security work: AI systems can be attacked or manipulated, and AI systems can also help triage suspicious content.

### Lightweight, live-demo culture

All records are from Prompt||GTFO and read like short, practical demos rather than formal research papers. Several contain live-demo elements: a Chrome extension demo that partially fails then works [record_id:2189], a live mail merge test to six recipients [record_id:2203], and interactive use of Claude or ChatGPT for phishing, dining, and notetaker/research automation tasks [record_id:2179; record_id:2225; record_id:2235]. This gives the corpus a workshop-like quality. The demonstrations are valuable for surfacing real workflows and rough edges, but they do not provide rigorous evaluation.

## Methods, Tools, And Approaches Discussed

Evron’s methods are largely prompt-driven and tool-assisted.

One method is adversarial prompt steering and injection against AI meeting notetakers. The record does not specify the exact payloads or notetaker platforms, but it states that Evron presented research on manipulating AI meeting notetakers through prompt steering and injection techniques [record_id:2179]. This approach treats the meeting transcript or spoken content as an input channel through which an attacker may influence downstream AI summaries or outputs.

A second method is attempted end-to-end research automation using Claude Code and ChatGPT Deep Research. The same record reports that Evron tried to “fully automate the research pipeline,” but the automation frequently produced false positives, fabricated statistics, and systemic failures requiring manual oversight [record_id:2179]. This is notable because it frames LLM research automation as both tempting and dangerous: the tools can generate volume, but without verification they may degrade evidence quality.

A third approach is AI-assisted software development through iterative prompting. In “Mail Goggles,” Evron uses GPT-5 to develop a Chrome extension inspired by a discontinued Gmail add-on that required math problems before sending emails [record_id:2189]. The workflow includes specialized prompts for developer and tester roles, addressing bugs, UI issues, and Manifest 3 challenges [record_id:2189]. The tool itself includes configurable difficulty levels, time limits, and advanced math options [record_id:2189].

A fourth approach is live code generation for Google Workspace automation. In “Simple Mail Merge w/ Claude,” Evron uses Claude to generate a Google Apps Script that adds a Mail Merge menu to Google Sheets [record_id:2203]. The generated workflow includes contact and draft tabs, personalization tags such as `{{first_name}}` and `{{last_name}}`, deduplication, test sends, and randomized pacing of 0.5–3 seconds to respect Gmail rate limits [record_id:2203]. He then pastes the code into Apps Script, authorizes it, and sends a six-recipient test email live [record_id:2203].

A fifth approach is LLM-assisted linguistic triage of phishing emails. Evron uses ChatGPT on a Hebrew phishing email to infer likely source-language influence through grammar interference patterns, cultural cues, and dialect analysis [record_id:2235]. The workflow scores likelihoods for several candidate source languages—Arabic, Farsi, Russian, and Chinese—and attempts to identify a specific Arabic dialect [record_id:2235]. The record frames this as a triage tool for targeted phishing assessment rather than a definitive attribution mechanism [record_id:2235].

Finally, the dining demonstration uses Claude as a contextual recommendation and translation assistant. Evron screenshots a Michelin-star restaurant menu, asks for recommendations suited to his simple palate, receives items to choose and avoid, and gets Portuguese phrases for communicating with waiters [record_id:2225]. While not security-focused, it shows the same method of converting a real-world ambiguity into a prompt-based decision-support workflow.

## Notable Talks, Records, And Evidence

The most important security record is “Manipulating Notetakers & Automating LLM Research Pipelines” [record_id:2179]. It matters because it combines two high-value AI security concerns: prompt injection against AI meeting notetakers and the unreliability of automated LLM research pipelines. The record’s strongest evidence claim is that automation produced false positives, fabricated statistics, and systemic failures requiring substantial manual oversight [record_id:2179]. For downstream researchers interested in AI security, this is the central record in the corpus.

“Linguistic Investigation of Phishing Emails” is the second major security-relevant record [record_id:2235]. It presents ChatGPT as an analyst’s triage assistant for phishing investigation, focusing on language interference, cultural cues, and dialect analysis [record_id:2235]. Its importance lies in showing how LLMs can assist early-stage assessment of targeted phishing, especially in multilingual contexts. However, because the record is a summary, it does not provide validation against known attacker origin or ground truth.

“Mail Goggles: The Lost Gmail Add-on” is representative of Evron’s AI-assisted development style [record_id:2189]. It shows the use of GPT-5 not merely for code generation but for iterative debugging with specialized developer and tester prompts [record_id:2189]. The partial live-demo failure is also notable: it demonstrates that AI-generated or AI-assisted software can be functional but fragile under presentation conditions [record_id:2189].

“Simple Mail Merge w/ Claude” is the cleanest example of successful live workflow automation [record_id:2203]. Claude generates a Google Apps Script that integrates with Google Sheets and Gmail, adds a mail merge menu, supports personalization and deduplication, includes test sends, and paces messages to account