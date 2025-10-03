"""Tests for Question 2"""
import unittest
from .solution import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
    
    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)
    
    def test_mixed_numbers(self):
        self.assertEqual(add_numbers(-5, 10), 5)

if __name__ == "__main__":
    unittest.main()
