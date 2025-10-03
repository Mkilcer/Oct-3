"""Tests for Question 4"""
import unittest
from .solution import factorial

class TestFactorial(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    
    def test_small_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == "__main__":
    unittest.main()
