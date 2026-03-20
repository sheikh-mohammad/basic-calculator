#!/usr/bin/env python3
"""
Simple wrapper to make the calculator executable
"""

import sys
import os

# Add the src directory to the path so we can import the calculator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from cli.calculator import main

if __name__ == "__main__":
    main()