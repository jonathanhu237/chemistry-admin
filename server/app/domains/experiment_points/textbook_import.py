from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.app.domains.experiment_points.canonical_points import candidate_point_key
from server.app.infrastructure.database import db_session


POINT_MARKER_RE = re.compile(r"[（(](?:点位|重复点位\s*\d+)[）)]")
HEADING_NUMBER_RE = re.compile(r"^\s*\d+[.、]\s*")
CHAPTER_NUMBER_RE = re.compile(r"第\s*(\d+)\s*章")
CHEM_NUMBER_TRANSLATION = str.maketrans(
    {
        "₀": "0",
        "₁": "1",
        "₂": "2",
        "₃": "3",
        "₄": "4",
        "₅": "5",
        "₆": "6",
        "₇": "7",
        "₈": "8",
        "₉": "9",
        "⁰": "0",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁷": "7",
        "⁸": "8",
        "⁹": "9",
        "⁺": "+",
        "⁻": "-",
        "₊": "+",
        "₋": "-",
    }
)


@dataclass(frozen=True)
class CatalogExperimentNode:
    chapter: str
    title: str
    line: int
    source_order: int


@dataclass(frozen=True)
class CatalogPointNode:
    chapter: str
    experiment: str
    folder_path: tuple[str, ...]
    title: str
    original_title: str
    line: int
    source_order: int
    experiment_point_order: int
    duplicate_ordinal: int

    @property
    def path_parts(self) -> tuple[str, ...]:
        return (self.chapter, self.experiment, *self.folder_path, self.title)


@dataclass(frozen=True)
class PointDescriptionNode:
    chapter: str
    experiment: str
    folder_path: tuple[str, ...]
    title: str
    original_title: str
    line: int
    source_order: int
    duplicate_ordinal: int
    principle: str
    phenomenon: str
    safety: str
    directory_path: tuple[str, ...]


@dataclass
class CatalogParseResult:
    experiments: list[CatalogExperimentNode] = field(default_factory=list)
    points: list[CatalogPointNode] = field(default_factory=list)


def normalize_import_text(value: str) -> str:
    normalized = str(value or "").translate(CHEM_NUMBER_TRANSLATION)
    normalized = unicodedata.normalize("NFKC", normalized)
    normalized = normalized.replace("（点位）", "")
    normalized = POINT_MARKER_RE.sub("", normalized)
    normalized = HEADING_NUMBER_RE.sub("", normalized)
    normalized = re.sub(r"\s+", "", normalized)
    normalized = normalized.replace("，", ",").replace("：", ":").replace("｜", "|")
    return normalized.strip().lower()


def clean_point_title(value: str) -> str:
    cleaned = str(value or "").translate(CHEM_NUMBER_TRANSLATION)
    cleaned = unicodedata.normalize("NFKC", cleaned).strip()
    cleaned = POINT_MARKER_RE.sub("", cleaned)
    cleaned = HEADING_NUMBER_RE.sub("", cleaned)
    return cleaned.strip()


