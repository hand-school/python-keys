import telebot
import src.config
import requests
import pyowm
import wikipediaapi
import datetime

bot = telebot.TeleBot(src.config.token)
url = 'http://api.openweathermap.org/data/2.5/weather'
wiki_wiki = wikipediaapi.Wikipedia('ru')



# @bot.message_handler(func=lambda message: True)
# def city_description(message):
#     page_py = wiki_wiki.page(f'{message.text}')
#     bot.send_message(message.chat.id, page_py.summary)


@bot.message_handler(content_types=['text'])
def city_weather(message):
    city_name = message.text
    chatId = message.chat.id

    try:
        params = {'APPID': src.config.api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        if weather["main"]['temp'] < 10:
            status = "Сейчас холодно!"
        elif weather["main"]['temp'] < 15:
            status = "Сейчас прохладно!"
        elif weather["main"]['temp'] > 30:
            status = "Сейчас жарко!"
        else:
            status = "Сейчас отличная температура!"

        bot.send_message(chatId, f"Текущая температура в городе " + str(weather["name"]) + ': ' + str(
            float(weather["main"]['temp'])) + "°С. Ощущается как: " + str(
            float(weather['main']['feels_like'])) + "\n" +
                         "Максимальная температура: " + str(float(weather['main']['temp_max'])) + "°С\n" +
                         "Минимальная температура: " + str(float(weather['main']['temp_min'])) + "°С\n" +
                         "Скорость ветра: " + str(float(weather['wind']['speed'])) + ' м/с' + "\n" +
                         "Давление: " + str(int(weather['main']['pressure'] * 0.750062)) + ' мм. рт. ст.' + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "Видимость: " + str(weather['visibility']) + " м\n" +
                         "Описание: " + str(weather['weather'][0]["description"])
                         + status + "\n\n")
        lon = str(float(weather['coord']['lon']))
        lat = str(float(weather['coord']['lat']))

    except Exception as e:
        bot.send_message(chatId, f"Произошла ошибка {e}. Город " + city_name + " не найден")

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/onecall",
                           params={'lat': lat, 'lon': lon, 'units': 'metric',
                                   'APPID': src.config.api_weather,  'cnt': 7})
        data = res.json()
        print(data)
        for i in data['daily']:
            bot.send_message(chatId, 'Дата ' + str(datetime.datetime.fromtimestamp(float(i['dt'])))
                             + '\nТемпература макс ' + str(float(i['temp']['max']))
                             + '\nТемпература мин ' + str(float(i['temp']['min']))
                             + '\nСкорость ветра: ' + str(float(i['wind_speed'])) + ' м/с')
    except Exception as e:
        bot.send_message(chatId, "Exception (forecast):", e)



