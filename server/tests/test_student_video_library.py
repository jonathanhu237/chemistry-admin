from __future__ import annotations

from contextlib import contextmanager
from typing import Any

import pytest
from fastapi import HTTPException

from server.app.auth import AuthUser
from server.app.config import Settings
from server.app.routers import student_video_library
from server.app.services import student_video_library_service
from server.app.services.student_video_library_service import _build_documents, search_student_video_library
from server.tests.route_helpers import assert_route


def _student_user() -> AuthUser:
    return AuthUser(
        id="student-video-library-user",
        username="20240002",
        role="student",
        display_name="Student",
        status="active",
        must_change_password=False,
        student_id="20240002",
        class_id="class-video",
    )


def _experiment(
    experiment_id: str,
    *,
    title: str,
    status: str = "published",
    chapter_id: str = "CH13",
    archived: bool = False,
    media_status: str = "published",
) -> dict[str, Any]:
    return {
        "id": experiment_id,
        "code": experiment_id.replace("EXP_", ""),
        "title": title,
        "summary": f"{title} summary",
        "status": status,
        "display_order": 1,
        "metadata": {
            "parent_code": "19-1",
            "parent_title": "Experiment 19-1",
            "module_display_title": "Chlorine water observation",
            "video_candidates": ["orange CCl4 layer"],
            "archived_by_catalog_seed": "true" if archived else "false",
        },
        "chapter_bindings": [{"chapter_id": chapter_id, "chapter_title": "Halogens", "coverage_type": "primary", "sort_order": 1}],
        "media_resources": [
            {
                "media_id": f"media-{experiment_id}",
                "title": "CCl4 orange layer video",
                "point_key": "orange-layer",
                "point_title": "Orange layer observation",
                "upload_status": "ready",
                "binding_status": media_status,
                "has_thumbnail": False,
            }
        ],
        "published_question_count": 2,
    }


def _profiles() -> list[dict[str, Any]]:
    return [
        {
            "enabled": True,
            "profile_id": "halogens-17",
            "chapter_id": "CH13",
            "title": "Halogens",
            "subtitle": "Halogen displacement",
            "family_name": "Group 17",
            "element_symbols": ["Cl", "Br", "I"],
            "default_element_symbol": "Cl",
            "property_sections": [
                {
                    "key": "oxidation",
                    "title": "Oxidation",
                    "formula": "Cl2 + 2Br- -> 2Cl- + Br2",
                    "experiment_keywords": ["chlorine", "orange"],
                }
            ],
        }
    ]


@contextmanager
def _fake_session():
    yield object()


def test_student_video_library_route_is_registered() -> None:
    assert_route("/api/student/video-library/search", "GET")


def test_video_library_rejects_non_experiment_video_domain() -> None:
    with pytest.raises(HTTPException) as exc_info:
        student_video_library.video_library_search(_student_user(), q="admin", domain="admin")

    assert exc_info.value.status_code == 400


def test_video_library_documents_only_include_student_visible_material() -> None:
    documents = _build_documents(
        [
            _experiment("EXP_VISIBLE", title="Visible chlorine displacement"),
            _experiment("EXP_DRAFT", title="Draft teacher-only experiment", status="draft"),
            _experiment("EXP_ARCHIVED", title="Archived experiment", archived=True),
            _experiment("EXP_F_AREA", title="F area experiment", chapter_id="CH21"),
            _experiment("EXP_HIDDEN_MEDIA", title="Hidden media", media_status="draft"),
        ],
        _profiles(),
    )

    search_text = "\n".join(document.search_text for document in documents)

    assert "Visible chlorine displacement" in search_text
    assert "Draft teacher-only experiment" not in search_text
    assert "Archived experiment" not in search_text
    assert "F area experiment" not in search_text
    assert "media-EXP_HIDDEN_MEDIA" not in search_text
    assert all(document.target for document in documents)


def test_video_library_local_search_returns_grouped_actionable_results(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(student_video_library_service, "db_session", _fake_session)
    monkeypatch.setattr(student_video_library_service, "_load_published_experiments", lambda _session: [_experiment("EXP_VISIBLE", title="Visible chlorine displacement")])
    monkeypatch.setattr(student_video_library_service, "_learning_profiles", _profiles)

    response = search_student_video_library(_student_user(), query="orange", limit=10)

    assert response.status == "ok"
    assert response.backend == "local"
    assert response.total >= 1
    assert response.groups
    assert all(item.target for group in response.groups for item in group.items)
    assert any(item.target and item.target.kind == "point_detail" for group in response.groups for item in group.items)


def test_video_library_disabled_search_returns_controlled_state(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(student_video_library_service, "db_session", _fake_session)
    monkeypatch.setattr(student_video_library_service, "_load_published_experiments", lambda _session: [_experiment("EXP_VISIBLE", title="Visible chlorine displacement")])
    monkeypatch.setattr(student_video_library_service, "_learning_profiles", _profiles)
    monkeypatch.setattr(
        student_video_library_service,
        "get_settings",
        lambda: Settings(video_library_search_enabled=False),
    )

    response = search_student_video_library(_student_user(), query="orange", limit=10)

    assert response.status == "disabled"
    assert response.backend == "disabled"
    assert response.groups == []
    assert response.browse.recommended
