#!/usr/bin/env python3
"""
Question 9: Write a program to generate Fibonacci sequence
"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    count = 10
    fib_sequence = fibonacci(count)
    print(f"First {count} numbers in Fibonacci sequence:")
    print(fib_sequence)
    return True

if __name__ == "__main__":
    main()
