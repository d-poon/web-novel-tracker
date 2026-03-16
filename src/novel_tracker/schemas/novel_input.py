from datetime import date

from pydantic import BaseModel, HttpUrl, field_validator


class NovelCreate(BaseModel):
    title: str
    site: str | None = None
    url: HttpUrl | None = None
    current_chapter: int | None = 0
    last_read_date: date | None = None
    notes: str | None = None

    @field_validator("title")
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title is required")
        return value.strip()

    @field_validator("current_chapter")
    def validate_current_chapter(cls, value):
        # This runs after pydantic parsing: ensure non-negative
        if value < 0:
            raise ValueError("Current chapter must be a non-negative integer")
        return value

    @field_validator("current_chapter", mode="before")
    def validate_current_chapter_type(cls, value):
        # Pre-parse validation: map None -> 0, accept ints and booleans,
        # reject floats, strings and container types so tests get ValidationError.
        if value is None:
            return 0
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, int):
            return value
        # Reject floats, strings, lists, dicts, etc.
        raise TypeError("Invalid type for current_chapter")

    @field_validator("site")
    def validate_site(cls, value):
        return value.strip() if value else None
