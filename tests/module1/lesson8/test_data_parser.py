import unittest

from src.module1.lesson8.data_parser import *


class TestTasks(unittest.TestCase):

    def test_parse_fio(self):
        self.assertEqual("Привет, Ivan Olegovich! Твоя фамилия Ivanov?", parse_fio("Ivan Ivanov Olegovich"))

    def test_horoscope(self):
        self.assertEqual("Aries ★★★★ ❤❤❤❤", horoscope(0))

    def test_list_params(self):
        self.assertEqual(
            "Sum: 68.49; Mean: 11.41; Min: -84.69; Max: 87.80",
            list_params("87,80 66,01 1,89 -84,69 -38,19 35,67")
        )

    def test_max_grade_people(self):
        self.assertEqual(
            "Cynthia",
            max_grade_people(
                "Marilyn 5,Claire 0,Larry 2,Ward 8,Cynthia 10,William 1,Jose 10,Joy 4,Vickey 4,Jonathan 0,Horace 4,James 2,Nora 4,Robert 9,David 6,Jorge 7,Jean 1,Betty 4,Warren 9,Carrie 1,Debra 8,John 0,Maxie 10")
        )


if __name__ == '__main__':
    unittest.main()
