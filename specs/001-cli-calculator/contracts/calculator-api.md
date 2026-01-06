# API Contract: Calculator Service

## Core Calculator Functions

### evaluate_expression(expression: str) -> float | int | str
**Description**: Evaluates a mathematical expression and returns the result or an error message.

**Parameters**:
- `expression` (str): A mathematical expression containing numbers and operators (+, -, *, /, parentheses). Supports flexible formatting with or without spaces between operands and operators.

**Returns**:
- `float | int | str`: The calculated result as a number (with up to 10 decimal places precision), or an error message as a string starting with "Error:"

**Examples**:
- Input: "5 + 3" → Output: 8
- Input: "3.14 * 2" → Output: 6.28
- Input: "5+3*2" → Output: 11  # Flexible formatting
- Input: "10 / 0" → Output: "Error: Division by zero"

**Error Cases**:
- Division by zero: Returns "Error: Division by zero"
- Invalid syntax: Returns "Error: Invalid expression"
- Non-numeric operands: Returns "Error: Invalid operands"

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
**Description**: Parses an expression into a list of tokens (numbers and operators). Supports flexible formatting with or without spaces between operands and operators.

**Parameters**:
- `expression` (str): A mathematical expression. Supports flexible formatting with or without spaces between operands and operators.

**Returns**:
- `list[float | str]`: A list of tokens representing the parsed expression

**Examples**:
- Input: "5 + 3" → Output: [5.0, '+', 3.0]
- Input: "5+3" → Output: [5.0, '+', 3.0]  # Flexible formatting
- Input: "(2 + 3) * 4" → Output: ['(', 2.0, '+', 3.0, ')', '*', 4.0]

## CLI Interface Functions

### run_interactive() -> None
**Description**: Starts the interactive command-line interface for the calculator.

**Parameters**: None
**Returns**: None

**Behavior**:
- Continuously prompts for user input
- Evaluates expressions and displays results
- Handles commands like 'quit', 'exit', and 'clear'
- Supports Ctrl+C to exit the calculator
- Displays error messages appropriately

### run_single_expression(expression: str) -> None
**Description**: Evaluates a single expression and prints the result.

**Parameters**:
- `expression` (str): A mathematical expression to evaluate

**Returns**: None

**Behavior**:
- Evaluates the provided expression
- Prints the result to stdout
- Exits after single evaluation
