# Basic CLI Calculator Constitution

## Core Principles

### I. Library-First
Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries
Every component of the calculator must be implemented as a reusable library module that can be tested independently.

### II. CLI Interface
Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats
The calculator must expose its functionality through a command-line interface with clear input/output protocols.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced
All calculator functionality must be developed using test-driven development practices with comprehensive test coverage.

### IV. Integration Testing
Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas
Integration tests must cover the interaction between different calculator components and edge cases like division by zero.

### V. Observability, Versioning & Breaking Changes, Simplicity
Text I/O ensures debuggability; Structured logging required; Or: MAJOR.MINOR.BUILD format; Or: Start simple, YAGNI principles
The calculator should provide clear output and logging for debugging, use semantic versioning, and follow the principle of simplicity.

### VI. Type Safety
Type hints must be used consistently throughout the codebase to ensure code correctness and maintainability.
Python type hints are mandatory for all functions, classes, and variables to improve code clarity and catch potential errors early.

## Development Constraints

### Technology Stack
Python 3.8+ with uv package manager; Type hints required for all code; Standard library modules preferred where possible.

### Testing Requirements
All code must have comprehensive unit tests covering normal operations, edge cases, and error conditions. Tests must be executable with pytest.

## Development Workflow

### Code Review Process
All changes must undergo peer review before merging. Pull requests must include passing tests and documentation updates.

### Release Process
Releases follow semantic versioning (MAJOR.MINOR.PATCH). Breaking changes require major version bumps, new features minor, and bug fixes patch.

## Governance
Constitution supersedes all other practices; Amendments require documentation, approval, migration plan
All PRs/reviews must verify compliance; Complexity must be justified; Use .specify/templates/commands/ for runtime development guidance

**Version**: 1.0.0 | **Ratified**: 2026-03-19 | **Last Amended**: 2026-03-19