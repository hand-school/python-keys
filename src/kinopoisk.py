from kinopoisk_api import KP
import random

kinopoisk = KP(token='9736285b-b7d0-4a40-9f9e-7cfb09354984')


def get_cinema(genre):
    search_result = kinopoisk.search(genre)
    return search_result[random.randrange(0, 4)].ru_name
