import unittest
from src.module1.lesson4.lists import *


class TestTasks(unittest.TestCase):

    def test_find_people(self):
        self.assertEqual(1, find_people(['Петров', 'Иванов', 'сидоров'], 'C'))

    def test_change_numbers(self):
        self.assertEqual([1, 2, 3, 0, 0, 0], change_numbers([1, 2, 3, 0, -2, -3]))
        self.assertEqual([], change_numbers([]))
