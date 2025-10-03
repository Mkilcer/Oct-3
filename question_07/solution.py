"""
Question 7: Prime Number Checker
Write a program that checks if a number is prime.
"""

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    test_numbers = [2, 3, 4, 17, 25, 29]
    for num in test_numbers:
        result = "prime" if is_prime(num) else "not prime"
        print(f"{num} is {result}")

if __name__ == "__main__":
    main()
