import unittest

from src.module1.lesson1 import simple


class TestSimple(unittest.TestCase):

    def test_amount(self):
        self.assertEqual(10, simple.amount(5, 5))
        self.assertEqual(-5, simple.amount(10, -15))
        self.assertEqual(28, simple.amount(12, 16))

    def test_subtraction(self):
        self.assertEqual(5, simple.subtraction(10, 5))
        self.assertEqual(15, simple.subtraction(10, -5))
        self.assertEqual(10, simple.subtraction(15,5))

    def test_multiplication(self):

        self.assertEqual(2, simple.multiplication(1, 2))
        self.assertEqual(0, simple.multiplication(0, 2))
        self.assertEqual(-2, simple.multiplication(-1, 2))


    def test_division(self):
        self.assertEqual(2.0, simple.division(2, 1))
        self.assertEqual(-2.0, simple.division(8, -4))
        self.assertAlmostEqual(0.6, simple.division(2, 3), delta=1e-1)

    def test_mod(self):
        self.assertEqual(2, simple.mod(2, 3))
        # self.assertAlmostEqual(-3.7, simple.mod(8.3, -4), delta=1e-5)

    def test_integer_part(self):
        self.assertEqual(2.0, simple.integer_part(2, 1))
        self.assertEqual(-2.0, simple.integer_part(8, -4))

    def test_discriminant(self):
        self.assertAlmostEqual(0.0, simple.discriminant(0.0, 0.0, 0.0), delta=1e-5)
        self.assertAlmostEqual(0.0, simple.discriminant(1.0, -2.0, 1.0), delta=1e-5)
        self.assertAlmostEqual(1.0, simple.discriminant(1.0, 3.0, 2.0), delta=1e-5)

    def test_sqrt(self):
        self.assertAlmostEqual(1.0, simple.sqrt(1.0, -2.0, 1.0), delta=1e-5)
        self.assertAlmostEqual(-3.0, simple.sqrt(1.0, 6.0, 9.0), delta=1e-5)

    def test_seconds(self):
        self.assertEqual(30035, simple.seconds(8, 20, 35))
        self.assertEqual(86400, simple.seconds(24, 0, 0))
        self.assertEqual(13, simple.seconds(0, 0, 13))

    def test_peoples_for_work(self):
        self.assertEqual(10, simple.peoples_for_work(100))
        self.assertEqual(3, simple.peoples_for_work(33))
        self.assertEqual(0, simple.peoples_for_work(0))

    def test_string_amount(self):
        self.assertEqual(25 , simple.string_amount("13", "12"))
        self.assertEqual(-1, simple.string_amount("0", "-1"))

    def test_swap(self):
        self.assertEqual(8521 , simple.swap(1528))
        self.assertEqual(1488, simple.swap(8481))
        self.assertEqual(7566, simple.swap(6567))

    def test_revert_number(self):
        self.assertEqual(874, simple.revert_number(478))
        self.assertEqual(201, simple.revert_number(102))


if __name__ == '__main__':
    unittest.main()
