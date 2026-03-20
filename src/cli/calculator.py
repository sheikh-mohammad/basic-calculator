#!/usr/bin/env python3
"""
CLI Calculator Application

This module provides a command-line interface for the calculator.
"""

import argparse
import sys
from src.lib.calculator import Calculator, CalculatorError


def main():
    """Main entry point for the CLI calculator."""
    parser = argparse.ArgumentParser(
        description="CLI Calculator - Perform basic arithmetic operations",
        prog="calculator"
    )

    parser.add_argument(
        "expression",
        nargs="?",
        help="Mathematical expression to evaluate (e.g., '2 + 3', '10 * 5')"
    )

    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Start interactive calculator mode"
    )

    args = parser.parse_args()

    calculator = Calculator()

    if args.interactive:
        interactive_mode(calculator)
    elif args.expression:
        try:
            result = calculator.calculate(args.expression)
            print(result)
        except CalculatorError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # No arguments provided, show help
        parser.print_help()


def interactive_mode(calculator: Calculator):
    """Run calculator in interactive mode."""
    print("CLI Calculator - Interactive Mode")
    print("Enter expressions like '2 + 3' or '10 * 5'")
    print("Type 'quit' or 'exit' to quit")
    print("-" * 40)

    while True:
        try:
            user_input = input("> ").strip()

            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break

            if user_input:
                result = calculator.calculate(user_input)
                print(result)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except CalculatorError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()