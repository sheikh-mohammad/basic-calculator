# Error Handling Patterns and Best Practices

## Python Error Handling Patterns

### 1. Exception Hierarchy and Specificity

Always catch more specific exceptions before general ones:

```python
try:
    result = perform_operation()
except ValueError as e:
    # Handle value-related errors specifically
    logger.warning(f"Value error: {e}")
except TypeError as e:
    # Handle type-related errors specifically
    logger.warning(f"Type error: {e}")
except Exception as e:
    # Handle all other exceptions as a fallback
    logger.error(f"Unexpected error: {e}", exc_info=True)
    raise
```

### 2. Context Managers for Resource Management

Use context managers to ensure resources are properly cleaned up:

```python
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

@contextmanager
def database_transaction(connection):
    """Context manager for database transactions"""
    transaction = connection.begin()
    try:
        yield connection
        transaction.commit()
    except Exception:
        transaction.rollback()
        logger.exception("Transaction failed, rolled back")
        raise
    finally:
        connection.close()

# Usage
with database_transaction(conn) as db:
    db.execute("INSERT INTO users ...")
```

### 3. Custom Exception Classes

Create domain-specific exceptions with additional context:

```python
class CalculatorError(Exception):
    """Base exception for calculator operations"""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero"""
    def __init__(self, dividend, operation="division"):
        self.dividend = dividend
        self.operation = operation
        super().__init__(f"Cannot perform {operation} with dividend {dividend} and divisor 0")

class InvalidInputError(CalculatorError):
    """Raised when invalid input is provided"""
    def __init__(self, input_value, expected_type):
        self.input_value = input_value
        self.expected_type = expected_type
        super().__init__(
            f"Invalid input '{input_value}' of type {type(input_value).__name__}, "
            f"expected {expected_type}"
        )
```

### 4. Logging and Error Context

Include relevant context in error logs:

```python
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_errors(func):
    """Decorator to log errors with function context"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(
                f"Error in {func.__name__}: {str(e)}",
                extra={
                    'function': func.__name__,
                    'args': str(args)[:100],  # Limit length
                    'kwargs': str(kwargs)[:100]  # Limit length
                },
                exc_info=True
            )
            raise
    return wrapper

@log_errors
def calculate(operation, *operands):
    # Your calculation logic here
    pass
```

### 5. Exception Chaining

Preserve original exception context:

```python
def process_calculation(user_input):
    try:
        parsed_input = parse_user_input(user_input)
        return perform_calculation(parsed_input)
    except ValueError as e:
        # Original error was ValueError from parsing
        raise CalculationError("Invalid calculation format") from e
    except ZeroDivisionError as e:
        # Original error was ZeroDivisionError from calculation
        raise CalculationError("Division by zero detected") from e
```

## JavaScript Error Handling Patterns

### 1. Custom Error Classes

Create domain-specific error classes:

```javascript
class CalculatorError extends Error {
  constructor(message, options = {}) {
    super(message);
    this.name = 'CalculatorError';
    this.timestamp = new Date().toISOString();
    this.operation = options.operation || null;
    this.input = options.input || null;

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, CalculatorError);
    }
  }
}

class DivisionByZeroError extends CalculatorError {
  constructor(dividend, operation = 'division') {
    super(`Cannot perform ${operation} with divisor 0`, {
      operation,
      input: { dividend, divisor: 0 }
    });
    this.name = 'DivisionByZeroError';
    this.dividend = dividend;
    this.operation = operation;
  }
}

class InvalidInputError extends CalculatorError {
  constructor(inputValue, expectedType) {
    super(`Invalid input '${inputValue}', expected ${expectedType}`, {
      input: inputValue,
      expectedType
    });
    this.name = 'InvalidInputError';
    this.inputValue = inputValue;
    this.expectedType = expectedType;
  }
}
```

### 2. Async Error Handling Patterns

Handle async errors properly:

