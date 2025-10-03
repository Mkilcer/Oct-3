"""
Question 5: Find Maximum
Write a program that finds the maximum value in a list of numbers.
"""

def find_max(numbers):
    """Find the maximum value in a list"""
    if not numbers:
        raise ValueError("List cannot be empty")
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

def main():
    test_list = [3, 7, 2, 9, 1, 5]
    print(f"The maximum value in {test_list} is: {find_max(test_list)}")

if __name__ == "__main__":
    main()
