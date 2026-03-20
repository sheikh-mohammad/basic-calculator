import pytest
from src.lib.calculator import Calculator, CalculatorError


def test_add():
    """Test addition operation."""
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(0, 0) == 0.0
    assert calc.add(1.5, 2.5) == 4.0


def test_subtract():
    """Test subtraction operation."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2.0
    assert calc.subtract(1, 1) == 0.0
    assert calc.subtract(-1, 1) == -2.0
    assert calc.subtract(5.5, 2.5) == 3.0


def test_multiply():
    """Test multiplication operation."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12.0
    assert calc.multiply(-2, 3) == -6.0
    assert calc.multiply(0, 5) == 0.0
    assert calc.multiply(2.5, 2) == 5.0


def test_divide():
    """Test division operation."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5
    assert calc.divide(-6, 2) == -3.0
    assert calc.divide(5, 1) == 5.0


def test_divide_by_zero():
    """Test division by zero raises error."""
    calc = Calculator()
    with pytest.raises(CalculatorError, match="Division by zero"):
        calc.divide(10, 0)


def test_calculate_addition():
    """Test calculate method with addition."""
    calc = Calculator()
    assert calc.calculate("2 + 3") == 5.0
    assert calc.calculate("10 + 5") == 15.0


def test_calculate_subtraction():
    """Test calculate method with subtraction."""
    calc = Calculator()
    assert calc.calculate("10 - 3") == 7.0
    assert calc.calculate("5 - 8") == -3.0


def test_calculate_multiplication():
    """Test calculate method with multiplication."""
    calc = Calculator()
    assert calc.calculate("3 * 4") == 12.0
    assert calc.calculate("2.5 * 2") == 5.0


def test_calculate_division():
    """Test calculate method with division."""
    calc = Calculator()
    assert calc.calculate("10 / 2") == 5.0
    assert calc.calculate("7 / 2") == 3.5


def test_calculate_division_by_zero():
    """Test calculate method with division by zero."""
    calc = Calculator()
    with pytest.raises(CalculatorError, match="Division by zero"):
        calc.calculate("10 / 0")


def test_calculate_single_number():
    """Test calculate method with single number."""
    calc = Calculator()
    assert calc.calculate("42") == 42.0
    assert calc.calculate("3.14") == 3.14


def test_last_result():
    """Test that last_result is updated correctly."""
    calc = Calculator()
    calc.add(2, 3)
    assert calc.last_result == 5.0

    calc.multiply(2, 3)
    assert calc.last_result == 6.0