```javascript
// Pattern 1: Async function with try/catch
async function safeCalculate(operation, ...operands) {
  try {
    // Validate inputs
    validateOperands(operands);

    // Perform calculation
    const result = await performCalculationAsync(operation, operands);

    return result;
  } catch (error) {
    if (error instanceof InvalidInputError) {
      console.error('Input validation failed:', error.message);
      throw error;
    } else if (error instanceof DivisionByZeroError) {
      console.error('Mathematical error:', error.message);
      throw error;
    } else {
      console.error('Unexpected calculation error:', error.message);
      // Wrap generic errors in domain-specific ones
      throw new CalculatorError('Calculation failed', {
        cause: error,
        operation,
        operands
      });
    }
  }
}

// Pattern 2: Promise error handling
function calculateWithPromise(operation, ...operands) {
  return performCalculationAsync(operation, operands)
    .catch(error => {
      if (error instanceof Error) {
        throw new CalculatorError(`Calculation failed: ${error.message}`, {
          cause: error,
          operation,
          operands
        });
      }
      throw new CalculatorError('Calculation failed with unknown error', {
        operation,
        operands
      });
    });
}
```

### 3. Error Cause Pattern

Maintain error context with cause:

```javascript
async function complexCalculation(input) {
  try {
    const parsed = parseInput(input);
    const validated = validateInput(parsed);
    return await executeCalculation(validated);
  } catch (originalError) {
    // Wrap with more context while preserving original
    throw new CalculatorError('Complex calculation failed', {
      cause: originalError,
      input,
      timestamp: new Date().toISOString()
    });
  }
}

// Higher-level function can access both wrapper and original error
async function handleCalculation(input) {
  try {
    return await complexCalculation(input);
  } catch (error) {
    console.error('Operation failed:', error.message);
    if (error.cause) {
      console.error('Root cause:', error.cause.message);
      console.error('Stack trace:', error.cause.stack);
    }
    console.error('Full stack:', error.stack);

    // Return safe default or re-throw based on error type
    if (error instanceof DivisionByZeroError) {
      return 0; // Safe default for division by zero
    }
    throw error;
  }
}
```

### 4. Error Boundary Pattern (Frontend)

For frontend JavaScript applications:

```javascript
class ErrorBoundary {
  constructor() {
    this.onError = null;
  }

  async executeWithErrorHandling(asyncFunction, ...args) {
    try {
      return await asyncFunction(...args);
    } catch (error) {
      console.error('Error caught by boundary:', error);

      // Log error for monitoring
      this.logError(error);

      // Call error handler if provided
      if (this.onError) {
        this.onError(error);
      }

      // Return safe fallback or re-throw
      throw error;
    }
  }

  logError(error) {
    // Send error to logging service
    console.error({
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent
    });
  }
}

// Usage
const errorBoundary = new ErrorBoundary();
errorBoundary.onError = (error) => {
  // Show user-friendly error message
  showErrorMessage('An error occurred during calculation');
};

await errorBoundary.executeWithErrorHandling(calculate, operation, a, b);
```

## Cross-Language Error Handling Consistency

### 1. Standardized Error Categories

Maintain consistent error categories across Python and JavaScript:

- **Validation Errors**: Input validation failures
- **Calculation Errors**: Mathematical operation failures
- **Resource Errors**: Resource unavailability
- **System Errors**: System-level failures

### 2. Consistent Error Response Format

When APIs communicate between Python backend and JavaScript frontend:

```python
# Python backend
def format_error_response(error, status_code=400):
    """Format error response consistently"""
    return {
        'error': {
            'type': type(error).__name__,
            'message': str(error),
            'code': status_code,
            'timestamp': datetime.utcnow().isoformat()
        }
    }, status_code
```

```javascript
// JavaScript frontend
class ApiError extends Error {
  constructor(response, message) {
    super(message);
    this.name = 'ApiError';
    this.response = response;
    this.status = response.status;
    this.timestamp = new Date().toISOString();
  }

  static async handleResponse(response) {
    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response,
        errorData.error?.message || `HTTP ${response.status}`
      );
    }
    return response.json();
  }
}
```

### 3. Logging Consistency

Use consistent logging formats:

```python
# Python
import logging
import json

logger = logging.getLogger(__name__)

def log_calculation_error(operation, operands, error):
    logger.error(
        "Calculation error",
        extra={
            "operation": operation,
            "operands": operands,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "timestamp": datetime.utcnow().isoformat()
        }
    )
```

```javascript
// JavaScript
function logCalculationError(operation, operands, error) {
  console.error({
    message: "Calculation error",
    operation,
    operands,
    error_type: error.constructor.name,
    error_message: error.message,
    timestamp: new Date().toISOString(),
    stack: error.stack
  });
}
```