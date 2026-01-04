# Sample Error Handling Implementations

## Python Error Handling Examples

### 1. Calculator with Error Handling

```python
import logging
from typing import Union, List
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CalculatorError(Exception):
    """Base exception for calculator operations"""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero"""
    def __init__(self, dividend):
        self.dividend = dividend
        super().__init__(f"Cannot divide {dividend} by zero")

class InvalidInputError(CalculatorError):
    """Raised when invalid input is provided"""
    def __init__(self, input_value, expected_type):
        self.input_value = input_value
        self.expected_type = expected_type
        super().__init__(
            f"Invalid input '{input_value}' of type {type(input_value).__name__}, "
            f"expected {expected_type}"
        )

class Calculator:
    """Calculator with comprehensive error handling"""

    def __init__(self):
        self.history = []

    def _validate_operands(self, *operands):
        """Validate that operands are numbers"""
        for operand in operands:
            if not isinstance(operand, (int, float)):
                raise InvalidInputError(operand, "number")

    def add(self, a: float, b: float) -> float:
        """Add two numbers with error handling"""
        try:
            self._validate_operands(a, b)
            result = a + b
            self.history.append(f"{a} + {b} = {result}")
            logger.info(f"Addition: {a} + {b} = {result}")
            return result
        except InvalidInputError:
            logger.error(f"Invalid input for addition: {a}, {b}")
            raise

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers with error handling"""
        try:
            self._validate_operands(a, b)
            result = a - b
            self.history.append(f"{a} - {b} = {result}")
            logger.info(f"Subtraction: {a} - {b} = {result}")
            return result
        except InvalidInputError:
            logger.error(f"Invalid input for subtraction: {a}, {b}")
            raise

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers with error handling"""
        try:
            self._validate_operands(a, b)
            result = a * b
            self.history.append(f"{a} * {b} = {result}")
            logger.info(f"Multiplication: {a} * {b} = {result}")
            return result
        except InvalidInputError:
            logger.error(f"Invalid input for multiplication: {a}, {b}")
            raise

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers with error handling"""
        try:
            self._validate_operands(a, b)
            if b == 0:
                raise DivisionByZeroError(a)
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            logger.info(f"Division: {a} / {b} = {result}")
            return result
        except InvalidInputError:
            logger.error(f"Invalid input for division: {a}, {b}")
            raise
        except DivisionByZeroError:
            logger.error(f"Division by zero attempted: {a} / {b}")
            raise

    def calculate(self, operation: str, *operands) -> float:
        """Perform calculation based on operation string"""
        operations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }

        if operation not in operations:
            raise CalculatorError(f"Unknown operation: {operation}")

        if len(operands) != 2:
            raise CalculatorError(f"Operation {operation} requires exactly 2 operands")

        return operations[operation](operands[0], operands[1])

# Example usage with error handling
def main():
    calc = Calculator()

    # Test cases
    test_cases = [
        ('add', 10, 5),
        ('subtract', 10, 5),
        ('multiply', 10, 5),
        ('divide', 10, 2),
        ('divide', 10, 0),  # This will raise DivisionByZeroError
        ('add', 'invalid', 5),  # This will raise InvalidInputError
    ]

    for operation, a, b in test_cases:
        try:
            result = calc.calculate(operation, a, b)
            print(f"{operation}({a}, {b}) = {result}")
        except DivisionByZeroError as e:
            print(f"DivisionByZeroError: {e}")
        except InvalidInputError as e:
            print(f"InvalidInputError: {e}")
        except CalculatorError as e:
            print(f"CalculatorError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

### 2. API Error Handler (Python Flask)

```python
from flask import Flask, request, jsonify
import logging
from functools import wraps

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIError(Exception):
    """Custom API exception with status code"""
    def __init__(self, message, status_code=400, payload=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

def handle_errors(f):
    """Decorator to handle errors in API endpoints"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except APIError as e:
            logger.error(f"API Error: {e.message}", extra=e.payload)
            return jsonify({
                'error': {
                    'message': e.message,
                    'code': e.status_code
                }
            }), e.status_code
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            return jsonify({
                'error': {
                    'message': 'Internal server error',
                    'code': 500
                }
            }), 500
    return decorated_function

@app.route('/calculate', methods=['POST'])
@handle_errors
def calculate():
    data = request.get_json()

    if not data or 'operation' not in data or 'operands' not in data:
        raise APIError('Missing required fields: operation and operands', 400)

    operation = data['operation']
    operands = data['operands']

    if not isinstance(operands, list) or len(operands) != 2:
        raise APIError('Operands must be a list with exactly 2 numbers', 400)

    calc = Calculator()
    result = calc.calculate(operation, *operands)

    return jsonify({
        'result': result,
        'operation': operation,
        'operands': operands
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## JavaScript Error Handling Examples

### 1. Calculator with Error Handling

```javascript
// Custom error classes
class CalculatorError extends Error {
  constructor(message, options = {}) {
    super(message);
    this.name = 'CalculatorError';
    this.timestamp = new Date().toISOString();
    this.operation = options.operation || null;
    this.operands = options.operands || null;

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, CalculatorError);
    }
  }
}

class DivisionByZeroError extends CalculatorError {
  constructor(dividend, operation = 'division') {
    super(`Cannot perform ${operation} with divisor 0`, {
      operation,
      operands: [dividend, 0]
    });
    this.name = 'DivisionByZeroError';
    this.dividend = dividend;
    this.operation = operation;
  }
}

class InvalidInputError extends CalculatorError {
  constructor(inputValue, expectedType) {
    super(`Invalid input '${inputValue}', expected ${expectedType}`, {
      expectedType
    });
    this.name = 'InvalidInputError';
    this.inputValue = inputValue;
    this.expectedType = expectedType;
  }
}

// Calculator class with error handling
class Calculator {
  constructor() {
    this.history = [];
    this.logger = console;
  }

  _validateOperands(...operands) {
    for (const operand of operands) {
      if (typeof operand !== 'number' || isNaN(operand)) {
        throw new InvalidInputError(operand, 'number');
      }
    }
  }

  add(a, b) {
    try {
      this._validateOperands(a, b);
      const result = a + b;
      this.history.push(`${a} + ${b} = ${result}`);
      this.logger.info(`Addition: ${a} + ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for addition: ${a}, ${b}`);
      }
      throw error;
    }
  }

  subtract(a, b) {
    try {
      this._validateOperands(a, b);
      const result = a - b;
      this.history.push(`${a} - ${b} = ${result}`);
      this.logger.info(`Subtraction: ${a} - ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for subtraction: ${a}, ${b}`);
      }
      throw error;
    }
  }

  multiply(a, b) {
    try {
      this._validateOperands(a, b);
      const result = a * b;
      this.history.push(`${a} * ${b} = ${result}`);
      this.logger.info(`Multiplication: ${a} * ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for multiplication: ${a}, ${b}`);
      }
      throw error;
    }
  }

  divide(a, b) {
    try {
      this._validateOperands(a, b);
      if (b === 0) {
        throw new DivisionByZeroError(a);
      }
      const result = a / b;
      this.history.push(`${a} / ${b} = ${result}`);
      this.logger.info(`Division: ${a} / ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for division: ${a}, ${b}`);
      } else if (error instanceof DivisionByZeroError) {
        this.logger.error(`Division by zero attempted: ${a} / ${b}`);
      }
      throw error;
    }
  }

  calculate(operation, ...operands) {
    const operations = {
      add: this.add.bind(this),
      subtract: this.subtract.bind(this),
      multiply: this.multiply.bind(this),
      divide: this.divide.bind(this)
    };

    if (!operations[operation]) {
      throw new CalculatorError(`Unknown operation: ${operation}`);
    }

    if (operands.length !== 2) {
      throw new CalculatorError(`Operation ${operation} requires exactly 2 operands`);
    }

    return operations[operation](operands[0], operands[1]);
  }
}

// Example usage with error handling
function main() {
  const calc = new Calculator();

  // Test cases
  const testCases = [
    ['add', 10, 5],
    ['subtract', 10, 5],
    ['multiply', 10, 5],
    ['divide', 10, 2],
    ['divide', 10, 0],  // This will throw DivisionByZeroError
    ['add', 'invalid', 5]  // This will throw InvalidInputError
  ];

  testCases.forEach(([operation, a, b]) => {
    try {
      const result = calc.calculate(operation, a, b);
      console.log(`${operation}(${a}, ${b}) = ${result}`);
    } catch (error) {
      if (error instanceof DivisionByZeroError) {
        console.log(`DivisionByZeroError: ${error.message}`);
      } else if (error instanceof InvalidInputError) {
        console.log(`InvalidInputError: ${error.message}`);
      } else if (error instanceof CalculatorError) {
        console.log(`CalculatorError: ${error.message}`);
      } else {
        console.log(`Unexpected error: ${error.message}`);
      }
    }
  });
}

// Run the example
main();
```

### 2. Async Calculator with Error Handling

```javascript
// Async calculator with proper error handling
class AsyncCalculator {
  constructor() {
    this.history = [];
    this.logger = console;
  }

  async _validateOperandsAsync(...operands) {
    return new Promise((resolve, reject) => {
      try {
        for (const operand of operands) {
          if (typeof operand !== 'number' || isNaN(operand)) {
            throw new InvalidInputError(operand, 'number');
          }
        }
        resolve();
      } catch (error) {
        reject(error);
      }
    });
  }

  async addAsync(a, b) {
    try {
      await this._validateOperandsAsync(a, b);

      // Simulate async operation
      await new Promise(resolve => setTimeout(resolve, 100));

      const result = a + b;
      this.history.push(`${a} + ${b} = ${result}`);
      this.logger.info(`Async Addition: ${a} + ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for async addition: ${a}, ${b}`);
      }
      throw error;
    }
  }

  async divideAsync(a, b) {
    try {
      await this._validateOperandsAsync(a, b);

      if (b === 0) {
        throw new DivisionByZeroError(a);
      }

      // Simulate async operation
      await new Promise(resolve => setTimeout(resolve, 100));

      const result = a / b;
      this.history.push(`${a} / ${b} = ${result}`);
      this.logger.info(`Async Division: ${a} / ${b} = ${result}`);
      return result;
    } catch (error) {
      if (error instanceof InvalidInputError) {
        this.logger.error(`Invalid input for async division: ${a}, ${b}`);
      } else if (error instanceof DivisionByZeroError) {
        this.logger.error(`Division by zero attempted in async: ${a} / ${b}`);
      }
      throw error;
    }
  }

  async calculateAsync(operation, ...operands) {
    const operations = {
      add: this.addAsync.bind(this),
      divide: this.divideAsync.bind(this)
    };

    if (!operations[operation]) {
      throw new CalculatorError(`Unknown async operation: ${operation}`);
    }

    if (operands.length !== 2) {
      throw new CalculatorError(`Operation ${operation} requires exactly 2 operands`);
    }

    return operations[operation](operands[0], operands[1]);
  }
}

// Example usage of async calculator
async function asyncExample() {
  const calc = new AsyncCalculator();

  const testCases = [
    ['add', 10, 5],
    ['divide', 10, 2],
    ['divide', 10, 0],  // This will throw DivisionByZeroError
    ['add', 'invalid', 5]  // This will throw InvalidInputError
  ];

  for (const [operation, a, b] of testCases) {
    try {
      const result = await calc.calculateAsync(operation, a, b);
      console.log(`Async ${operation}(${a}, ${b}) = ${result}`);
    } catch (error) {
      if (error instanceof DivisionByZeroError) {
        console.log(`DivisionByZeroError: ${error.message}`);
      } else if (error instanceof InvalidInputError) {
        console.log(`InvalidInputError: ${error.message}`);
      } else if (error instanceof CalculatorError) {
        console.log(`CalculatorError: ${error.message}`);
      } else {
        console.log(`Unexpected error: ${error.message}`);
      }
    }
  }
}

// Run the async example
asyncExample();
```

### 3. Frontend Error Handler for Calculator UI

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculator with Error Handling</title>
  <style>
    .calculator {
      max-width: 400px;
      margin: 20px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
    }
    .input-group {
      margin-bottom: 10px;
    }
    input, select, button {
      width: 100%;
      padding: 8px;
      margin-bottom: 5px;
      box-sizing: border-box;
    }
    .error {
      color: red;
      font-size: 14px;
      margin-top: 5px;
    }
    .result {
      margin-top: 15px;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <h2>Calculator with Error Handling</h2>
    <div class="input-group">
      <input type="number" id="num1" placeholder="Enter first number">
    </div>
    <div class="input-group">
      <select id="operation">
        <option value="add">Addition (+)</option>
        <option value="subtract">Subtraction (-)</option>
        <option value="multiply">Multiplication (×)</option>
        <option value="divide">Division (÷)</option>
      </select>
    </div>
    <div class="input-group">
      <input type="number" id="num2" placeholder="Enter second number">
    </div>
    <button id="calculate">Calculate</button>
    <div id="error" class="error"></div>
    <div id="result" class="result" style="display: none;"></div>
  </div>

  <script>
    // Include the Calculator class and error classes from previous example here
    // (Calculator class and error classes would be defined above)

    // Error boundary for UI
    class UIErrorBoundary {
      constructor(errorContainerId) {
        this.errorContainer = document.getElementById(errorContainerId);
      }

      async executeWithErrorHandling(asyncFunction, ...args) {
        try {
          this.clearError();
          return await asyncFunction(...args);
        } catch (error) {
          this.displayError(error);
          throw error;
        }
      }

      displayError(error) {
        if (this.errorContainer) {
          this.errorContainer.textContent = error.message;
          this.errorContainer.style.display = 'block';
        }
        console.error('UI Error:', error);
      }

      clearError() {
        if (this.errorContainer) {
          this.errorContainer.textContent = '';
          this.errorContainer.style.display = 'none';
        }
      }
    }

    // Initialize calculator and error boundary
    const calculator = new Calculator();
    const errorBoundary = new UIErrorBoundary('error');

    // Handle calculate button click
    document.getElementById('calculate').addEventListener('click', async () => {
      const num1 = parseFloat(document.getElementById('num1').value);
      const operation = document.getElementById('operation').value;
      const num2 = parseFloat(document.getElementById('num2').value);
      const resultContainer = document.getElementById('result');

      try {
        const result = await errorBoundary.executeWithErrorHandling(
          calculator.calculate.bind(calculator),
          operation,
          num1,
          num2
        );

        resultContainer.textContent = `Result: ${num1} ${getOperationSymbol(operation)} ${num2} = ${result}`;
        resultContainer.style.display = 'block';
      } catch (error) {
        resultContainer.style.display = 'none';
      }
    });

    function getOperationSymbol(operation) {
      const symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷'
      };
      return symbols[operation] || operation;
    }
  </script>
</body>
</html>
```