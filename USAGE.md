# Usage Guide - Assignment 5 Menu System

## Quick Start

### For Professors - Interactive Menu
```bash
python3 menu.py
```
This launches an interactive menu where you can:
- Select any of the 10 questions (1-10)
- Run solutions to see example outputs
- Run tests to verify correctness
- Run all tests at once (option 11)

### Quick Demonstration
```bash
python3 demo.py
```
Shows all 10 questions and their outputs in sequence - great for a quick overview!

### Run All Tests
```bash
python3 run_all_tests.py
```
Runs all 30 unit tests across all 10 questions with verbose output.

## Individual Question Testing

### Run a specific solution
```bash
python3 question_01/solution.py
python3 question_05/solution.py
```

### Run tests for a specific question
```bash
python3 -m unittest question_01.test_solution
python3 -m unittest question_07.test_solution
```

## Question List

| # | Question | Description |
|---|----------|-------------|
| 1 | Hello World | Classic greeting program |
| 2 | Sum of Two Numbers | Add two numbers together |
| 3 | Even or Odd | Determine if a number is even or odd |
| 4 | Factorial | Calculate factorial of a number |
| 5 | Find Maximum | Find the maximum value in a list |
| 6 | Reverse String | Reverse a string |
| 7 | Prime Number Checker | Check if a number is prime |
| 8 | Fibonacci Sequence | Generate Fibonacci numbers |
| 9 | Palindrome Checker | Check if a string is a palindrome |
| 10 | Count Vowels | Count vowels in a string |

## Menu System Features

The interactive menu (`menu.py`) provides:

1. **Main Menu**: Select from 10 questions or run all tests
2. **Question Submenu**: For each question, you can:
   - Run the solution to see example output
   - Run the tests to verify correctness
   - Run both solution and tests together
3. **Batch Testing**: Option to run all tests at once
4. **Clear Output**: Clean, formatted output with progress indicators

## Testing Information

- **Total Tests**: 30 unit tests across 10 questions
- **Test Framework**: Python's built-in `unittest` module
- **Coverage**: Each question has multiple test cases covering:
  - Normal cases
  - Edge cases
  - Error conditions

## Repository Structure

```
Oct-3/
├── README.md           # Main documentation
├── USAGE.md            # This file - usage guide
├── menu.py             # Interactive menu system
├── demo.py             # Demonstration script
├── run_all_tests.py    # Batch test runner
├── .gitignore          # Git ignore rules
└── question_XX/        # Question directories (01-10)
    ├── __init__.py     # Package marker
    ├── solution.py     # Solution implementation
    └── test_solution.py # Unit tests
```

## Tips for Professors

1. **First Time Setup**: Just run `python3 menu.py` - no installation needed!
2. **Quick Check**: Run `python3 demo.py` to see all questions work
3. **Verify Tests**: Run `python3 run_all_tests.py` to verify all 30 tests pass
4. **Individual Inspection**: Use the menu to dive into specific questions
5. **Code Review**: Each solution is self-contained in its own directory

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)
- Works on Linux, macOS, and Windows
