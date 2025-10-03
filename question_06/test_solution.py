"""Tests for Question 6"""
import unittest
from .solution import reverse_string

class TestReverseString(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

if __name__ == "__main__":
    unittest.main()
