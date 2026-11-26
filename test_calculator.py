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
        output = calculator.format_result("power", 2, 3, 8)
        self.assertIn("[SCIENTIFIC]", output)
        self.assertIn("8", output)


if __name__ == "__main__":
    unittest.main()
