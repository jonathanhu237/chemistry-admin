from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class LegacyStudentVideoPointItem(BaseModel):
    id: str
    node_id: str
    chapter_id: str | None = None
    title: str
    summary: str = ""
    snippet: str = ""
    catalog_path: list[str] = Field(default_factory=list)
    media_count: int = 0
    published_media_count: int = 0
    thumbnail_path: str | None = None
    is_recommended: bool = False
    recommended_order: int | None = None


class LegacyStudentVideoPointResponse(BaseModel):
    status: Literal["ok", "empty"] = "ok"
    query: str = ""
    total: int = 0
    items: list[LegacyStudentVideoPointItem] = Field(default_factory=list)


class LegacyRecommendationUpdateRequest(BaseModel):
    recommended: bool = True
    sort_order: int = 0
