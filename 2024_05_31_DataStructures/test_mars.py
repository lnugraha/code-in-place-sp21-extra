# python3 -m unittest test_mars.py

import unittest
from mars import calculate_mars_weight

class TestFactorial(unittest.TestCase):
    def test_factorial_iteration(self):
        self.assertAlmostEqual(calculate_mars_weight(10), 3.78)
        self.assertAlmostEqual(calculate_mars_weight(100), 37.8)

    def test_negative(self):
        self.assertRaises(ValueError, calculate_mars_weight, 0)
        self.assertRaises(ValueError, calculate_mars_weight, -1)

    def test_nonnumber(self):
        self.assertRaises(TypeError, calculate_mars_weight, True)
        self.assertRaises(TypeError, calculate_mars_weight, "codeinplace")
