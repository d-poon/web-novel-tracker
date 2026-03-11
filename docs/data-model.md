# Data Model

## Overview

The Web Novel Tracker application stores information about web novels and a user's reading progress. The data model is intentionally simple, focusing on a single core entity: **Novel**.

The model is designed to support tracking reading progress, storing metadata about each novel, and allowing future extensions such as filtering, statistics, or additional metadata.

---

# Core Entity

## Novel

The **Novel** entity represents a single tracked web novel and its associated reading progress.

### Fields

| Field             | Type              | Description                             |
| ----------------- | ----------------- | --------------------------------------- |
| `title`           | string            | The title of the web novel              |
| `site`            | string (optional) | The website where the novel is hosted   |
| `current_chapter` | integer           | The latest chapter the user has read    |
| `last_read_date`  | date (optional)   | The date when the novel was last read   |
| `notes`           | string (optional) | User notes or reminders about the novel |

---

# Domain Model Representation

Within the application, the Novel entity is represented as a domain model.

Example conceptual representation:

```
Novel
 ├─ title
 ├─ site
 ├─ current_chapter
 ├─ last_read_date
 └─ notes
```

This domain model is used throughout the application for business logic and operations such as updating reading progress or generating statistics.

---

# Persistence Model

Novel data is stored locally using **SQLite**.

Each novel corresponds to a row in a database table.

Example conceptual schema:

```
novels
 ├─ id (primary key)
 ├─ title
 ├─ site
 ├─ current_chapter
 ├─ last_read_date
 └─ notes
```

The repository layer handles reading and writing this data while abstracting away database details from the rest of the application.

---

# Input Validation

User input is validated using schema models before being converted into domain objects.

Example input schema:

```
NovelCreate
 ├─ title
 ├─ site
 ├─ current_chapter
 └─ notes
```

Schemas ensure that:

* required fields are provided
* values are correctly typed
* invalid data is rejected before entering the domain layer

---

# Data Flow

The following sequence shows how novel data moves through the system:

```
CLI Input
   ↓
Schema Validation
   ↓
Domain Model Creation
   ↓
Repository Persistence
   ↓
SQLite Database
```

This layered approach ensures that validation, business logic, and persistence remain clearly separated.

---

# Future Extensions

The data model is designed to support future enhancements. Possible additions include:

* tracking total chapters
* reading status (reading, completed, dropped)
* rating or scoring
* tags or genres
* bookmark or favorite indicators

These extensions could be implemented without major architectural changes due to the current layered design.

---

# Summary

The Web Novel Tracker data model centers around the **Novel** entity, which captures reading progress and basic metadata about each tracked novel.

By separating domain models, validation schemas, and persistence logic, the application maintains a clean structure that supports both maintainability and future expansion.
