#!/usr/bin/env python3
"""
Main entry point for the CLI Calculator.

This module provides the main interface for the calculator application,
allowing users to perform basic mathematical operations through a command-line
interface with support for order of operations, error handling, and more.
"""

import sys
from src.calculator.cli import CalculatorCLI


def main():
    """Main entry point for the calculator application."""
    cli = CalculatorCLI()

    # Check if an expression was provided as a command-line argument
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        cli.run_single_expression(expression)
    else:
        # Run in interactive mode
        cli.run()


if __name__ == "__main__":
    main()