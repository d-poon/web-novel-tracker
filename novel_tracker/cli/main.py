import typer

from novel_tracker.cli.commands import register_commands
from novel_tracker.utils.logging_config import setup_logging

setup_logging()

app = typer.Typer(help="Web Novel Tracker CLI")

register_commands(app)


def main():
    app()


if __name__ == "__main__":
    main()
