"""Tests for Question 7"""
import unittest
from .solution import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(29))
    
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(25))
    
    def test_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

if __name__ == "__main__":
    unittest.main()
