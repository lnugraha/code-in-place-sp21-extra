# python3 -m unittest test_factorial.py

import unittest
from factorial import factorial_iteration
from factorial import factorial_dynamic_programming

class TestFactorial(unittest.TestCase):
    def test_factorial_iteration(self):
        self.assertEqual(factorial_iteration(1), 1)
        self.assertEqual(factorial_iteration(0), 1)
        self.assertEqual(factorial_iteration(5), 120)

        self.assertEqual(factorial_dynamic_programming(1), 1)
        self.assertEqual(factorial_dynamic_programming(0), 1)
        self.assertEqual(factorial_dynamic_programming(4), 24)

    def test_negative(self):
        self.assertRaises(ValueError, factorial_iteration, -1)
        self.assertRaises(ValueError, factorial_dynamic_programming, -5)

    def test_nonnumber(self):
        self.assertRaises(TypeError, factorial_iteration, True)
        self.assertRaises(TypeError, factorial_iteration, "codeinplace")

        self.assertRaises(TypeError, factorial_dynamic_programming, True)
        self.assertRaises(TypeError, factorial_dynamic_programming, "codeinplace")
