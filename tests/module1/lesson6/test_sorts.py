import unittest
from src.module1.lesson6.sorts import *


class TestTasks(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 100], bubble_sort([100, 2, 4, 5, 3, 1]))

    def test_selection_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 100], selection_sort([100, 2, 4, 5, 3, 1]))

    def test_insert_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 100], insert_sort([100, 2, 4, 5, 3, 1]))

    def test_get_max_and_min(self):
        self.assertEqual((-3, 201), get_max_and_min([2, 5, 7, 100, 3, 1, -3, 201]))

    def test_quick_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 100], quick_sort([100, 2, 4, 5, 3, 1]))
