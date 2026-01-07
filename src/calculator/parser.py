"""
Expression parser module for the calculator.

This module provides functionality to parse and validate mathematical expressions,
including handling of operator precedence and parentheses.
"""

import ast
import operator
from typing import Union, List, Tuple


class ExpressionParser:
    """
    Expression parser that handles mathematical expressions with proper validation.

    This class provides methods for parsing, validating, and evaluating mathematical
    expressions safely using AST (Abstract Syntax Tree) to prevent code injection.
    """

    def __init__(self):
        """Initialize the expression parser."""
        # Define allowed operations for safe evaluation
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg,  # Unary minus for negative numbers
        }

    def parse(self, expression: str) -> Union[float, int, str]:
        """
        Parse and evaluate a mathematical expression safely.

        Args:
            expression: A string containing a mathematical expression

        Returns:
            The result of the calculation or an error message
        """
        try:
            # Remove all whitespace for consistent parsing
            expression = expression.replace(" ", "")

            if not expression:
                return "Error: Empty expression"

            # Check for division by zero in simple cases
            if "/0" in expression or "/0.0" in expression:
                return "Error: Division by zero"

            # Use AST to safely evaluate the expression
            node = ast.parse(expression, mode='eval')
            result = self._eval_node(node.body)

            # Check if result is a finite number
            if isinstance(result, (int, float)) and (result != float('inf') and result != float('-inf')):
                return result
            else:
                return "Error: Result is not a finite number"

        except ZeroDivisionError:
            return "Error: Division by zero"
        except SyntaxError:
            return "Error: Invalid expression syntax"
        except Exception as e:
            return f"Error: {str(e)}"

    def _eval_node(self, node) -> Union[float, int]:
        """
        Recursively evaluate an AST node.

        Args:
            node: An AST node to evaluate

        Returns:
            The numeric result of the evaluation
        """
        if isinstance(node, ast.Constant):  # Numbers, strings, etc. (Python 3.8+)
            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise ValueError(f"Unsupported constant type: {type(node.value)}")
        # Only check for ast.Num if it exists (older Python versions)
        elif hasattr(ast, 'Num') and isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):  # Binary operations (+, -, *, /)
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op = self.operators.get(type(node.op))

            if op is None:
                raise ValueError(f"Unsupported operation: {type(node.op)}")

            return op(left, right)
        elif isinstance(node, ast.UnaryOp):  # Unary operations (- for negative numbers)
            operand = self._eval_node(node.operand)
            op = self.operators.get(type(node.op))

            if op is None:
                raise ValueError(f"Unsupported unary operation: {type(node.op)}")

            return op(operand)
        elif isinstance(node, ast.Name):  # Variable names (which should not be in math expressions)
            raise ValueError(f"Invalid identifier: {node.id}")
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")

    def validate_expression(self, expression: str) -> Tuple[bool, str]:
        """
        Validate a mathematical expression without evaluating it.

        Args:
            expression: A string containing a mathematical expression

        Returns:
            A tuple of (is_valid, error_message)
        """
        try:
            # Remove all whitespace for consistent parsing
            expression = expression.replace(" ", "")

            if not expression:
                return False, "Empty expression"

            # Check for balanced parentheses
            if expression.count('(') != expression.count(')'):
                return False, "Unbalanced parentheses"

            # Try to parse the expression
            ast.parse(expression, mode='eval')

            return True, ""
        except SyntaxError:
            return False, "Invalid expression syntax"
        except Exception as e:
            return False, f"Validation error: {str(e)}"