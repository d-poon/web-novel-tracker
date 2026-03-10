import typer

from novel_tracker.cli.commands.commands import app as commands_app
from novel_tracker.utils.logging_config import setup_logging

setup_logging()

app = typer.Typer(help="Web Novel Tracker CLI")

app.add_typer(commands_app)


def main():
    app()


if __name__ == "__main__":
    main()
