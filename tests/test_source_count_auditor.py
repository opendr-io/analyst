import json
import sqlite3
from pathlib import Path

from tools import source_count_auditor as auditor


def _make_db(path: Path, sources: list[str]) -> None:
    with sqlite3.connect(path) as conn:
        conn.execute("CREATE TABLE records (id INTEGER PRIMARY KEY, source TEXT)")
        for source in sources:
            conn.execute("INSERT INTO records(source) VALUES (?)", (source,))
        conn.commit()


def test_audit_sources_reports_ok_for_matching_json_export(tmp_path, monkeypatch):
    export_dir = tmp_path / "exports"
    export_dir.mkdir()
    export = export_dir / "bsideslv-talks-20260101T000000Z.json"
    export.write_text(
        json.dumps(
            {
                "talks": [
                    {
                        "event": "BSidesLV 2025",
                        "year": 2025,
                        "session_id": "A1",
                        "title": "First Talk",
                        "speakers": "Speaker One",
                        "abstract": "A real talk abstract with enough useful detail.",
                        "url": "https://archive.bsideslv.org/2025/talks#first",
                    },
                    {
                        "event": "BSidesLV 2025",
                        "year": 2025,
                        "session_id": "A2",
                        "title": "Second Talk",
                        "speakers": "Speaker Two",
                        "abstract": "Another real talk abstract with enough useful detail.",
                        "url": "https://archive.bsideslv.org/2025/talks#second",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    db_path = tmp_path / "knowledge.sqlite3"
    _make_db(db_path, ["bsideslv", "bsideslv"])
    monkeypatch.setattr(
        auditor,
        "SOURCE_SPECS",
        [auditor.SourceSpec("bsideslv", auditor.latest("exports/bsideslv-talks-*.json"))],
    )

    rows = auditor.audit_sources(root=tmp_path, db_path=db_path)

    assert rows[0].source == "bsideslv"
    assert rows[0].db_count == 2
    assert rows[0].expected_count == 2
    assert rows[0].raw_count == 2
    assert rows[0].status == "ok"


def test_audit_sources_reports_mismatch(tmp_path, monkeypatch):
    export_dir = tmp_path / "exports"
    export_dir.mkdir()
    export = export_dir / "unprompted2026_latest.json"
    export.write_text(
        json.dumps(
            {
                "playlist": "example",
                "records": [
                    {
                        "id": "one",
                        "talk_title": "First",
                        "speakers": "Speaker One",
                        "abstract": "A substantial video abstract about AI security.",
                        "url": "https://www.youtube.com/watch?v=one",
                    },
                    {
                        "id": "two",
                        "talk_title": "Second",
                        "speakers": "Speaker Two",
                        "abstract": "Another substantial video abstract about AI security.",
                        "url": "https://www.youtube.com/watch?v=two",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    db_path = tmp_path / "knowledge.sqlite3"
    _make_db(db_path, ["unprompted2026"])
    monkeypatch.setattr(
        auditor,
        "SOURCE_SPECS",
        [auditor.SourceSpec("unprompted2026", auditor.fixed("exports/unprompted2026_latest.json"))],
    )

    rows = auditor.audit_sources(root=tmp_path, db_path=db_path)

    assert rows[0].db_count == 1
    assert rows[0].expected_count == 2
    assert rows[0].status == "mismatch"


def test_format_table_includes_status_and_artifact():
    table = auditor.format_table(
        [
            auditor.AuditRow(
                source="bsideslv",
                db_count=200,
                expected_count=200,
                raw_count=200,
                status="ok",
                path="exports/bsideslv.json",
                note="parser unique dedupe count",
            )
        ]
    )

    assert "bsideslv" in table
    assert "ok" in table
    assert "exports/bsideslv.json" in table