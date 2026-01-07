"""
Unit tests for the expression parser.

These tests verify that the expression parser correctly handles
basic mathematical operations as specified in User Story 1.
"""

import pytest
from src.calculator.parser import ExpressionParser


class TestParserBasicOperations:
    """Test class for basic parsing operations."""

    def setup_method(self):
        """Set up a fresh parser instance for each test."""
        self.parser = ExpressionParser()

    def test_addition_parsing(self):
        """Test that addition expressions are parsed correctly."""
        result = self.parser.parse("5 + 3")
        assert result == 8.0

    def test_subtraction_parsing(self):
        """Test that subtraction expressions are parsed correctly."""
        result = self.parser.parse("10 - 4")
        assert result == 6.0

    def test_multiplication_parsing(self):
        """Test that multiplication expressions are parsed correctly."""
        result = self.parser.parse("6 * 7")
        assert result == 42.0

    def test_division_parsing(self):
        """Test that division expressions are parsed correctly."""
        result = self.parser.parse("15 / 3")
        assert result == 5.0

    def test_single_number_parsing(self):
        """Test that single numbers are parsed correctly."""
        result = self.parser.parse("42")
        assert result == 42.0

    def test_negative_number_parsing(self):
        """Test that negative numbers are parsed correctly."""
        result = self.parser.parse("-5")
        assert result == -5.0

        result = self.parser.parse("10 + -5")
        assert result == 5.0

    def test_parsing_with_spaces(self):
        """Test that expressions with spaces are parsed correctly."""
        result = self.parser.parse(" 5 + 3 ")
        assert result == 8.0

        result = self.parser.parse("10-4")
        assert result == 6.0

        result = self.parser.parse("6 *7")
        assert result == 42.0

        result = self.parser.parse("15/ 3")
        assert result == 5.0

    def test_parsing_without_spaces(self):
        """Test that expressions without spaces are parsed correctly."""
        result = self.parser.parse("5+3")
        assert result == 8.0

        result = self.parser.parse("10-4")
        assert result == 6.0

        result = self.parser.parse("6*7")
        assert result == 42.0

        result = self.parser.parse("15/3")
        assert result == 5.0

    def test_expression_validation_valid(self):
        """Test that valid expressions are validated correctly."""
        is_valid, error_msg = self.parser.validate_expression("5 + 3")
        assert is_valid
        assert error_msg == ""

    def test_expression_validation_invalid(self):
        """Test that invalid expressions are caught correctly."""
        is_valid, error_msg = self.parser.validate_expression("5 +")
        assert not is_valid
        assert "syntax" in error_msg.lower()

    def test_expression_validation_empty(self):
        """Test that empty expressions are caught correctly."""
        is_valid, error_msg = self.parser.validate_expression("")
        assert not is_valid
        assert "empty" in error_msg.lower()

    def test_expression_validation_unbalanced_parens(self):
        """Test that unbalanced parentheses are caught correctly."""
        is_valid, error_msg = self.parser.validate_expression("(5 + 3")
        assert not is_valid
        assert "parentheses" in error_msg.lower()