# Professor Menu System - Usage Guide

## Overview

This repository provides a complete testing environment for 10 programming questions with an interactive menu system designed specifically for professors to easily test student code submissions.

## Quick Start

```bash
python3 menu.py
```

## Menu System Features

### Main Menu
When you run the menu, you'll see:
- **Options 1-10**: Test individual question solutions
- **Option 11**: Run all questions sequentially with a summary report
- **Option 0**: Exit the menu

### Interactive Testing
- Select any question number to run that specific solution
- View the output immediately
- Get success/failure status
- Press Enter to return to the main menu

### Batch Testing
- Select option 11 to run all questions
- See each question's output in sequence
- Get a comprehensive summary at the end showing which questions passed/failed
- Useful for quick verification of all solutions

## Question List

1. **Print "Hello, World!"** - Basic output test
2. **Add two numbers** - Arithmetic operation
3. **Check if a number is even or odd** - Conditional logic
4. **Find the factorial of a number** - Recursion
5. **Reverse a string** - String manipulation
6. **Check if a string is a palindrome** - String comparison
7. **Find the largest number in a list** - List operations
8. **Count vowels in a string** - String iteration and counting
9. **Generate Fibonacci sequence** - Sequence generation
10. **Check if a number is prime** - Number theory

## Manual Testing

You can also run individual solutions directly without the menu:

```bash
python3 question_01/solution.py
python3 question_02/solution.py
# ... etc
```

## Directory Structure

```
Oct-3/
├── README.md              # Project overview
├── USAGE_GUIDE.md        # This file
├── menu.py               # Interactive menu system
├── question_01/
│   └── solution.py       # Question 1 solution
├── question_02/
│   └── solution.py       # Question 2 solution
├── ...
└── question_10/
    └── solution.py       # Question 10 solution
```

## For Students

Students should place their solution code in the appropriate `question_XX/solution.py` file, ensuring:
- The file is named exactly `solution.py`
- It can be run with `python3 solution.py`
- It produces the expected output
- The main logic is in a `main()` function

## For Professors

The menu system makes grading easy:
1. Students submit their solutions in the correct question folders
2. Run `python3 menu.py`
3. Test individual questions or all at once
4. Review outputs and success/failure status
5. The system tracks which solutions work correctly

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## Examples

### Testing a Single Question
```
Enter your choice: 5

============================================================
Question 5: Reverse a string
============================================================

Original: Python Programming
Reversed: gnimmargorP nohtyP

============================================================
✓ Question 5 completed successfully
============================================================
```

### Running All Questions
Select option 11 to see all outputs followed by a summary showing how many questions passed.

## Troubleshooting

If a solution fails to run:
- Check that the solution.py file exists in the correct question folder
- Verify the Python syntax is correct
- Ensure all required functions are defined
- Check file permissions (files should be executable)

## Support

For issues or questions about the menu system, please refer to the main README.md file.
