from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Query

from server.app.auth import AuthUser, require_roles
from server.app.domains.assessments.smart_assessment import submit_student_smart_assessment
from server.app.domains.student_legacy.video_points import legacy_student_video_points
from server.app.student_legacy_schemas import LegacyStudentVideoPointResponse
from server.app.student_smart_assessment_schemas import StudentSmartAssessmentSubmitRequest, StudentSmartAssessmentSubmitResponse


router = APIRouter(prefix="/api/student/legacy", tags=["student-legacy"])
StudentUser = Annotated[AuthUser, Depends(require_roles("student"))]


@router.get("/video-points", response_model=LegacyStudentVideoPointResponse)
def legacy_video_points(
    user: StudentUser,
    q: Annotated[str, Query(max_length=120)] = "",
    limit: Annotated[int, Query(ge=1, le=500)] = 200,
) -> LegacyStudentVideoPointResponse:
    return legacy_student_video_points(query=q, limit=limit)


@router.post("/smart-assessment/submit", response_model=StudentSmartAssessmentSubmitResponse)
def legacy_submit_smart_assessment(
    payload: StudentSmartAssessmentSubmitRequest,
    user: StudentUser,
) -> StudentSmartAssessmentSubmitResponse:
    return submit_student_smart_assessment(user, payload)
