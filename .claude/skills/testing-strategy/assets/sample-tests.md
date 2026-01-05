# Sample Test Implementations

## Python Test Examples (pytest)

### 1. Calculator Unit Tests

```python
# tests/test_calculator.py
import pytest
from myapp.calculator import Calculator, CalculationError


class TestCalculator:
    """Unit tests for Calculator class"""

    @pytest.fixture
    def calculator(self):
        """Fixture to provide calculator instance for tests"""
        return Calculator()

    def test_add_positive_numbers(self, calculator):
        """Test adding positive numbers"""
        result = calculator.add(2, 3)
        assert result == 5

    def test_add_negative_numbers(self, calculator):
        """Test adding negative numbers"""
        result = calculator.add(-2, -3)
        assert result == -5

    def test_add_zero(self, calculator):
        """Test adding with zero"""
        result = calculator.add(5, 0)
        assert result == 5

    def test_subtract(self, calculator):
        """Test subtraction"""
        result = calculator.subtract(5, 3)
        assert result == 2

    def test_multiply(self, calculator):
        """Test multiplication"""
        result = calculator.multiply(3, 4)
        assert result == 12

    def test_divide(self, calculator):
        """Test division"""
        result = calculator.divide(10, 2)
        assert result == 5

    def test_divide_by_zero_raises_error(self, calculator):
        """Test that division by zero raises an error"""
        with pytest.raises(CalculationError, match="Cannot divide by zero"):
            calculator.divide(10, 0)

    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (100, 200, 300)
    ])
    def test_add_parametrized(self, calculator, a, b, expected):
        """Test add function with multiple parameter sets"""
        result = calculator.add(a, b)
        assert result == expected


class TestCalculatorAdvanced:
    """Advanced tests for Calculator class"""

    def test_complex_calculation(self):
        """Test complex calculation involving multiple operations"""
        calc = Calculator()
        result = calc.evaluate_expression("(2 + 3) * 4 - 5")
        assert result == 15

    def test_large_numbers(self):
        """Test operations with large numbers"""
        calc = Calculator()
        large_num = 10**10
        result = calc.add(large_num, large_num)
        assert result == 2 * (10**10)
```

### 2. API Integration Tests

```python
# tests/test_api.py
import pytest
import json
from myapp.app import create_app
from myapp.database import Database
import tempfile
import os


@pytest.fixture
def temp_db():
    """Create temporary database for testing"""
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        db = Database(temp.name)
        yield db
        os.unlink(temp.name)


@pytest.fixture
def client(temp_db):
    """Create test client for API"""
    app = create_app(temp_db)
    with app.test_client() as client:
        yield client


class TestCalculatorAPI:
    """Integration tests for calculator API endpoints"""

    def test_calculate_add_endpoint(self, client):
        """Test addition endpoint"""
        response = client.post('/api/calculate',
                             json={'operation': 'add', 'operands': [2, 3]})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 5

    def test_calculate_divide_endpoint(self, client):
        """Test division endpoint"""
        response = client.post('/api/calculate',
                             json={'operation': 'divide', 'operands': [10, 2]})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 5.0

    def test_calculate_divide_by_zero(self, client):
        """Test division by zero error handling"""
        response = client.post('/api/calculate',
                             json={'operation': 'divide', 'operands': [10, 0]})
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

    def test_invalid_operation(self, client):
        """Test invalid operation handling"""
        response = client.post('/api/calculate',
                             json={'operation': 'invalid', 'operands': [2, 3]})
        assert response.status_code == 400

    @pytest.mark.parametrize("operation,operands,expected", [
        ('add', [5, 3], 8),
        ('subtract', [10, 4], 6),
        ('multiply', [3, 7], 21),
        ('divide', [15, 3], 5.0)
    ])
    def test_parametrized_operations(self, client, operation, operands, expected):
        """Test multiple operations with parametrized tests"""
        response = client.post('/api/calculate',
                             json={'operation': operation, 'operands': operands})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == expected
```

### 3. Conftest.py for Shared Fixtures

```python
# tests/conftest.py
import pytest
import tempfile
import os
from myapp.database import Database
from myapp.app import create_app


@pytest.fixture(scope="session")
def temp_db_path():
    """Create temporary database path for session"""
    temp_path = tempfile.mktemp(suffix='.db')
    yield temp_path
    if os.path.exists(temp_path):
        os.remove(temp_path)


@pytest.fixture(scope="session")
def database(temp_db_path):
    """Create database instance for session"""
    db = Database(temp_db_path)
    yield db


@pytest.fixture(scope="session")
def app(database):
    """Create app instance for session"""
    app = create_app(database)
    yield app


@pytest.fixture
def client(app):
    """Create test client"""
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_calculation_data():
    """Sample data for calculation tests"""
    return {
        'addition': {'operation': 'add', 'operands': [5, 3], 'expected': 8},
        'subtraction': {'operation': 'subtract', 'operands': [10, 4], 'expected': 6},
        'multiplication': {'operation': 'multiply', 'operands': [3, 7], 'expected': 21},
        'division': {'operation': 'divide', 'operands': [15, 3], 'expected': 5.0}
    }
```

