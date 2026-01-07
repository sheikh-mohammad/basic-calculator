"""
Unit tests for the calculator core functionality.

These tests verify that basic mathematical operations work correctly
as specified in User Story 1.
"""

import pytest
from src.calculator.core import Calculator


class TestCalculatorBasicOperations:
    """Test class for basic mathematical operations."""

    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calculator = Calculator()

    def test_addition_operation(self):
        """Test basic addition operation: 5 + 3 = 8."""
        result = self.calculator.evaluate("5 + 3")
        assert result == 8.0

    def test_subtraction_operation(self):
        """Test basic subtraction operation: 10 - 4 = 6."""
        result = self.calculator.evaluate("10 - 4")
        assert result == 6.0

    def test_multiplication_operation(self):
        """Test basic multiplication operation: 6 * 7 = 42."""
        result = self.calculator.evaluate("6 * 7")
        assert result == 42.0

    def test_division_operation(self):
        """Test basic division operation: 15 / 3 = 5."""
        result = self.calculator.evaluate("15 / 3")
        assert result == 5.0

    def test_simple_numbers(self):
        """Test that single numbers are returned as themselves."""
        result = self.calculator.evaluate("42")
        assert result == 42.0

    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        result = self.calculator.evaluate("-5")
        assert result == -5.0

        result = self.calculator.evaluate("10 + -5")
        assert result == 5.0

    def test_zero_operations(self):
        """Test operations involving zero."""
        result = self.calculator.evaluate("0 + 5")
        assert result == 5.0

        result = self.calculator.evaluate("5 * 0")
        assert result == 0.0

    def test_clear_function(self):
        """Test that the clear function works."""
        # Perform a calculation to populate history
        self.calculator.evaluate("5 + 3")

        # Verify history is not empty
        assert len(self.calculator.get_history()) > 0

        # Clear the calculator
        result = self.calculator.clear()

        # Verify the result and that history is empty
        assert result == "Calculator cleared"
        assert len(self.calculator.get_history()) == 0

    def test_history_tracking(self):
        """Test that calculation history is properly tracked."""
        # Perform a few calculations
        self.calculator.evaluate("5 + 3")
        self.calculator.evaluate("10 - 4")

        # Get history
        history = self.calculator.get_history()

        # Verify history contains the calculations
        assert len(history) == 2
        assert history[0][0] == "5 + 3"  # First element is the expression
        assert history[0][1] == 8.0       # Second element is the result
        assert history[1][0] == "10 - 4"  # Third calculation
        assert history[1][1] == 6.0       # Third result