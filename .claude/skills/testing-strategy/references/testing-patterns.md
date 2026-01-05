# Testing Patterns and Best Practices

## Python Testing Patterns with pytest

### 1. Test Organization and Structure

#### Test File Organization
```python
# tests/test_calculator.py
import pytest
from myapp.calculator import Calculator

class TestCalculator:
    """Test class for Calculator functionality"""

    def test_add_positive_numbers(self):
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5

    def test_add_negative_numbers(self):
        calc = Calculator()
        result = calc.add(-2, -3)
        assert result == -5
```

#### Test Package Structure
```
tests/
├── __init__.py
├── test_calculator.py
├── test_api/
│   ├── __init__.py
│   ├── test_users.py
│   └── test_auth.py
├── conftest.py  # Shared fixtures
└── fixtures/
    ├── __init__.py
    └── sample_data.py
```

### 2. Advanced Fixture Patterns

#### Session-scoped Fixtures
```python
# conftest.py
import pytest
import tempfile
import os
from myapp.database import Database

@pytest.fixture(scope="session")
def database():
    """Create database instance for entire test session"""
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        db = Database(temp.name)
        yield db
        os.unlink(temp.name)

@pytest.fixture(scope="session")
def app(database):
    """Create app instance with database dependency"""
    from myapp import create_app
    app = create_app(database)
    yield app
```

#### Factory Fixtures
```python
@pytest.fixture
def user_factory():
    """Factory fixture to create users with different configurations"""
    def _create_user(name="Test User", email="test@example.com", active=True):
        from myapp.models import User
        return User(name=name, email=email, active=active)
    return _create_user

def test_user_factory(user_factory):
    user = user_factory("John Doe", "john@example.com", True)
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.active is True

    admin_user = user_factory("Admin", "admin@example.com", False)
    assert admin_user.active is False
```

#### Parametrized Fixtures
```python
@pytest.fixture(params=["sqlite", "postgres"])
def database_type(request):
    """Parametrized fixture to test with different database types"""
    return request.param

def test_database_connection(database_type):
    """Test database connection with different database types"""
    # Test logic here will run for both sqlite and postgres
    assert database_type in ["sqlite", "postgres"]
```

### 3. Test Data Management

#### Using pytest-datafiles for File-based Tests
```python
import json
import pytest

@pytest.fixture
def sample_config(tmp_path):
    """Create sample configuration file for testing"""
    config_data = {
        "debug": True,
        "database_url": "sqlite:///test.db",
        "api_key": "test-key"
    }
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(config_data))
    return config_file

def test_load_config(sample_config):
    """Test loading configuration from file"""
    from myapp.config import load_config
    config = load_config(str(sample_config))
    assert config["debug"] is True
    assert config["database_url"] == "sqlite:///test.db"
```

### 4. Testing with Mocks and Patches

#### Using unittest.mock with pytest
```python
from unittest.mock import Mock, patch, MagicMock
import pytest

def test_with_patch():
    """Test using patch decorator"""
    with patch('myapp.external_api.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'ok'}
        from myapp.external_api import fetch_data

        result = fetch_data('http://api.example.com')

        assert result == {'status': 'ok'}
        mock_get.assert_called_once_with('http://api.example.com')

def test_with_mock():
    """Test using mock objects"""
    mock_service = Mock()
    mock_service.process.return_value = "processed"

    from myapp.processor import DataProcessor
    processor = DataProcessor(mock_service)

    result = processor.handle_data("input")

    assert result == "processed"
    mock_service.process.assert_called_once_with("input")
```

### 5. Testing Asynchronous Code

#### Testing async functions with pytest-asyncio
```python
import pytest
import asyncio
from pytest_asyncio import fixture

@pytest.mark.asyncio
async def test_async_calculator():
    """Test async calculator functions"""
    from myapp.async_calculator import AsyncCalculator

    calc = AsyncCalculator()
    result = await calc.add_async(2, 3)
    assert result == 5

@fixture
async def async_client():
    """Async fixture for client setup"""
    from myapp.client import AsyncClient
    client = AsyncClient()
    await client.connect()
    yield client
    await client.disconnect()

@pytest.mark.asyncio
async def test_with_async_fixture(async_client):
    """Test using async fixture"""
    result = await async_client.fetch_data("test")
    assert result is not None
```

## JavaScript Testing Patterns with Jest

### 1. Test Organization and Structure

#### Test File Organization
```javascript
// tests/Calculator.test.js
const Calculator = require('../src/Calculator');

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  test('should add two positive numbers correctly', () => {
    const result = calculator.add(2, 3);
    expect(result).toBe(5);
  });

  test('should add negative numbers correctly', () => {
    const result = calculator.add(-2, -3);
    expect(result).toBe(-5);
  });
});
```

#### Test Directory Structure
```
tests/
├── unit/
│   ├── Calculator.test.js
│   └── utils/
│       ├── stringUtils.test.js
│       └── numberUtils.test.js
├── integration/
│   ├── api.test.js
│   └── database.test.js
├── e2e/
│   └── user-flow.test.js
├── fixtures/
│   ├── sample-data.json
│   └── mock-responses.js
└── setup/
    ├── jest.setup.js
    └── test-utils.js
```

### 2. Advanced Mocking Patterns

