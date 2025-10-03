"""Tests for Question 9"""
import unittest
from .solution import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
    
    def test_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()
