
![Alt text](docs/analyst.gif)
### Analyst

An agent that answers questions about cybersecurity conference research using an agent curated knowledge base. UI is via Jupyter notebook or command prompt.SQL queries can also be used to search for researchers, talks, or tools. 

Answers to free-form questions are given from three dozen pre-processed topic summaries compiled by a knowledge agent. There are also summaries for each conference and for authors with more than one presentation in the data. The current dataset includes summaries compiled from publc data in the PROMPT|GTFO Youtube channel and these recent conference abstracts:

2025 conferences: CAMLIS, Blackhat, DEFCON, BsidesLV, BSides SF. 2026 conferences: Unprompted.

- **Question** Answers questions using the pre-processed topic summaries from the conference list above. Summaries are also available for conferences and authors with multiple talks.
- **Query**  Runs deterministic annotation/database queries and does not call an LLM.
- **Status** checks the knowledge/index state in the SQLite data layer.

## Quickstart

### 1. Set up Python dependencies

Use a virtual environment if possible.

```powershell
python -m venv analyst
python -m pip install -r requirements.txt
```

### 2. Configure API keys

Create or update `.env` in the repo root.

```text
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
```

The active LLM provider and model names are configured in `config/llm.ini`.

### 3. Verify the database

The default database is:

```text
knowledge/knowledge.sqlite3
```

Run a quick search:

```powershell
python -m knowledge_indexing.knowledge_index --query "threat modeling" --limit 5
```

Audit imported source counts against local source artifacts:

```powershell
python tools\source_count_auditor.py --strict
```

## Common Workflows

### Ask questions

the_analyst is the primary interface. See [docs/analyst.md](docs/analyst.md) for its
tool routing, evidence rules, author behavior, configuration, and failure modes.

Interactive mode:

```powershell
python the_analyst.py
```

Ask one question from the command line:

```powershell
python the_analyst.py "question: How is threat modeling being done using AI?"
```

Use `question:` when the answer should come from generated summary files.
analyst routes these requests to up to three relevant summaries by default and
does not fill gaps with general knowledge. Use `query:` when you want
deterministic keyword search over record annotations.

```powershell
python the_analyst.py "query: cryptocurrency wallet fraud"
```

The QA agent should cite which summary files or annotation query results it used.

Analyst Jupyter notebook UI:

```text
the-analyst.ipynb
```

The analyst notebook exposes the constrained `question:` path, deterministic `query:`
path, and status check.

## Output Locations

Primary working data:

```text
knowledge/knowledge.sqlite3
```

Generated reports and summaries:

```text
summaries/
knowledge/open-topic-report.md
knowledge/exports/
```

Logs and status:

```text
knowledge/import.log
knowledge/classify-run.log
```

Prompt files:

```text
knowledge_agenting/prompts/
```

Topic summary design notes:

```text
docs/topic-summary-design.md
```

## Safety Checks

Before large write operations, make a SQLite backup:

```powershell
Copy-Item knowledge\knowledge.sqlite3 knowledge-backup-$(Get-Date -Format yyyyMMdd-HHmmss).sqlite3
```

Run read-only summary dry-runs before expensive LLM calls:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --topic "Threat modeling" --dry-run
```

Run focused tests after code changes:

```powershell
python -m pytest -q tests\test_topic_summarizer.py
python -m pytest -q tests\test_knowledge_qa.py
```

## Useful Review Commands

Count or inspect annotations:

```powershell
python -m knowledge_indexing.knowledge_index --latest-annotations --limit 20
python -m knowledge_indexing.knowledge_index --list-annotations --annotation-query "cryptocurrency" --limit 20
```

Inspect classifications:

```powershell
python -m knowledge_indexing.knowledge_index --list-classifications --limit 20
python -m knowledge_indexing.knowledge_index --low-confidence-classifications --limit 50
```

List records for a topic:

```powershell
python -m knowledge_indexing.knowledge_index --list-topic-records "Threat modeling" --limit 50
```


### Generate long-form summaries

Use the `knowledge_agenting.topic_summarizer` module for the current spec-compliant summary generator. It can summarize by topic, source, or author.

Dry run one topic without calling the LLM or writing artifacts:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --topic "Threat modeling" --dry-run
```

Write preflight prompt/audit/manifest artifacts during a dry-run:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --topic "Threat modeling" --dry-run --write-preflight-artifacts
```

Generate one topic summary:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --topic "Threat modeling"
```

Generate all topic summaries with parallel workers:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --all --parallel 4
```

List existing topic summaries:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --list-summaries
```

List topics that currently have classified records and can be summarized:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --list-topics
```

Generate source summaries:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by source --all --parallel 4
```

Generate author summaries for authors with at least two records:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by author --all --parallel 4
```

Generate only missing author summaries and leave existing author summaries untouched:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by author --all --skip-existing --parallel 4
```

List missing author summaries without generating or writing anything:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by author --all --list-missing
```

Author summaries use the `summarize_author` model from `config/llm.ini`.
Use `--min-records 1` explicitly to include single-record authors.
Coauthored records are included in each individual author's summary; comma, semicolon,
ampersand, and `and` separators are expanded during author grouping.

Individual authors are normalized in SQLite:

```text
authors             unique author names
author_records      author-to-record links
```

`records.author` retains the original imported author string for provenance.

Summary output files are written to:

```text
summaries/topics/*.md
summaries/sources/*.md
summaries/authors/*.md
```

Operational artifacts are kept separate:

```text
summaries/artifacts/topics/*
summaries/artifacts/sources/*
summaries/artifacts/authors/*
```

Artifacts include prompt inputs, audit JSON, manifest JSON, and archived prior outputs. Topic summaries are stored as Markdown files; SQLite does not store the summary bodies.
