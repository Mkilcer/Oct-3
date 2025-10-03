# Oct-3 - Assignment 5: Programming Questions Menu System

This repository contains 10 programming questions with solutions and tests, along with an interactive menu system for professors to test all code.

## Repository Structure

```
Oct-3/
├── menu.py                  # Main menu system
├── question_01/            # Question 1: Hello World
│   ├── solution.py
│   └── test_solution.py
├── question_02/            # Question 2: Sum of Two Numbers
│   ├── solution.py
│   └── test_solution.py
...
└── question_10/            # Question 10: Count Vowels
    ├── solution.py
    └── test_solution.py
```

## Available Questions

1. **Hello World** - Classic greeting program
2. **Sum of Two Numbers** - Add two numbers together
3. **Even or Odd** - Determine if a number is even or odd
4. **Factorial** - Calculate factorial of a number
5. **Find Maximum** - Find the maximum value in a list
6. **Reverse String** - Reverse a string
7. **Prime Number Checker** - Check if a number is prime
8. **Fibonacci Sequence** - Generate Fibonacci numbers
9. **Palindrome Checker** - Check if a string is a palindrome
10. **Count Vowels** - Count vowels in a string

## How to Use the Menu System

### Running the Main Menu

```bash
python3 menu.py
```

The menu will display all 10 questions and provide the following options:
- Select a question (1-10) to run its solution and/or tests
- Choose option 11 to run ALL tests at once
- Choose option 0 to exit

### Running Individual Questions

For each question, you can:
1. Run the solution to see example output
2. Run the tests to verify correctness
3. Run both solution and tests

### Running Tests Directly

To run tests for a specific question:
```bash
python3 -m unittest question_01.test_solution
```

To run all tests:
```bash
python3 -m unittest discover -s . -p "test_*.py"
```

### Running Solutions Directly

To run a specific solution:
```bash
python3 question_01/solution.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Testing

All questions include comprehensive unit tests using Python's `unittest` framework. Each test file validates the functionality of its corresponding solution.

## For Professors

The menu system (`menu.py`) is specifically designed to make it easy to:
- Browse all 10 questions
- Test individual questions or all at once
- Verify that all code works correctly
- See example outputs for each program

Simply run `python3 menu.py` and follow the interactive prompts.
