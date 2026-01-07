"""
Command-line interface module for the calculator.

This module provides the CLI interface that handles user input,
command processing, and output formatting.
"""

import sys
from typing import NoReturn
from .core import Calculator, CalculatorState
from .parser import ExpressionParser


class CalculatorCLI:
    """
    Command-line interface for the calculator application.

    This class handles user interaction, command processing, and output formatting.
    """

    def __init__(self):
        """Initialize the CLI with a calculator instance."""
        self.calculator = Calculator()
        self.running = True

    def run(self) -> NoReturn:
        """
        Run the calculator in interactive mode.

        This method starts the interactive loop that prompts users for input
        and processes their commands until they choose to exit.
        """
        print("Calculator started. Enter expressions or commands ('quit', 'exit', or Ctrl+C to exit).")

        while self.running:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                # Process commands
                if user_input.lower() in ['quit', 'exit']:
                    print("Calculator closed.")
                    break
                elif user_input.lower() in ['clear', 'c']:
                    result = self.calculator.clear()
                    print(result)
                elif user_input.lower() == 'history':
                    history = self.calculator.get_history()
                    if history:
                        for expr, res, timestamp in history:
                            print(f"{expr} = {res}")
                    else:
                        print("No calculation history available.")
                else:
                    # Process mathematical expression
                    result = self.calculator.evaluate(user_input)
                    print(result)

            except KeyboardInterrupt:
                print("\nCalculator closed.")
                break
            except EOFError:
                print("\nCalculator closed.")
                break

    def run_single_expression(self, expression: str) -> None:
        """
        Run a single expression and exit.

        Args:
            expression: The mathematical expression to evaluate
        """
        result = self.calculator.evaluate(expression)
        print(result)