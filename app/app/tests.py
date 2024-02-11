"""
Sample TestCase
"""

from django.test import SimpleTestCase
from app.calc import add, subtract


class CalcTest(SimpleTestCase):
    """
    Test Calc Module
    """

    """
    Testing Add Functionality
    """
    #  Adding two positive integers
    def test_add_positive_integers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    #  Adding two negative integers
    def test_add_negative_integers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    #  Adding a positive and a negative integer
    def test_add_positive_and_negative_integers(self):
        result = add(2, -3)
        self.assertEqual(result, -1)

    #  Adding two very large integers that exceed the maximum integer value
    def test_add_very_large_integers(self):
        result = add(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
                     1)
        self.assertEqual(result,
                         10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    #  Adding zero to an integer
    def test_add_zero_to_integer(self):
        result = add(5, 0)
        self.assertEqual(result, 5)

    """
       Testing Subtract Functionality
    """
    #  Returns the correct result when subtracting two positive integers
    def test_subtract_positive_integers(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    #  Returns the correct result when subtracting a positive integer from zero
    def test_subtract_positive_from_zero(self):
        result = subtract(0, 5)
        self.assertEqual(result, -5)

    #  Returns the correct result when subtracting a negative integer from a positive integer
    def test_subtract_negative_from_positive(self):
        result = subtract(10, -3)
        self.assertEqual(result, 13)

    #  Returns the correct result when subtracting zero from a positive integer
    def test_subtract_zero_from_positive(self):
        result = subtract(8, 0)
        self.assertEqual(result, 8)

    #  Returns the correct result when subtracting zero from a negative integer
    def test_subtract_zero_from_negative(self):
        result = subtract(-5, 0)
        self.assertEqual(result, -5)

    #  Returns the correct result when subtracting a positive integer from itself
    def test_subtract_positive_from_positive(self):
        result = subtract(7, 7)
        self.assertEqual(result, 0)


