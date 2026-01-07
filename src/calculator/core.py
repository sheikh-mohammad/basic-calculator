"""
Core calculator logic module.

This module contains the Calculator class that handles the core mathematical
operations, expression evaluation, and state management.
"""

import operator
from typing import Union, Optional
from enum import Enum
from datetime import datetime
from .parser import ExpressionParser


class CalculatorState(Enum):
    """Enumeration of calculator states."""
    READY = "ready"
    PROCESSING = "processing"
    ERROR = "error"
    EXIT = "exit"


class Calculator:
    """
    Core calculator class that handles mathematical operations and state management.

    This class provides methods for evaluating mathematical expressions,
    handling errors, and maintaining calculator state.
    """

    def __init__(self):
        """Initialize the calculator with default state and history."""
        self.state = CalculatorState.READY
        self.history = []
        self.operator_precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }
        self.parser = ExpressionParser()

    def evaluate(self, expression: str) -> Union[float, int, str]:
        """
        Evaluate a mathematical expression and return the result.

        Args:
            expression: A string containing a mathematical expression

        Returns:
            The result of the calculation as a number, or an error message as a string
        """
        self.state = CalculatorState.PROCESSING

        try:
            # Use the ExpressionParser to evaluate the expression safely
            result = self.parser.parse(expression)

            # Add to history if successful
            if isinstance(result, (int, float)):
                # Format result to maintain precision (up to 10 decimal places)
                formatted_result = self._format_result(result)
                self.history.append((expression, formatted_result, datetime.now()))
                self.state = CalculatorState.READY
                return formatted_result
            else:
                # Result is already an error message string
                self.state = CalculatorState.ERROR
                return result

        except Exception as e:
            self.state = CalculatorState.ERROR
            error_msg = f"Error: {str(e)}"
            self.history.append((expression, error_msg, datetime.now()))
            return error_msg

    def _format_result(self, result: Union[float, int]) -> Union[float, int]:
        """
        Format the result to maintain proper precision.

        Args:
            result: The numeric result to format

        Returns:
            The formatted result maintaining up to 10 decimal places precision
        """
        # If it's an integer or a float that's essentially an integer, return as int
        if isinstance(result, int) or (isinstance(result, float) and result.is_integer()):
            return int(result)

        # For floats, round to 10 decimal places to maintain precision
        # but avoid floating point representation issues
        formatted = round(result, 10)

        # Remove trailing zeros after decimal point for cleaner output
        # but keep at least one decimal place if it's not a whole number
        if isinstance(formatted, float):
            # Format to max 10 decimal places, removing trailing zeros
            formatted_str = f"{formatted:.10f}".rstrip('0').rstrip('.')
            return float(formatted_str)

        return formatted


    def clear(self) -> str:
        """
        Clear the calculator state and history.

        Returns:
            A confirmation message
        """
        self.state = CalculatorState.READY
        self.history = []
        return "Calculator cleared"

    def get_history(self) -> list:
        """
        Get the calculation history.

        Returns:
            A list of tuples containing (expression, result, timestamp)
        """
        return self.history

    def get_state(self) -> CalculatorState:
        """
        Get the current calculator state.

        Returns:
            The current CalculatorState
        """
        return self.state