# Data Model: CLI Calculator

## Core Entities

### MathematicalExpression
- **Type**: `str`
- **Description**: A string containing numbers and operators that represents a calculation to be performed; supports flexible formatting with or without spaces between operands and operators
- **Validation**: Must contain valid mathematical operators (+, -, *, /, parentheses) and operands; must support flexible formatting (with/without spaces)
- **Examples**: "5 + 3", "10.5 - 3.2", "(2 + 3) * 4", "5+3*2"

### CalculationResult
- **Type**: `float | int | str`
- **Description**: The numerical output produced by evaluating a mathematical expression or an error message
- **Validation**: Must be a numeric value (with up to 10 decimal places precision) or a string starting with "Error:"
- **Examples**: 8, 7.85, "Error: Division by zero"

### CalculatorState
- **Type**: `Enum`
- **Description**: The current status of the calculator; maintains state after errors to allow continued operation
- **Values**:
  - `READY`: Awaiting user input
  - `PROCESSING`: Currently evaluating an expression
  - `ERROR`: In error state after invalid input; maintains state to allow continued operation
  - `EXIT`: Calculator is shutting down
- **Default**: `READY`

### OperatorPrecedence
- **Type**: `dict[str, int]`
- **Description**: Defines the precedence level of mathematical operators
- **Values**:
  - `+`: 1
  - `-`: 1
  - `*`: 2
  - `/`: 2
- **Validation**: Higher number indicates higher precedence

## Data Flow

### Input Processing
1. User provides `MathematicalExpression` as string input
2. Expression is validated for proper syntax and characters
3. Expression is parsed into tokens (numbers, operators, parentheses)
4. Expression is evaluated respecting `OperatorPrecedence`
5. Result is returned as `CalculationResult`

### Error Handling
1. If division by zero detected → return error message as `CalculationResult`
2. If invalid syntax detected → return error message as `CalculationResult`
3. Calculator state transitions to `ERROR` but maintains application state for continued operation (does not crash)
4. After error, calculator remains in `ERROR` state until user intervention (clear command or valid input) to return to `READY` state

## Validation Rules

### Expression Validation
- Must contain only digits, decimal points, mathematical operators (+, -, *, /), and parentheses
- Must have balanced parentheses
- Must have valid operator/operand alternation
- Must not have consecutive operators (except for negative numbers)
- Should support flexible formatting (with or without spaces between operands and operators)

### Result Validation
- Results must be finite numbers (not inf or NaN)
- Division by zero must be caught and handled
- Expression evaluation must not exceed system limits
- Results should maintain up to 10 decimal places precision for floating-point calculations

## State Transitions

```
READY → PROCESSING → (SUCCESS → READY) or (ERROR → ERROR - maintains app state)
ERROR → READY (after clear command or new valid input)
READY → EXIT (on quit, exit command, or Ctrl+C)
ERROR → EXIT (on quit, exit command, or Ctrl+C)
```

## Relationships

- `CalculatorState` determines what operations are valid
- `MathematicalExpression` is processed to produce `CalculationResult`
- `OperatorPrecedence` guides the evaluation of `MathematicalExpression`
- Error conditions cause transition to `ERROR` state with error message in `CalculationResult`