def _content_hash(*parts: str) -> str:
    payload = "\n---\n".join(parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _chapter_id(chapter: str) -> str:
    match = CHAPTER_NUMBER_RE.search(chapter)
    return f"CH{match.group(1)}" if match else ""


def _source_digest(*parts: str) -> str:
    return hashlib.sha1("||".join(parts).encode("utf-8")).hexdigest()[:12].upper()


def parse_experiment_catalog_markdown(path: str | Path) -> CatalogParseResult:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    current_chapter = ""
    current_experiment = ""
    experiments: list[CatalogExperimentNode] = []
    bullets: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines, 1):
        if line.startswith("# "):
            current_chapter = line[2:].strip()
            current_experiment = ""
            continue
        if line.startswith("## "):
            current_experiment = line[3:].strip()
            if current_chapter and current_experiment:
                experiments.append(
                    CatalogExperimentNode(
                        chapter=current_chapter,
                        title=current_experiment,
                        line=line_number,
                        source_order=len(experiments) + 1,
                    )
                )
            continue
        if not line.lstrip().startswith("- ") or not current_chapter or not current_experiment:
            continue
        bullets.append(
            {
                "line": line_number,
                "chapter": current_chapter,
                "experiment": current_experiment,
                "indent": len(line) - len(line.lstrip(" ")),
                "text": line.lstrip()[2:].strip(),
            }
        )

    points: list[CatalogPointNode] = []
    folder_stack: list[dict[str, Any]] = []
    per_experiment_order: dict[tuple[str, str], int] = {}
    duplicate_counts: dict[tuple[str, str, str], int] = {}
    for index, bullet in enumerate(bullets):
        while folder_stack and int(folder_stack[-1]["indent"]) >= int(bullet["indent"]):
            folder_stack.pop()
        next_bullet = bullets[index + 1] if index + 1 < len(bullets) else None
        is_leaf = not (next_bullet and int(next_bullet["indent"]) > int(bullet["indent"]))
        if not is_leaf:
            folder_stack.append(bullet)
            continue
        experiment_key = (bullet["chapter"], bullet["experiment"])
        point_order = per_experiment_order.get(experiment_key, 0) + 1
        per_experiment_order[experiment_key] = point_order
        title = clean_point_title(str(bullet["text"]))
        duplicate_key = (bullet["chapter"], bullet["experiment"], normalize_import_text(title))
        duplicate_ordinal = duplicate_counts.get(duplicate_key, 0) + 1
        duplicate_counts[duplicate_key] = duplicate_ordinal
        points.append(
            CatalogPointNode(
                chapter=str(bullet["chapter"]),
                experiment=str(bullet["experiment"]),
                folder_path=tuple(clean_point_title(str(item["text"])) for item in folder_stack),
                title=title,
                original_title=str(bullet["text"]),
                line=int(bullet["line"]),
                source_order=len(points) + 1,
                experiment_point_order=point_order,
                duplicate_ordinal=duplicate_ordinal,
            )
        )
    return CatalogParseResult(experiments=experiments, points=points)


def _extract_labeled_section(block: str, label: str, next_labels: tuple[str, ...]) -> str:
    start = block.find(label)
    if start < 0:
        return ""
    start += len(label)
    end_positions = [block.find(next_label, start) for next_label in next_labels]
    end_positions = [position for position in end_positions if position >= 0]
    end = min(end_positions) if end_positions else len(block)
    return block[start:end].strip()


def _parse_directory_path(block: str) -> tuple[str, ...]:
    match = re.search(r"\*\*目录路径：\*\*\s*(.+)", block)
    if not match:
        return ()
    raw_path = match.group(1).strip()
    return tuple(clean_point_title(part) for part in raw_path.split("/") if clean_point_title(part))


def parse_point_description_markdown(path: str | Path) -> list[PointDescriptionNode]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    headings: list[tuple[int, int, str]] = []
    for line_number, line in enumerate(lines, 1):
        if not line.startswith("#"):
            continue
        match = re.match(r"^(#{2,4})\s+(.+)$", line)
        if match:
            headings.append((line_number, len(match.group(1)), match.group(2).strip()))
    descriptions: list[PointDescriptionNode] = []
    current_chapter = ""
    current_experiment = ""
    duplicate_counts: dict[tuple[str, str, str], int] = {}
    for index, (line_number, level, title) in enumerate(headings):
        next_line = headings[index + 1][0] if index + 1 < len(headings) else len(lines) + 1
        if level == 2:
            current_chapter = title
            current_experiment = ""
            continue
        if level == 3:
            current_experiment = title
            continue
        if level != 4 or not current_chapter or not current_experiment:
            continue
        block = "\n".join(lines[line_number: next_line - 1])
        directory_path = _parse_directory_path(block)
        point_title = clean_point_title(title)
        folder_path: tuple[str, ...] = ()
        duplicate_key = (current_chapter, current_experiment, normalize_import_text(point_title))
        duplicate_ordinal = duplicate_counts.get(duplicate_key, 0) + 1
        duplicate_counts[duplicate_key] = duplicate_ordinal
        descriptions.append(
            PointDescriptionNode(
                chapter=current_chapter,
                experiment=current_experiment,
                folder_path=folder_path,
                title=point_title,
                original_title=title,
                line=line_number,
                source_order=len(descriptions) + 1,
                duplicate_ordinal=duplicate_ordinal,
                principle=_extract_labeled_section(block, "实验原理：", ("现象解释：", "安全提示：")),
                phenomenon=_extract_labeled_section(block, "现象解释：", ("安全提示：",)),
                safety=_extract_labeled_section(block, "安全提示：", ()),
                directory_path=directory_path,
            )
        )
    return descriptions


