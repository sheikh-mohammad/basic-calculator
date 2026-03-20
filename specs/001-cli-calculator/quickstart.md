# Quickstart Guide: CLI Calculator

## Overview

This guide explains how to use and develop the CLI calculator feature. The calculator provides basic arithmetic operations through a command-line interface.

## Installation

The CLI calculator requires Python 3.8 or higher. No additional dependencies are needed as it uses only standard library modules.

To install and run:

1. Clone the repository
2. Navigate to the project root directory
3. Run the calculator directly: `python -m src.cli.calculator`

## Usage

The calculator accepts expressions in the format: `operand1 operator operand2`

### Basic Operations

- Addition: `2 + 3` → `5`
- Subtraction: `10 - 4` → `6`
- Multiplication: `5 * 6` → `30`
- Division: `15 / 3` → `5`

### Decimal Numbers

- Decimal operations: `3.5 + 2.1` → `5.6`
- Division with decimals: `7.8 / 2` → `3.9`

### Error Handling

- Division by zero: `10 / 0` → `Error: Division by zero`
- Invalid operators: `5 @ 3` → `Error: Invalid operator`
- Non-numeric input: `five + three` → `Error: Invalid input`

## Development

### Project Structure

```
src/
├── lib/                 # Core calculator library
│   └── calculator.py    # Main calculator implementation
├── cli/                 # Command-line interface
│   └── calculator.py    # CLI wrapper
tests/                   # Test suite
├── unit/                # Unit tests
├── integration/         # Integration tests
└── contract/            # Contract tests
```

### Running Tests

All tests can be run using pytest:

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run contract tests only
pytest tests/contract/
```

### Adding New Features

When extending the calculator:

1. Add functionality to the core library in `src/lib/calculator.py`
2. Update the CLI interface in `src/cli/calculator.py` if needed
3. Add comprehensive tests in the appropriate test directories
4. Follow the existing code style and type hinting conventions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with comprehensive tests
4. Submit a pull request for review

## Support

For issues or feature requests, please open an issue in the repository.