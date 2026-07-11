# Topic Summary Design

## Goal

Topic summaries are read by knowledge agents, not primarily by humans. Their job is to help downstream research agents answer open-ended questions about research, talks, presentations, tools, techniques, claims, and evidence by routing to the right records inside a topic.

A good topic summary should let an agent identify:

- relevant record IDs
- subtopics and adjacent concepts
- search terms, aliases, tools, people, organizations, claims, and use cases
- which records to inspect next for a specific question
- which talks or presentations are representative of a theme
- which tools, projects, methods, or workflows are mentioned and why they matter
- which records contain evidence for a claim versus commentary, logistics, or market context

The summary should be a long-form research report and synthesis layer, not a database-style index. SQL queries and annotations can produce record lists, keyword lists, tool lists, and subtopic indexes; the topic summary should instead explain what the records collectively say.

## Source Data

For topic summaries, use raw record text as the primary evidence source. The purpose is to get research synthesis that goes beyond annotation-level extraction:

- argument structure
- methodology
- caveats and limitations
- relationships between records
- implicit assumptions
- why a record matters
- whether a record is technical evidence, commentary, logistics, or market context

Annotations can still be included as secondary context or used in audits, but the summary model should reason from the full records.

## Current Fit

For the current database, every topic fits comfortably in one GPT-5.5 prompt.

Using compact annotation/classification fields, the largest estimated topic prompts are roughly:

- `Exploit development and vulnerability discovery`: 164 records, about 55k estimated input tokens
- `Detection engineering, SOC, SIEM, and threat hunting`: 159 records, about 53k estimated input tokens
- `Application security`: 146 records, about 48k estimated input tokens
- `OT and IoT security`: 136 records, about 44k estimated input tokens

Using full raw records, the largest estimated topic prompts are still only about 58k estimated input tokens.

Using annotations plus full raw records, the largest estimated topic prompts are:

- `Exploit development and vulnerability discovery`: 164 records, about 115k estimated input tokens
- `Detection engineering, SOC, SIEM, and threat hunting`: 159 records, about 113k estimated input tokens
- `Application security`: 146 records, about 94k estimated input tokens
- `OT and IoT security`: 136 records, about 87k estimated input tokens

All fit comfortably in a 1M-token GPT-5.5 input window.

Given a 1M-token input window, chunking is not required for the current dataset.

Recommended rule:

```text
if estimated_input_tokens < 750k:
    single-pass topic summary
else:
    stop and notify the user
```

The summarizer should not silently switch into chunk/funnel mode. If a topic exceeds the single-pass safety threshold, it should stop before making any LLM call and report:

- topic name
- expected record count
- estimated input tokens
- configured safety threshold
- largest records by token estimate, if available
- recommended options, such as increasing the threshold, reducing included fields, or explicitly approving a chunked design

## Summary Size

The output should be large enough to preserve routing coverage but not so large that it buries answers.

Recommended output targets:

- 1-10 records: 1k-3k tokens
- 10-50 records: 4k-8k tokens
- 50-100 records: 8k-15k tokens
- 100+ records: 15k-30k tokens

Large summaries should remain structured and repetitive. Do not use maximum output length just because the model allows it.

## Deterministic Coverage Guarantees

Coverage must be enforced by deterministic code, not trusted to the LLM.

Preflight should:

- verify every classified record has topic metadata required for summary lookup
- verify every `record_classifications.primary_topic` exists in `topics`
- load all records whose `records.agent_topics` contains the target topic
- compute expected record count before prompt construction
- build the prompt from the loaded record set
- extract record IDs from the prompt payload
- verify prompt record IDs exactly equal expected topic record IDs
- verify there are no duplicate or unexpected prompt record IDs
- fail before the LLM call if any coverage check fails

Postflight should:

- parse the generated summary for record IDs
- verify every expected record ID appears at least once in the output
- record any missing, duplicate, or unexpected output record IDs
- fail or mark the summary incomplete if output coverage is not exact
- write an audit file with expected IDs, loaded IDs, prompt IDs, output IDs, missing IDs, and output metadata

The LLM should receive cooperative instructions, but code remains responsible for verification.

The summary prompt should say:

```text
Every record ID must appear at least once in the final summary.
Do not omit minor records; mention them in Coverage and Evidence Notes if they do not fit a major theme.
Use record IDs when discussing findings, themes, trends, examples, tools, talks, or claims.
Write a long-form research report, not a database-style index.
Do not include a Subtopic Index, Tool And Project Index, Technique And Method Index, Threat / Risk / Use Case Index, People And Organizations Index, or Question Routing Hints section.
```

## Recommended Summary Structure

```markdown
# Topic: <topic>

## Executive Summary
Concise meta-summary of what the records collectively say about this topic.

## Research Landscape
What kinds of records are included, which sources or talk types dominate, and what the overall research area looks like.

## Major Themes And Trends
Narrative synthesis of identifiable themes, trends, disagreements, shifts, and recurring concerns across the records.

## Methods, Tools, And Approaches Discussed
Notable methods, tools, workflows, architectures, techniques, or approaches, written as prose with record IDs.

## Notable Talks, Records, And Evidence
The most important or representative records and why they matter.

## Gaps, Limits, And Open Questions
What the records do not answer, where evidence is thin, and what future research questions remain.

## Coverage And Evidence Notes
Account for all records, including minor, ambiguous, logistical, or weakly tied records, so every record ID appears at least once.
```

