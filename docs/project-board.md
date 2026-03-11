# Project Board Workflow

## Overview

The Web Novel Tracker project uses a **GitHub Project board** to manage development tasks, track progress, and organize work. The board follows a simplified **Kanban workflow**, allowing issues to move through different stages from planning to completion.

The board provides visibility into:

* current development work
* planned features
* completed tasks
* overall project progress

---

# Workflow Stages

The project board contains the following columns:

```
Backlog → Planned → In Progress → Done
```

Each column represents a stage in the development lifecycle.

---

## Backlog

The **Backlog** contains all issues that represent potential work for the project.

Typical backlog items include:

* feature ideas
* architectural improvements
* bug reports
* technical debt
* documentation tasks

Issues remain in the backlog until they are prioritized for development.

---

## Planned

Issues move to **Planned** once they are selected for implementation.

At this stage:

* requirements are understood
* the task is scoped
* the issue may be assigned to a developer

Planned issues represent the **next set of work to be implemented**.

---

## In Progress

Issues move to **In Progress** when active development begins.

Typical activities during this stage include:

* implementing the feature
* writing tests
* refactoring code
* updating documentation

Issues in this stage should usually have:

* an assigned developer
* an associated branch or pull request

---

## Done

Issues move to **Done** once the work has been completed.

Completion typically means:

* code has been implemented
* tests are passing
* the issue has been closed
* changes have been merged into the main branch

Closed issues serve as a record of completed work and project history.

---

# Issue Lifecycle

The typical lifecycle for a task is:

```
Issue created
      ↓
Added to Backlog
      ↓
Moved to Planned when prioritized
      ↓
Moved to In Progress when development begins
      ↓
Closed and moved to Done when complete
```

This process keeps work organized and transparent.

---

# Issue Types

Issues may represent different kinds of work, such as:

### Feature

New functionality added to the application.

Examples:

* Add CLI command to update chapter progress
* Implement novel statistics tracking

---

### Bug

Issues that fix incorrect or unexpected behavior.

Examples:

* Fix incorrect chapter sorting
* Handle missing novel titles during input

---

### Chore

Maintenance tasks that improve the project but do not add new functionality.

Examples:

* Refactor repository structure
* Improve logging configuration
* Update project documentation

---

### Documentation

Tasks focused on improving project documentation.

Examples:

* Add architecture documentation
* Update README usage examples

---

# Relationship Between Issues and Commits

Development tasks are tracked using GitHub issues. When implementing a task, commits may reference the corresponding issue.

Example commit message:

```
feat: implement novel statistics command

Fixes #12
```

When merged into the main branch, GitHub automatically closes the referenced issue.

---

# Milestones

Milestones are used to group related issues into larger project goals.

Examples of milestones may include:

* MVP CLI functionality
* Repository persistence layer
* Testing improvements

Milestones provide a way to measure progress toward larger deliverables.

---

# Benefits of the Workflow

Using a structured project board provides several benefits:

* clear visibility of project progress
* organized task management
* traceability between issues and commits
* easier prioritization of future work

This workflow helps keep development organized while maintaining a simple and transparent process.

---

# Summary

The GitHub Project board serves as the central tool for managing work within the Web Novel Tracker project. By organizing tasks into clear stages, the board helps maintain a structured development process while keeping project progress easy to track.
