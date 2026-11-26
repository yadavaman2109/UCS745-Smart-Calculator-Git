"""Unit tests for Smart CLI Calculator."""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.divide(10, 5), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_format_result(self):
        output = calculator.format_result("divide", 22, 7, 22 / 7, precision=3)
        self.assertIn("[LOG]", output)
        self.assertIn("3.143", output)


if __name__ == "__main__":
    unittest.main()
