from __future__ import annotations

import json
from typing import Annotated, Any

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from server.app.auth import AuthUser, require_roles
from server.app.config import get_settings
from server.app.database import db_session
from server.app.feedback import create_feedback_attachment_record, create_feedback_record, normalize_feedback_type
from server.app.schemas import FeedbackSubmitRequest, FeedbackSubmitResponse


router = APIRouter(prefix="/api/student", tags=["student-feedback"])
StudentUser = Annotated[AuthUser, Depends(require_roles("student"))]


def _parse_metadata(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid feedback metadata") from exc
    if not isinstance(value, dict):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid feedback metadata")
    return value


async def _read_optional_attachment(attachment: UploadFile | None) -> tuple[str, bytes, str | None] | None:
    if attachment is None or not attachment.filename:
        return None
    content = await attachment.read()
    return attachment.filename, content, attachment.content_type


@router.post("/feedback", response_model=FeedbackSubmitResponse)
async def submit_student_feedback(
    user: StudentUser,
    feedback_type: Annotated[str, Form()] = "system_issue",
    content: Annotated[str, Form(min_length=1, max_length=4000)] = "",
    page_path: Annotated[str | None, Form(max_length=500)] = None,
    chapter_id: Annotated[str | None, Form(max_length=128)] = None,
    unit_id: Annotated[str | None, Form(max_length=128)] = None,
    knowledge_point_id: Annotated[str | None, Form(max_length=128)] = None,
    experiment_id: Annotated[str | None, Form(max_length=128)] = None,
    metadata: Annotated[str | None, Form()] = None,
    attachment: Annotated[UploadFile | None, File()] = None,
) -> FeedbackSubmitResponse:
    clean_content = content.strip()
    if len(clean_content) < 5:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Feedback content must be at least 5 characters")

    attachment_payload = await _read_optional_attachment(attachment)
    payload = FeedbackSubmitRequest(
        student_id=user.student_id or user.username,
        class_id=user.class_id,
        feedback_type=normalize_feedback_type(feedback_type),
        content=clean_content,
        chapter_id=chapter_id,
        unit_id=unit_id,
        knowledge_point_id=knowledge_point_id,
        experiment_id=experiment_id,
        page_path=page_path,
        metadata=_parse_metadata(metadata),
    )

    if get_settings().data_backend != "postgres":
        item = create_feedback_record(payload)
        attachment_count = 0
        if attachment_payload:
            create_feedback_attachment_record(
                item["id"],
                filename=attachment_payload[0],
                content=attachment_payload[1],
                content_type=attachment_payload[2],
            )
            attachment_count = 1
        return FeedbackSubmitResponse(id=item["id"], status=item["status"], attachment_count=attachment_count)

    with db_session() as session:
        item = create_feedback_record(payload, session=session)
        attachment_count = 0
        if attachment_payload:
            create_feedback_attachment_record(
                item["id"],
                filename=attachment_payload[0],
                content=attachment_payload[1],
                content_type=attachment_payload[2],
                session=session,
            )
            attachment_count = 1
        return FeedbackSubmitResponse(id=item["id"], status=item["status"], attachment_count=attachment_count)
