"""Tests for Question 5"""
import unittest
from .solution import find_max

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max([3, 7, 2, 9, 1]), 9)
    
    def test_negative_numbers(self):
        self.assertEqual(find_max([-5, -2, -8, -1]), -1)
    
    def test_single_element(self):
        self.assertEqual(find_max([42]), 42)
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

if __name__ == "__main__":
    unittest.main()
