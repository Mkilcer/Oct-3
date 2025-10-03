"""
Question 4: Factorial
Write a program that calculates the factorial of a number.
"""

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    test_values = [0, 1, 5, 7]
    for num in test_values:
        print(f"Factorial of {num} is {factorial(num)}")

if __name__ == "__main__":
    main()
