"""Tests for Question 10"""
import unittest
from .solution import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(count_vowels("Hello World"), 3)
    
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
    
    def test_no_vowels(self):
        self.assertEqual(count_vowels("xyz"), 0)
    
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

if __name__ == "__main__":
    unittest.main()
