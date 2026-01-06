# Data Model: CLI Calculator

## Core Entities

### MathematicalExpression
- **Type**: `str`
- **Description**: A string containing numbers and operators that represents a calculation to be performed
- **Validation**: Must contain valid mathematical operators (+, -, *, /, parentheses) and operands
- **Examples**: "5 + 3", "10.5 - 3.2", "(2 + 3) * 4"

### CalculationResult
- **Type**: `Union[float, int, str]`
- **Description**: The numerical output produced by evaluating a mathematical expression or an error message
- **Validation**: Must be a numeric value or a string starting with "Error:"
- **Examples**: 8, 7.85, "Error: Division by zero"

### CalculatorState
- **Type**: `Enum`
- **Description**: The current status of the calculator
- **Values**:
  - `READY`: Awaiting user input
  - `PROCESSING`: Currently evaluating an expression
  - `ERROR`: In error state after invalid input
  - `EXIT`: Calculator is shutting down
- **Default**: `READY`

### OperatorPrecedence
- **Type**: `Dict[str, int]`
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
3. Calculator state transitions to `ERROR`
4. After error, calculator returns to `READY` state after user action

## Validation Rules

### Expression Validation
- Must contain only digits, decimal points, mathematical operators (+, -, *, /), and parentheses
- Must have balanced parentheses
- Must have valid operator/operand alternation
- Must not have consecutive operators (except for negative numbers)

### Result Validation
- Results must be finite numbers (not inf or NaN)
- Division by zero must be caught and handled
- Expression evaluation must not exceed system limits

## State Transitions

```
READY → PROCESSING → (SUCCESS → READY) or (ERROR → ERROR)
ERROR → READY (after clear or new valid input)
READY → EXIT (on quit command)
```

## Relationships

- `CalculatorState` determines what operations are valid
- `MathematicalExpression` is processed to produce `CalculationResult`
- `OperatorPrecedence` guides the evaluation of `MathematicalExpression`
- Error conditions cause transition to `ERROR` state with error message in `CalculationResult`