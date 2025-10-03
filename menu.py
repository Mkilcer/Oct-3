#!/usr/bin/env python3
"""
Professor Menu System - Test All 10 Question Codes
This menu allows professors to run and test solutions for all 10 questions.
"""

import os
import sys
import subprocess
from pathlib import Path

class ProfessorMenu:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.questions = {
            1: "Print 'Hello, World!'",
            2: "Add two numbers",
            3: "Check if a number is even or odd",
            4: "Find the factorial of a number",
            5: "Reverse a string",
            6: "Check if a string is a palindrome",
            7: "Find the largest number in a list",
            8: "Count vowels in a string",
            9: "Generate Fibonacci sequence",
            10: "Check if a number is prime"
        }
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the menu header"""
        print("=" * 60)
        print(" " * 15 + "PROFESSOR TEST MENU")
        print("=" * 60)
        print()
    
    def display_menu(self):
        """Display the main menu options"""
        print("Available Questions:")
        print("-" * 60)
        for num, description in self.questions.items():
            print(f"  {num:2d}. {description}")
        print("-" * 60)
        print("  11. Run All Questions")
        print("   0. Exit")
        print()
    
    def run_question(self, question_num):
        """Run a specific question's solution"""
        if question_num not in self.questions:
            print(f"Error: Invalid question number {question_num}")
            return False
        
        question_dir = self.base_dir / f"question_{question_num:02d}"
        solution_file = question_dir / "solution.py"
        
        if not solution_file.exists():
            print(f"Error: Solution file not found for question {question_num}")
            return False
        
        print(f"\n{'=' * 60}")
        print(f"Question {question_num}: {self.questions[question_num]}")
        print(f"{'=' * 60}\n")
        
        try:
            result = subprocess.run(
                [sys.executable, str(solution_file)],
                cwd=str(question_dir),
                capture_output=False,
                text=True
            )
            
            print(f"\n{'=' * 60}")
            if result.returncode == 0:
                print(f"✓ Question {question_num} completed successfully")
            else:
                print(f"✗ Question {question_num} failed with exit code {result.returncode}")
            print(f"{'=' * 60}\n")
            
            return result.returncode == 0
        
        except Exception as e:
            print(f"Error running question {question_num}: {e}")
            return False
    
    def run_all_questions(self):
        """Run all questions sequentially"""
        print("\n" + "=" * 60)
        print(" " * 15 + "RUNNING ALL QUESTIONS")
        print("=" * 60 + "\n")
        
        results = {}
        for question_num in range(1, 11):
            success = self.run_question(question_num)
            results[question_num] = success
            input("\nPress Enter to continue to next question...")
            self.clear_screen()
            self.display_header()
        
        # Display summary
        print("\n" + "=" * 60)
        print(" " * 20 + "SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for success in results.values() if success)
        total = len(results)
        
        for question_num, success in results.items():
            status = "✓ PASS" if success else "✗ FAIL"
            print(f"  Question {question_num:2d}: {status} - {self.questions[question_num]}")
        
        print("-" * 60)
        print(f"  Total: {passed}/{total} passed")
        print("=" * 60 + "\n")
    
    def run(self):
        """Main menu loop"""
        while True:
            self.clear_screen()
            self.display_header()
            self.display_menu()
            
            try:
                choice = input("Enter your choice: ").strip()
                
                if choice == '0':
                    print("\nExiting... Goodbye!")
                    break
                
                if choice == '11':
                    self.run_all_questions()
                    input("\nPress Enter to return to main menu...")
                    continue
                
                try:
                    question_num = int(choice)
                    if question_num in self.questions:
                        self.run_question(question_num)
                        input("\nPress Enter to return to main menu...")
                    else:
                        print(f"\nInvalid choice: {choice}")
                        input("Press Enter to continue...")
                except ValueError:
                    print(f"\nInvalid input: {choice}")
                    input("Press Enter to continue...")
            
            except KeyboardInterrupt:
                print("\n\nExiting... Goodbye!")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                input("Press Enter to continue...")

def main():
    """Entry point for the professor menu system"""
    menu = ProfessorMenu()
    menu.run()

if __name__ == "__main__":
    main()
