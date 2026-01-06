---
id: "004"
title: "Flexible CLI Interface Design"
status: "Accepted"
date: "2026-01-07"
references:
  - "specs/001-cli-calculator/plan.md"
  - "specs/001-cli-calculator/research.md"
  - "specs/001-cli-calculator/spec.md"
---

# ADR 004: Flexible CLI Interface Design

## Context

The calculator needs to provide a user-friendly command-line interface that supports both single-expression mode and interactive mode. The interface should accommodate flexible input formats and provide multiple ways to exit the application. Users should be able to enter expressions with or without spaces.

## Decision

We will implement a flexible CLI interface with:

- **Interactive Mode**: Continuous prompt for expressions until user exits
- **Flexible Formatting**: Support for expressions with or without spaces between operands and operators
- **Multiple Exit Options**: Support for 'quit', 'exit' commands and Ctrl+C
- **Built-in Python Functions**: Using `input()` for prompts and `sys` for exit handling
- **Clear Prompts**: User-friendly prompts and clear result display

The interface will preprocess input to handle flexible formatting and provide consistent user experience.

## Alternatives Considered

- **Alternative 1**: Strict formatting requirements (require spaces between operands/operators)
  - Pros: Simplified parsing logic
  - Cons: Less user-friendly, restrictive input format

- **Alternative 2**: Third-party CLI libraries (click, typer, argparse)
  - Pros: Feature-rich, built-in validation
  - Cons: Violates minimal dependency principle, overkill for simple calculator

- **Alternative 3**: Single-mode interface (only interactive OR single expression)
  - Pros: Simplified implementation
  - Cons: Less flexible for different use cases

## Consequences

### Positive
- User-friendly interface supporting various input styles
- Flexible usage patterns (interactive or single expressions)
- Multiple exit options for user preference
- Minimal dependencies as required by constitution
- Consistent cross-platform experience

### Negative
- More complex input parsing to handle flexible formatting
- Need to implement custom tokenizer for flexible input
- Additional validation for exit commands
- More complex state management for interactive mode

## Status

Accepted - Enhances user experience while maintaining simplicity and minimal dependencies.