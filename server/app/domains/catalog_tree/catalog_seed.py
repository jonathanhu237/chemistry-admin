from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy import text

from server.app.infrastructure.settings import ROOT

CATALOG_SEED_DIR = ROOT / "data" / "seed" / "experiment_catalog"
CATALOG_TREE_SEED_PATH = CATALOG_SEED_DIR / "catalog_tree.json"
CANONICAL_POINT_GROUPS_SEED_PATH = CATALOG_SEED_DIR / "canonical_point_groups.json"
POINT_CONTENT_EXAMPLES_SEED_PATH = CATALOG_SEED_DIR / "point_content_examples.json"
CATALOG_SEED_VALIDATION_REPORT_PATH = (
    ROOT / "data" / "seed" / "import_reports" / "catalog_outline_seed_validation_report.json"
)

EXPECTED_CATALOG_COUNTS = {
    "total_nodes": 569,
    "directory_nodes": 176,
    "point_nodes": 393,
    "point_placements": 393,
    "canonical_points": 357,
    "duplicate_group_count": 32,
    "duplicate_placement_surplus": 36,
    "chapter_21_nodes": 0,
    "point_content_examples": 30,
}

CORRECTED_HYPOCHLORITE_PARENT = (
    "第13章 卤族元素",
    "五、卤素含氧酸盐的氧化性",
    "次氯酸盐的氧化性",
)
CORRECTED_HYPOCHLORITE_POINTS = {"NaClO + MnSO₄", "NaClO + 品红溶液"}
CORRECTED_SAMPLE_WORDING = "NaClO + 品红溶液"
LEGACY_IDENTITY_KEYS = {
    "experiment_id",
    "legacy_experiment_id",
    "point_key",
    "legacy_point_key",
}


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def _json(value: Any) -> str:
    return json.dumps(value if value is not None else {}, ensure_ascii=False, default=str)


def _json_array(value: Any) -> str:
    return json.dumps(value if value is not None else [], ensure_ascii=False, default=str)


def load_catalog_seed(path: Path = CATALOG_TREE_SEED_PATH) -> list[dict[str, Any]]:
    data = _read_json(path)
    nodes = data.get("nodes")
    if not isinstance(nodes, list):
        raise ValueError(f"{path} must contain a top-level nodes list")
    return [dict(item) for item in nodes if isinstance(item, dict)]


def load_canonical_point_seed(path: Path = CATALOG_TREE_SEED_PATH) -> list[dict[str, Any]]:
    data = _read_json(path)
    canonical_points = data.get("canonical_points")
    if isinstance(canonical_points, list):
        return [dict(item) for item in canonical_points if isinstance(item, dict)]
    nodes = [dict(item) for item in data.get("nodes") or [] if isinstance(item, dict)]
    by_canonical: dict[str, dict[str, Any]] = {}
    for node in nodes:
        if node.get("node_kind") != "point":
            continue
        canonical_point_id = str(node.get("canonical_point_id") or "").strip()
        if not canonical_point_id:
            continue
        by_canonical.setdefault(
            canonical_point_id,
            {
                "canonical_point_id": canonical_point_id,
                "title": node.get("title") or "",
                "summary": "",
                "status": "published",
                "placement_seed_keys": [],
                "metadata": {"derived_from": "legacy_catalog_tree_nodes"},
            },
        )
        by_canonical[canonical_point_id]["placement_seed_keys"].append(node.get("seed_key"))
    return list(by_canonical.values())


def load_point_content_examples(path: Path = POINT_CONTENT_EXAMPLES_SEED_PATH) -> list[dict[str, Any]]:
    data = _read_json(path)
    examples = data.get("examples")
    if not isinstance(examples, list):
        raise ValueError(f"{path} must contain a top-level examples list")
    return [dict(item) for item in examples if isinstance(item, dict)]


