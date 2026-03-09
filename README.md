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

Add a novel:
