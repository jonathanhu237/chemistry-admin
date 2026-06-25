from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from sqlalchemy import text

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.infrastructure.database import db_session

EXPECTED_SOURCE_DOCUMENTS = 2
EXPECTED_SOURCE_CHUNKS = 3637


def _scalar(session: Any, sql: str) -> int:
    return int(session.execute(text(sql)).scalar_one() or 0)


def verify() -> dict[str, Any]:
    with db_session() as session:
        counts = {
            "source_documents": _scalar(session, "SELECT COUNT(*) FROM source_documents"),
            "source_chunks": _scalar(session, "SELECT COUNT(*) FROM source_chunks"),
            "optional_chunk_embeddings": _scalar(session, "SELECT COUNT(*) FROM chunk_embeddings"),
            "legacy_links": _scalar(session, "SELECT COUNT(*) FROM links"),
            "legacy_questions": _scalar(session, "SELECT COUNT(*) FROM questions"),
            "legacy_resources": _scalar(session, "SELECT COUNT(*) FROM resources"),
            "formal_experiments": _scalar(session, "SELECT COUNT(*) FROM formal_experiments WHERE status <> 'archived'"),
            "experiment_question_banks": _scalar(session, "SELECT COUNT(*) FROM experiment_question_banks"),
            "experiment_questions": _scalar(session, "SELECT COUNT(*) FROM experiment_questions"),
        }
        checks = {
            "old_chunk_ids": _scalar(session, "SELECT COUNT(*) FROM source_chunks WHERE id LIKE 'CHK_DOC_%'"),
            "old_courseware_documents": _scalar(session, "SELECT COUNT(*) FROM source_documents WHERE id LIKE 'DOC_CH%'"),
            "canonical_chunks": _scalar(
                session,
                "SELECT COUNT(*) FROM source_chunks WHERE metadata->>'source_role' = 'canonical_textbook'",
            ),
            "questions_without_source_refs": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions
                WHERE cardinality(source_chunk_ids) > 0
                  AND jsonb_array_length(source_refs) = 0
                """,
            ),
            "questions_with_missing_chunks": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions q
                WHERE EXISTS (
                  SELECT 1
                  FROM unnest(q.source_chunk_ids) AS cid
                  WHERE NOT EXISTS (
                    SELECT 1
                    FROM source_chunks sc
                    WHERE sc.id = cid
                      AND sc.metadata->>'source_role' = 'canonical_textbook'
                  )
                )
                """,
            ),
            "question_banks_without_experiment": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_question_banks
                WHERE experiment_id IS NULL OR btrim(experiment_id) = ''
                """,
            ),
            "questions_without_experiment": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions
                WHERE experiment_id IS NULL OR btrim(experiment_id) = ''
                """,
            ),
            "questions_without_bank": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions q
                WHERE q.bank_id IS NULL
                  OR NOT EXISTS (
                    SELECT 1
                    FROM experiment_question_banks b
                    WHERE b.id = q.bank_id
                  )
                """,
            ),
            "questions_without_point_nodes": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions
                WHERE COALESCE(array_length(primary_point_node_ids, 1), 0) = 0
                """,
            ),
            "questions_without_canonical_points": _scalar(
                session,
                """
                SELECT COUNT(*)
                FROM experiment_questions
                WHERE COALESCE(array_length(primary_canonical_point_ids, 1), 0) = 0
                """,
            ),
            "questions_with_missing_point_nodes": _scalar(
                session,
                """
                WITH refs AS (
                  SELECT q.id AS question_id, unnest(q.primary_point_node_ids) AS node_id
                  FROM experiment_questions q
                  WHERE q.primary_point_node_ids IS NOT NULL
                )
                SELECT COUNT(*)
                FROM refs
                LEFT JOIN experiment_catalog_nodes n ON n.id = refs.node_id
                WHERE n.id IS NULL
                """,
            ),
            "questions_with_missing_canonical_points": _scalar(
                session,
                """
                WITH refs AS (
                  SELECT q.id AS question_id, unnest(q.primary_canonical_point_ids) AS canonical_point_id
                  FROM experiment_questions q
                  WHERE q.primary_canonical_point_ids IS NOT NULL
                )
                SELECT COUNT(*)
                FROM refs
                LEFT JOIN experiment_catalog_points p ON p.id = refs.canonical_point_id
                WHERE p.id IS NULL
                """,
            ),
        }

    errors: list[str] = []
    expected_counts = {
        "source_documents": EXPECTED_SOURCE_DOCUMENTS,
        "source_chunks": EXPECTED_SOURCE_CHUNKS,
        "legacy_links": 0,
        "legacy_questions": 0,
        "legacy_resources": 0,
    }
    for key, expected in expected_counts.items():
        actual = counts.get(key)
        if actual != expected:
            errors.append(f"{key}: expected {expected}, got {actual}")
    for key in [
        "old_chunk_ids",
        "old_courseware_documents",
        "questions_without_source_refs",
        "questions_with_missing_chunks",
        "question_banks_without_experiment",
        "questions_without_experiment",
        "questions_without_bank",
        "questions_without_point_nodes",
        "questions_without_canonical_points",
        "questions_with_missing_point_nodes",
        "questions_with_missing_canonical_points",
    ]:
        if checks[key] != 0:
            errors.append(f"{key}: expected 0, got {checks[key]}")
    if checks["canonical_chunks"] != EXPECTED_SOURCE_CHUNKS:
        errors.append(f"canonical_chunks: expected {EXPECTED_SOURCE_CHUNKS}, got {checks['canonical_chunks']}")

    return {
        "ok": not errors,
        "errors": errors,
        "counts": counts,
        "checks": checks,
    }


def main() -> None:
    result = verify()
    sys.stdout.buffer.write((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    if not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
