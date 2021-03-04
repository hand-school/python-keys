from kinopoisk_api import KP

kinopoisk = KP(token='9736285b-b7d0-4a40-9f9e-7cfb09354984')
search = kinopoisk.search('Анимэ')

for item in search:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
