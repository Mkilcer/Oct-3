#!/usr/bin/env python3
"""
Assignment 5 - Main Menu System
This menu allows professors to select and test any of the 10 programming questions.
"""

import sys
import os
import subprocess
import importlib.util

# Question descriptions
QUESTIONS = {
    1: "Hello World",
    2: "Sum of Two Numbers",
    3: "Even or Odd",
    4: "Factorial",
    5: "Find Maximum",
    6: "Reverse String",
    7: "Prime Number Checker",
    8: "Fibonacci Sequence",
    9: "Palindrome Checker",
    10: "Count Vowels"
}

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def display_menu():
    """Display the main menu"""
    clear_screen()
    print("=" * 60)
    print("        ASSIGNMENT 5 - MAIN MENU")
    print("=" * 60)
    print("\nAvailable Questions:")
    print("-" * 60)
    
    for num, desc in QUESTIONS.items():
        print(f"  {num:2d}. {desc}")
    
    print("-" * 60)
    print("  11. Run ALL tests")
    print("   0. Exit")
    print("=" * 60)

def run_solution(question_num):
    """Run the solution for a specific question"""
    folder = f"question_{question_num:02d}"
    solution_path = os.path.join(folder, "solution.py")
    
    if not os.path.exists(solution_path):
        print(f"\nError: Solution file not found for question {question_num}")
        return False
    
    print(f"\n{'=' * 60}")
    print(f"Running Question {question_num}: {QUESTIONS[question_num]}")
    print(f"{'=' * 60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, solution_path],
            cwd=os.getcwd(),
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error running solution: {e}")
        return False

def run_tests(question_num):
    """Run tests for a specific question"""
    folder = f"question_{question_num:02d}"
    test_path = os.path.join(folder, "test_solution.py")
    
    if not os.path.exists(test_path):
        print(f"\nError: Test file not found for question {question_num}")
        return False
    
    print(f"\n{'=' * 60}")
    print(f"Running Tests for Question {question_num}: {QUESTIONS[question_num]}")
    print(f"{'=' * 60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", f"{folder}.test_solution"],
            cwd=os.getcwd(),
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

def run_all_tests():
    """Run tests for all questions"""
    print("\n" + "=" * 60)
    print("RUNNING ALL TESTS")
    print("=" * 60 + "\n")
    
    passed = 0
    failed = 0
    
    for question_num in range(1, 11):
        folder = f"question_{question_num:02d}"
        test_path = os.path.join(folder, "test_solution.py")
        
        if os.path.exists(test_path):
            print(f"Testing Question {question_num}: {QUESTIONS[question_num]}...")
            result = subprocess.run(
                [sys.executable, "-m", "unittest", f"{folder}.test_solution"],
                cwd=os.getcwd(),
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"  ✓ PASSED\n")
                passed += 1
            else:
                print(f"  ✗ FAILED")
                print(result.stderr)
                failed += 1
        else:
            print(f"  ⚠ Test file not found\n")
            failed += 1
    
    print("=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)

def handle_question(question_num):
    """Handle user selection of a specific question"""
    if question_num not in QUESTIONS:
        print(f"\nInvalid question number: {question_num}")
        return
    
    while True:
        print(f"\n{'=' * 60}")
        print(f"Question {question_num}: {QUESTIONS[question_num]}")
        print(f"{'=' * 60}")
        print("1. Run Solution")
        print("2. Run Tests")
        print("3. Run Both")
        print("0. Back to Main Menu")
        print("-" * 60)
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            run_solution(question_num)
            input("\nPress Enter to continue...")
        elif choice == '2':
            run_tests(question_num)
            input("\nPress Enter to continue...")
        elif choice == '3':
            run_solution(question_num)
            print()
            run_tests(question_num)
            input("\nPress Enter to continue...")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '0':
            print("\nExiting... Goodbye!")
            sys.exit(0)
        elif choice == '11':
            run_all_tests()
            input("\nPress Enter to continue...")
        elif choice.isdigit():
            question_num = int(choice)
            if 1 <= question_num <= 10:
                handle_question(question_num)
            else:
                print("\nInvalid choice. Please enter a number between 0 and 11.")
                input("\nPress Enter to continue...")
        else:
            print("\nInvalid input. Please enter a number.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
