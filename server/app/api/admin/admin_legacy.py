from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from server.app.auth import AuthUser, require_teacher_console_user
from server.app.domains.student_legacy.video_points import (
    legacy_student_video_points,
    set_legacy_video_point_recommendation,
)
from server.app.student_legacy_schemas import LegacyRecommendationUpdateRequest, LegacyStudentVideoPointResponse


router = APIRouter(prefix="/api/admin/legacy", tags=["admin-legacy"])


@router.get("/video-points", response_model=LegacyStudentVideoPointResponse)
def admin_legacy_video_points(
    q: str = Query(default="", max_length=120),
    limit: int = Query(default=500, ge=1, le=500),
    user: AuthUser = Depends(require_teacher_console_user),
) -> LegacyStudentVideoPointResponse:
    return legacy_student_video_points(query=q, limit=limit)


@router.put("/video-points/{node_id}/recommendation", response_model=LegacyStudentVideoPointResponse)
def admin_set_legacy_video_point_recommendation(
    node_id: str,
    payload: LegacyRecommendationUpdateRequest,
    user: AuthUser = Depends(require_teacher_console_user),
) -> LegacyStudentVideoPointResponse:
    updated = set_legacy_video_point_recommendation(
        node_id=node_id,
        recommended=payload.recommended,
        sort_order=payload.sort_order,
        user_id=user.id,
    )
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legacy video point not found")
    return legacy_student_video_points(query="", limit=500)
