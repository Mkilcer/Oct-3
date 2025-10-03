#!/usr/bin/env python3
"""
Simple test runner to execute all tests for all questions.
"""

import unittest
import sys

def run_all_tests():
    """Discover and run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test modules
    for i in range(1, 11):
        module_name = f"question_{i:02d}.test_solution"
        try:
            tests = loader.loadTestsFromName(module_name)
            suite.addTests(tests)
        except Exception as e:
            print(f"Warning: Could not load tests from {module_name}: {e}")
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on success
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
