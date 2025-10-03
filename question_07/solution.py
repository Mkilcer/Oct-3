#!/usr/bin/env python3
"""
Question 7: Write a program to find the largest number in a list
"""

def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

def main():
    numbers = [23, 45, 12, 78, 34, 90, 56]
    largest = find_largest(numbers)
    print(f"The largest number in {numbers} is: {largest}")
    return True

if __name__ == "__main__":
    main()
