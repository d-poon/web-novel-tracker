# Web Novel Tracker (CLI)

![Python](https://img.shields.io/badge/python-3.11-blue)
![CLI](https://img.shields.io/badge/CLI-Typer-green)
![Lint](https://img.shields.io/badge/lint-ruff-yellow)
![Database](https://img.shields.io/badge/database-SQLite-lightgrey)

A Python CLI application for tracking reading progress across multiple web novels.

## Engineering Focus

This project was built to practice clean Python architecture, CLI tooling,
and testable design aligned with software quality engineering practices.

## Installation

Clone the repository:

git clone https://github.com/d-poon/web-novel-tracker.git

cd web-novel-tracker

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

Install dependencies:

pip install -e .

## Development

Project progress is tracked using a GitHub Project Board:

👉 https://github.com/users/d-poon/projects/1

## Features

- Add and track web novels
- Update current chapter progress
- Store notes per novel
- Sort and filter tracked novels
- SQLite persistent storage
- CLI interface built with Typer
- Linting via Ruff

## Technology Stack

Python 3.11+

Core tools:

- Typer (CLI framework)
- SQLite (local persistence)
- Pydantic (data validation)
- Ruff (linting)
- Pytest (planned testing framework)

Development tooling:

- GitHub Actions (CI)
- GitHub Projects (task tracking)

## Architecture

The project follows a layered architecture designed to separate concerns
and keep business logic independent from infrastructure.

User CLI
   │
   ▼
CLI Commands (Typer)
   │
   ▼
Application Services
   │
   ▼
Domain Models
   │
   ▼
Repository Layer
   │
   ▼
SQLite Database

## Project Structure

web-novel-tracker/
│
├── src/novel_tracker/
│   ├── cli/              # CLI commands and interface
│   ├── application/      # Application services
│   ├── domain/           # Core domain models
│   ├── repositories/     # Repository interfaces
│   ├── infrastructure/   # Database and external integrations
│   └── schemas/          # Input validation schemas
│
├── tests/                # Test suite
├── docs/                 # Project documentation
└── pyproject.toml

## Example Usage

### Initialize the Database

Before using the tracker, initialize the SQLite database.

```bash
python -m novel_tracker db init
```

Output:

```
Web Novel Tracker initialized.
```

---

### Add a New Novel

```bash
python -m novel_tracker novel add
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
python -m novel_tracker novel list
```

or

```bash
python -m novel_tracker novel ls
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
python -m novel_tracker novel get "Lord of the Mysteries"
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
python -m novel_tracker novel update
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
python -m novel_tracker novel delete "Lord of the Mysteries"
```

---

### Sort Results When Listing

```bash
python -m novel_tracker novel list --sort-by title
```

or

```bash
python -m novel_tracker novel list --sort-by last_read_date
```

---

### Show CLI Help

```bash
python -m novel_tracker --help
```

This displays all available commands and options.

## Documentation

- [Architecture](docs/architecture.md)
- [Testing](docs/testing.md)
- [Project Board](docs/project-board.md)
- [Data Model](docs/data-model.md)

## Roadmap

Planned improvements:

- Add pytest test suite
- Improve CLI filtering and sorting
- Add export/import functionality
- Improve statistics reporting
- Expand test coverage

