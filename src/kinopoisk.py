from kinopoisk_api import KP

kinopoisk = KP(token='9736285b-b7d0-4a40-9f9e-7cfb09354984')


def get_cinema(genre):
    search_result = kinopoisk.search(genre)
    return search_result[0].ru_name