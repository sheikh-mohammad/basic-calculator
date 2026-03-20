# CLI Calculator

A simple command-line calculator that performs basic arithmetic operations.

## Features

- Basic arithmetic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Support for decimal numbers
- Interactive mode for continuous calculations
- Error handling for invalid operations (like division by zero)

## Installation

```bash
pip install .
```

## Usage

### Command Line Mode

```bash
# Perform a calculation
calculator "2 + 3"

# Perform a more complex calculation
calculator "10 * 5 - 2"

# Division with decimals
calculator "7.5 / 2"
```

### Interactive Mode

```bash
calculator --interactive
# or
calculator -i
```

In interactive mode, you can enter expressions one by one until you type `quit` or `exit`.

## Examples

```bash
$ calculator "2 + 3"
5.0

$ calculator "10 * 5 - 2"
48.0

$ calculator "7.5 / 2"
3.75

$ calculator --interactive
CLI Calculator - Interactive Mode
Enter expressions like '2 + 3' or '10 * 5'
Type 'quit' or 'exit' to quit
----------------------------------------
> 2 + 3
5.0
> 10 * 5
50.0
> quit
Goodbye!
```

## Running Tests

```bash
pytest tests/
```

## License

MIT
