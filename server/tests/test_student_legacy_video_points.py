from __future__ import annotations

import inspect
from contextlib import contextmanager

from server.app.domains.student_legacy import video_points
from server.app.domains.student_legacy.video_points import legacy_student_video_points
from server.tests.route_helpers import assert_route


def _rows() -> list[dict[str, object]]:
    return [
        {
            "node_id": "point-recommended-no-video",
            "chapter_id": "chapter-halogen",
            "chapter_title": "Chapter 13",
            "node_title": "Recommended point without video",
            "summary": "Recommended but no playable media.",
            "point_title": "Recommended point without video",
            "principle_equation": "",
            "principle_text": "",
            "phenomenon_explanation": "",
            "safety_note": "",
            "catalog_path": ["Chapter 13", "No video"],
            "media_count": 0,
            "thumbnail_path": None,
            "is_recommended": True,
            "recommended_order": 0,
        },
        {
            "node_id": "point-recommended-video",
            "chapter_id": "chapter-halogen",
            "chapter_title": "Chapter 13",
            "node_title": "Recommended point with video",
            "summary": "Recommended and playable.",
            "point_title": "Recommended point with video",
            "principle_equation": "",
            "principle_text": "",
            "phenomenon_explanation": "",
            "safety_note": "",
            "catalog_path": ["Chapter 13", "With video"],
            "media_count": 2,
            "thumbnail_media_id": "media-2",
            "is_recommended": True,
            "recommended_order": 0,
        },
        {
            "node_id": "point-1",
            "chapter_id": "chapter-halogen",
            "chapter_title": "第13章 卤族元素",
            "node_title": "氯水漂白性实验",
            "summary": "观察氯水漂白现象。",
            "point_title": "氯水漂白性实验",
            "principle_equation": "Cl2 + H2O -> HCl + HClO",
            "principle_text": "",
            "phenomenon_explanation": "试纸逐渐褪色。",
            "safety_note": "注意通风。",
            "catalog_path": ["第13章 卤族元素", "氯的氧化性", "氯水漂白性实验"],
            "media_count": 1,
            "thumbnail_media_id": "media-1",
        },
        {
            "node_id": "point-no-video",
            "chapter_id": "chapter-halogen",
            "chapter_title": "第13章 卤族元素",
            "node_title": "KI水溶液中碘离子检验",
            "summary": "观察KI与氯水反应后的颜色变化。",
            "point_title": "KI水溶液中碘离子检验",
            "principle_equation": "Cl2 + 2I- -> 2Cl- + I2",
            "principle_text": "",
            "phenomenon_explanation": "加入淀粉后出现蓝色。",
            "safety_note": "",
            "catalog_path": ["第13章 卤族元素", "卤素离子的还原性", "KI水溶液中碘离子检验"],
            "media_count": 0,
            "thumbnail_path": None,
        },
    ]


@contextmanager
def _fake_db_session():
    yield object()


def test_student_legacy_video_points_route_is_registered() -> None:
    assert_route("/api/student/legacy/video-points", "GET")
    assert_route("/api/student/legacy/smart-assessment/submit", "POST")
    assert_route("/api/admin/legacy/video-points", "GET")
    assert_route("/api/admin/legacy/video-points/{node_id}/recommendation", "PUT")


def test_legacy_video_point_query_uses_point_content_primary_key() -> None:
    source = inspect.getsource(video_points._legacy_video_point_rows)

    assert "pc.id" not in source
    assert "pc.node_id" in source


def test_legacy_video_points_include_no_video_points_and_filter_query(monkeypatch) -> None:
    monkeypatch.setattr(video_points, "db_session", _fake_db_session)
    monkeypatch.setattr(video_points, "_ensure_recommendation_table", lambda _session: None)
    monkeypatch.setattr(video_points, "_legacy_video_point_rows", lambda _session: _rows())

    all_points = legacy_student_video_points(query="", limit=10)

    assert all_points.total == 4
    assert [item.node_id for item in all_points.items] == [
        "point-recommended-video",
        "point-1",
        "point-recommended-no-video",
        "point-no-video",
    ]
    assert all_points.items[0].published_media_count == 2
    assert all_points.items[0].thumbnail_path == "/api/student/media/assets/media-2/thumbnail"
    assert all_points.items[0].is_recommended is True
    assert all_points.items[2].published_media_count == 0
    assert all_points.items[2].is_recommended is True

    filtered = legacy_student_video_points(query="KI 蓝色", limit=10)

    assert filtered.total == 1
    assert filtered.items[0].node_id == "point-no-video"
    assert filtered.items[0].thumbnail_path is None
