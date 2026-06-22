from __future__ import annotations

import server.app.domains.questions.workbench as question_workbench_service
from server.app.domains.questions.workbench import _question_workbench_rag_gate


class _Runtime:
    def __init__(self, **values):
        self.values = values

    def model_dump(self):
        return dict(self.values)


class _Config:
    def __init__(self, runtime):
        self.rag_runtime = runtime


def test_question_workbench_rag_gate_blocks_when_rag_access_disabled(monkeypatch):
    monkeypatch.setattr(
        question_workbench_service,
        "get_ai_configuration_response",
        lambda can_edit=False, auto_check=False: _Config(
            _Runtime(
                rag_enabled=False,
                textbook_rag_status="disabled",
                textbook_rag_message="RAG 已关闭",
            )
        ),
    )

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is False
    assert gate["reason_code"] == "rag_disabled"


def test_question_workbench_rag_gate_allows_when_textbook_rag_is_healthy(monkeypatch):
    monkeypatch.setattr(
        question_workbench_service,
        "get_ai_configuration_response",
        lambda can_edit=False, auto_check=False: _Config(
            _Runtime(
                rag_enabled=True,
                textbook_rag_status="healthy",
                textbook_rag_message="教材 RAG 已配置，Elasticsearch 索引可访问。",
                textbook_rag_index="canonical-rag-chunks-qwen-v1",
            )
        ),
    )

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is True
    assert gate["retrieval_mode"] == "qwen_es_textbook_rag"
    assert gate["rag_runtime"]["textbook_rag_index"] == "canonical-rag-chunks-qwen-v1"


def test_question_workbench_rag_gate_blocks_when_textbook_rag_is_unhealthy(monkeypatch):
    monkeypatch.setattr(
        question_workbench_service,
        "get_ai_configuration_response",
        lambda can_edit=False, auto_check=False: _Config(
            _Runtime(
                rag_enabled=True,
                textbook_rag_status="index_missing",
                textbook_rag_message="教材 RAG 索引不存在。",
            )
        ),
    )

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is False
    assert gate["reason_code"] == "index_missing"
    assert "索引" in gate["message"]
