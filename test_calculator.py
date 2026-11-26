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

    def test_scientific_operations(self):
        self.assertEqual(calculator.power(2, 5), 32)
        self.assertEqual(calculator.modulus(17, 5), 2)

    def test_format_result(self):
        sci_out = calculator.format_result("power", 2, 3, 8, precision=0)
        self.assertIn("[LOG]", sci_out)
        self.assertIn("POWER(2, 3) -> 8", sci_out)

        prec_out = calculator.format_result("divide", 22, 7, 22 / 7, precision=3)
        self.assertIn("DIVIDE(22, 7) -> 3.143", prec_out)


if __name__ == "__main__":
    unittest.main()
