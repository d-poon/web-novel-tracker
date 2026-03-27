from novel_tracker.domain.models.novel import Novel


def format_novel_typer(novel) -> str:
    return (
        f"{novel.title} - Site: {novel.site} "
        f"- URL: {novel.url} - Chapter {novel.current_chapter} - "
        f"Last Read: {novel.last_read_date} - Notes: {novel.notes}"
    )


def shorten(text: str, length: int = 30) -> str:
    if not text:
        return ""
    return text[:length] + "..." if len(text) > length else text


def format_novel_list_table(novels: list[Novel]) -> str:
    header = f"{'TITLE':20} {'SITE':12} {'CHAPTER':8} {'LAST READ':12} NOTES"
    separator = "-" * 70

    rows = []
    for n in novels:
        rows.append(
            f"{n.title[:20]:20} "
            f"{(n.site or '')[:12]:12} "
            f"{n.current_chapter:<8} "
            f"{str(n.last_read_date or ''):12} "
            f"{(shorten(n.notes) or '')}"
        )

    return "\n".join([header, separator, *rows])
