import typer

# Reusable Typer argument/option definitions to avoid repeated configuration
TITLE_ARG = typer.Argument(..., help="Title of the novel")
SITE_OPTION = typer.Option(
    None, help="Site where the novel is hosted", prompt="Novel Site"
)
URL_OPTION = typer.Option(None, help="URL of the novel", prompt="Novel URL")
CURRENT_CHAPTER_OPTION = typer.Option(1, min=1, help="Current chapter number")
LAST_READ_DATE_OPTION = typer.Option(
    None, help="Date when the novel was last read", prompt="Last Read Date"
)
NOTES_OPTION = typer.Option(None, help="Notes about the novel", prompt="Notes")
SORT_BY_OPTION = typer.Option(
    "title",
    "--sort-by",
    help="Field to sort by (title, site, url, current_chapter, last_read_date)",
)
