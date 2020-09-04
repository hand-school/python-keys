import unittest

from src.module1.lesson2 import tasks


class TestTasks(unittest.TestCase):

    def test_is_digit(self):
        self.assertEqual(True, tasks.is_digit(2))
        self.assertEqual(False, tasks.is_digit("sadfds"))

    def test_check_type(self):
        self.assertEqual(1, tasks.check_type("Hello"))
        self.assertEqual(2, tasks.check_type(5))
        self.assertEqual(3, tasks.check_type(5.4))
        self.assertEqual(4, tasks.check_type(True))

    def test_compare(self):
        self.assertEqual(1, tasks.compare(5, 3))
        self.assertEqual(-1, tasks.compare(4, 5))
        self.assertEqual(0, tasks.compare(5, 5))

    def test_age_description(self):
        self.assertEqual("1 год", tasks.age_description(1))
        self.assertEqual("21 год", tasks.age_description(21))
        self.assertEqual("132 года", tasks.age_description(132))
        self.assertEqual("12 лет", tasks.age_description(12))
        self.assertEqual("111 лет", tasks.age_description(111))
        self.assertEqual("199 лет", tasks.age_description(199))

    def test_triangle_kind(self):
        self.assertEqual(-1, tasks.triangle_kind(3.0, 7.5, 4.0))
        self.assertEqual(1, tasks.triangle_kind(5.0, 3.0, 4.0))
        self.assertEqual(2, tasks.triangle_kind(4.0, 6.0, 8.0))
        self.assertEqual(0, tasks.triangle_kind(1.0, 1.5, 1.5))


if __name__ == '__main__':
    unittest.main()
