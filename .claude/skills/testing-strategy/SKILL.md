---
name: testing-strategy
description: This skill should be used when implementing comprehensive testing strategies for both Python and JavaScript applications, including unit tests, integration tests, and end-to-end tests using pytest for Python and Jest/Vitest for JavaScript.
---

# Testing Strategy Guide

Provides comprehensive guidance for implementing testing strategies in both Python and JavaScript applications, including unit tests, integration tests, and end-to-end tests using pytest for Python and Jest/Vitest for JavaScript.

## Core Testing Principles

### Testing Pyramid
- **Unit Tests**: Test individual functions/components in isolation (majority of tests)
- **Integration Tests**: Test how multiple units work together
- **End-to-End Tests**: Test complete user workflows through the UI

### General Best Practices
- Write tests that are fast, reliable, and maintainable
- Follow the AAA pattern (Arrange, Act, Assert)
- Keep tests independent and isolated
- Use descriptive test names that explain expected behavior
- Test behavior, not implementation details
- Apply the "F.I.R.S.T" principles: Fast, Independent, Repeatable, Self-validating, Timely

## Python Testing with pytest

### Basic Test Structure
```python
import pytest

def add(a, b):
    return a + b

def test_add_positive_numbers():
    """Test adding positive numbers"""
    result = add(2, 3)
    assert result == 5

def test_add_negative_numbers():
    """Test adding negative numbers"""
    result = add(-2, -3)
    assert result == -5
```

### Fixtures for Test Setup
```python
import pytest

@pytest.fixture
def sample_numbers():
    """Fixture that provides sample numbers for tests"""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def calculator():
    """Fixture that provides a calculator instance"""
    from myapp.calculator import Calculator
    return Calculator()

def test_calculator_add(calculator, sample_numbers):
    """Test calculator add method with fixture data"""
    result = calculator.add(sample_numbers[0], sample_numbers[1])
    assert result == 3
```

### Parametrized Tests
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    """Test add function with multiple parameter sets"""
    result = add(a, b)
    assert result == expected
```

### Testing Exceptions
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    """Test that dividing by zero raises an exception"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)
```

### Test Fixtures with Setup/Teardown
```python
import pytest

@pytest.fixture(scope="function")  # Runs for each test
def temp_file():
    """Create temporary file for testing"""
    import tempfile
    import os

    temp_path = tempfile.mktemp()
    with open(temp_path, 'w') as f:
        f.write("test content")

    yield temp_path  # Provide the temp file to test

    # Cleanup after test
    if os.path.exists(temp_path):
        os.remove(temp_path)

def test_file_operations(temp_file):
    """Test file operations using temporary file"""
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "test content"
```

## JavaScript Testing with Jest

### Basic Test Structure
```javascript
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;

// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

### Using Matchers
```javascript
test('testing different matchers', () => {
  const value = 5;

  // Equality matchers
  expect(value).toBe(5);
  expect(value).toEqual(5);

  // Truthiness
  expect(value).toBeTruthy();
  expect(null).toBeFalsy();

  // Numbers
  expect(value).toBeGreaterThan(3);
  expect(value).toBeGreaterThanOrEqual(5);

  // Strings
  expect('hello world').toContain('world');

  // Arrays
  expect([1, 2, 3]).toContain(2);
});
```

### Asynchronous Testing
```javascript
// async function example
function fetchUser(id) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ id, name: 'John Doe' });
    }, 100);
  });
}

test('fetches user asynchronously', async () => {
  const user = await fetchUser(1);
  expect(user).toEqual({
    id: 1,
    name: 'John Doe'
  });
});

// Testing with Promises
test('fetches user with promise', () => {
  return expect(fetchUser(1)).resolves.toEqual({
    id: 1,
    name: 'John Doe'
  });
});
```

### Mocking and Spying
```javascript
// Using mock functions
test('calls callback for each element in array', () => {
  const mockCallback = jest.fn(x => x * 2);
  const array = [1, 2, 3];

  array.forEach(mockCallback);

  // Assertions about mock calls
  expect(mockCallback.mock.calls.length).toBe(3);
  expect(mockCallback.mock.results[0].value).toBe(2);
  expect(mockCallback.mock.results[1].value).toBe(4);
  expect(mockCallback.mock.results[2].value).toBe(6);
});

// Mocking modules
jest.mock('./api', () => ({
  fetchData: jest.fn(() => Promise.resolve({ data: 'mocked' }))
}));

test('uses mocked API', async () => {
  const { fetchData } = require('./api');
  const result = await fetchData();
  expect(fetchData).toHaveBeenCalled();
  expect(result).toEqual({ data: 'mocked' });
});
```

### Setup and Teardown
```javascript
// Runs before each test
beforeEach(() => {
  // Setup code
});

// Runs after each test
afterEach(() => {
  // Cleanup code
});

// Runs once before all tests in this block
beforeAll(() => {
  // Global setup
});

// Runs once after all tests in this block
afterAll(() => {
  // Global cleanup
});

