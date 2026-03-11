# Architecture

## Overview

**Web Novel Tracker** is a CLI-based application designed to track reading progress for web novels. The system follows a **layered architecture inspired by Clean Architecture principles**, separating responsibilities across domain logic, application orchestration, infrastructure, and user interface layers.

This structure improves maintainability, testability, and extensibility while keeping the domain logic independent of external systems.

---

# Architectural Layers

The project is organized into several logical layers:

```
CLI (Typer Commands)
        ↓
Application Services
        ↓
Domain Models
        ↓
Repository Interfaces
        ↓
Infrastructure Implementations
```

Each layer has a clearly defined responsibility and dependency direction.

Dependencies always flow **inward toward the domain layer**, preventing infrastructure or UI concerns from polluting business logic.

---

# Layer Responsibilities

## CLI Layer (`cli/`)

The CLI layer provides the user interface through command-line commands implemented with Typer.

Responsibilities:

* Parsing command-line arguments
* Invoking application services
* Formatting output for display
* Handling user interaction

Example responsibilities:

* `novel-tracker add`
* `novel-tracker list`
* `novel-tracker update`
* `novel-tracker stats`

The CLI layer **should not contain business logic**.

---

## Application Layer (`application/`)

The application layer orchestrates the core workflows of the system.

Responsibilities:

* Coordinating domain objects
* Calling repository interfaces
* Executing application use cases
* Managing transaction boundaries

Example responsibilities:

* Creating novels
* Updating chapter progress
* Retrieving lists of novels
* Calculating reading statistics

Application services act as the **bridge between the CLI and domain layers**.

---

## Domain Layer (`domain/`)

The domain layer contains the **core business logic and entities** of the application.

Responsibilities:

* Defining domain models
* Enforcing business rules
* Representing the core concepts of the system

Example domain entity:

```
Novel
 ├─ title
 ├─ site
 ├─ current_chapter
 ├─ last_read_date
 └─ notes
```

The domain layer is intentionally independent of:

* databases
* frameworks
* CLI logic

This ensures the business logic remains stable even if infrastructure changes.

---

## Repository Interfaces (`domain/repositories/`)

Repository interfaces define how the domain interacts with persistence mechanisms.

Responsibilities:

* Declaring methods for data access
* Abstracting away storage implementation details

Example interface methods:

```
add_novel()
get_novels()
update_novel()
delete_novel()
```

The domain and application layers depend only on these **interfaces**, not on concrete database implementations.

---

## Infrastructure Layer (`infrastructure/`)

The infrastructure layer implements external system integrations.

Responsibilities:

* Database connections
* Repository implementations
* Logging configuration
* File system interactions

Example infrastructure components:

```
SQLite repository implementation
Database connection management
Application logging
```

Infrastructure components fulfill the contracts defined by repository interfaces.

---

# Data Flow Example

Example flow for adding a novel:

```
User runs CLI command
      ↓
CLI command parses arguments
      ↓
Application service receives validated data
      ↓
Domain model is created
      ↓
Repository interface is called
      ↓
SQLite repository persists the data
```

This separation ensures each layer has a single responsibility.

---

# Schema Validation

Input validation is handled using **Pydantic schemas** located in the `schemas/` directory.

Schemas are responsible for:

* Validating user input
* Enforcing input constraints
* Converting input into structured data

Example schema:

```
NovelCreate
 ├─ title
 ├─ site
 ├─ current_chapter
 └─ notes
```

Schemas are used before creating domain models to ensure the application receives valid data.

---

# Testing Strategy

The project uses **pytest** for automated testing.

Tests are separated into:

```
tests/
   unit/
   integration/
```

Unit tests verify:

* domain model behavior
* application services
* validation logic

Integration tests verify:

* repository interactions
* CLI command behavior
* database integration

This layered testing approach ensures both correctness and reliability.

---

# Design Goals

The architecture aims to achieve the following goals:

### Maintainability

Clear separation of responsibilities makes the system easier to modify and extend.

### Testability

Business logic can be tested independently from infrastructure.

### Flexibility

Storage mechanisms or UI layers can be replaced without modifying domain logic.

### Simplicity

Despite using layered architecture concepts, the implementation remains lightweight and suitable for a small CLI application.

---

# Future Improvements

Potential architectural improvements include:

* Adding database migrations
* Supporting alternative storage backends
* Implementing import/export functionality
* Adding more advanced CLI filtering and sorting

These enhancements can be implemented without major architectural changes due to the current layered design.

---

# Summary

The Web Novel Tracker project demonstrates a practical implementation of layered architecture for a Python CLI application.

By separating the system into CLI, application, domain, repository, and infrastructure layers, the project maintains clear boundaries between concerns while remaining easy to understand and extend.
