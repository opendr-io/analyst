from pathlib import Path

from knowledge_indexing import knowledge_config as cfg
from knowledge_indexing.knowledge_db import open_db
from knowledge_indexing.knowledge_topics import seed_topics


def test_seed_topics_writes_loaded_seed_topic_file(tmp_path: Path):
    db_path = tmp_path / "knowledge.sqlite3"

    count = seed_topics(db_path)

    with open_db(db_path) as conn:
        rows = conn.execute("SELECT name, query, description FROM topics ORDER BY id").fetchall()

    assert count == len(cfg.SEED_TOPICS)
    assert [(row["name"], row["query"]) for row in rows] == cfg.SEED_TOPICS
    assert [(row["name"], row["description"]) for row in rows] == cfg.SEED_TOPICS
