import unittest

from src.module1.lesson1.simple import *


class TestSimple(unittest.TestCase):

    def test_amount(self):
        self.assertEqual(10, amount(5, 5))
        self.assertEqual(-5, amount(10, -15))

    def test_subtraction(self):
        self.assertEqual(5, subtraction(10, 5))
        self.assertEqual(15, subtraction(10, -5))

    def test_multiplication(self):
        self.assertEqual(2, multiplication(1, 2))
        self.assertEqual(0, multiplication(0, 2))
        self.assertEqual(-2, multiplication(-1, 2))

    def test_division(self):
        self.assertEqual(2.0, division(2, 1))
        self.assertEqual(-2.0, division(8, -4))

    def test_mod(self):
        self.assertEqual(0, mod(2, 1))
        self.assertAlmostEqual(-3.7, mod(8.3, -4), delta=1e-5)

    def test_integer_part(self):
        self.assertEqual(2.0, integer_part(2, 1))
        self.assertEqual(-2.0, integer_part(8, -4))

    def test_discriminant(self):
        self.assertAlmostEqual(0.0, discriminant(0.0, 0.0, 0.0), delta=1e-5)
        self.assertAlmostEqual(0.0, discriminant(1.0, -2.0, 1.0), delta=1e-5)
        self.assertAlmostEqual(1.0, discriminant(1.0, 3.0, 2.0), delta=1e-5)

    def test_sqrt(self):
        self.assertAlmostEqual(1.0, sqrt(1.0, -2.0, 1.0), delta=1e-5)
        self.assertAlmostEqual(-3.0, sqrt(1.0, 6.0, 9.0), delta=1e-5)

    def test_seconds(self):
        self.assertEqual(30035, seconds(8, 20, 35))
        self.assertEqual(86400, seconds(24, 0, 0))
        self.assertEqual(13, seconds(0, 0, 13))

    def test_peoples_for_work(self):
        self.assertEqual(10, peoples_for_work(100))
        self.assertEqual(3, peoples_for_work(33))
        self.assertEqual(0, peoples_for_work(0))

    def test_string_amount(self):
        self.assertEqual(25, string_amount("13", "12"))
        self.assertEqual(-1, string_amount("0", "-1"))

    def test_swap(self):#исправить
        self.assertEqual(251, swap(152))
        self.assertEqual(1488, swap(8481))
        self.assertEqual(75678566, swap(65678567))

    def test_next_int(self):
        self.assertEqual(12, next_int(10))
        self.assertEqual(14, next_int(12))

    def test_revert_number(self):
        self.assertEqual(874, revert_number(478))
        self.assertEqual(201, revert_number(102))


if __name__ == '__main__':
    unittest.main()
