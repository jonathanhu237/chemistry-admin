from __future__ import annotations

from server.app.admin_main import app


def _routes_for(path: str) -> list[object]:
    return [route for route in app.routes if getattr(route, "path", "") == path]


def test_class_dashboard_route_is_registered_once() -> None:
    routes = _routes_for("/api/admin/analytics/classes/{class_id}/dashboard")

    assert len(routes) == 1
    assert "GET" in getattr(routes[0], "methods", set())


def test_student_report_route_is_registered_once() -> None:
    routes = _routes_for("/api/admin/analytics/classes/{class_id}/students/{student_id}")

    assert len(routes) == 1
    assert "GET" in getattr(routes[0], "methods", set())


def test_class_weak_points_route_is_registered_once() -> None:
    routes = _routes_for("/api/admin/analytics/classes/{class_id}/weak-points")

    assert len(routes) == 1
    assert "GET" in getattr(routes[0], "methods", set())


def test_class_export_route_is_registered_once() -> None:
    routes = _routes_for("/api/admin/analytics/classes/{class_id}/export")

    assert len(routes) == 1
    assert "GET" in getattr(routes[0], "methods", set())
