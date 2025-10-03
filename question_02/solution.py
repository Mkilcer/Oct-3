#!/usr/bin/env python3
"""
Question 2: Write a program to add two numbers
"""

def add_numbers(a, b):
    return a + b

def main():
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
    return True

if __name__ == "__main__":
    main()
