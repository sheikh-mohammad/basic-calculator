"""
Basic Calculator Library for CLI Calculator

This module provides core arithmetic operations for the CLI calculator.
"""

from typing import Union, Tuple
import math


class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


class Calculator:
    """A basic calculator that performs arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.last_result = 0.0

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a: First operand
            b: Second operand

        Returns:
            The sum of a and b
        """
        result = a + b
        self.last_result = result
        return result

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract second number from first number.

        Args:
            a: First operand
            b: Second operand

        Returns:
            The difference of a and b
        """
        result = a - b
        self.last_result = result
        return result

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a: First operand
            b: Second operand

        Returns:
            The product of a and b
        """
        result = a * b
        self.last_result = result
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Divide first number by second number.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            The quotient of a and b

        Raises:
            CalculatorError: If divisor is zero
        """
        if b == 0:
            raise CalculatorError("Division by zero")
        result = a / b
        self.last_result = result
        return result

    def calculate(self, expression: str) -> float:
        """
        Parse and calculate a mathematical expression.

        Args:
            expression: Mathematical expression like "2 + 3" or "10 * 5"

        Returns:
            The result of the calculation

        Raises:
            CalculatorError: If expression is invalid or division by zero occurs
        """
        # Remove whitespace
        expression = expression.strip()

        # Simple parsing for basic operations
        if '+' in expression:
            parts = expression.split('+')
            if len(parts) != 2:
                raise CalculatorError("Invalid expression")
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            return self.add(a, b)
        elif '-' in expression:
            # Need to be careful with negative numbers
            if expression.count('-') == 1 and expression.startswith('-'):
                # This is a negative number, not subtraction
                raise CalculatorError("Invalid expression")
            else:
                # Check if it's subtraction
                parts = expression.split('-', 1)  # Split only on first '-'
                if len(parts) != 2:
                    raise CalculatorError("Invalid expression")
                a = float(parts[0].strip())
                b = float(parts[1].strip())
                return self.subtract(a, b)
        elif '*' in expression:
            parts = expression.split('*')
            if len(parts) != 2:
                raise CalculatorError("Invalid expression")
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            return self.multiply(a, b)
        elif '/' in expression:
            parts = expression.split('/')
            if len(parts) != 2:
                raise CalculatorError("Invalid expression")
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            return self.divide(a, b)
        else:
            # Single number
            return float(expression)