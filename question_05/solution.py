#!/usr/bin/env python3
"""
Question 5: Write a program to reverse a string
"""

def reverse_string(text):
    return text[::-1]

def main():
    test_string = "Python Programming"
    reversed_text = reverse_string(test_string)
    print(f"Original: {test_string}")
    print(f"Reversed: {reversed_text}")
    return True

if __name__ == "__main__":
    main()
