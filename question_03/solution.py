"""
Question 3: Even or Odd
Write a program that determines if a number is even or odd.
"""

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def main():
    test_numbers = [4, 7, 10, 15, 22]
    for num in test_numbers:
        result = "even" if is_even(num) else "odd"
        print(f"{num} is {result}")

if __name__ == "__main__":
    main()