## Audit Requirements

Each generated summary should have a companion audit file. The audit should include:

- topic name
- summary status: `complete`, `incomplete`, or `failed`
- model
- generated timestamp
- taxonomy version or topic table snapshot hash
- prompt version
- source database path and database fingerprint
- expected record count
- loaded record count
- expected record IDs
- record IDs included in prompt
- record IDs found in output
- missing output record IDs
- duplicate output record IDs
- unexpected output record IDs
- output token or character estimate
- summary input artifact path
- summary file path

If any record ID is missing from the final output, the summary job should fail or mark the summary as incomplete.

Only complete summaries should replace the current Markdown output by default. Incomplete or failed attempts should remain in run artifacts and audit files.

## Run Artifacts

Each summary run should save enough information to reproduce and debug the LLM call.

Recommended layout:

```text
summaries/
  topics/
    <topic-slug>.md
  sources/
    <source-slug>.md
  authors/
    <author-slug>.md
  artifacts/
    topics/
      <topic-slug>.audit.json
      <topic-slug>.prompt-input.md
      <topic-slug>.manifest.json
      archive/
        <topic-slug>-<timestamp>.md
    sources/
      <source-slug>.audit.json
      <source-slug>.prompt-input.md
      <source-slug>.manifest.json
      archive/
        <source-slug>-<timestamp>.md
    authors/
      <author-slug>.audit.json
      <author-slug>.prompt-input.md
      <author-slug>.manifest.json
      archive/
        <author-slug>-<timestamp>.md
```

There should be one current summary per topic. The current summary for a topic lives at:

```text
summaries/topics/<topic-slug>.md
```

The companion files under `summaries/artifacts/topics/` describe the current
summary:

- `<topic-slug>.audit.json`: deterministic coverage, source fingerprints, output status, and record ID checks
- `<topic-slug>.prompt-input.md`: exact prompt payload sent to the model
- `<topic-slug>.manifest.json`: model, prompt version, database fingerprint, topic metadata, and artifact paths

Older complete, incomplete, or failed runs should be moved under the matching
`summaries/artifacts/<group>/archive/` folder instead of replacing the current
artifact history.

The filesystem is the source for summary outputs and full run artifacts. SQLite should not store the many-page summary body.

Chunking should only happen after explicit user approval or a deliberate design change. If approved in the future, keep chunk artifacts in the same summaries folder under a topic-specific chunk prefix:

```text
summaries/
  topics/
    <topic-slug>.md
  artifacts/
    topics/
      <topic-slug>.manifest.json
      <topic-slug>.audit.json
      <topic-slug>.chunks/
        chunk-001.input.md
        chunk-001.output.md
        chunk-002.input.md
        chunk-002.output.md
      <topic-slug>.synthesis/
        final.input.md
        final.output.md
```

## Record ID Format

Prompt inputs and summary outputs should use a strict record ID format so postflight checks are reliable.

Use:

```text
[record_id:1234]
```

Do not rely on ambiguous plain numbers. The postflight parser should extract only this format when checking summary coverage.

## Staleness Detection

Topic summaries become stale when any of their source evidence changes.

A summary should be considered stale if any of these change:

- records included in the topic
- record raw text
- record annotations
- record classifications
- topic definitions
- summary prompt version
- model or model configuration, if strict reproducibility is required

The audit should include a source fingerprint that can be recomputed before reuse. A practical fingerprint is a hash over:

- topic name
- ordered record IDs
- per-record `records.updated/imported` proxy fields available in the DB
- per-record annotation `updated_at`
- per-record classification `updated_at`
- topic table `updated_at` for the topic
- prompt version

If the fingerprint differs, the summary should be treated as stale and regenerated.

## Secondary Topic Policy

Topic summaries include every record where the topic appears in `records.agent_topics`.

That means summaries include:

- records whose primary topic is the target topic
- records whose secondary topics include the target topic

The audit should distinguish primary-topic records from secondary-topic records so an agent can understand why a record appears in the topic summary.

## Rationale Policy

Classification rationale can be useful but is not authoritative.

Some rationale text was generated before taxonomy updates or manual backfills. The raw record text is authoritative for topic-summary synthesis. Rationale may be included as context, but the model should not treat it as ground truth when it conflicts with the raw record.

## Failure And Retry Behavior

If postflight detects missing record IDs:

1. Retry once with a stricter repair prompt that includes the missing IDs and asks the model to revise the summary while preserving existing structure.
2. Re-run postflight coverage checks.
3. If coverage still fails, mark the run `incomplete` or `failed` and require review before treating the summary as complete.

The job should never silently accept a summary that omits expected records.

## Practical Implication

The topic summary should synthesize full record text, not just the compact annotation cards.

Annotations remain valuable for:

- SQL and keyword search
- validating topic coverage
- detecting missing records
- helping an agent retrieve exact records after a summary routes it there

The summary should provide a research map over the raw records so an agent can understand themes and reasoning that annotations may not fully capture.