## JavaScript Test Examples (Jest)

### 1. Calculator Unit Tests

```javascript
// tests/calculator.test.js
const Calculator = require('../src/calculator');
const { CalculationError } = require('../src/errors');

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  describe('Basic Operations', () => {
    test('should add two positive numbers correctly', () => {
      const result = calculator.add(2, 3);
      expect(result).toBe(5);
    });

    test('should add negative numbers correctly', () => {
      const result = calculator.add(-2, -3);
      expect(result).toBe(-5);
    });

    test('should add with zero correctly', () => {
      const result = calculator.add(5, 0);
      expect(result).toBe(5);
    });

    test('should subtract correctly', () => {
      const result = calculator.subtract(5, 3);
      expect(result).toBe(2);
    });

    test('should multiply correctly', () => {
      const result = calculator.multiply(3, 4);
      expect(result).toBe(12);
    });

    test('should divide correctly', () => {
      const result = calculator.divide(10, 2);
      expect(result).toBe(5);
    });

    test('should throw error when dividing by zero', () => {
      expect(() => {
        calculator.divide(10, 0);
      }).toThrow(CalculationError);
      expect(() => {
        calculator.divide(10, 0);
      }).toThrow('Cannot divide by zero');
    });
  });

  describe('Advanced Operations', () => {
    test('should evaluate complex expression', () => {
      const result = calculator.evaluateExpression('(2 + 3) * 4 - 5');
      expect(result).toBe(15);
    });

    test('should handle large numbers', () => {
      const largeNum = Math.pow(10, 10);
      const result = calculator.add(largeNum, largeNum);
      expect(result).toBe(2 * Math.pow(10, 10));
    });
  });

  describe('Parameterized Tests', () => {
    test.each([
      [2, 3, 5],
      [0, 0, 0],
      [-1, 1, 0],
      [10, -5, 5],
      [100, 200, 300]
    ])('adds %i + %i to equal %i', (a, b, expected) => {
      expect(calculator.add(a, b)).toBe(expected);
    });

    test.each([
      ['add', [5, 3], 8],
      ['subtract', [10, 4], 6],
      ['multiply', [3, 7], 21],
      ['divide', [15, 3], 5]
    ])('performs %s operation correctly', (operation, operands, expected) => {
      const result = calculator[operation](...operands);
      expect(result).toBe(expected);
    });
  });
});
```

### 2. API Integration Tests

```javascript
// tests/api.test.js
const request = require('supertest');
const app = require('../src/app');
const { Calculator } = require('../src/calculator');

describe('Calculator API', () => {
  describe('POST /api/calculate', () => {
    test('should perform addition correctly', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation: 'add', operands: [2, 3] })
        .expect(200);

      expect(response.body).toEqual({
        result: 5,
        operation: 'add',
        operands: [2, 3]
      });
    });

    test('should perform division correctly', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation: 'divide', operands: [10, 2] })
        .expect(200);

      expect(response.body).toEqual({
        result: 5,
        operation: 'divide',
        operands: [10, 2]
      });
    });

    test('should return error for division by zero', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation: 'divide', operands: [10, 0] })
        .expect(400);

      expect(response.body).toHaveProperty('error');
      expect(response.body.error).toContain('Cannot divide by zero');
    });

    test('should return error for invalid operation', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation: 'invalid', operands: [2, 3] })
        .expect(400);

      expect(response.body).toHaveProperty('error');
    });

    test.each([
      ['add', [5, 3], 8],
      ['subtract', [10, 4], 6],
      ['multiply', [3, 7], 21],
      ['divide', [15, 3], 5]
    ])('should perform %s operation correctly', async (operation, operands, expected) => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation, operands })
        .expect(200);

      expect(response.body.result).toBe(expected);
    });
  });

  describe('Error Handling', () => {
    test('should handle missing operation parameter', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operands: [2, 3] })
        .expect(400);

      expect(response.body).toHaveProperty('error');
    });

    test('should handle missing operands parameter', async () => {
      const response = await request(app)
        .post('/api/calculate')
        .send({ operation: 'add' })
        .expect(400);

      expect(response.body).toHaveProperty('error');
    });
  });
});
```

### 3. Mocking and Spying Tests

