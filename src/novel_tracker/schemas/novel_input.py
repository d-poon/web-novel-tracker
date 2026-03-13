from datetime import date

from pydantic import BaseModel, HttpUrl, field_validator


class NovelCreate(BaseModel):
    title: str
    site: str | None = None
    url: HttpUrl | None = None
    current_chapter: int = 0
    last_read_date: date | None = None
    notes: str | None = None

    @field_validator("title")
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title is required")
        return value.strip()

    @field_validator("current_chapter")
    def validate_current_chapter(cls, value):
        if value < 0:
            raise ValueError("Current chapter must be a non-negative integer")
        return value

    @field_validator("site")
    def validate_site(cls, value):
        return value.strip() if value else None