def validate_catalog_seed(
    nodes: list[dict[str, Any]],
    examples: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    errors: list[str] = []
    by_key: dict[str, dict[str, Any]] = {}
    child_counts: dict[str, int] = {}
    path_to_nodes: dict[str, list[dict[str, Any]]] = {}
    point_nodes: list[dict[str, Any]] = []

    for index, node in enumerate(nodes, start=1):
        seed_key = str(node.get("seed_key") or "").strip()
        parent_seed_key = str(node.get("parent_seed_key") or "").strip()
        node_kind = str(node.get("node_kind") or "").strip()
        path_titles = node.get("path_titles")
        if not seed_key:
            errors.append(f"nodes[{index}]: seed_key is required")
            continue
        if seed_key in by_key:
            errors.append(f"nodes[{index}]: duplicate seed_key {seed_key}")
        by_key[seed_key] = node
        if node_kind not in {"directory", "point"}:
            errors.append(f"{seed_key}: invalid node_kind {node_kind!r}")
        if node_kind == "point":
            point_nodes.append(node)
            canonical_point_id = str(node.get("canonical_point_id") or "").strip()
            if not canonical_point_id:
                errors.append(f"{seed_key}: point placement requires canonical_point_id")
        elif str(node.get("canonical_point_id") or "").strip():
            errors.append(f"{seed_key}: directory node must not have canonical_point_id")
        if not isinstance(path_titles, list) or not path_titles:
            errors.append(f"{seed_key}: path_titles must be a non-empty list")
        else:
            path_to_nodes.setdefault(" / ".join(str(item) for item in path_titles), []).append(node)
        if parent_seed_key:
            child_counts[parent_seed_key] = child_counts.get(parent_seed_key, 0) + 1

    for seed_key, node in by_key.items():
        parent_seed_key = str(node.get("parent_seed_key") or "").strip()
        if parent_seed_key and parent_seed_key not in by_key:
            errors.append(f"{seed_key}: parent_seed_key does not resolve: {parent_seed_key}")
        if node.get("node_kind") == "point" and child_counts.get(seed_key, 0) > 0:
            errors.append(f"{seed_key}: point node has children")

    directory_nodes = [node for node in nodes if node.get("node_kind") == "directory"]
    canonical_ids = [str(node.get("canonical_point_id") or "").strip() for node in point_nodes]
    canonical_ids = [canonical_point_id for canonical_point_id in canonical_ids if canonical_point_id]
    title_groups: dict[str, list[dict[str, Any]]] = {}
    for node in point_nodes:
        title_groups.setdefault(str(node.get("title") or ""), []).append(node)
    duplicate_groups = {title: rows for title, rows in title_groups.items() if len(rows) > 1}
    duplicate_placement_surplus = sum(len(rows) - 1 for rows in duplicate_groups.values())
    for title, rows in duplicate_groups.items():
        grouped_canonical_ids = {str(row.get("canonical_point_id") or "").strip() for row in rows}
        if len(grouped_canonical_ids) != 1:
            errors.append(f"duplicate placement title {title!r} must resolve to one reviewed canonical_point_id")
    chapter_21_nodes = [node for node in nodes if int(node.get("chapter_number") or 0) == 21]
    placeholder_nodes = [
        node
        for node in nodes
        if "暂无对应实验内容" in str(node.get("title") or "")
        or any("暂无对应实验内容" in str(part) for part in (node.get("path_titles") or []))
    ]

    counts = {
        "total_nodes": len(nodes),
        "directory_nodes": len(directory_nodes),
        "point_nodes": len(point_nodes),
        "point_placements": len(point_nodes),
        "canonical_points": len(set(canonical_ids)),
        "duplicate_group_count": len(duplicate_groups),
        "duplicate_placement_surplus": duplicate_placement_surplus,
        "chapter_21_nodes": len(chapter_21_nodes),
        "placeholder_nodes": len(placeholder_nodes),
    }
    for key in [
        "total_nodes",
        "directory_nodes",
        "point_nodes",
        "point_placements",
        "canonical_points",
        "duplicate_group_count",
        "duplicate_placement_surplus",
        "chapter_21_nodes",
    ]:
        expected = EXPECTED_CATALOG_COUNTS[key]
        if counts[key] != expected:
            errors.append(f"{key}: expected {expected}, got {counts[key]}")
    if placeholder_nodes:
        errors.append("chapter 21 placeholder text must not be seeded")

    hypochlorite_nodes = [
        node
        for node in point_nodes
        if tuple(node.get("path_titles") or [])[: len(CORRECTED_HYPOCHLORITE_PARENT)] == CORRECTED_HYPOCHLORITE_PARENT
    ]
    hypochlorite_titles = {str(node.get("title") or "") for node in hypochlorite_nodes}
    missing_hypochlorite = sorted(CORRECTED_HYPOCHLORITE_POINTS - hypochlorite_titles)
    if missing_hypochlorite:
        errors.append("missing corrected hypochlorite point(s): " + ", ".join(missing_hypochlorite))
    hypochlorite_canonical_ids = {
        str(node.get("canonical_point_id") or "").strip()
        for node in hypochlorite_nodes
        if str(node.get("title") or "") in CORRECTED_HYPOCHLORITE_POINTS
    }
    if len(hypochlorite_canonical_ids) != len(CORRECTED_HYPOCHLORITE_POINTS):
        errors.append("corrected hypochlorite sibling points must target distinct canonical experiments")

    example_counts: dict[str, int] = {
        "point_content_examples": 0,
        "unique_target_seed_keys": 0,
        "unique_target_canonical_point_ids": 0,
    }
    if examples is not None:
        target_seed_keys: list[str] = []
        target_canonical_point_ids: list[str] = []
        semantic_mapped_examples = 0
        reviewed_override_examples = 0
        ambiguous_example_mappings = 0
        corrected_wording_examples = 0
        for index, example in enumerate(examples, start=1):
            leaked_keys = sorted(key for key in LEGACY_IDENTITY_KEYS if example.get(key))
            if leaked_keys:
                errors.append(f"examples[{index}]: legacy identity keys are not allowed: {', '.join(leaked_keys)}")
            target_seed_key = str(example.get("target_seed_key") or "").strip()
            if not target_seed_key:
                errors.append(f"examples[{index}]: target_seed_key is required")
                continue
            target_seed_keys.append(target_seed_key)
            target_canonical_point_id = str(example.get("target_canonical_point_id") or "").strip()
            if not target_canonical_point_id:
                errors.append(f"examples[{index}]: target_canonical_point_id is required")
            else:
                target_canonical_point_ids.append(target_canonical_point_id)
            target = by_key.get(target_seed_key)
            if not target:
                errors.append(f"examples[{index}]: target seed key does not resolve: {target_seed_key}")
            elif target.get("node_kind") != "point":
                errors.append(f"examples[{index}]: target must resolve to a point node: {target_seed_key}")
            elif target_canonical_point_id and target_canonical_point_id != str(target.get("canonical_point_id") or ""):
                errors.append(f"examples[{index}]: target_canonical_point_id does not match target placement")
            target_path_titles = example.get("target_path_titles") or []
            if target and list(target.get("path_titles") or []) != list(target_path_titles):
                errors.append(f"examples[{index}]: target path does not match catalog seed")
            semantic_mapping = example.get("semantic_mapping")
            if not isinstance(semantic_mapping, dict):
                errors.append(f"examples[{index}]: semantic_mapping report is required")
            else:
                if semantic_mapping.get("method") != "semantic_title_path_reagent_match":
                    errors.append(f"examples[{index}]: unsupported semantic mapping method")
                candidates = semantic_mapping.get("top_candidates")
                if not isinstance(candidates, list) or not candidates:
                    errors.append(f"examples[{index}]: semantic_mapping.top_candidates is required")
                elif target_seed_key not in {str(candidate.get("seed_key") or "") for candidate in candidates if isinstance(candidate, dict)}:
                    errors.append(f"examples[{index}]: target seed key is missing from semantic candidates")
                review_status = str(semantic_mapping.get("review_status") or "")
                if review_status not in {"semantic_match", "reviewed_override"}:
                    errors.append(f"examples[{index}]: invalid semantic mapping review_status")
                semantic_mapped_examples += 1
                if review_status == "reviewed_override":
                    reviewed_override_examples += 1
                    override = semantic_mapping.get("override")
                    if not isinstance(override, dict) or not override.get("reason"):
                        errors.append(f"examples[{index}]: reviewed_override requires override reason")
                if bool(semantic_mapping.get("ambiguous")):
                    ambiguous_example_mappings += 1
                correction = semantic_mapping.get("wording_correction")
                if isinstance(correction, dict):
                    corrected_wording_examples += 1
            if int(example.get("example_number") or 0) == 21:
                correction = (example.get("semantic_mapping") or {}).get("wording_correction")
                if not isinstance(correction, dict) or correction.get("corrected") != CORRECTED_SAMPLE_WORDING:
                    errors.append(f"examples[{index}]: corrected sample wording must be recorded")
            for field in ["principle_text", "phenomenon_explanation", "safety_note"]:
                if not str(example.get(field) or "").strip():
                    errors.append(f"examples[{index}]: {field} is required")
        example_counts = {
            "point_content_examples": len(examples),
            "unique_target_seed_keys": len(set(target_seed_keys)),
            "unique_target_canonical_point_ids": len(set(target_canonical_point_ids)),
            "semantic_mapped_examples": semantic_mapped_examples,
            "reviewed_override_examples": reviewed_override_examples,
            "ambiguous_example_mappings": ambiguous_example_mappings,
            "corrected_wording_examples": corrected_wording_examples,
        }
        if len(examples) != EXPECTED_CATALOG_COUNTS["point_content_examples"]:
            errors.append(
                f"point_content_examples: expected {EXPECTED_CATALOG_COUNTS['point_content_examples']}, got {len(examples)}"
            )
        if len(set(target_seed_keys)) != len(target_seed_keys):
            errors.append("point content examples must target unique catalog point nodes")
        if len(set(target_canonical_point_ids)) != len(target_canonical_point_ids):
            errors.append("point content examples must target unique canonical point ids")

    return {
        "ok": not errors,
        "errors": errors,
        "counts": {**counts, **example_counts},
        "corrected_hypochlorite_points": sorted(hypochlorite_titles & CORRECTED_HYPOCHLORITE_POINTS),
        "corrected_sample_wording": CORRECTED_SAMPLE_WORDING,
    }


def validate_catalog_seed_files(
    *,
    catalog_path: Path = CATALOG_TREE_SEED_PATH,
    examples_path: Path = POINT_CONTENT_EXAMPLES_SEED_PATH,
) -> dict[str, Any]:
    nodes = load_catalog_seed(catalog_path)
    examples = load_point_content_examples(examples_path)
    result = validate_catalog_seed(nodes, examples)
    return {
        **result,
        "catalog_seed": str(catalog_path.relative_to(ROOT).as_posix()),
        "point_content_examples_seed": str(examples_path.relative_to(ROOT).as_posix()),
    }


def reset_legacy_experiment_seed_data(session: Any) -> dict[str, int]:
    statements: list[tuple[str, str]] = [
        ("question_workbench_candidates", "DELETE FROM experiment_question_workbench_candidates"),
        ("question_workbench_turns", "DELETE FROM experiment_question_workbench_turns"),
        ("question_workbench_sessions", "DELETE FROM experiment_question_workbench_sessions"),
        ("question_drafts", "DELETE FROM experiment_question_drafts"),
        ("questions", "DELETE FROM experiment_questions"),
        ("question_banks", "DELETE FROM experiment_question_banks"),
        ("question_generations", "DELETE FROM experiment_question_generations"),
        ("question_imports", "DELETE FROM experiment_question_imports"),
        ("legacy_point_evidence", "DELETE FROM experiment_video_point_evidence"),
        ("catalog_search_state", "DELETE FROM experiment_catalog_point_search_index_state"),
        ("catalog_point_jobs", "DELETE FROM experiment_catalog_point_jobs"),
        ("catalog_point_evidence_bindings", "DELETE FROM experiment_catalog_point_evidence_bindings"),
        ("catalog_point_evidence_state", "DELETE FROM experiment_catalog_point_evidence_state"),
        ("catalog_media_bindings", "DELETE FROM experiment_catalog_point_media_bindings"),
        ("catalog_related_links", "DELETE FROM experiment_catalog_point_related_links"),
        ("catalog_reaction_equations", "DELETE FROM experiment_catalog_point_reaction_equations"),
        ("catalog_point_content", "DELETE FROM experiment_catalog_point_content"),
        ("catalog_legacy_identity_map", "DELETE FROM experiment_catalog_legacy_identity_map"),
        ("catalog_point_identity_map", "DELETE FROM experiment_catalog_point_identity_map"),
        ("catalog_nodes", "DELETE FROM experiment_catalog_nodes"),
        ("catalog_points", "DELETE FROM experiment_catalog_points"),
        (
            "legacy_video_point_search_state",
            "DELETE FROM experiment_video_point_search_index_state",
        ),
        ("legacy_point_related_links", "DELETE FROM experiment_point_related_links"),
        ("legacy_point_learning_content", "DELETE FROM experiment_point_learning_content"),
        ("legacy_video_points", "DELETE FROM experiment_video_points"),
        (
            "legacy_experiment_media_bindings",
            """
            DELETE FROM media_bindings
            WHERE target_type = 'experiment'
              AND (
                metadata ? 'point_key'
                OR metadata ? 'point_title'
                OR metadata ? 'catalog_node_id'
              )
            """,
        ),
    ]
    report: dict[str, int] = {}
    for key, statement in statements:
        result = session.execute(text(statement))
        report[key] = max(int(result.rowcount or 0), 0)
    return report


def import_catalog_seed(
    session: Any,
    *,
    nodes: list[dict[str, Any]] | None = None,
    canonical_points: list[dict[str, Any]] | None = None,
    examples: list[dict[str, Any]] | None = None,
    reset: bool = True,
) -> dict[str, Any]:
    nodes = nodes or load_catalog_seed()
    canonical_points = canonical_points or load_canonical_point_seed()
    examples = examples or load_point_content_examples()
    validation = validate_catalog_seed(nodes, examples)
    if not validation["ok"]:
        raise ValueError("Catalog outline seed validation failed:\n" + "\n".join(validation["errors"][:80]))

    reset_report = reset_legacy_experiment_seed_data(session) if reset else {}
    imported_nodes = 0
    imported_canonical_points = 0
    imported_examples = 0
    queued_search_documents = 0
    now = datetime.now(timezone.utc).isoformat()

    for point in canonical_points:
        placement_seed_keys = point.get("placement_seed_keys") if isinstance(point.get("placement_seed_keys"), list) else []
        metadata = {
            "catalog_outline_seed": True,
            "source_doc": point.get("source_doc") or "docs/实验目录_整理版.md",
            "placement_seed_keys": placement_seed_keys,
            "grouping_decision": point.get("grouping_decision") or "singleton_point_node",
            "imported_at": now,
            **(point.get("metadata") if isinstance(point.get("metadata"), dict) else {}),
        }
        session.execute(
            text(
                """
                INSERT INTO experiment_catalog_points (
                  id, title, summary, status, metadata, published_at, updated_at
                )
                VALUES (
                  :id, :title, :summary, 'published', CAST(:metadata AS jsonb), now(), now()
                )
                ON CONFLICT (id) DO UPDATE SET
                  title = EXCLUDED.title,
                  summary = EXCLUDED.summary,
                  status = EXCLUDED.status,
                  metadata = EXCLUDED.metadata,
                  published_at = COALESCE(experiment_catalog_points.published_at, EXCLUDED.published_at),
                  archived_at = NULL,
                  updated_at = now()
                """
            ),
            {
                "id": point["canonical_point_id"],
                "title": point["title"],
                "summary": point.get("summary") or "",
                "metadata": _json(metadata),
            },
        )
        imported_canonical_points += 1

    for node in nodes:
        metadata = {
            "catalog_outline_seed": True,
            "seed_key": node["seed_key"],
            "placement_node_id": node["seed_key"],
            "canonical_point_id": node.get("canonical_point_id"),
            "source_doc": node.get("source_doc"),
            "source_line": node.get("source_line"),
            "path_titles": node.get("path_titles") or [],
            "imported_at": now,
        }
        session.execute(
            text(
                """
                INSERT INTO experiment_catalog_nodes (
                  id, chapter_id, parent_id, node_kind, title, summary, status, display_order,
                  canonical_point_id, metadata, published_at, updated_at
                )
                VALUES (
                  :id, :chapter_id, :parent_id, :node_kind, :title, '', 'published', :display_order,
                  :canonical_point_id, CAST(:metadata AS jsonb), now(), now()
                )
                ON CONFLICT (id) DO UPDATE SET
                  chapter_id = EXCLUDED.chapter_id,
                  parent_id = EXCLUDED.parent_id,
                  node_kind = EXCLUDED.node_kind,
                  title = EXCLUDED.title,
                  status = EXCLUDED.status,
                  display_order = EXCLUDED.display_order,
                  canonical_point_id = EXCLUDED.canonical_point_id,
                  metadata = EXCLUDED.metadata,
                  published_at = COALESCE(experiment_catalog_nodes.published_at, EXCLUDED.published_at),
                  updated_at = now()
                """
            ),
            {
                "id": node["seed_key"],
                "chapter_id": node["chapter_id"],
                "parent_id": node.get("parent_seed_key") or None,
                "node_kind": node["node_kind"],
                "title": node["title"],
                "display_order": int(node.get("display_order") or 0),
                "canonical_point_id": node.get("canonical_point_id") if node.get("node_kind") == "point" else None,
                "metadata": _json(metadata),
            },
        )
        imported_nodes += 1

    for example in examples:
        metadata = {
            "catalog_outline_point_content_seed": True,
            "example_number": example.get("example_number"),
            "target_seed_key": example.get("target_seed_key"),
            "target_canonical_point_id": example.get("target_canonical_point_id"),
            "source_doc": example.get("source_doc"),
            "source_line_start": example.get("source_line_start"),
            "source_line_end": example.get("source_line_end"),
            "target_path_titles": example.get("target_path_titles") or [],
            "imported_at": now,
        }
        session.execute(
            text(
                """
                INSERT INTO experiment_catalog_point_content (
                  node_id, canonical_point_id, point_title, teacher_note, principle_mode, principle_equation, principle_text,
                  phenomenon_explanation, safety_note, content_status, published_at, metadata, updated_at
                )
                VALUES (
                  :node_id, :canonical_point_id, :point_title, '', 'text', NULL, :principle_text,
                  :phenomenon_explanation, :safety_note, 'published', now(),
                  CAST(:metadata AS jsonb), now()
                )
                ON CONFLICT (node_id) DO UPDATE SET
                  canonical_point_id = EXCLUDED.canonical_point_id,
                  point_title = EXCLUDED.point_title,
                  teacher_note = EXCLUDED.teacher_note,
                  principle_mode = EXCLUDED.principle_mode,
                  principle_equation = EXCLUDED.principle_equation,
                  principle_text = EXCLUDED.principle_text,
                  phenomenon_explanation = EXCLUDED.phenomenon_explanation,
                  safety_note = EXCLUDED.safety_note,
                  content_status = EXCLUDED.content_status,
                  published_at = COALESCE(experiment_catalog_point_content.published_at, EXCLUDED.published_at),
                  metadata = EXCLUDED.metadata,
                  updated_at = now()
                """
            ),
            {
                "node_id": example["target_seed_key"],
                "canonical_point_id": example["target_canonical_point_id"],
                "point_title": (example.get("target_path_titles") or [example.get("example_title")])[-1],
                "principle_text": example["principle_text"],
                "phenomenon_explanation": example["phenomenon_explanation"],
                "safety_note": example["safety_note"],
                "metadata": _json(metadata),
            },
        )
        imported_examples += 1
        session.execute(
            text(
                """
                INSERT INTO experiment_catalog_point_search_index_state (
                  node_id, placement_node_id, canonical_point_id, document_id, desired_action, sync_status, attempts, updated_at
                )
                VALUES (:node_id, :node_id, :canonical_point_id, :node_id, 'upsert', 'pending', 0, now())
                ON CONFLICT (node_id) DO UPDATE SET
                  placement_node_id = EXCLUDED.placement_node_id,
                  canonical_point_id = EXCLUDED.canonical_point_id,
                  document_id = EXCLUDED.document_id,
                  desired_action = 'upsert',
                  sync_status = 'pending',
                  attempts = 0,
                  last_error = NULL,
                  updated_at = now()
                """
            ),
            {"node_id": example["target_seed_key"], "canonical_point_id": example["target_canonical_point_id"]},
        )
        queued_search_documents += 1

    return {
        "imported_at": now,
        "reset": bool(reset),
        "reset_report": reset_report,
        "canonical_points": imported_canonical_points,
        "catalog_nodes": imported_nodes,
        "directory_nodes": validation["counts"]["directory_nodes"],
        "point_nodes": validation["counts"]["point_nodes"],
        "point_placements": validation["counts"]["point_placements"],
        "canonical_point_count": validation["counts"]["canonical_points"],
        "duplicate_group_count": validation["counts"]["duplicate_group_count"],
        "duplicate_placement_surplus": validation["counts"]["duplicate_placement_surplus"],
        "ambiguous_duplicate_count": 0,
        "point_content_examples": imported_examples,
        "queued_search_documents": queued_search_documents,
        "validation": validation,
        "preserved_resources": [
            "source_documents",
            "source_chunks",
            "chunk_embeddings",
            "data/seed/canonical_rag/**",
            "data/seed/search/**",
            "app_users",
            "roles/classes/courses",
            "media_assets",
        ],
    }
