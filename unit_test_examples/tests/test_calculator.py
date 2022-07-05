import unittest
import unit_test_examples.tools.calculator as calc

class TestCalculator(unittest.TestCase):
    """For testing various methods in the Calculator class.
    """

    def test_addition(self):
        actual = calc.addition(1, 4)
        expected = 5
        self.assertEqual(actual, expected)

    def test_subtraction(self):
        actual = calc.subtraction(8, 2)
        expected = 6
        self.assertEqual(actual, expected)

    def test_multiplication(self):
        actual = calc.subtraction(3, 2)
        expected = 6
        self.assertEqual(actual, expected)

    def test_division(self):
        actual = calc.subtraction(10, 2)
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()