#!/usr/bin/env python3
"""
Question 6: Write a program to check if a string is a palindrome
"""

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    test_string = "racecar"
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome')
    else:
        print(f'"{test_string}" is not a palindrome')
    return True

if __name__ == "__main__":
    main()
