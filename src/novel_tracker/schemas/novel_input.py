from datetime import date

from pydantic import BaseModel, HttpUrl, field_validator


def normalize_string_fields(value):
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        return value if value else None


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
        if isinstance(value, int):
            return value
        # Reject floats, strings, lists, dicts, etc.
        raise TypeError("Invalid type for current_chapter")

    @field_validator("notes", "site", mode="before")
    def normalize_fields(cls, value):
        return normalize_string_fields(value)


class NovelUpdate(BaseModel):
    title: str
    site: str | None = None
    url: HttpUrl | None = None
    current_chapter: int | None = None
    last_read_date: date | None = None
    notes: str | None = None

    @field_validator("title")
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title is required")
        return value.strip()

    @field_validator("site", "notes", mode="before")
    def normalize_fields(cls, value):
        return normalize_string_fields(value)

    @field_validator("current_chapter", mode="before")
    def validate_current_chapter_type(cls, value):
        if value is None:
            return None  # IMPORTANT: don't default to 0
        if isinstance(value, int):
            return value
        raise TypeError("Invalid type for current_chapter")

    @field_validator("current_chapter")
    def validate_current_chapter(cls, value):
        if value is not None and value < 0:
            raise ValueError("Current chapter must be a non-negative integer")
        return value
