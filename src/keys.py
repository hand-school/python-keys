import requests
from bs4 import BeautifulSoup

URL = 'https://www.ivi.ru'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko Chrome/88.0.4324.111 Mobile Safari/537.36',
    'accept': '* / *'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.fine_all('div',
                          class_='gallery__item')

    print(items)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('GG')


parse()
