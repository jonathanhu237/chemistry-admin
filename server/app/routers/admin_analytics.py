from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Path, Response

from server.app.auth import AuthUser, require_roles
from server.app.services.analytics_service import (
    export_class_report_response,
    get_class_dashboard,
    get_class_weak_points,
    get_student_report,
)


router = APIRouter(prefix="/api/admin", tags=["experiment-admin"])


@router.get("/analytics/classes/{class_id}/dashboard")
async def admin_class_dashboard(
    class_id: str = Path(min_length=1),
    experiment_id: str | None = None,
    user: AuthUser = Depends(require_roles("admin", "teacher")),
) -> dict[str, Any]:
    return get_class_dashboard(class_id=class_id, experiment_id=experiment_id, user=user)


@router.get("/analytics/classes/{class_id}/students/{student_id}")
async def admin_student_report(
    class_id: str = Path(min_length=1),
    student_id: str = Path(min_length=1),
    user: AuthUser = Depends(require_roles("admin", "teacher")),
) -> dict[str, Any]:
    return get_student_report(class_id=class_id, student_id=student_id, user=user)


@router.get("/analytics/classes/{class_id}/weak-points")
async def admin_class_weak_points(
    class_id: str = Path(min_length=1),
    experiment_id: str | None = None,
    user: AuthUser = Depends(require_roles("admin", "teacher")),
) -> dict[str, Any]:
    return get_class_weak_points(class_id=class_id, experiment_id=experiment_id, user=user)


@router.get("/analytics/classes/{class_id}/export")
async def admin_export_class_report(
    class_id: str = Path(min_length=1),
    user: AuthUser = Depends(require_roles("admin", "teacher")),
) -> Response:
    return export_class_report_response(class_id=class_id, user=user)
