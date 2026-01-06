# Quickstart Guide: CLI Calculator

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Setup
1. Clone or create the calculator project
2. Navigate to the project directory
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Calculator
### Direct execution:
```bash
python calculator.py
```

### Interactive mode:
The calculator will start in interactive mode where you can enter expressions one by one:
```
Calculator started. Enter expressions or 'quit' to exit.
> 5 + 3
8
> (10 + 5) * 2
30
> quit
Calculator closed.
```

### Single expression:
You can also pass an expression directly:
```bash
python calculator.py "5 + 3 * 2"
# Output: 11
```

## Usage Examples
- Basic operations: `5 + 3`, `10 - 4`, `6 * 7`, `15 / 3`
- Decimal numbers: `3.14 * 2.5`, `10.5 + 3.25`
- Order of operations: `2 + 3 * 4` evaluates to `14`, not `20`
- Parentheses: `(2 + 3) * 4` evaluates to `20`
- Division by zero: `5 / 0` returns "Error: Division by zero"

## Available Commands
- `quit` or `exit`: Close the calculator
- `clear` or `c`: Reset the current calculation
- Any valid mathematical expression

## Error Handling
- Invalid expressions will return an error message
- Division by zero is handled gracefully
- Invalid syntax will show appropriate error messages