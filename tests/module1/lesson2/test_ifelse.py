import unittest

from src.module1.lesson2.ifelse import *


class TestTasks(unittest.TestCase):

    def test_is_digit(self):
        self.assertEqual(True, is_digit(2))
        self.assertEqual(False, is_digit("sadfds"))

    def test_is_password_valid(self):
        self.assertEqual(False, is_password_valid("123456simple"))
        self.assertEqual(True, is_password_valid("simple123456"))

    def test_sign_in(self):
        self.assertEqual("Логин неверный", sign_in("dsfsdf", "123456"))
        self.assertEqual("Логин неверный", sign_in("dsfsdf", "simple123456"))
        self.assertEqual("Неверный пароль", sign_in("login123", "123456"))
        self.assertEqual("Успешный вход", sign_in("login123", "simple123456"))

    def test_check_type(self):
        self.assertEqual(1, check_type("Hello"))
        self.assertEqual(2, check_type(5))
        self.assertEqual(3, check_type(5.4))
        self.assertEqual(4, check_type(True))

    def test_compare(self):
        self.assertEqual(1, compare(5, 3))
        self.assertEqual(-1, compare(4, 5))
        self.assertEqual(0, compare(5, 5))

    def test_age_description(self):
        self.assertEqual("1 год", age_description(1))
        self.assertEqual("21 год", age_description(21))
        self.assertEqual("132 года", age_description(132))
        self.assertEqual("12 лет", age_description(12))
        self.assertEqual("111 лет", age_description(111))
        self.assertEqual("199 лет", age_description(199))


    def test_maximum(self):
        self.assertEqual(10, maximum(10, 3, 4)[0])
        self.assertEqual(1, maximum(1, 1, 1)[0])
        self.assertEqual(-5, maximum(-5, -5, -120)[0])

    def test_triangle_kind(self):
        self.assertEqual(-1, triangle_kind(3.0, 7.5, 4.0))
        self.assertEqual(1, triangle_kind(5.0, 3.0, 4.0))
        self.assertEqual(2, triangle_kind(4.0, 6.0, 8.0))
        self.assertEqual(0, triangle_kind(1.0, 1.5, 1.5))

    def test_multi_div(self):
        self.assertEqual(2, multi_div(10, 5, "div"))
        self.assertEqual(10, multi_div(2, 5, "multi"))
        self.assertEqual(50, multi_div(10, 5, "text"))
        self.assertEqual("Error", multi_div(10, 0, "div"))

    def test_can_move(self):
        self.assertEqual(True, can_move(1, 1, 1, 8))
        self.assertEqual(True, can_move(2, 1, 5, 1))
        self.assertEqual(False, can_move(1, 1, 5, 6))
        self.assertEqual(False, can_move(5, 5, 4, 4))

    def test_table_colors(self):
        self.assertEqual(True, table_colors(1, 1, 1, 1))
        self.assertEqual(True, table_colors(1, 1, 8, 8))
        self.assertEqual(True, table_colors(4, 4, 7, 5))
        self.assertEqual(False, table_colors(2, 3, 8, 8))


if __name__ == '__main__':
    unittest.main()
