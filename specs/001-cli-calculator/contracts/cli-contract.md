# CLI Calculator API Contract

## Overview

This document defines the contract for the CLI calculator's command-line interface.

## Interface Specification

### Input Format

The calculator accepts expressions in the format:
```
<operand1> <operator> <operand2>
```

Where:
- `operand1` and `operand2` are numeric values (integers or decimals)
- `operator` is one of: +, -, *, /

### Output Format

#### Successful Calculations
- Output: `<result>` (single line, numeric value)
- Example: `2 + 3` → `5`

#### Error Conditions
- Output: `Error: <message>` (single line, error message)
- Examples:
  - `10 / 0` → `Error: Division by zero`
  - `5 @ 3` → `Error: Invalid operator`
  - `five + three` → `Error: Invalid input`

## Command Line Interface

### Invocation
```
python -m src.cli.calculator [<expression>]
```

If no expression is provided, the calculator will enter interactive mode.

### Interactive Mode
In interactive mode, the calculator will:
1. Display a prompt (e.g., "calc> ")
2. Accept expressions one at a time
3. Display results or errors
4. Continue until user exits (Ctrl+C or 'quit')

## Error Codes

| Error | Description |
|-------|-------------|
| 0 | Successful operation |
| 1 | Invalid input |
| 2 | Division by zero |
| 3 | Invalid operator |

## Examples

### Direct Expression
```bash
$ python -m src.cli.calculator "2 + 3"
5

$ python -m src.cli.calculator "10 / 0"
Error: Division by zero
```

### Interactive Mode
```bash
$ python -m src.cli.calculator
calc> 2 + 3
5
calc> 10 / 0
Error: Division by zero
calc> quit
```