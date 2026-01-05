<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.0.0 (initial creation)
Modified principles: none (new file)
Added sections: All sections
Removed sections: none
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: none
-->
# Basic Calculator Constitution

## Core Principles

### I. Mathematical Accuracy
All calculations must maintain high precision for both integer and floating-point arithmetic. Decimal calculations must preserve precision according to mathematical standards. Order of operations must follow BODMAS rules (Brackets, Orders, Division/Multiplication, Addition/Subtraction).

### II. User Input Validation
All user inputs must be validated before processing. Invalid inputs must be rejected gracefully with clear error messages. Division by zero must be detected and handled appropriately. Overflow conditions must be detected and managed.

### III. Test-First (NON-NEGOTIABLE)
All functionality must be covered by unit tests before implementation. TDD approach required: Tests written → Test approval → Tests fail → Implementation → Tests pass. Frontend tests using Jest/Vitest, backend tests using pytest.

### IV. Cross-Platform Compatibility
The calculator must function identically across all supported platforms. Mobile responsiveness is mandatory. Keyboard and click input methods must both be supported. Display must be clear and accessible on all screen sizes.

### V. Error Handling and Recovery
All error conditions must be anticipated and handled gracefully. Error messages must be user-friendly and actionable. The calculator must return to a valid state after error conditions. Clear functions (C, CE) must be available for error recovery.

### VI. Minimalist Interface Design
User interface must follow minimalistic design principles. Only essential elements must be displayed. Visual design must prioritize usability over decorative elements. Target users are general users requiring basic to intermediate calculations.

## Technical Constraints

The following constraints must be adhered to in all implementations:
- Frontend: HTML, CSS, JavaScript with Tailwind CSS for styling
- Backend: Python for complex calculations with type hints for clarity
- Platform: Must be mobile responsive
- Deployment: Vercel CLI for deployment
- Testing: Unit tests required for both frontend (Jest/Vitest) and backend (pytest)

## Development Workflow

All changes must follow the red-green-refactor cycle. Code reviews must verify compliance with all principles. New features must include corresponding tests. Error handling must be implemented before core functionality. Performance considerations must be validated for all mathematical operations.

## Governance

This constitution supersedes all other development practices for the Basic Calculator project. All code changes must demonstrate compliance with these principles. Amendments to this constitution require documentation of rationale and approval. 

Version: 1.0.0 | Ratified: 2026-01-05 | Last Amended: 2026-01-05