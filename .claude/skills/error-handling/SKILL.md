---
name: error-handling
description: This skill should be used when implementing robust error handling in both Python and JavaScript applications, including try/catch blocks, custom exceptions/errors, logging, and graceful error recovery.
---

# Error Handling Guide

Provides comprehensive guidance for implementing robust error handling in both Python and JavaScript applications, including try/catch blocks, custom exceptions/errors, logging, and graceful error recovery.

## Core Error Handling Principles

### General Best Practices
- Be specific with exception/error types rather than catching generic ones
- Don't ignore errors - either handle them properly or let them propagate
- Log errors appropriately without exposing sensitive information
- Use finally blocks or context managers for resource cleanup
- Preserve original error context when transforming errors
- Create custom exceptions/errors for domain-specific conditions

### Python Error Handling

#### Basic Try/Except Structure
```python
try:
    x = int(input("Please enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid number input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
    raise  # Re-raise unexpected exceptions
```

#### Specific Exception Handling
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise  # Re-raise unexpected exceptions
```

#### Using Else and Finally Clauses
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()  # Only executes if no exception occurred
    finally:
        print("Finished processing", arg)  # Always executes
```

#### Custom Exceptions
```python
class ValidationError(Exception):
    """Raised when validation fails"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class CalculationError(Exception):
    """Raised when a calculation operation fails"""
    pass
```

#### Context Managers for Resource Management
```python
# Preferred approach - automatic cleanup
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

#### Exception Chaining
```python
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc  # Preserve original exception

# Or disable chaining
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```

### JavaScript Error Handling

#### Basic Try/Catch Structure
```javascript
try {
  // statements to try
  monthName = getMonthName(myMonth); // function could throw exception
} catch (e) {
  monthName = "unknown";
  logMyErrors(e); // pass exception object to error handler
} finally {
  // Always executes after try and catch blocks
  cleanupResources();
}
```

#### Custom Error Classes
```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
    this.timestamp = new Date().toISOString();
  }
}

class CalculationError extends Error {
  constructor(message, operation) {
    super(message);
    this.name = 'CalculationError';
    this.operation = operation;
  }
}
```

#### Async Error Handling with async/await
```javascript
async function asyncFunction() {
  try {
    const result = await someAsyncOperation();
    return result;
  } catch (error) {
    // Handle the error that occurred in the async operation
    console.error(`${error.name}: ${error.message}`);
    // You can re-throw or handle differently based on error type
    throw error;
  }
}
```

#### Error Cause for Better Debugging
```javascript
async function complexAsyncOperation() {
  try {
    await stepOne();
    await stepTwo();
    await stepThree();
  } catch (originalError) {
    // Wrap with more context while preserving original error
    throw new Error('Complex operation failed', {
      cause: originalError
    });
  }
}
```

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing error handling patterns, logging infrastructure, framework-specific error handling |
| **Conversation** | User's specific error handling requirements, error recovery expectations, logging preferences |
| **Skill References** | Language-specific error handling patterns, best practices, common anti-patterns |
| **User Guidelines** | Project-specific conventions, team standards, security requirements for error handling |

Ensure all required context is gathered before implementing.

## Implementation Standards

### Python Implementation Standards
- Use specific exception types rather than bare `except:`
- Follow the exception hierarchy appropriately
- Use context managers for resource management
- Implement proper logging with appropriate log levels
- Create custom exceptions for domain-specific errors
- Preserve exception context when re-raising

### JavaScript Implementation Standards
- Use Error objects rather than primitive values for throwing
- Create custom error classes that extend built-in Error
- Handle async errors with try/catch when using await
- Use error cause property to maintain error context
- Implement proper error logging without exposing sensitive data
- Use instanceof checks for specific error type handling

### Cross-Language Consistency
- Maintain consistent error categorization across languages
- Use similar logging formats and levels
- Implement similar error recovery strategies
- Document error handling patterns consistently

## Error Handling Patterns

### Python Patterns

#### Validation Pattern
```python
def validate_input(data):
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary", "type_error")
    if "value" not in data:
        raise ValidationError("Missing required field: value", "missing_field")
    return data
```

#### Resource Management Pattern
```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    conn = None
    try:
        conn = create_connection()
        yield conn
    except Exception as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()
```

### JavaScript Patterns

#### Validation Pattern
```javascript
function validateInput(data) {
  if (typeof data !== 'object' || data === null) {
    throw new ValidationError("Input must be an object", "type_error");
  }
  if (!data.hasOwnProperty('value')) {
    throw new ValidationError("Missing required field: value", "missing_field");
  }
  return data;
}
```

#### Async Pattern
```javascript
async function safeAsyncOperation(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    if (error instanceof TypeError) {
      // Network error
      console.error('Network error:', error.message);
    } else {
      // Other error
      console.error('Operation failed:', error.message);
    }
    throw error;
  }
}
```

## Quality Checklist

### Python Error Handling
- [ ] Specific exception types used instead of generic catch-all
- [ ] Context managers used for resource management
- [ ] Custom exceptions created for domain-specific errors
- [ ] Exception chaining implemented where appropriate
- [ ] Proper logging implemented without sensitive data exposure
- [ ] Resources properly cleaned up in finally blocks

### JavaScript Error Handling
- [ ] Custom error classes extend built-in Error
- [ ] Async errors properly handled with try/catch
- [ ] Error cause used to maintain context
- [ ] Appropriate error types checked with instanceof
- [ ] Proper logging implemented without sensitive data exposure
- [ ] Error stack traces preserved for debugging

### Cross-Language Consistency
- [ ] Similar error categorization across languages
- [ ] Consistent logging formats
- [ ] Similar error recovery strategies
- [ ] Documented error handling patterns