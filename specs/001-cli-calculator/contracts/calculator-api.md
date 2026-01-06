# API Contract: Calculator Service

## Core Calculator Functions

### evaluate_expression(expression: str) -> float | int | str
**Description**: Evaluates a mathematical expression using secure parsing and returns the result or an error message. Implements safe evaluation to prevent code injection.

**Parameters**:
- `expression` (str): A mathematical expression containing numbers and operators (+, -, *, /, parentheses). Supports flexible formatting with or without spaces between operands and operators.

**Returns**:
- `float | int | str`: The calculated result as a number (with up to 10 decimal places precision), or an error message as a string starting with "Error:"; maintains application state after errors

**Examples**:
- Input: "5 + 3" → Output: 8
- Input: "3.14 * 2" → Output: 6.28
- Input: "5+3*2" → Output: 11  # Flexible formatting
- Input: "10 / 0" → Output: "Error: Division by zero"

**Error Cases**:
- Division by zero: Returns "Error: Division by zero"
- Invalid syntax: Returns "Error: Invalid expression"
- Non-numeric operands: Returns "Error: Invalid operands"
- Code injection attempts: Safely rejected by secure parser

### validate_expression(expression: str) -> bool
**Description**: Validates if an expression contains only valid mathematical characters.

**Parameters**:
- `expression` (str): A potential mathematical expression

**Returns**:
- `bool`: True if expression is valid, False otherwise

**Examples**:
- Input: "5 + 3" → Output: True
- Input: "abc + def" → Output: False

### parse_expression(expression: str) -> list[float | str]
**Description**: Parses an expression into a list of tokens (numbers and operators) using secure parsing. Supports flexible formatting with or without spaces between operands and operators.

**Parameters**:
- `expression` (str): A mathematical expression. Supports flexible formatting with or without spaces between operands and operators.

**Returns**:
- `list[float | str]`: A list of tokens representing the parsed expression; implements security validation to prevent code injection

**Examples**:
- Input: "5 + 3" → Output: [5.0, '+', 3.0]
- Input: "5+3" → Output: [5.0, '+', 3.0]  # Flexible formatting
- Input: "(2 + 3) * 4" → Output: ['(', 2.0, '+', 3.0, ')', '*', 4.0]

### get_calculation_history() -> list[tuple[str, str | float | int]]
**Description**: Retrieves the history of previous calculations for user reference.

**Parameters**: None
**Returns**:
- `list[tuple[str, str | float | int]]`: List of tuples containing (expression, result) for previous calculations

**Examples**:
- Input: None → Output: [("5 + 3", 8), ("10 - 4", 6), ("2 * 3", 6)]

## CLI Interface Functions

### run_interactive() -> None
**Description**: Starts the interactive command-line interface for the calculator with secure expression evaluation and history support.

**Parameters**: None
**Returns**: None

**Behavior**:
- Continuously prompts for user input with support for flexible formatting
- Evaluates expressions using secure parsing and displays results
- Handles commands like 'quit', 'exit', 'clear', and 'history'
- Supports multiple exit options: 'quit' command, 'exit' command, and Ctrl+C
- Maintains application state after errors to allow continued operation
- Maintains and displays calculation history for user reference
- Displays error messages appropriately without crashing

### run_single_expression(expression: str) -> None
**Description**: Evaluates a single expression and prints the result.

**Parameters**:
- `expression` (str): A mathematical expression to evaluate

**Returns**: None

**Behavior**:
- Evaluates the provided expression
- Prints the result to stdout
- Exits after single evaluation
