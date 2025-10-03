# Oct-3 - Professor Test Menu System

This repository contains solutions for 10 programming questions and a menu system for professors to easily test all codes.

## Structure

The repository is organized as follows:
- `question_01/` through `question_10/` - Each folder contains a `solution.py` file with the answer to that question
- `menu.py` - Interactive menu system for testing all questions

## Questions

1. **Question 1**: Print "Hello, World!"
2. **Question 2**: Add two numbers
3. **Question 3**: Check if a number is even or odd
4. **Question 4**: Find the factorial of a number
5. **Question 5**: Reverse a string
6. **Question 6**: Check if a string is a palindrome
7. **Question 7**: Find the largest number in a list
8. **Question 8**: Count vowels in a string
9. **Question 9**: Generate Fibonacci sequence
10. **Question 10**: Check if a number is prime

## Usage

### Running the Menu System

To start the interactive professor menu:

```bash
python3 menu.py
```

### Menu Options

The menu provides the following options:
- **1-10**: Run individual question solutions
- **11**: Run all questions sequentially with a summary
- **0**: Exit the menu

### Running Individual Questions

You can also run individual question solutions directly:

```bash
python3 question_01/solution.py
python3 question_02/solution.py
# ... and so on
```

## Requirements

- Python 3.6 or higher

## For Professors

The menu system is designed to make testing student submissions easy:
1. Launch the menu with `python3 menu.py`
2. Select a specific question (1-10) to test
3. Or select option 11 to run all questions and see a summary
4. Each solution will execute and display its output
5. The menu tracks success/failure for each question
