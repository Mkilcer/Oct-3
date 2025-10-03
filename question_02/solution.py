"""
Question 2: Sum of Two Numbers
Write a program that takes two numbers and returns their sum.
"""

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def main():
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
