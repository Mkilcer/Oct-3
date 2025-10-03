"""
Question 6: Reverse String
Write a program that reverses a string.
"""

def reverse_string(text):
    """Reverse the given string"""
    return text[::-1]

def main():
    test_strings = ["hello", "Python", "12345"]
    for s in test_strings:
        print(f"'{s}' reversed is '{reverse_string(s)}'")

if __name__ == "__main__":
    main()
