#!/usr/bin/env python3
"""
Question 10: Write a program to check if a number is prime
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    test_number = 17
    if is_prime(test_number):
        print(f"{test_number} is a prime number")
    else:
        print(f"{test_number} is not a prime number")
    return True

if __name__ == "__main__":
    main()
