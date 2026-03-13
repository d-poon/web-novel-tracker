import pytest
from pydantic import ValidationError

from novel_tracker.schemas.novel_input import NovelCreate


def test_novel_create_validates_title():
    with pytest.raises(ValueError, match="Title is required"):
        NovelCreate(title="   ")


def test_novel_create_validates_title_2():
    with pytest.raises(ValueError, match="Title is required"):
        NovelCreate(title=" ")


def test_novel_create_validates_title_3():
    with pytest.raises(ValueError, match="Title is required"):
        NovelCreate(title="")


def test_novel_create_validates_title_4():
    with pytest.raises(ValidationError):
        NovelCreate(title=None)
