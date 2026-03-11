# Web Novel Tracker (CLI)

![Python](https://img.shields.io/badge/python-3.11-blue)
![CLI](https://img.shields.io/badge/CLI-Typer-green)
![Lint](https://img.shields.io/badge/lint-ruff-yellow)
![Database](https://img.shields.io/badge/database-SQLite-lightgrey)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)
![Architecture](https://img.shields.io/badge/architecture-layered-blueviolet)
![Tests](https://github.com/d-poon/web-novel-tracker/actions/workflows/tests.yml/badge.svg)

A Python CLI application for tracking reading progress across multiple web novels.

---

# Engineering Focus

This project was built to practice clean Python architecture, CLI tooling,  
and testable design aligned with software quality engineering practices.

The system emphasizes:

- separation of concerns
- layered architecture
- deterministic testing
- maintainable CLI tooling

---

## Installation

Clone the repository:

git clone https://github.com/d-poon/web-novel-tracker.git

cd web-novel-tracker

Create and activate a virtual environment:

python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

Install the project:

pip install -e .

This install the CLI command:

novel-tracker

## Quick Start

Initialize t he database:

novel-tracker db init

Add a novel:

novel-tracker novel add

List tracked novels:

novel-tracker novel list

## Development

Project progress is tracked using a GitHub Project Board:

👉 https://github.com/users/d-poon/projects/1

### Setup Development Environment

Install development dependencies:

pip install .[dev]

The [dev] extra installs additional development tools defined in
pyproject.toml, including:

pytest (testing)

pytest-cov (coverage reporting)

ruff (linting)

### Running Tests

Run the full test suite:

pytest

Run tests with coverage reporting:

pytest

## Features

- Add and track web novels
- Update current chapter progress
- Store notes per novel
- Sort and filter tracked novels
- SQLite persistent storage
- CLI interface built with Typer
- Linting via Ruff
- Automated testing with Pytest

## Technology Stack

Python 3.11+

Core tools:

- Typer (CLI framework)
- SQLite (local persistent storage)
- Pydantic (data validation)
- Ruff (linting and formatting)
- Pytest (testing framework)
- Pytest-cov (coverage reporting)

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

novel-tracker db init

Output:

Web Novel Tracker initialized.

---

### Add a New Novel

novel_tracker novel add

The CLI will prompt for the required fields.

Example prompts:

Title: Lord of the Mysteries
Site: Webnovel
URL: https://example.com
Current Chapter: 120
Last Read Date: 2026-03-09
Notes: Starting the second arc

---

### List Tracked Novels

novel_tracker novel list

or

novel_tracker novel ls

Example output:

Title                   Site       Chapter
-------------------------------------------
Lord of the Mysteries   Webnovel   120
Reverend Insanity       Webnovel   450

---

### Get Details for a Specific Novel

novel_tracker novel get "Lord of the Mysteries"

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

novel_tracker novel update

The CLI will prompt for updated fields.

Example:

Title: Lord of the Mysteries
Current Chapter: 135
Last Read Date: 2026-03-10
Notes: Finished arc 2

---

### Delete a Novel

novel_tracker novel delete "Lord of the Mysteries"

---

### Sort Results When Listing

novel_tracker novel list --sort-by title

or

novel_tracker novel list --sort-by last_read_date

---

### Show CLI Help

novel_tracker --help

This displays all available commands and options.

## Testingg Strategy
The project includes automated tests written with Pytest.

Testing focuses on:

- application service logic
- input validation and schema behavior
- repository persistence logic
- CLI command behavior

Tests are organized into:

tests/
  unit/
  integration/

Coverage reports can be generated using:

pytest --cov=novel_tracker

## Documentation

- [Architecture](docs/architecture.md)
- [Testing](docs/testing.md)
- [Project Board](docs/project-board.md)
- [Data Model](docs/data-model.md)

## Roadmap

Planned improvements:

- Expand automated test coverage
- Add repository integration tests
- Add CLI command tests
- Improve filtering and sorting capabilities
- Add export/import functionality
- Improve statistics reporting
