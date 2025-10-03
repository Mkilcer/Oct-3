"""Tests for Question 8"""
import unittest
from .solution import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_zero_terms(self):
        self.assertEqual(fibonacci(0), [])
    
    def test_one_term(self):
        self.assertEqual(fibonacci(1), [0])
    
    def test_multiple_terms(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

if __name__ == "__main__":
    unittest.main()
