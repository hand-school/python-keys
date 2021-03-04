import requests
from bs4 import BeautifulSoup


def parse():
    Url = 'https://www.kinopoisk.ru/lists/navigator/Comedy/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-T815 Build/NRD90M) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 67.0.3396.103 YaBrowser / 18.7.1.575.01 Safari/537.36'
    }

    response = requests.get(Url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    films = soup.find_all('div', class_='desktop-seo-selection-film-item selection-list__film')
    comps = []

    for film in films:
        comps.append({
            'title': film.find('a',
                               class_='_32YH6y--9Wy_h18jNjcExG _1MG74vTvaoBQmB-_AmSxe5 rX2wg-Vp7_P1amxEKCGQU _1C4nU_2YNS1qfctqWyz5D4').get_text(
                strip=True)
        })

        for comp in comps:
            print(comp['title'])


parse()