def _json(value: Any) -> str:
    return json.dumps(value if value is not None else {}, ensure_ascii=False, default=str)


def _load_existing_experiments(session: Any) -> dict[str, dict[str, Any]]:
    rows = session.execute(
        text("SELECT id, code, title, metadata FROM formal_experiments WHERE status <> 'archived'")
    ).mappings().all()
    by_key: dict[str, dict[str, Any]] = {}
    for row in rows:
        by_key[normalize_import_text(str(row["title"]))] = dict(row)
    return by_key


def _table_exists(session: Any, table_name: str) -> bool:
    try:
        return bool(session.execute(text("SELECT to_regclass(:table_name)"), {"table_name": f"public.{table_name}"}).scalar_one())
    except SQLAlchemyError:
        return False


def _create_experiment(session: Any, experiment: CatalogExperimentNode, *, dry_run: bool) -> dict[str, Any]:
    digest = _source_digest(experiment.chapter, experiment.title)
    experiment_id = f"EXP_TB_{digest}"
    code = f"TB-{digest[:8]}"
    metadata = {
        "custom": True,
        "source": "textbook_experiment_catalog_import",
        "source_chapter": experiment.chapter,
        "source_title": experiment.title,
        "source_line": experiment.line,
    }
    if dry_run:
        return {"id": experiment_id, "code": code, "title": experiment.title, "metadata": metadata}
    display_order = int(session.execute(text("SELECT COALESCE(MAX(display_order), 0) + 1 FROM formal_experiments")).scalar_one())
    session.execute(
        text(
            """
            INSERT INTO formal_experiments (
              id, code, title, title_en, summary, status, display_order,
              source_refs, metadata, published_at, updated_at
            )
            VALUES (
              :id, :code, :title, NULL, :summary, 'draft', :display_order,
              '[]'::jsonb, CAST(:metadata AS jsonb), NULL, now()
            )
            ON CONFLICT (id) DO UPDATE SET
              title = EXCLUDED.title,
              summary = EXCLUDED.summary,
              metadata = formal_experiments.metadata || EXCLUDED.metadata,
              updated_at = now()
            """
        ),
        {
            "id": experiment_id,
            "code": code,
            "title": experiment.title,
            "summary": f"{experiment.chapter} / {experiment.title}",
            "display_order": display_order,
            "metadata": _json(metadata),
        },
    )
    chapter_id = _chapter_id(experiment.chapter)
    if chapter_id:
        session.execute(
            text(
                """
                INSERT INTO experiment_chapter_bindings (experiment_id, chapter_id, coverage_type, sort_order)
                SELECT :experiment_id, :chapter_id, 'primary', 1
                WHERE EXISTS (SELECT 1 FROM chapters WHERE id = :chapter_id)
                ON CONFLICT (experiment_id, chapter_id) DO UPDATE SET
                  coverage_type = EXCLUDED.coverage_type,
                  updated_at = now()
                """
            ),
            {"experiment_id": experiment_id, "chapter_id": chapter_id},
        )
    return {"id": experiment_id, "code": code, "title": experiment.title, "metadata": metadata}


def _load_points(session: Any, experiment_id: str) -> list[dict[str, Any]]:
    return [
        dict(row)
        for row in session.execute(
            text(
                """
                SELECT experiment_id, point_key, point_title, display_order, source, metadata
                FROM experiment_video_points
                WHERE experiment_id = :experiment_id AND status = 'active'
                ORDER BY display_order, point_key
                """
            ),
            {"experiment_id": experiment_id},
        ).mappings().all()
    ]


