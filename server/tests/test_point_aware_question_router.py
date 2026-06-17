from __future__ import annotations

from server.app.admin_main import app


def test_point_aware_suggestion_route_stays_registered() -> None:
    routes = [
        route
        for route in app.routes
        if getattr(route, "path", "") == "/api/admin/question-banks/point-aware-suggestions"
        and "POST" in getattr(route, "methods", set())
    ]

    assert len(routes) == 1
