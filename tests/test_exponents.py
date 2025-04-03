import unittest
import sys
import os

# Add the src directory to the Python path, import exponents.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from math_plus.exponents import Exponent, product

# Test class for product function
class TestProductFunction(unittest.TestCase):
    def test_product_same_base(self):
        exp1 = Exponent(2, 3)  # 2^3
        exp2 = Exponent(2, 4)  # 2^4
        result = product(exp1, exp2)
        self.assertEqual(result, 2**(3+4))  # Should be 2^(3+4) = 2^7 = 128

    def test_product_different_base_same_exponent(self):
        exp1 = Exponent(3, 2)  # 3^2
        exp2 = Exponent(5, 2)  # 5^2
        result = product(exp1, exp2)
        self.assertEqual(result, (3*5)**2)  # Should be (3*5)^2 = 15^2 = 225

    def test_product_different_base_different_exponent(self):
        exp1 = Exponent(4, 3)  # 4^3
        exp2 = Exponent(5, 2)  # 5^2
        result = product(exp1, exp2)
        self.assertEqual(result, (4**3)*(5**2))  # Should be (4^3)*(5^2) = (64)*(25) = 1600

    def test_product_invalid_input(self):
        with self.assertRaises(ValueError):
            product(Exponent(4, 3), Exponent(5, 2), Exponent(6, 1))


if __name__ == "__main__":
    unittest.main()

