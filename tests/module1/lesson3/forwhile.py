import unittest

from src.module1.lesson3.forwhile import *


class TestTasks(unittest.TestCase):

    def test_counter(self):
        self.assertEqual(11, counter(1, 10, 1))
        self.assertEqual(15, counter(1, 2, 7))

    def test_num_count(self):
        self.assertEqual(1, num_count(1))
        self.assertEqual(3, num_count(123))
        self.assertEqual(10, num_count(1231231231))

    def test_custom_len(self):
        self.assertEqual(3, custom_len("123"))
        self.assertEqual(0, custom_len(""))
        self.assertEqual(7, custom_len("1212123"))

    def test_revert(self):
        pass  # TODO: тесты написать самостоятельно

    def test_counter_for(self):
        self.assertEqual(15, counter_for(1, 2, 7))
        self.assertEqual(11, counter_for(1, 10, 1))

    def test_num_count_for(self):
        self.assertEqual(1, num_count_for(1))
        self.assertEqual(3, num_count_for(123))
        self.assertEqual(10, num_count_for(1231231231))

    def test_custom_len_for(self):
        self.assertEqual(3, custom_len_for("123"))
        self.assertEqual(0, custom_len_for(""))
        self.assertEqual(7, custom_len_for("1212123"))

    def test_revert_for(self):
        self.assertEqual("2636544", revert_for("4456362"))
        self.assertEqual("", revert_for(""))
        self.assertEqual("xadsvfsa", revert_for("asfvsdax"))

    def test_compute(self):
        self.assertEqual(30, compute(4))
        self.assertEqual(1, compute(1))


if __name__ == '__main__':
    unittest.main()
