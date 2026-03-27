import sys
from typing import Any

import typer


def prompt_if_interactive(value: Any, prompt_text: str, default: Any = "") -> Any:
    """
    Prompt the user only if running interactively (stdin is a tty) and value is None.

    Args:
        value: Current value of the field.
        prompt_text: Text to display to the user.
        default: Default value if user presses Enter.

    Returns:
        The original value if not None, or user input if prompted.
    """
    if sys.stdin.isatty():
        return typer.prompt(prompt_text) if value is None else value
    return value
