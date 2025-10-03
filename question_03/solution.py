#!/usr/bin/env python3
"""
Question 3: Write a program to check if a number is even or odd
"""

def is_even(number):
    return number % 2 == 0

def main():
    test_number = 15
    if is_even(test_number):
        print(f"{test_number} is even")
    else:
        print(f"{test_number} is odd")
    return True

if __name__ == "__main__":
    main()
