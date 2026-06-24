from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any
from uuid import UUID

from sqlalchemy import text

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.infrastructure.database import db_session

DEFAULT_OUTPUT = ROOT / "data" / "seed" / "question_bank" / "current_question_bank_seed.json"
DEFAULT_REPORT = ROOT / "data" / "seed" / "import_reports" / "current_question_bank_seed_export_report.json"


def _json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, list | tuple):
        return [_json_ready(item) for item in value]
    if isinstance(value, datetime | date):
        return value.isoformat()
    if isinstance(value, Decimal):
        as_float = float(value)
        return int(as_float) if as_float.is_integer() else as_float
    if isinstance(value, UUID):
        return str(value)
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _question_payload(row: dict[str, Any]) -> dict[str, Any]:
    metadata = dict(row.get("metadata") or {})
    primary_point_node_ids = list(row.get("primary_point_node_ids") or [])
    primary_canonical_point_ids = list(row.get("primary_canonical_point_ids") or [])
    source_placement_node_ids = list(row.get("source_placement_node_ids") or [])
    if primary_point_node_ids:
        metadata["primary_point_node_ids"] = primary_point_node_ids
    if primary_canonical_point_ids:
        metadata["primary_canonical_point_ids"] = primary_canonical_point_ids
    if source_placement_node_ids:
        metadata["source_placement_node_ids"] = source_placement_node_ids
    return _json_ready(
        {
            "question_id": row["question_id"],
            "bank_id": row["bank_id"],
            "experiment_id": row["experiment_id"],
            "experiment_code": row["experiment_code"],
            "experiment_title": row["experiment_title"],
            "bank_kind": row["bank_kind"],
            "bank_status": row["bank_status"],
            "question_type": row["question_type"],
            "stem": row["stem"],
            "options": row.get("options") or [],
            "answer": row.get("answer") or {},
            "explanation": row.get("explanation"),
            "difficulty": row.get("difficulty") or "basic",
            "related_chapter_ids": list(row.get("related_chapter_ids") or []),
            "related_knowledge_point_ids": list(row.get("related_knowledge_point_ids") or []),
            "source_chunk_ids": list(row.get("source_chunk_ids") or []),
            "source_refs": row.get("source_refs") or [],
            "primary_point_node_ids": primary_point_node_ids,
            "primary_canonical_point_ids": primary_canonical_point_ids,
            "source_placement_node_ids": source_placement_node_ids,
            "status": row["question_status"],
            "metadata": metadata,
        }
    )


def _load_questions(*, status_filter: str | None, bank_kind: str | None) -> list[dict[str, Any]]:
    where = ["q.bank_id IS NOT NULL"]
    params: dict[str, Any] = {}
    if status_filter:
        where.append("q.status = :status_filter")
        params["status_filter"] = status_filter
    if bank_kind:
        where.append("b.bank_kind = :bank_kind")
        params["bank_kind"] = bank_kind
    with db_session() as session:
        rows = session.execute(
            text(
                f"""
                SELECT q.id::text AS question_id,
                       q.bank_id::text AS bank_id,
                       q.experiment_id,
                       fe.code AS experiment_code,
                       fe.title AS experiment_title,
                       b.bank_kind,
                       b.status AS bank_status,
                       q.question_type,
                       q.stem,
                       q.options,
                       q.answer,
                       q.explanation,
                       q.difficulty,
                       q.related_chapter_ids,
                       q.related_knowledge_point_ids,
                       q.source_chunk_ids,
                       q.source_refs,
                       q.primary_point_node_ids,
                       q.primary_canonical_point_ids,
                       q.source_placement_node_ids,
                       q.status AS question_status,
                       q.metadata,
                       fe.display_order,
                       q.created_at,
                       q.updated_at
                FROM experiment_questions q
                JOIN experiment_question_banks b ON b.id = q.bank_id
                JOIN formal_experiments fe ON fe.id = q.experiment_id
                WHERE {" AND ".join(where)}
                ORDER BY fe.display_order NULLS LAST,
                         fe.code,
                         q.question_type,
                         q.created_at,
                         q.id
                """
            ),
            params,
        ).mappings()
        return [_question_payload(dict(row)) for row in rows]


def _group_experiments(questions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for question in questions:
        experiment_id = str(question["experiment_id"])
        experiment = grouped.setdefault(
            experiment_id,
            {
                "experiment_id": experiment_id,
                "experiment_code": question.get("experiment_code"),
                "experiment_title": question.get("experiment_title"),
                "bank_kind": question.get("bank_kind"),
                "bank_status": question.get("bank_status"),
                "question_count": 0,
                "question_type_counts": {},
            },
        )
        experiment["question_count"] += 1
        question_type = str(question.get("question_type") or "")
        experiment["question_type_counts"][question_type] = int(experiment["question_type_counts"].get(question_type) or 0) + 1
    return list(grouped.values())


def _summary(questions: list[dict[str, Any]], experiments: list[dict[str, Any]]) -> dict[str, Any]:
    by_type = Counter(str(question.get("question_type") or "") for question in questions)
    by_status = Counter(str(question.get("status") or "") for question in questions)
    by_bank_kind = Counter(str(question.get("bank_kind") or "") for question in questions)
    by_chapter = Counter(
        chapter_id
        for question in questions
        for chapter_id in [str(item) for item in question.get("related_chapter_ids") or [] if str(item).strip()]
    )
    return {
        "experiment_count": len(experiments),
        "question_count": len(questions),
        "question_type_counts": dict(sorted(by_type.items())),
        "question_status_counts": dict(sorted(by_status.items())),
        "bank_kind_counts": dict(sorted(by_bank_kind.items())),
        "chapter_counts": dict(sorted(by_chapter.items())),
        "questions_with_primary_point_nodes": sum(1 for question in questions if question.get("primary_point_node_ids")),
        "questions_with_canonical_points": sum(1 for question in questions if question.get("primary_canonical_point_ids")),
        "questions_with_source_refs": sum(1 for question in questions if question.get("source_refs")),
    }


def build_seed(*, status_filter: str | None, bank_kind: str | None) -> dict[str, Any]:
    questions = _load_questions(status_filter=status_filter, bank_kind=bank_kind)
    experiments = _group_experiments(questions)
    return {
        "metadata": {
            "artifact_type": "current_question_bank_seed",
            "version": "current-question-bank-seed-v1",
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "source": "experiment_question_banks + experiment_questions",
            "status_filter": status_filter,
            "bank_kind_filter": bank_kind,
            "import_note": "The top-level questions array is accepted by the teacher question-bank import API.",
            "summary": _summary(questions, experiments),
        },
        "questions": questions,
        "experiments": experiments,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the current DB question bank as production seed data.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--status", default="published", help="Question status filter. Use empty string to export all statuses.")
    parser.add_argument("--bank-kind", default="generated", help="Bank kind filter. Use empty string to export all bank kinds.")
    args = parser.parse_args()

    status_filter = args.status.strip() or None
    bank_kind = args.bank_kind.strip() or None
    seed = build_seed(status_filter=status_filter, bank_kind=bank_kind)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "ok": True,
        "seed_path": args.output.relative_to(ROOT).as_posix() if args.output.is_relative_to(ROOT) else str(args.output),
        "seed_sha256": _sha256(args.output),
        **seed["metadata"]["summary"],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write((json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
