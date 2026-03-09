# Web Novel Tracker (CLI)

A Python CLI application for tracking reading progress across multiple web novels.

## Engineering Focus

This project was built to practice clean Python architecture, CLI tooling,
and testable design aligned with software quality engineering practices.


## Features

- Add and track web novels
- Update current chapter progress
- Store notes per novel
- Sort and filter tracked novels
- SQLite persistent storage
- CLI interface built with Typer
- Unit tested with Pytest
- Linting via Ruff
- CI validation via GitHub Actions

## Architecture

The project follows a layered architecture:

CLI Layer
↓
Service Layer
↓
Repository Layer
↓
SQLite Database

This separation allows business logic to be tested independently from the CLI.

## Example Commands

## Example Usage

## Example Usage

### Initialize the Database

Before using the tracker, initialize the SQLite database.

```bash
python -m novel_tracker init
```

Output:

```
Web Novel Tracker initialized.
```

---

### Add a New Novel

```bash
python -m novel_tracker add
```

The CLI will prompt for the required fields.

Example prompts:

```
Title: Lord of the Mysteries
Site: Webnovel
URL: https://example.com
Current Chapter: 120
Last Read Date: 2026-03-09
Notes: Starting the second arc
```

---

### List Tracked Novels

```bash
python -m novel_tracker list
```

or

```bash
python -m novel_tracker ls
```

Example output:

```
Title                   Site       Chapter
-------------------------------------------
Lord of the Mysteries   Webnovel   120
Reverend Insanity       Webnovel   450
```

---

### Get Details for a Specific Novel

```bash
python -m novel_tracker get "Lord of the Mysteries"
```

Example output:

```
Title: Lord of the Mysteries
Site: Webnovel
Current Chapter: 120
Last Read Date: 2026-03-09
Notes: Starting the second arc
```

---

### Update an Existing Novel

```bash
python -m novel_tracker update
```

The CLI will prompt for updated fields.

Example:

```
Title: Lord of the Mysteries
Current Chapter: 135
Last Read Date: 2026-03-10
Notes: Finished arc 2
```

---

### Delete a Novel

```bash
python -m novel_tracker delete "Lord of the Mysteries"
```

---

### Sort Results When Listing

```bash
python -m novel_tracker list --sort-by title
```

or

```bash
python -m novel_tracker list --sort-by last_read_date
```

---

### Show CLI Help

```bash
python -m novel_tracker --help
```

This displays all available commands and options.


