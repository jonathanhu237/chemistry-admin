from __future__ import annotations

from server.app.admin_main import app


def _routes_for(path: str, method: str) -> list[object]:
    return [
        route
        for route in app.routes
        if getattr(route, "path", "") == path and method in getattr(route, "methods", set())
    ]


def test_question_draft_routes_are_registered_once() -> None:
    assert len(_routes_for("/api/admin/question-banks/drafts", "GET")) == 1
    assert len(_routes_for("/api/admin/question-banks/drafts/{draft_id}", "PATCH")) == 1
    assert len(_routes_for("/api/admin/question-banks/drafts/{draft_id}/publish", "POST")) == 1
    assert len(_routes_for("/api/admin/question-banks/drafts/{draft_id}/reject", "POST")) == 1
