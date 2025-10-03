#!/usr/bin/env python3
"""
Question 4: Write a program to find the factorial of a number
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
    return True

if __name__ == "__main__":
    main()