def _match_point(existing_points: list[dict[str, Any]], point: CatalogPointNode) -> dict[str, Any] | None:
    normalized_title = normalize_import_text(point.title)
    same_title = [row for row in existing_points if normalize_import_text(str(row.get("point_title") or "")) == normalized_title]
    path_text = " / ".join(point.folder_path)
    if path_text:
        for row in same_title:
            metadata = row.get("metadata") if isinstance(row.get("metadata"), dict) else {}
            if (
                normalize_import_text(str(metadata.get("textbook_folder_path") or "")) == normalize_import_text(path_text)
                and int(metadata.get("duplicate_ordinal") or point.duplicate_ordinal) == point.duplicate_ordinal
            ):
                return row
    for row in same_title:
        metadata = row.get("metadata") if isinstance(row.get("metadata"), dict) else {}
        if metadata.get("duplicate_ordinal") and int(metadata.get("duplicate_ordinal") or 0) == point.duplicate_ordinal:
            return row
    if point.duplicate_ordinal > 1:
        return None
    if len(same_title) == 1:
        return same_title[0]
    return None


def _create_point(session: Any, experiment_id: str, point: CatalogPointNode, *, dry_run: bool) -> dict[str, Any]:
    point_key = candidate_point_key(point.experiment_point_order - 1, point.title)
    metadata = {
        "source": "textbook_experiment_catalog_import",
        "textbook_chapter": point.chapter,
        "textbook_experiment": point.experiment,
        "textbook_folder_path": " / ".join(point.folder_path),
        "textbook_path": " / ".join(point.path_parts),
        "source_line": point.line,
        "source_order": point.source_order,
        "duplicate_ordinal": point.duplicate_ordinal,
        "original_title": point.original_title,
    }
    row = {
        "experiment_id": experiment_id,
        "point_key": point_key,
        "point_title": point.title,
        "display_order": point.experiment_point_order,
        "source": "manual",
        "metadata": metadata,
    }
    if dry_run:
        return row
    session.execute(
        text(
            """
            INSERT INTO experiment_video_points (
              experiment_id, point_key, point_title, display_order, source, status, metadata, updated_at
            )
            VALUES (
              :experiment_id, :point_key, :point_title, :display_order, 'manual', 'active',
              CAST(:metadata AS jsonb), now()
            )
            ON CONFLICT (experiment_id, point_key) DO UPDATE SET
              point_title = EXCLUDED.point_title,
              display_order = LEAST(experiment_video_points.display_order, EXCLUDED.display_order),
              metadata = experiment_video_points.metadata || EXCLUDED.metadata,
              updated_at = now()
            """
        ),
        {
            "experiment_id": experiment_id,
            "point_key": point_key,
            "point_title": point.title,
            "display_order": point.experiment_point_order,
            "metadata": _json(metadata),
        },
    )
    return row


