from __future__ import annotations

from server.app.admin_main import app


def _routes_for(path: str, method: str) -> list[object]:
    return [
        route
        for route in app.routes
        if getattr(route, "path", "") == path and method in getattr(route, "methods", set())
    ]


def _assert_route(path: str, method: str) -> None:
    assert len(_routes_for(path, method)) == 1


def test_question_bank_overview_routes_are_registered_once() -> None:
    _assert_route("/api/admin/question-banks/chapters", "GET")
    _assert_route("/api/admin/question-banks/chapter-questions", "GET")
    _assert_route("/api/admin/question-banks/assistant/preview", "POST")
    _assert_route("/api/admin/question-banks", "GET")


def test_question_bank_question_routes_are_registered_once() -> None:
    _assert_route("/api/admin/question-banks/questions", "GET")
    _assert_route("/api/admin/question-banks/questions", "POST")
    _assert_route("/api/admin/question-banks/questions/{question_id}", "PATCH")
    _assert_route("/api/admin/question-banks/questions/{question_id}/publish", "POST")
    _assert_route("/api/admin/question-banks/questions/{question_id}/disable", "POST")


def test_question_bank_import_export_routes_are_registered_once() -> None:
    _assert_route("/api/admin/question-banks/import", "POST")
    _assert_route("/api/admin/question-banks/export", "GET")
