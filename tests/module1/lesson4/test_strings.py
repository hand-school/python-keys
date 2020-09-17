import unittest

from src.module1.lesson4.strings import *


class TestTasks(unittest.TestCase):

    def test_use_len(self):
        self.assertEqual(11, use_len("Hello world"))
        self.assertEqual(1100, use_len("Hello world" * 100))

    def test_cut_word(self):
        self.assertEqual("П-т", cut_word("Привет"))
        self.assertEqual("H-w", cut_word("Hello world"))

    def test_r_l_find(self):
        self.assertEqual((1, 1), r_l_find("Привет", "р"))
        self.assertEqual((4, 7), r_l_find("Hello world", "o"))

    def test_replace_chars(self):
        self.assertEqual("П*ивет, мой д*уг", replace_chars("Привет, мой друг", "р", "*"))

    def test_count_chars(self):
        self.assertEqual(2, count_chars("Hello world", "o"))

    def test_second_symbol(self):
        pass