def import_textbook_experiment_catalog(
    *,
    catalog_path: str | Path,
    description_path: str | Path | None = None,
    dry_run: bool = True,
    user_id: str | None = None,
) -> dict[str, Any]:
    catalog = parse_experiment_catalog_markdown(catalog_path)
    descriptions = parse_point_description_markdown(description_path) if description_path else []
    description_lookup = {
        (
            normalize_import_text(item.chapter),
            normalize_import_text(item.experiment),
            normalize_import_text(item.title),
            item.duplicate_ordinal,
        ): item
        for item in descriptions
    }
    report: dict[str, Any] = {
        "dry_run": dry_run,
        "catalog_path": str(catalog_path),
        "description_path": str(description_path) if description_path else "",
        "catalog_experiments": len(catalog.experiments),
        "catalog_points": len(catalog.points),
        "description_points": len(descriptions),
        "matched_experiments": 0,
        "created_experiments": 0,
        "matched_points": 0,
        "created_points": 0,
        "updated_descriptions": 0,
        "unresolved_descriptions": [],
        "duplicates": [],
        "applied_at": datetime.now(timezone.utc).isoformat() if not dry_run else None,
    }
    duplicate_tracker: dict[tuple[str, str, str], int] = {}
    for point in catalog.points:
        key = (point.chapter, point.experiment, normalize_import_text(point.title))
        duplicate_tracker[key] = duplicate_tracker.get(key, 0) + 1
    report["duplicates"] = [
        {"chapter": chapter, "experiment": experiment, "title": title, "count": count}
        for (chapter, experiment, title), count in duplicate_tracker.items()
        if count > 1
    ]
    with db_session() as session:
        point_table_exists = _table_exists(session, "experiment_video_points")
        content_table_exists = _table_exists(session, "experiment_point_learning_content")
        report["missing_tables"] = [
            table
            for table, exists in {
                "experiment_video_points": point_table_exists,
                "experiment_point_learning_content": content_table_exists,
            }.items()
            if not exists
        ]
        if report["missing_tables"] and not dry_run:
            raise RuntimeError(f"Required tables are missing: {', '.join(report['missing_tables'])}")
        existing_experiments = _load_existing_experiments(session)
        experiment_rows: dict[tuple[str, str], dict[str, Any]] = {}
        for experiment in catalog.experiments:
            key = normalize_import_text(experiment.title)
            existing = existing_experiments.get(key)
            if existing:
                report["matched_experiments"] += 1
                row = existing
            else:
                report["created_experiments"] += 1
                row = _create_experiment(session, experiment, dry_run=dry_run)
                existing_experiments[key] = row
            experiment_rows[(experiment.chapter, experiment.title)] = row

        point_rows_by_description_key: dict[tuple[str, str, str, int], dict[str, Any]] = {}
        existing_points_cache: dict[str, list[dict[str, Any]]] = {}
        for point in catalog.points:
            experiment = experiment_rows.get((point.chapter, point.experiment))
            if not experiment:
                continue
            experiment_id = str(experiment["id"])
            existing_points = existing_points_cache.setdefault(
                experiment_id,
                _load_points(session, experiment_id) if point_table_exists else [],
            )
            matched = _match_point(existing_points, point)
            if matched:
                report["matched_points"] += 1
                point_row = matched
            else:
                report["created_points"] += 1
                point_row = _create_point(session, experiment_id, point, dry_run=dry_run)
                existing_points.append(point_row)
            desc_key = (
                normalize_import_text(point.chapter),
                normalize_import_text(point.experiment),
                normalize_import_text(point.title),
                point.duplicate_ordinal,
            )
            point_rows_by_description_key[desc_key] = point_row

        for desc_key, description in description_lookup.items():
            point_row = point_rows_by_description_key.get(desc_key)
            if not point_row:
                report["unresolved_descriptions"].append(
                    {
                        "line": description.line,
                        "chapter": description.chapter,
                        "experiment": description.experiment,
                        "title": description.title,
                    }
                )
                continue
            report["updated_descriptions"] += 1
            if dry_run or not content_table_exists:
                continue
            metadata = {
                "source": "textbook_point_description_import",
                "source_file": str(description_path),
                "source_line": description.line,
                "source_order": description.source_order,
                "textbook_chapter": description.chapter,
                "textbook_experiment": description.experiment,
                "textbook_folder_path": " / ".join(description.folder_path),
                "textbook_directory_path": " / ".join(description.directory_path),
                "content_hash": _content_hash(description.principle, description.phenomenon, description.safety),
                "imported_at": datetime.now(timezone.utc).isoformat(),
            }
            session.execute(
                text(
                    """
                    INSERT INTO experiment_point_learning_content (
                      experiment_id, point_key, principle_mode, principle_equation, principle_text,
                      phenomenon_explanation, safety_note, content_status, created_by, updated_by,
                      metadata, updated_at
                    )
                    VALUES (
                      :experiment_id, :point_key, 'text', NULL, :principle_text,
                      :phenomenon_explanation, :safety_note, 'draft',
                      CAST(:user_id AS uuid), CAST(:user_id AS uuid), CAST(:metadata AS jsonb), now()
                    )
                    ON CONFLICT (experiment_id, point_key) DO UPDATE SET
                      principle_mode = 'text',
                      principle_equation = NULL,
                      principle_text = EXCLUDED.principle_text,
                      phenomenon_explanation = EXCLUDED.phenomenon_explanation,
                      safety_note = EXCLUDED.safety_note,
                      content_status = 'draft',
                      updated_by = EXCLUDED.updated_by,
                      metadata = experiment_point_learning_content.metadata || EXCLUDED.metadata,
                      updated_at = now()
                    """
                ),
                {
                    "experiment_id": point_row["experiment_id"],
                    "point_key": point_row["point_key"],
                    "principle_text": description.principle,
                    "phenomenon_explanation": description.phenomenon,
                    "safety_note": description.safety,
                    "user_id": user_id,
                    "metadata": _json(metadata),
                },
            )
    return report
