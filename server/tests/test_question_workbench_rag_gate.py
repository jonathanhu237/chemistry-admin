from __future__ import annotations

from dataclasses import replace

from server.app.infrastructure.settings import Settings
import server.app.domains.questions.workbench as question_workbench_service
from server.app.domains.questions.workbench import _question_workbench_rag_gate


def _ai_settings(**overrides):
    values = {
        "agent_llm_provider": "openai",
        "agent_llm_base_url": "https://api.deepseek.com",
        "agent_llm_model": "deepseek-chat",
        "agent_llm_api_key": "configured",
    }
    values.update(overrides)
    return replace(Settings(), **values)


def test_question_workbench_gate_blocks_when_question_bank_assistant_disabled(monkeypatch):
    monkeypatch.setattr(question_workbench_service, "get_settings", lambda: _ai_settings())
    monkeypatch.setattr(question_workbench_service, "effective_ai_settings", lambda settings: settings)
    monkeypatch.setattr(question_workbench_service, "ai_feature_enabled", lambda name: False if name == "question_bank_assistant" else True)

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is False
    assert gate["reason_code"] == "question_bank_assistant_disabled"


def test_question_workbench_gate_blocks_when_llm_is_not_configured(monkeypatch):
    monkeypatch.setattr(question_workbench_service, "get_settings", lambda: _ai_settings(agent_llm_api_key=""))
    monkeypatch.setattr(question_workbench_service, "effective_ai_settings", lambda settings: settings)
    monkeypatch.setattr(question_workbench_service, "ai_feature_enabled", lambda name: True)

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is False
    assert gate["reason_code"] == "llm_not_configured"


def test_question_workbench_gate_allows_generation_when_textbook_rag_is_healthy(monkeypatch):
    monkeypatch.setattr(question_workbench_service, "get_settings", lambda: _ai_settings())
    monkeypatch.setattr(question_workbench_service, "effective_ai_settings", lambda settings: settings)
    monkeypatch.setattr(question_workbench_service, "ai_feature_enabled", lambda name: True)
    monkeypatch.setattr(question_workbench_service, "effective_textbook_rag_settings", lambda: {"enabled": True})
    monkeypatch.setattr(
        question_workbench_service,
        "_textbook_rag_runtime_status",
        lambda settings, *, rag_enabled: {
            "enabled": True,
            "status": "healthy",
            "message": "External textbook RAG is healthy.",
            "models": {"embedding": "qwen-embed", "rerank": "qwen-rerank"},
            "diagnostics": {"index_exists": True},
        },
    )

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is True
    assert gate["textbook_rag_status"] == "healthy"
    assert gate["rag_runtime"]["evidence_source"] == "external_textbook_rag"


def test_question_workbench_gate_blocks_when_textbook_rag_is_unhealthy(monkeypatch):
    monkeypatch.setattr(question_workbench_service, "get_settings", lambda: _ai_settings())
    monkeypatch.setattr(question_workbench_service, "effective_ai_settings", lambda settings: settings)
    monkeypatch.setattr(question_workbench_service, "ai_feature_enabled", lambda name: True)
    monkeypatch.setattr(question_workbench_service, "effective_textbook_rag_settings", lambda: {"enabled": True})
    monkeypatch.setattr(
        question_workbench_service,
        "_textbook_rag_runtime_status",
        lambda settings, *, rag_enabled: {
            "enabled": True,
            "status": "elasticsearch_unreachable",
            "message": "External textbook RAG Elasticsearch is unreachable.",
            "models": {},
            "diagnostics": {"elasticsearch_error": "timeout"},
        },
    )

    gate = _question_workbench_rag_gate()

    assert gate["healthy"] is False
    assert gate["reason_code"] == "elasticsearch_unreachable"
    assert gate["textbook_rag_status"] == "elasticsearch_unreachable"
