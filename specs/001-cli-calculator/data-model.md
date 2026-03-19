# Data Model: CLI Calculator

## Overview

This document defines the data structures and entities for the CLI calculator feature. Based on the feature specification, the calculator operates on a single core entity representing arithmetic operations.

## Entities

### Calculation

Represents a single arithmetic operation with two operands and an operator.

**Attributes:**
- `operand1`: float - First numeric operand
- `operator`: str - Mathematical operator (+, -, *, /)
- `operand2`: float - Second numeric operand
- `result`: float - Result of the calculation (optional, computed field)

**Relationships:**
- None

**Validation Rules:**
- `operand1` and `operand2` must be numeric values
- `operator` must be one of: '+', '-', '*', '/'
- Division by zero must be prevented and handled appropriately
- Decimal precision must be maintained to 2 decimal places

**State Transitions:**
- Calculation object is created with operands and operator
- Calculation is processed to produce a result
- Error states are possible for invalid operations

## Data Flow

1. User provides input in format: "operand1 operator operand2"
2. Input is parsed into Calculation entity components
3. Calculation entity validates inputs
4. Calculation entity performs operation
5. Result is formatted and displayed to user
6. Error conditions are handled gracefully with appropriate messages

## Persistence

No persistent storage is required for this feature. All calculations are transient and processed in memory only.