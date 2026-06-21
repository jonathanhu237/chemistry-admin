from __future__ import annotations

import inspect
from typing import Any

from server.app.domains.catalog_tree import jobs


class _Result:
    def __init__(self, row: dict[str, Any] | None = None, rows: list[dict[str, Any]] | None = None) -> None:
        self.row = row
        self.rows = rows or ([] if row is None else [row])

    def mappings(self) -> "_Result":
        return self

    def first(self) -> dict[str, Any] | None:
        return self.row

    def all(self) -> list[dict[str, Any]]:
        return self.rows

    def scalars(self) -> "_Result":
        return self


class _FakeSession:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def execute(self, statement: Any, params: dict[str, Any] | None = None) -> _Result:
        self.calls.append({"sql": str(statement), "params": params or {}})
        if "RETURNING id, node_id, job_type" in str(statement):
            return _Result(
                {
                    "id": "00000000-0000-0000-0000-000000000001",
                    "node_id": (params or {}).get("node_id"),
                    "job_type": (params or {}).get("job_type"),
                    "trigger_source": (params or {}).get("trigger_source"),
                    "status": "pending",
                    "attempts": 0,
                    "max_attempts": (params or {}).get("max_attempts", 3),
                    "payload": {},
                    "result": {},
                }
            )
        return _Result()


def _call_with_param(session: _FakeSession, key: str, value: Any) -> dict[str, Any]:
    return next(call for call in session.calls if call["params"].get(key) == value)


def test_enqueue_point_job_is_idempotent_for_open_equivalent_work() -> None:
    session = _FakeSession()

    row = jobs.enqueue_point_job(
        session,
        node_id="cat-point-1",
        job_type="rag_evidence_refresh",
        trigger_source="manual",
        payload={"reason": "manual_refresh"},
    )

    assert row["node_id"] == "cat-point-1"
    assert row["job_type"] == "rag_evidence_refresh"
    insert_call = _call_with_param(session, "job_type", "rag_evidence_refresh")
    assert "ON CONFLICT (idempotency_key) WHERE status IN ('pending', 'running')" in insert_call["sql"]
    assert insert_call["params"]["idempotency_key"].startswith("catalog-point:cat-point-1:rag_evidence_refresh:")
    assert insert_call["params"]["placement_node_id"] == "cat-point-1"
    assert insert_call["params"]["canonical_point_id"] == "cat-point-1"


def test_queue_es_sync_job_records_desired_action_and_catalog_node_identity() -> None:
    session = _FakeSession()

    jobs.queue_es_sync_job(session, node_id="cat-point-1", action="delete", trigger_source="automatic")

    params = _call_with_param(session, "job_type", "es_delete")["params"]
    assert params["node_id"] == "cat-point-1"
    assert params["job_type"] == "es_delete"
    assert params["placement_node_id"] == "cat-point-1"
    assert params["canonical_point_id"] == "cat-point-1"
    assert params["trigger_source"] == "automatic"
    assert '"desired_action": "delete"' in params["payload"]


def test_mark_point_evidence_stale_does_not_block_or_auto_refresh_by_default(monkeypatch) -> None:
    session = _FakeSession()

    monkeypatch.setattr(jobs, "get_settings", lambda: type("Settings", (), {"catalog_point_evidence_auto_refresh": False})())

    jobs.mark_point_evidence_stale(session, node_id="cat-point-1", reason="point_content_edited")

    stale_call = _call_with_param(session, "evidence_status", "stale")["params"]
    assert stale_call["node_id"] == "cat-point-1"
    assert stale_call["canonical_point_id"] == "cat-point-1"
    assert stale_call["source_placement_node_id"] == "cat-point-1"
    assert stale_call["stale_reason"] == "point_content_edited"


def test_worker_claim_uses_database_locking_to_avoid_duplicate_execution() -> None:
    source = inspect.getsource(jobs.claim_next_point_job)

    assert "FOR UPDATE SKIP LOCKED" in source
    assert "status = 'pending'" in source
    assert "attempts < max_attempts" in source


def test_process_point_job_records_bge_unavailable_as_diagnostic_status(monkeypatch) -> None:
    calls: list[dict[str, Any]] = []
    job = jobs.CatalogPointJob(
        id="00000000-0000-0000-0000-000000000002",
        node_id="cat-point-1",
        job_type="rag_evidence_refresh",
        attempts=1,
        payload={},
    )

    def raise_unavailable(_job: jobs.CatalogPointJob) -> dict[str, Any]:
        raise jobs.CatalogPointJobUnavailable("BGE service is unreachable")

    monkeypatch.setattr(jobs, "_process_rag_evidence_refresh", raise_unavailable)
    monkeypatch.setattr(
        jobs,
        "_mark_evidence_failure",
        lambda **kwargs: calls.append({"kind": "evidence_failure", **kwargs}),
    )
    monkeypatch.setattr(
        jobs,
        "fail_point_job",
        lambda failed_job, error, status_value="failed", result=None: calls.append(
            {"kind": "job_failure", "job_id": failed_job.id, "error": error, "status": status_value}
        ),
    )

    jobs.process_point_job(job)

    assert calls[0]["kind"] == "evidence_failure"
    assert calls[0]["node_id"] == "cat-point-1"
    assert calls[0]["evidence_status"] == "unavailable"
    assert calls[1]["kind"] == "job_failure"
    assert calls[1]["status"] == "unavailable"
    assert "BGE service is unreachable" in calls[1]["error"]


def test_rag_runtime_gate_requires_configured_hybrid_bge() -> None:
    settings = type(
        "Settings",
        (),
        {
            "rag_hybrid_bge_enabled": False,
            "rag_query_generation_enabled": True,
            "rag_bge_service_url": "",
            "rag_vector_top_k": 24,
            "rag_rerank_top_k": 9,
            "rag_final_top_k": 5,
        },
    )()

    gate = jobs._rag_runtime_gate(settings)

    assert gate["healthy"] is False
    assert gate["status"] == "unavailable"
    assert gate["reason_code"] == "hybrid_bge_disabled"
