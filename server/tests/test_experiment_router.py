from __future__ import annotations

from server.app.admin_main import app


def _routes_for(path: str) -> list[object]:
    return [route for route in app.routes if getattr(route, "path", "") == path]


def _assert_route(path: str, method: str) -> None:
    routes = [route for route in _routes_for(path) if method in getattr(route, "methods", set())]

    assert len(routes) == 1


def test_experiment_catalog_routes_are_registered_once() -> None:
    _assert_route("/api/admin/experiments", "GET")
    _assert_route("/api/admin/experiments", "POST")
    _assert_route("/api/admin/experiments/{experiment_id}", "GET")
    _assert_route("/api/admin/experiments/{experiment_id}", "PATCH")
    _assert_route("/api/admin/experiments/{experiment_id}/chapter-bindings", "PUT")


def test_experiment_video_routes_are_registered_once() -> None:
    _assert_route("/api/admin/experiments/{experiment_id}/videos/upload", "POST")
    _assert_route("/api/admin/experiments/{experiment_id}/videos/bind", "POST")
    _assert_route("/api/admin/experiments/{experiment_id}/video-points", "GET")
    _assert_route("/api/admin/experiments/{experiment_id}/video-points/{point_key}/resources", "POST")
    _assert_route("/api/admin/experiment-videos", "GET")
