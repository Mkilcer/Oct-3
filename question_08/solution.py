#!/usr/bin/env python3
"""
Question 8: Write a program to count vowels in a string
"""

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

def main():
    test_string = "Hello World"
    vowel_count = count_vowels(test_string)
    print(f'The string "{test_string}" contains {vowel_count} vowels')
    return True

if __name__ == "__main__":
    main()
