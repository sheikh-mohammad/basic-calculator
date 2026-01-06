<!-- SYNC IMPACT REPORT
Version change: 1.2.0 → 1.3.0 (minor enhancement)
Modified principles: None
Added sections: Technical Constraints update (added uv package manager)
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: Update all templates to reference uv package manager
-->
# Basic Calculator Constitution

## Core Principles

### I. Mathematical Accuracy
All calculations must maintain high precision for both integer and floating-point arithmetic. Decimal calculations must preserve precision according to mathematical standards. Order of operations must follow BODMAS rules (Brackets, Orders, Division/Multiplication, Addition/Subtraction). The calculator must support the core mathematical operations: Addition (+), Subtraction (-), Multiplication (*), and Division (/).

### II. User Input Validation
All user inputs must be validated before processing. Invalid inputs must be rejected gracefully with clear error messages. Division by zero must be detected and handled appropriately. Overflow conditions must be detected and managed. Invalid operations must be identified and handled with appropriate user feedback.

### III. Test-First (NON-NEGOTIABLE)
All functionality must be covered by unit tests before implementation. TDD approach required: Tests written → Test approval → Tests fail → Implementation → Tests pass. Frontend tests using Jest/Vitest, backend tests using pytest.

### IV. Cross-Platform Compatibility
The calculator must function identically across all supported platforms. Mobile responsiveness is mandatory. Keyboard and click input methods must both be supported. Display must be clear and accessible on all screen sizes. Implementation will follow a phased approach: Phase 1 includes keyboard input (CLI), Phase 2 adds click buttons with both keyboard and click input support.

### V. Error Handling and Recovery
All error conditions must be anticipated and handled gracefully. Error messages must be user-friendly and actionable. The calculator must return to a valid state after error conditions. Clear functions (C, CE) must be available for error recovery. Optional previous calculation history must be maintained for user reference.

### VI. Minimalist Interface Design
User interface must follow minimalistic design principles. Only essential elements must be displayed. Visual design must prioritize usability over decorative elements. Target users are general users requiring basic to intermediate calculations. Display must show current input and optionally previous calculation history.

### VII. Atomic Commits
All commits must be atomic, containing the smallest possible logical change. Each commit must represent a single, complete feature, bug fix, or improvement. Every code change must be accompanied by running `/sp.git_commit_pr` to ensure proper commit and pull request creation. Commits must have clear, descriptive messages following conventional commit format.

### VIII. Spec-Driven Development (SDD)
All development must follow Spec-Driven Development principles. Features must be specified before implementation with clear user stories, requirements, and success criteria. Design documents must be created and approved before coding begins. Implementation must strictly adhere to specifications with any deviations requiring specification updates.

### IX. Python Type Hints
All Python code must include comprehensive type hints for function parameters, return values, and variable declarations. Type hints must accurately reflect the actual types used and be maintained throughout the development lifecycle. Static type checking must pass before code is committed.

### X. Code Documentation
All code must include appropriate documentation and comments explaining complex logic, algorithms, and business rules. Public functions, classes, and modules must have docstrings describing their purpose, parameters, and return values. Comments must explain the "why" behind non-obvious implementation choices, not just the "what".

## Technical Constraints

The following constraints must be adhered to in all implementations:
- Frontend: HTML, CSS, JavaScript with Tailwind CSS for styling
- Backend: Python for complex calculations with type hints for clarity
- Package Management: Use uv as the Python package manager for fast dependency resolution and installation
- Platform: Must be mobile responsive
- Deployment: Vercel CLI for deployment
- Testing: Unit tests required for both frontend (Jest/Vitest) and backend (pytest)
- Git workflow: All changes must be committed using atomic commits and `/sp.git_commit_pr` command

## Development Workflow

All changes must follow the red-green-refactor cycle. Code reviews must verify compliance with all principles. New features must include corresponding tests. Error handling must be implemented before core functionality. Performance considerations must be validated for all mathematical operations. Implementation should follow phased delivery approach where Phase 1 delivers core functionality and Phase 2 adds enhanced features. All code changes must follow Spec-Driven Development principles with proper specifications created before implementation.

## Governance

This constitution supersedes all other development practices for the Basic Calculator project. All code changes must demonstrate compliance with these principles. Amendments to this constitution require documentation of rationale and approval.

Version: 1.3.0 | Ratified: 2026-01-05 | Last Amended: 2026-01-07