describe('group of tests', () => {
  beforeEach(() => {
    // Setup specific to this group
  });

  test('first test', () => {
    // Test implementation
  });

  test('second test', () => {
    // Test implementation
  });
});
```

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing test structure, testing frameworks in use, code organization patterns |
| **Conversation** | User's specific testing requirements, coverage expectations, CI/CD integration needs |
| **Skill References** | Testing frameworks documentation, best practices, common patterns |
| **User Guidelines** | Project-specific conventions, team standards, quality requirements |

Ensure all required context is gathered before implementing.

## Implementation Standards

### Python Implementation Standards
- Use pytest for test discovery and execution
- Follow naming conventions: `test_*.py` and `*_test.py`
- Use descriptive test function names
- Leverage fixtures for setup/teardown
- Use parametrized tests for multiple inputs
- Apply appropriate test scopes (function, class, module, session)
- Include proper assertions with clear error messages

### JavaScript Implementation Standards
- Use Jest for comprehensive testing framework
- Follow naming conventions: `*.test.js` or `*.spec.js`
- Use descriptive test names in it/describe blocks
- Implement proper mocking strategies
- Handle asynchronous code appropriately
- Use appropriate matchers for different assertion types
- Include proper cleanup in setup/teardown hooks

### Cross-Language Consistency
- Maintain consistent test structure across languages
- Use similar naming conventions where possible
- Apply similar testing strategies and patterns
- Document testing approaches consistently

## Testing Patterns

### Unit Testing Patterns

#### Python Unit Test
```python
import pytest
from unittest.mock import Mock, patch

class Calculator:
    def add(self, a, b):
        return a + b

    def complex_calculation(self, a, b, multiplier_service):
        sum_result = self.add(a, b)
        return multiplier_service.multiply(sum_result, 2)

def test_calculator_add():
    """Unit test for add method"""
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

def test_calculator_complex_calculation():
    """Unit test with mocked dependency"""
    calc = Calculator()
    mock_multiplier = Mock()
    mock_multiplier.multiply.return_value = 10

    result = calc.complex_calculation(2, 3, mock_multiplier)

    assert result == 10
    mock_multiplier.multiply.assert_called_once_with(5, 2)
```

#### JavaScript Unit Test
```javascript
class Calculator {
  add(a, b) {
    return a + b;
  }

  async complexCalculation(a, b, multiplierService) {
    const sumResult = this.add(a, b);
    return await multiplierService.multiply(sumResult, 2);
  }
}

test('Calculator add returns correct sum', () => {
  const calc = new Calculator();
  const result = calc.add(2, 3);
  expect(result).toBe(5);
});

test('Calculator complex calculation with mocked service', async () => {
  const calc = new Calculator();
  const mockMultiplier = {
    multiply: jest.fn().mockResolvedValue(10)
  };

  const result = await calc.complexCalculation(2, 3, mockMultiplier);

  expect(result).toBe(10);
  expect(mockMultiplier.multiply).toHaveBeenCalledWith(5, 2);
});
```

### Integration Testing Patterns

#### Python Integration Test
```python
import pytest
import tempfile
import os
from myapp.database import Database
from myapp.user_service import UserService

@pytest.fixture
def temp_db():
    """Create temporary database for integration tests"""
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        db = Database(temp.name)
        yield db
        os.unlink(temp.name)

def test_user_creation_integration(temp_db):
    """Integration test for user creation across multiple components"""
    user_service = UserService(temp_db)

    user_id = user_service.create_user("john@example.com", "John Doe")

    user = user_service.get_user(user_id)
    assert user.email == "john@example.com"
    assert user.name == "John Doe"

    # Verify data was persisted
    assert temp_db.get_user_count() == 1
```

#### JavaScript Integration Test
```javascript
const request = require('supertest');
const app = require('../app');
const { User } = require('../models');

describe('User API Integration', () => {
  beforeEach(async () => {
    // Clear database before each test
    await User.destroy({ where: {} });
  });

  test('creates user via API and stores in database', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({
        email: 'john@example.com',
        name: 'John Doe'
      })
      .expect(201);

    // Verify response
    expect(response.body.email).toBe('john@example.com');
    expect(response.body.name).toBe('John Doe');

    // Verify data stored in database
    const user = await User.findByPk(response.body.id);
    expect(user).not.toBeNull();
    expect(user.email).toBe('john@example.com');
  });
});
```

## Quality Checklist

### Python Testing
- [ ] Tests use pytest framework properly
- [ ] Fixtures are used for test setup/teardown
- [ ] Parametrized tests cover multiple scenarios
- [ ] Exception testing implemented where appropriate
- [ ] Test names are descriptive and clear
- [ ] Tests are independent and isolated
- [ ] Appropriate assertion messages provided

### JavaScript Testing
- [ ] Tests use Jest framework properly
- [ ] Appropriate matchers used for assertions
- [ ] Mocking implemented for external dependencies
- [ ] Asynchronous code handled correctly
- [ ] Setup/teardown hooks used appropriately
- [ ] Test names are descriptive and clear
- [ ] Tests are independent and isolated

### Testing Strategy
- [ ] Unit tests cover individual functions/components
- [ ] Integration tests verify component interactions
- [ ] Test coverage meets project requirements
- [ ] Tests are fast and reliable
- [ ] Test organization follows project conventions
- [ ] Error conditions are properly tested