#### Mock Implementation Patterns
```javascript
// Mock with implementation
const mockDatabase = {
  findUser: jest.fn().mockImplementation(async (id) => {
    if (id === 1) {
      return { id: 1, name: 'John' };
    }
    throw new Error('User not found');
  })
};

// Mock with chained calls
const mockQueryBuilder = {
  where: jest.fn().mockReturnThis(),
  select: jest.fn().mockReturnThis(),
  orderBy: jest.fn().mockReturnThis(),
  execute: jest.fn().mockResolvedValue([{ id: 1, name: 'John' }])
};

// Mock constructor
class MockDatabase {
  constructor() {
    this.data = [];
  }

  async save(item) {
    this.data.push(item);
    return { id: this.data.length, ...item };
  }

  async findAll() {
    return this.data;
  }
}

jest.mock('../src/database', () => ({
  Database: MockDatabase
}));
```

#### Mock Timers and Time-based Functions
```javascript
// Mock timers for testing time-based functionality
beforeEach(() => {
  jest.useFakeTimers();
});

afterEach(() => {
  jest.useRealTimers();
});

test('delays execution by specified time', () => {
  const delayedFunction = jest.fn();
  const delayExecution = (fn, delay) => setTimeout(fn, delay);

  delayExecution(delayedFunction, 1000);

  expect(delayedFunction).not.toHaveBeenCalled();
  jest.advanceTimersByTime(1000);
  expect(delayedFunction).toHaveBeenCalledTimes(1);
});

// Mock Date and time functions
test('formats current date correctly', () => {
  const fixedDate = new Date('2023-01-01T10:00:00.000Z');
  jest.setSystemTime(fixedDate);

  const formatter = require('../src/dateFormatter');
  const result = formatter.getCurrentDate();

  expect(result).toBe('2023-01-01');

  jest.useRealTimers();
});
```

### 3. Testing Different Scenarios

#### Testing Error Scenarios
```javascript
test('throws error when dividing by zero', () => {
  const calculator = new Calculator();

  expect(() => {
    calculator.divide(10, 0);
  }).toThrow('Division by zero is not allowed');

  // Or with async functions
  expect(async () => {
    await calculator.divideAsync(10, 0);
  }).rejects.toThrow('Division by zero is not allowed');
});

// Testing with error matching
test('handles invalid input gracefully', () => {
  const calculator = new Calculator();

  expect(() => {
    calculator.add('invalid', 5);
  }).toThrow(/^Invalid input:/);
});
```

#### Testing API Calls
```javascript
const axios = require('axios');
const MockAdapter = require('axios-mock-adapter');

describe('API Service', () => {
  let mock;

  beforeEach(() => {
    mock = new MockAdapter(axios);
  });

  afterEach(() => {
    mock.reset();
  });

  test('fetches user data successfully', async () => {
    const userData = { id: 1, name: 'John Doe' };
    mock.onGet('/api/users/1').reply(200, userData);

    const apiService = require('../src/apiService');
    const result = await apiService.getUser(1);

    expect(result).toEqual(userData);
    expect(mock.history.get[0].url).toBe('/api/users/1');
  });

  test('handles API errors gracefully', async () => {
    mock.onGet('/api/users/999').reply(404);

    const apiService = require('../src/apiService');

    await expect(apiService.getUser(999)).rejects.toThrow('User not found');
  });
});
```

### 4. Snapshot Testing

#### Component Snapshot Testing
```javascript
// For React components
import React from 'react';
import { render } from '@testing-library/react';
import Calculator from '../src/components/Calculator';

test('Calculator component matches snapshot', () => {
  const { asFragment } = render(<Calculator />);
  expect(asFragment()).toMatchSnapshot();
});

// For data snapshots
test('calculator operations produce consistent results', () => {
  const calculator = new Calculator();

  const results = {
    add: calculator.add(2, 3),
    subtract: calculator.subtract(5, 3),
    multiply: calculator.multiply(4, 3),
    divide: calculator.divide(10, 2)
  };

  expect(results).toMatchSnapshot();
});
```

### 5. End-to-End Testing Patterns

#### Using Testing Library Patterns
```javascript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Calculator from '../src/components/Calculator';

test('performs calculation through UI', async () => {
  render(<Calculator />);

  // Find and interact with elements
  const input1 = screen.getByLabelText(/first number/i);
  const input2 = screen.getByLabelText(/second number/i);
  const addButton = screen.getByRole('button', { name: /add/i });
  const resultElement = screen.getByTestId('result');

  // Perform user interactions
  userEvent.type(input1, '5');
  userEvent.type(input2, '3');
  userEvent.click(addButton);

  // Wait for and verify results
  await waitFor(() => {
    expect(resultElement).toHaveTextContent('8');
  });
});
```

## Cross-Language Testing Consistency

### 1. Standardized Test Structure

#### Consistent Test Naming
- Python: `test_[feature]_[scenario]`
- JavaScript: `should [behavior] when [condition]`

#### Consistent Test Organization
- Group related tests in classes/describe blocks
- Use setup/teardown for common operations
- Isolate tests from each other

### 2. Shared Testing Concepts

#### Test Data Management
Both languages should follow similar patterns for test data:
- Use factories for creating test objects
- Separate test data from test logic
- Use fixtures for common test data

#### Mocking Strategies
- Mock external dependencies consistently
- Verify interactions with mocks
- Use dependency injection for testability

### 3. Quality Metrics

#### Coverage Requirements
- Unit tests: 80%+ coverage for individual functions
- Integration tests: Focus on critical paths
- End-to-end tests: Cover main user journeys

#### Performance Requirements
- Unit tests: < 100ms per test
- Integration tests: < 1000ms per test
- End-to-end tests: < 10000ms per test

### 4. Continuous Integration Patterns

#### Test Execution Order
1. Fast unit tests first
2. Integration tests second
3. End-to-end tests last (or in parallel)

#### Parallel Execution
- Run independent tests in parallel
- Group dependent tests in same execution context
- Use appropriate test isolation strategies