```javascript
// tests/mocking.test.js
const Calculator = require('../src/calculator');
const { ExternalAPIService } = require('../src/external-api');

describe('Mocking Tests', () => {
  test('should use mocked external API service', async () => {
    // Create a mock for the external API service
    const mockAPIService = {
      fetchRate: jest.fn().mockResolvedValue(1.25)
    };

    const calculator = new Calculator();

    // Use the mocked service
    const result = await calculator.calculateWithRate(100, mockAPIService);

    expect(result).toBe(125); // 100 * 1.25
    expect(mockAPIService.fetchRate).toHaveBeenCalledTimes(1);
  });

  test('should spy on calculator methods', () => {
    const calculator = new Calculator();
    const addSpy = jest.spyOn(calculator, 'add');

    const result = calculator.add(2, 3);

    expect(result).toBe(5);
    expect(addSpy).toHaveBeenCalledWith(2, 3);
    expect(addSpy).toHaveBeenCalledTimes(1);

    addSpy.mockRestore(); // Clean up the spy
  });

  test('should mock module functions', async () => {
    // Mock the entire external API module
    jest.mock('../src/external-api', () => ({
      ExternalAPIService: jest.fn().mockImplementation(() => ({
        fetchRate: jest.fn().mockResolvedValue(2.0)
      }))
    }));

    const { Calculator } = require('../src/calculator');
    const calculator = new Calculator();

    const result = await calculator.calculateWithRate(50);

    expect(result).toBe(100); // 50 * 2.0
  });

  test('should mock with different implementations', () => {
    const calculator = new Calculator();
    const mockAdd = jest.spyOn(calculator, 'add').mockImplementation((a, b) => a - b);

    const result = calculator.add(5, 3);

    expect(result).toBe(2); // Actually performed subtraction due to mock
    mockAdd.mockRestore();
  });
});
```

### 4. Frontend Component Tests (using Jest + Testing Library)

```javascript
// tests/components/CalculatorComponent.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import CalculatorComponent from '../../src/components/CalculatorComponent';

describe('CalculatorComponent', () => {
  test('renders calculator interface', () => {
    render(<CalculatorComponent />);

    expect(screen.getByRole('textbox', { name: /display/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /add/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /subtract/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /multiply/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /divide/i })).toBeInTheDocument();
  });

  test('performs addition through UI', async () => {
    render(<CalculatorComponent />);

    const display = screen.getByRole('textbox', { name: /display/i });
    const num1Input = screen.getByLabelText(/first number/i);
    const num2Input = screen.getByLabelText(/second number/i);
    const addButton = screen.getByRole('button', { name: /add/i });

    fireEvent.change(num1Input, { target: { value: '5' } });
    fireEvent.change(num2Input, { target: { value: '3' } });
    fireEvent.click(addButton);

    await waitFor(() => {
      expect(display.value).toBe('8');
    });
  });

  test('displays error for division by zero', async () => {
    render(<CalculatorComponent />);

    const display = screen.getByRole('textbox', { name: /display/i });
    const num1Input = screen.getByLabelText(/first number/i);
    const num2Input = screen.getByLabelText(/second number/i);
    const divideButton = screen.getByRole('button', { name: /divide/i });

    fireEvent.change(num1Input, { target: { value: '10' } });
    fireEvent.change(num2Input, { target: { value: '0' } });
    fireEvent.click(divideButton);

    await waitFor(() => {
      expect(display.value).toContain('Error');
    });
  });

  test('clears input when clear button is clicked', () => {
    render(<CalculatorComponent />);

    const num1Input = screen.getByLabelText(/first number/i);
    const num2Input = screen.getByLabelText(/second number/i);
    const clearButton = screen.getByRole('button', { name: /clear/i });

    fireEvent.change(num1Input, { target: { value: '5' } });
    fireEvent.change(num2Input, { target: { value: '3' } });

    expect(num1Input.value).toBe('5');
    expect(num2Input.value).toBe('3');

    fireEvent.click(clearButton);

    expect(num1Input.value).toBe('');
    expect(num2Input.value).toBe('');
  });
});
```

### 5. Jest Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'node',
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/index.js', // Exclude entry point
    '!src/config/**', // Exclude configuration files
  ],
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'lcov', 'html'],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  setupFilesAfterEnv: ['<rootDir>/tests/setup.js'],
  testPathIgnorePatterns: [
    '<rootDir>/node_modules/',
    '<rootDir>/tests/fixtures/',
  ],
  transform: {
    '^.+\\.jsx?$': 'babel-jest',
  },
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
};
```

### 6. Test Setup File

```javascript
// tests/setup.js
// Setup file for Jest tests

// Mock global objects if needed
global.fetch = require('node-fetch');

// Setup for React testing
if (typeof window !== 'undefined') {
  // Mock window properties for browser environment
  Object.defineProperty(window, 'matchMedia', {
    writable: true,
    value: jest.fn().mockImplementation(query => ({
      matches: false,
      media: query,
      onchange: null,
      addListener: jest.fn(),
      removeListener: jest.fn(),
      addEventListener: jest.fn(),
      removeEventListener: jest.fn(),
      dispatchEvent: jest.fn(),
    })),
  });
}

// Setup for database connections or other global test utilities
beforeEach(() => {
  // Setup before each test
});

afterEach(() => {
  // Cleanup after each test
  jest.clearAllMocks();
});
```

These examples demonstrate comprehensive testing strategies for both Python and JavaScript applications, following best practices for unit testing, integration testing, and component testing.