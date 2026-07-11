# Data Flow

The Analyst is a research and analysis pipeline built around an existing SQLite knowledge base. Source scraping, collection, and ingestion are outside this project. Nothing annotates, classifies, or summarizes records automatically.

```mermaid
flowchart TD
    USER([User])

    subgraph indexing["knowledge_indexing"]
        SEARCH[FTS and structured database queries]
        REVIEW[Review records, annotations, and classifications]
    end

    subgraph database["knowledge/knowledge.sqlite3"]
        RECORDS[(records)]
        AUTHORS[(authors)]
        AUTHOR_RECORDS[(author_records)]
        ANNOTATIONS[(record_annotations)]
        CLASSIFICATIONS[(record_classifications)]
        TOPICS[(topics)]
        ERRORS[(annotation and classification errors)]
    end

    subgraph agents["knowledge_agenting"]
        AGENT_CLI["python -m knowledge_agenting.knowledge_agent"]
        ANNOTATE[Annotate records]
        CLASSIFY[Classify records]
        TOPIC_SUMMARIZER["python -m knowledge_agenting.topic_summarizer"]
    end

    subgraph outputs["Filesystem Outputs"]
        TOPIC_MD["summaries/topics/*.md"]
        SOURCE_MD["summaries/sources/*.md"]
        AUTHOR_MD["summaries/authors/*.md"]
        ARTIFACTS["summaries/artifacts/{topics,sources,authors}/*.json and *.md"]
    end

    ANALYST[anayst.py]
    ANSWER([Answer])

    RECORDS --> ANNOTATE
    AGENT_CLI --> ANNOTATE
    ANNOTATE --> ANNOTATIONS
    ANNOTATE --> ERRORS

    RECORDS --> CLASSIFY
    ANNOTATIONS --> CLASSIFY
    TOPICS --> CLASSIFY
    AGENT_CLI --> CLASSIFY
    CLASSIFY --> CLASSIFICATIONS
    CLASSIFY --> RECORDS
    CLASSIFY --> ERRORS

    RECORDS --> TOPIC_SUMMARIZER
    CLASSIFICATIONS --> TOPIC_SUMMARIZER
    TOPICS --> TOPIC_SUMMARIZER
    AUTHORS --> TOPIC_SUMMARIZER
    AUTHOR_RECORDS --> TOPIC_SUMMARIZER
    TOPIC_SUMMARIZER --> TOPIC_MD
    TOPIC_SUMMARIZER --> SOURCE_MD
    TOPIC_SUMMARIZER --> AUTHOR_MD
    TOPIC_SUMMARIZER --> ARTIFACTS

    USER --> ANALYST
    ANALYST --> SEARCH
    SEARCH --> RECORDS
    REVIEW --> RECORDS
    REVIEW --> ANNOTATIONS
    REVIEW --> CLASSIFICATIONS
    ANALYST --> ANNOTATIONS
    ANALYST --> TOPIC_MD
    ANALYST --> SOURCE_MD
    ANALYST --> AUTHOR_MD
    ANALYST --> ANSWER
```





## Project Boundary

The pipeline begins with:

```text
knowledge/knowledge.sqlite3
```

How source material is scraped, collected, transformed, or inserted into that
database is not part of this project. Within the database, `records.author`
retains source provenance while `authors` and `author_records` provide normalized
individual-author relationships.

## Enrichment

Annotation and classification are separate manual operations:

```powershell
python -m knowledge_agenting.knowledge_agent annotate
python -m knowledge_agenting.knowledge_agent classify
```

Annotation writes compact structured evidence to `record_annotations`.
Classification reads records, annotations, and the curated `topics` table, then
writes `record_classifications` and `records.agent_topics`. Failed calls are
recorded in durable error tables. Database changes do not trigger
classification.

## Summaries

Grouped summaries are generated manually:

```powershell
python -m knowledge_agenting.topic_summarizer --group-by topic --all
python -m knowledge_agenting.topic_summarizer --group-by source --all
python -m knowledge_agenting.topic_summarizer --group-by author --all
```

Topic summaries include records where the topic is primary or secondary. Source
summaries include every record from that source. Author summaries use normalized
author links and default to authors with at least two records.

Summary bodies are Markdown files, not SQLite rows. Prompt inputs, audits,
manifests, and archived prior runs are stored under
`summaries/artifacts/<group>/`.

## Questions

Run Analyst with:

```powershell
python the_analyst.py
```

Analyst routes requests to raw record search, structured annotation queries, topic/source/author summary files, or exact author evidence. Multi-record authors use their generated author summary; a single-record author returns the complete underlying record.