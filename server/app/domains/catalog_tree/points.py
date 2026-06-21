from __future__ import annotations

from typing import Any

from sqlalchemy import text

from server.app.catalog_tree_schemas import CatalogPointContentRequest, CatalogPointPublicationRequest
from server.app.domains.catalog_tree.common import clean, content_publication_errors, dump_model, get_content, get_node, json_dump, point_capable
from server.app.domains.catalog_tree.common import active_placement_ids_for_canonical_point, canonical_point_id_for_node
from server.app.domains.catalog_tree.equations import normalize_reaction_equations, replace_reaction_equations
from server.app.domains.catalog_tree.jobs import mark_point_evidence_stale
from server.app.domains.catalog_tree.search_documents import queue_index_state
from server.app.domains.errors import DomainHTTPException as HTTPException, domain_status as status
from server.app.infrastructure.database import db_session


def save_point_content(*, node_id: str, payload: CatalogPointContentRequest, user: Any) -> dict[str, Any]:
    data = dump_model(payload)
    with db_session() as session:
        node = get_node(session, node_id)
        if not point_capable(node):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Directory nodes cannot own point content")
        if node.get("has_children"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Point nodes cannot have children")
        canonical_point_id = canonical_point_id_for_node(session, node_id)
        mode = clean(data.get("principle_mode") or "text")
        principle_equation = clean(data.get("principle_equation"))
        principle_text = clean(data.get("principle_text"))
        reaction_inputs = data.get("reaction_equations") if isinstance(data.get("reaction_equations"), list) else []
        if mode == "equation" and not reaction_inputs and principle_equation:
            reaction_inputs = [{"raw_text": principle_equation, "row_order": 1}]
        normalized_equations = normalize_reaction_equations(reaction_inputs)
        if mode == "equation":
            principle_equation = "\n".join(row["raw_text"] for row in normalized_equations if clean(row.get("raw_text")))
            principle_text = ""
        elif mode == "text":
            principle_equation = ""
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Principle mode must be equation or text")
        point_title = clean(data.get("point_title"))
        result = session.execute(
            text(
                """
                UPDATE experiment_catalog_point_content
                SET point_title = :point_title,
                  teacher_note = :teacher_note,
                  principle_mode = :principle_mode,
                  principle_equation = :principle_equation,
                  principle_text = :principle_text,
                  phenomenon_explanation = :phenomenon_explanation,
                  safety_note = :safety_note,
                  content_status = 'draft',
                  canonical_point_id = :canonical_point_id,
                  updated_by = CAST(:user_id AS uuid),
                  metadata = experiment_catalog_point_content.metadata || CAST(:metadata AS jsonb),
                  updated_at = now()
                WHERE canonical_point_id = :canonical_point_id
                   OR node_id = :node_id
                """
            ),
            {
                "node_id": node_id,
                "canonical_point_id": canonical_point_id,
                "point_title": point_title,
                "teacher_note": clean(data.get("teacher_note")),
                "principle_mode": mode,
                "principle_equation": principle_equation or None,
                "principle_text": principle_text or None,
                "phenomenon_explanation": clean(data.get("phenomenon_explanation")),
                "safety_note": clean(data.get("safety_note")),
                "metadata": json_dump(data.get("metadata") if isinstance(data.get("metadata"), dict) else {}),
                "user_id": user.id,
            },
        )
        if int(result.rowcount or 0) == 0:
            session.execute(
                text(
                    """
                    INSERT INTO experiment_catalog_point_content (
                      node_id, canonical_point_id, point_title, teacher_note, principle_mode, principle_equation, principle_text,
                      phenomenon_explanation, safety_note, content_status, created_by, updated_by, metadata, updated_at
                    )
                    VALUES (
                      :node_id, :canonical_point_id, :point_title, :teacher_note, :principle_mode, :principle_equation, :principle_text,
                      :phenomenon_explanation, :safety_note, 'draft', CAST(:user_id AS uuid), CAST(:user_id AS uuid),
                      CAST(:metadata AS jsonb), now()
                    )
                    """
                ),
                {
                    "node_id": node_id,
                    "canonical_point_id": canonical_point_id,
                    "point_title": point_title,
                    "teacher_note": clean(data.get("teacher_note")),
                    "principle_mode": mode,
                    "principle_equation": principle_equation or None,
                    "principle_text": principle_text or None,
                    "phenomenon_explanation": clean(data.get("phenomenon_explanation")),
                    "safety_note": clean(data.get("safety_note")),
                    "metadata": json_dump(data.get("metadata") if isinstance(data.get("metadata"), dict) else {}),
                    "user_id": user.id,
                },
            )
        if mode == "equation":
            replace_reaction_equations(
                session,
                node_id=node_id,
                canonical_point_id=canonical_point_id,
                equations=normalized_equations,
            )
        session.execute(
            text(
                """
                UPDATE experiment_catalog_points
                SET title = :title, updated_by = CAST(:user_id AS uuid), updated_at = now()
                WHERE id = :canonical_point_id
                """
            ),
            {"canonical_point_id": canonical_point_id, "title": point_title, "user_id": user.id},
        )
        session.execute(
            text(
                """
                UPDATE experiment_catalog_nodes
                SET title = :title, updated_by = CAST(:user_id AS uuid), updated_at = now()
                WHERE canonical_point_id = :canonical_point_id
                  AND node_kind = 'point'
                """
            ),
            {"canonical_point_id": canonical_point_id, "title": point_title, "user_id": user.id},
        )
        for placement_node_id in active_placement_ids_for_canonical_point(session, canonical_point_id):
            queue_index_state(session, node_id=placement_node_id, action="delete")
        mark_point_evidence_stale(session, node_id=node_id, reason="point_content_edited")
    from server.app.domains.catalog_tree.nodes import get_node_detail

    return get_node_detail(node_id=node_id)


def set_point_content_publication(*, node_id: str, payload: CatalogPointPublicationRequest, user: Any) -> dict[str, Any]:
    with db_session() as session:
        node = get_node(session, node_id)
        if not point_capable(node):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Directory nodes cannot publish point content")
        canonical_point_id = canonical_point_id_for_node(session, node_id)
        content = get_content(session, node_id)
        if not content:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Point content must be saved first")
        if payload.action == "publish":
            errors = content_publication_errors(node, content)
            if errors:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=errors)
            content_status = "published"
            node_status = "published"
            action = "upsert"
            published_sql = "published_at = now(), published_by = CAST(:user_id AS uuid),"
            node_published_sql = "published_at = COALESCE(published_at, now()),"
        elif payload.action in {"unpublish", "archive"}:
            content_status = "archived" if payload.action == "archive" else "draft"
            node_status = "archived" if payload.action == "archive" else "draft"
            action = "delete"
            published_sql = "published_at = NULL, published_by = NULL,"
            node_published_sql = "published_at = NULL,"
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported publication action")
        session.execute(
            text(
                f"""
                UPDATE experiment_catalog_point_content
                SET content_status = :content_status,
                    {published_sql}
                    updated_by = CAST(:user_id AS uuid),
                    updated_at = now()
                WHERE canonical_point_id = :canonical_point_id
                   OR node_id = :node_id
                """
            ),
            {"node_id": node_id, "canonical_point_id": canonical_point_id, "content_status": content_status, "user_id": user.id},
        )
        session.execute(
            text(
                f"""
                UPDATE experiment_catalog_points
                SET status = :status,
                    {node_published_sql}
                    updated_by = CAST(:user_id AS uuid),
                    updated_at = now()
                WHERE id = :canonical_point_id
                """
            ),
            {"canonical_point_id": canonical_point_id, "status": node_status, "user_id": user.id},
        )
        session.execute(
            text(
                f"""
                UPDATE experiment_catalog_nodes
                SET status = :status,
                    {node_published_sql}
                    updated_by = CAST(:user_id AS uuid),
                    updated_at = now()
                WHERE id = :node_id
                """
            ),
            {"node_id": node_id, "status": node_status, "user_id": user.id},
        )
        for placement_node_id in active_placement_ids_for_canonical_point(session, canonical_point_id):
            queue_index_state(session, node_id=placement_node_id, action=action)
        mark_point_evidence_stale(session, node_id=node_id, reason=f"point_content_{payload.action}")
    from server.app.domains.catalog_tree.nodes import get_node_detail

    return get_node_detail(node_id=node_id)
