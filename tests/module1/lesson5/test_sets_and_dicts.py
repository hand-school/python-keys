import unittest
from src.module1.lesson5.sets_and_dicts import *


class TestTasks(unittest.TestCase):

    def test_country_capital(self):
        self.assertEqual("Москва", country_capital('Россия'))
        self.assertEqual("Киев", country_capital('Украина'))

    def test_add_to_set(self):
        self.assertEqual({100}, add_to_set(100))

    def test_add_to_dict(self):
        self.assertEqual({'a': 100}, add_to_dict('a', 100))

    def test_max_word_repeated(self):
        self.assertEqual('de', max_word_repeated('de fef vsc de ss de cd'))

    def test_lists_to_dict(self):
        self.assertEqual({'Леша': 4, 'Олег': 5}, lists_to_dict(['Леша', 'Олег'], [4, 5]))


if __name__ == '__main__':
    unittest.main()
