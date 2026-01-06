---
id: "002"
title: "Secure Expression Evaluation Approach"
status: "Accepted"
date: "2026-01-07"
references:
  - "specs/001-cli-calculator/plan.md"
  - "specs/001-cli-calculator/research.md"
  - "specs/001-cli-calculator/data-model.md"
---

# ADR 002: Secure Expression Evaluation Approach

## Context

The calculator needs to evaluate mathematical expressions provided by users. This presents a security risk if not handled properly, as naive implementations using eval() can execute arbitrary code. We need a safe approach that handles mathematical operations while preventing code injection.

## Decision

We will implement a custom expression evaluator using Python's AST (Abstract Syntax Tree) module to safely parse and evaluate mathematical expressions. This approach:

- Parses expressions into an AST representation
- Validates the AST contains only allowed operations (+, -, *, /, parentheses, numbers)
- Evaluates the safe AST to compute the result
- Provides proper operator precedence (BODMAS) naturally through AST structure

Dependencies will be managed using uv for fast dependency resolution and installation.

## Alternatives Considered

- **Alternative 1**: Using Python's `eval()` function
  - Pros: Simple implementation, handles all operations automatically
  - Cons: Major security vulnerability allowing arbitrary code execution

- **Alternative 2**: Third-party expression evaluation libraries (e.g., numexpr)
  - Pros: Robust, well-tested, handles complex expressions
  - Cons: Adds external dependency, potentially overkill for basic calculator

- **Alternative 3**: Manual tokenization and evaluation with precedence rules
  - Pros: Complete control over allowed operations, educational value
  - Cons: More complex implementation, potential for precedence bugs

## Consequences

### Positive
- Secure against code injection attacks
- Maintains full control over allowed operations
- Properly handles operator precedence naturally
- Aligns with minimal dependency requirements
- Provides educational value in understanding expression parsing
- uv package manager ensures fast dependency resolution and installation

### Negative
- More complex implementation than using eval()
- Requires custom AST traversal logic
- Potential performance overhead compared to native eval()
- Need to handle edge cases (division by zero, precision) manually

## Status

Accepted - Security considerations outweigh implementation complexity concerns.