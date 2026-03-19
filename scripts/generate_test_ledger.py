# scripts/generate_test_ledger.py

import ast
import importlib.util
import inspect
import subprocess
from datetime import date
from pathlib import Path

# CONFIGURATION
TESTS_DIR = Path(__file__).parent.parent / "tests"
FIXTURES_DIR = TESTS_DIR / "fixtures"
OUTPUT_FILE = TESTS_DIR / "TEST_LEDGER.md"

# Test function marker names
AI_MARKER = "generated_by_ai"
HUMAN_ADDED = "human_added"
HUMAN_REVIEWED = "human_reviewed"

# Fixture metadata attributes
FIXTURE_FLAGS = ["is_ai_generated", "is_human_added", "is_human_reviewed"]

# Get today's date in YYYY-MM-DD format
today = date.today().isoformat()


# -------------------- HELPERS ---------------------
# Function to get git username for attribution
def get_git_username():
    """Get the current git username for attribution."""
    try:
        name = (
            subprocess.check_output(["git", "config", "user.name"])
            .decode("utf-8")
            .strip()
        )
        return name if name else "Unknown"
    except Exception:
        return "Unknown"


# Helper to parse pytest.mark decorators
def get_test_markers(func_node):
    markers = []
    for decorator in func_node.decorator_list:
        # @pytest.mark.marker_name
        if isinstance(decorator, ast.Attribute) and decorator.attr in [
            AI_MARKER,
            HUMAN_ADDED,
            HUMAN_REVIEWED,
        ]:
            markers.append(decorator.attr)
        # @pytest.mark.marker_name(...)
        elif isinstance(decorator, ast.Call):
            if isinstance(decorator.func, ast.Attribute) and decorator.func.attr in [
                AI_MARKER,
                HUMAN_ADDED,
                HUMAN_REVIEWED,
            ]:
                markers.append(decorator.func.attr)
    return markers


def import_fixtures_from_dir(fixtures_path: Path):
    """
    Scan a directory of fixture modules and return all fixture functions.

    Uses AST parsing to detect @pytest.fixture decorators, then imports the
    module only to access function objects and metadata (docstrings, flags).
    """
    fixtures = []

    for file_path in fixtures_path.rglob("*.py"):
        if file_path.name == "__init__.py":
            continue

        # Step 1 — parse AST to find fixture function names
        with open(file_path, encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=str(file_path))

        fixture_names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for dec in node.decorator_list:
                    # Match @pytest.fixture or @pytest.fixture(...)
                    if (isinstance(dec, ast.Attribute) and dec.attr == "fixture") or (
                        isinstance(dec, ast.Call)
                        and isinstance(dec.func, ast.Attribute)
                        and dec.func.attr == "fixture"
                    ):
                        fixture_names.append(node.name)

        if not fixture_names:
            continue  # skip files with no fixtures

        # Step 2 — import the module dynamically
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Step 3 — collect fixture functions and their metadata
        for name in fixture_names:
            func = getattr(module, name, None)
            if not func:
                continue
            # Include any metadata flags even if False
            fixtures.append((name, func))

    return fixtures


def truncate_name(s, max_length=50):
    """Truncate a string to a maximum length, adding ellipsis if needed."""
    return s if len(s) <= max_length else s[: max_length - 3] + "..."


def truncate_notes(notes, max_length=80):
    """Truncate notes to a maximum length for display in the ledger."""
    if not notes:
        return ""
    return notes if len(notes) <= max_length else notes[: max_length - 3] + "..."


def shorten_module_path(module_path, max_length=30):
    """Shorten a module path to fit within a maximum length."""
    if len(module_path) <= max_length:
        return module_path
    parts = module_path.split("/")
    if len(parts) <= 2:
        return truncate_name(module_path, max_length)
    return f"{parts[0]}/.../{parts[-1]}"


# --------------------- COLLECT TESTS ----------------------
test_entries = []

for py_file in TESTS_DIR.rglob("test_*.py"):
    with py_file.open("r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=str(py_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
                markers = get_test_markers(node)
                entry = {
                    "name": truncate_name(node.name),
                    "module": shorten_module_path(py_file.name),
                    "ai_scaffold": "✅" if AI_MARKER in markers else "",
                    "human_added": "✅" if HUMAN_ADDED in markers else "",
                    "human_reviewed": "✅" if HUMAN_REVIEWED in markers else "",
                    "notes": "",
                    "type": "test",
                }
                test_entries.append(entry)

# --------------------- COLLECT FIXTURES ----------------------
fixture_entries = []

fixtures = import_fixtures_from_dir(FIXTURES_DIR)

for name, fix in fixtures:
    fixture_entries.append(
        {
            "name": name,
            "module": fix.__module__,
            "type": "fixture",
            "ai_scaffold": "✅" if getattr(fix, "is_ai_generated", False) else "",
            "human_added": "✅" if getattr(fix, "is_human_added", False) else "",
            "human_reviewed": "✅" if getattr(fix, "is_human_reviewed", False) else "",
            "notes": truncate_notes(inspect.getdoc(fix) or "", 60),
        }
    )

# --------------------- SORT TESTS AND FIXTURES ----------------------

# Sort by AI first, then human added, then human reviewed
test_entries.sort(key=lambda x: x["ai_scaffold"], reverse=True)
fixture_entries.sort(key=lambda x: x["ai_scaffold"], reverse=True)


# --------------------- Generate Markdown ---------------------


def get_column_widths(rows, headers):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    return widths


def format_row(row, widths):
    # Add one space padding on both sides for readability
    return (
        "| "
        + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))
        + " |"
    )


def entry_to_row(entry):
    """Convert a fixture or test entry into a table row, truncating long notes."""
    return [
        truncate_name(entry["name"], 35),
        truncate_name(entry["module"], 20),
        entry["type"],
        entry["ai_scaffold"],
        entry["human_added"],
        entry["human_reviewed"],
        truncate_notes(entry.get("notes", ""), 60),
    ]


def generate_markdown_table(entries):
    headers = [
        "Name",
        "Module",
        "Type",
        "AI?",
        "NonAI?",
        "Reviewed?",
        "Notes",
    ]

    rows = [entry_to_row(entry) for entry in entries]

    widths = get_column_widths(rows, headers)

    table = [format_row(headers, widths)]
    # Add separator row
    table.append("| " + " | ".join("-" * w for w in widths) + " |")
    for row in rows:
        table.append(format_row(row, widths))

    return "\n".join(table)


with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    f.write("_This file is auto-generated. Do not edit manually._\n\n")
    f.write("# AI vs Human Test Ledger\n\n")
    f.write("**Project:** Novel Tracker\n")
    f.write(f"**Maintainer:** {get_git_username()}\n")
    f.write(f"**Date:** {today}\n\n")

    f.write("## Test Matrix\n\n")
    f.write(generate_markdown_table(test_entries))

    f.write("\n\n## Fixture Matrix\n\n")
    f.write(generate_markdown_table(fixture_entries))

print(f"✅ TEST_LEDGER.md generated at {OUTPUT_FILE}")
