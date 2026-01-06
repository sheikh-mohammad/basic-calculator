---
id: "001"
title: "Python-based CLI Calculator Architecture"
status: "Accepted"
date: "2026-01-07"
references:
  - "specs/001-cli-calculator/plan.md"
  - "specs/001-cli-calculator/research.md"
  - ".specify/memory/constitution.md"
---

# ADR 001: Python-based CLI Calculator Architecture

## Context

We need to implement a command-line interface calculator that supports basic mathematical operations (addition, subtraction, multiplication, division) with proper order of operations (BODMAS). The solution must be cross-platform, secure, and follow the project constitution requirements for type hints and testing.

## Decision

We will implement the CLI calculator using:

- **Language**: Python 3.8+
- **Core Dependencies**: Built-in Python modules (ast, operator, sys, re)
- **Testing Framework**: pytest
- **Architecture**: Single-module application with separation of concerns
- **Type Hints**: Comprehensive typing as required by constitution

The architecture will be organized as:
- `core.py`: Main calculator logic with expression evaluation
- `parser.py`: Expression parsing and validation
- `cli.py`: Command-line interface
- Comprehensive test coverage using pytest

## Alternatives Considered

- **Alternative 1**: Third-party math libraries (e.g., numexpr, sympy)
  - Pros: More robust mathematical functions, built-in security
  - Cons: Increased dependencies, potential bloat for simple calculator

- **Alternative 2**: Multiple separate tools/libraries (argparse, click, etc.)
  - Pros: Feature-rich CLI capabilities
  - Cons: Violates minimal dependency principle from constitution

- **Alternative 3**: Different languages (JavaScript/Node.js, Go)
  - Pros: Different ecosystems, performance characteristics
  - Cons: Doesn't align with constitution requirements, team familiarity

## Consequences

### Positive
- Leverages Python's built-in security features (avoiding eval())
- Cross-platform compatibility out-of-the-box
- Aligns with constitution requirements for type hints and testing
- Minimal external dependencies reduce maintenance burden
- Built-in AST module provides safe expression evaluation
- pytest provides comprehensive testing capabilities

### Negative
- Need to implement custom parser instead of using built-in eval()
- Additional complexity in handling operator precedence manually
- Limited by Python's floating-point precision (though adequate for calculator)

## Status

Accepted - Aligns with project constitution and technical requirements.