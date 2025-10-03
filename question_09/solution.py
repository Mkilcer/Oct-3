"""
Question 9: Palindrome Checker
Write a program that checks if a string is a palindrome.
"""

def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and spaces)"""
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

def main():
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for s in test_strings:
        result = "is" if is_palindrome(s) else "is not"
        print(f"'{s}' {result} a palindrome")

if __name__ == "__main__":
    main()
