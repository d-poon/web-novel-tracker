import typer

from novel_tracker.cli.commands.database_commands import app as database_app
from novel_tracker.cli.commands.novel_commands import app as commands_app
from novel_tracker.infrastructure.logging.logging_config import setup_logging

setup_logging()

app = typer.Typer(help="Web Novel Tracker CLI")

app.add_typer(
    commands_app, name="novel", help="Commands to manage your web novel tracking."
)
app.add_typer(database_app, name="db", help="Commands to manage database operations.")


def main():
    app()


if __name__ == "__main__":
    main()
