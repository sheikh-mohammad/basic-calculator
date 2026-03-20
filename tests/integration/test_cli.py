import subprocess
import sys
import os


def test_cli_basic_calculation():
    """Test basic CLI calculation."""
    result = subprocess.run([
        sys.executable, "-m", "src.cli.calculator", "2 + 3"
    ], capture_output=True, text=True, cwd="D:/sdd-basic-cli-calculator")

    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_division():
    """Test CLI division."""
    result = subprocess.run([
        sys.executable, "-m", "src.cli.calculator", "10 / 2"
    ], capture_output=True, text=True, cwd="D:/sdd-basic-cli-calculator")

    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_division_by_zero():
    """Test CLI division by zero error."""
    result = subprocess.run([
        sys.executable, "-m", "src.cli.calculator", "10 / 0"
    ], capture_output=True, text=True, cwd="D:/sdd-basic-cli-calculator")

    assert result.returncode == 1
    assert "Error: Division by zero" in result.stdout


def test_cli_interactive_mode():
    """Test CLI interactive mode (basic test)."""
    # Just verify the module can be imported and run without crashing
    # This is a bit tricky to test properly without stdin, so we'll check it runs
    result = subprocess.run([
        sys.executable, "-c", "import src.cli.calculator; print('Import successful')"
    ], capture_output=True, text=True, cwd="D:/sdd-basic-cli-calculator")

    # Should not crash
    assert result.returncode == 0
    assert "Import successful" in result.stdout