"""
Question 10: Count Vowels
Write a program that counts the number of vowels in a string.
"""

def count_vowels(text):
    """Count the number of vowels in a string"""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def main():
    test_strings = ["Hello World", "Python Programming", "aeiou"]
    for s in test_strings:
        count = count_vowels(s)
        print(f"'{s}' has {count} vowels")

if __name__ == "__main__":
    main()
