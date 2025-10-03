"""Tests for Question 3"""
import unittest
from .solution import is_even

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(10))
    
    def test_odd_numbers(self):
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(15))

if __name__ == "__main__":
    unittest.main()
