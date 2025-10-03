#!/usr/bin/env python3
"""
Demonstration script showing the functionality of all 10 questions.
This shows professors what each question does without needing to use the interactive menu.
"""

import sys
import os

def demo_question(num, description):
    """Run a demonstration of a specific question"""
    folder = f"question_{num:02d}"
    solution_path = os.path.join(folder, "solution.py")
    
    print(f"\n{'=' * 70}")
    print(f"Question {num}: {description}")
    print(f"{'=' * 70}")
    
    if os.path.exists(solution_path):
        print("Sample Output:")
        print("-" * 70)
        os.system(f"{sys.executable} {solution_path}")
        print("-" * 70)
    else:
        print(f"Error: Solution file not found")

def main():
    """Run demonstrations of all questions"""
    questions = [
        (1, "Hello World"),
        (2, "Sum of Two Numbers"),
        (3, "Even or Odd"),
        (4, "Factorial"),
        (5, "Find Maximum"),
        (6, "Reverse String"),
        (7, "Prime Number Checker"),
        (8, "Fibonacci Sequence"),
        (9, "Palindrome Checker"),
        (10, "Count Vowels")
    ]
    
    print("\n" + "=" * 70)
    print(" " * 15 + "ASSIGNMENT 5 - DEMONSTRATION")
    print(" " * 10 + "Showing all 10 programming questions")
    print("=" * 70)
    
    for num, desc in questions:
        demo_question(num, desc)
    
    print("\n" + "=" * 70)
    print("Demonstration complete!")
    print("Run 'python3 menu.py' for interactive testing")
    print("Run 'python3 run_all_tests.py' to run all unit tests")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
