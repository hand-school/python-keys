import unittest
from src.module1.lesson4.lists import *


class TestTasks(unittest.TestCase):

    def test_find_numbers(self):
        self.assertEqual(1, find_numbers([1,-1,2]))

    def test_find_people(self):
        self.assertEqual(1, find_people(['Петров', 'Иванов', 'Сидоров'], 'С'))

    def test_change_numbers(self):
        self.assertEqual([1, 2, 3, 0, 0, 0], change_numbers([1, 2, 3, 0, -2, -3]))
        self.assertEqual([], change_numbers([]))

    def test_list_revert(self):
        self.assertEqual([6, 5, 4, 3, 2, 1], list_revert([1, 2, 3, 4, 5, 6]))
        self.assertEqual([], list_revert([]))

    def test_to_char_sequence(self):
        self.assertEqual(['H', 'e', 'l', 'l', 'o'], to_char_sequence("Hello"))

    def test_list_to_string(self):
        self.assertEqual('He123l__В', list_to_string(['H', 'e', '123', 'l', '__В']))

    def test_common_part_of_lists(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 456],
            common_part_of_lists(
                [1, 2, 3, 4, 5, 11, 123, 324, 456],
                [-11, -5, 0, 1, 2, 3, 4, 5, 331, 456, 1024, 23]
            )
        )
        self.assertEqual([], common_part_of_lists([], []))

    def test_uncommon_part_of_lists(self):
        expected = [-11, -5, 0, 11, 123, 324, 331, 1024, 23]
        actual = uncommon_part_of_lists(
            [1, 2, 3, 4, 5, 11, 123, 324, 456],
            [-11, -5, 0, 1, 2, 3, 4, 5, 331, 456, 1024, 23]
        )
        for element in expected:
            self.assertTrue(element in actual, 'Expected ' + str(expected) + '   Actual ' + str(actual))
        self.assertEqual([], uncommon_part_of_lists([], []))

    def test_rebase(self):
        self.assertEqual(
            [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'],
             ['John', 'Smith', '7'], ['John', 'Ivanov', '6']],
            rebase(
                ['Ivan Ivanov 5', 'Petr Petrov 3', 'Jeff Downing 10', 'Petr Ivanov 7', 'John Smith 7', 'John Ivanov 6']
            ))

    def test_get_names(self):
        self.assertEqual(
            ['Ivan', 'Petr', 'Jeff', 'Petr', 'John', 'John'],
            get_names(
                [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'],
                 ['John', 'Smith', '7'], ['John', 'Ivanov', '6']])
        )
