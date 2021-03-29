import telebot
import src.config
import requests
import pyowm
import wikipediaapi
import datetime

bot = telebot.TeleBot(src.config.token)
url = 'http://api.openweathermap.org/data/2.5/weather'
wiki_wiki = wikipediaapi.Wikipedia('ru')


keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Привет')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Фильм')
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('Пока')


# @bot.message_handler(func=lambda message: True)
# def city_description(message):
#     page_py = wiki_wiki.page(f'{message.text}')
#     bot.send_message(message.chat.id, page_py.summary)


@bot.message_handler(content_types=['text'])
def city_weather(message):
    city_name = message.text
    chatid = message.chat.id
    username = message.from_user.first_name

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

        # (chatid, f"Текущая температура в городе " + str(weather["name"]) + ': ' + str(
        #     float(weather["main"]['temp'])) + "°С. Ощущается как: " + str(
        #     float(weather['main']['feels_like'])) + "\n" +
        #                  "Максимальная температура: " + str(float(weather['main']['temp_max'])) + "°С\n" +
        #                  "Минимальная температура: " + str(float(weather['main']['temp_min'])) + "°С\n" +
        #                  "Скорость ветра: " + str(float(weather['wind']['speed'])) + ' м/с' + "\n" +
        #                  "Давление: " + str(int(weather['main']['pressure'] * 0.750062)) + ' мм. рт. ст.' + "\n" +
        #                  "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
        #                  "Видимость: " + str(weather['visibility']) + " м\n" +
        #                  "Описание: " + str(weather['weather'][0]["description"])
        #                  + status + "\n\n")
        lon = str(float(weather['coord']['lon']))
        lat = str(float(weather['coord']['lat']))

    except Exception as e:
        bot.send_message(chatid, f"Произошла ошибка {e}. Город " + city_name + " не найден")

    count = 0 #Счетчик для дней
    day_dict = {
        0: "Сегодня",
        1: "Завтра",
        2: "Послезавтра",
        3: "Через 2 дня",
        4: "Через 3 дня",
        5: "Через 4 дня",
        6: "Через 5 дней",
        7: "Через 6 дней"
    }
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/onecall",
                           params={'lat': lat, 'lon': lon, 'units': 'metric',
                                   'APPID': src.config.api_weather,  'cnt': 7})
        data = res.json()
        print(data)
        for i in data['daily']:
            day_dict[i] = bot.send_message(chatid, 'Дата ' + str(datetime.datetime.fromtimestamp(float(i['dt'])))
                             + '\nТемпература макс ' + str(float(i['temp']['max']))
                             + '\nТемпература мин ' + str(float(i['temp']['min']))
                             + '\nСкорость ветра: ' + str(float(i['wind_speed'])) + ' м/с'
                             + '\nРассвет: ' + str(datetime.datetime.fromtimestamp(float(i['sunrise']))))
    except Exception as e:
        bot.send_message(chatid, "Exception (forecast):", e)

    if city_name == ' ':
        if telebot.types.InlineKeyboardButton.text in day_dict:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text=0, callback_data='Сегодня'))
            markup.add(telebot.types.InlineKeyboardButton(text=1, callback_data='Завтра'))
            markup.add(telebot.types.InlineKeyboardButton(text=2, callback_data=''))
            markup.add(telebot.types.InlineKeyboardButton(text=3, callback_data=''))
            markup.add(telebot.types.InlineKeyboardButton(text=4, callback_data=''))
            markup.add(telebot.types.InlineKeyboardButton(text=5, callback_data=''))
            markup.add(telebot.types.InlineKeyboardButton(text=6, callback_data=''))
            markup.add(telebot.types.InlineKeyboardButton(text=7, callback_data=''))
            bot.send_message(chatid, text="Какой день вас интересует?", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
        answer = ''
        if call.data == 'Сегодня':
            answer = ""
        elif call.data == 'Завтра':
            answer = 'https://www.kinopoisk.ru/film/535341/'
        elif call.data == '3':
            answer = 'https://www.kinopoisk.ru/film/1009536/'
        elif call.data == '4':
            answer = 'https://www.kinopoisk.ru/film/467099/'
        elif call.data == '5':
            answer = 'https://www.kinopoisk.ru/film/81621/!'
        elif call.data == '6':
            answer = 'https://www.kinopoisk.ru/film/220541/'
        elif call.data == '7':
            answer = 'https://www.kinopoisk.ru/film/22803/'
        elif call.data == '8':
            answer = 'https://www.kinopoisk.ru/film/652833/'

        else:
            bot.send_message(call.message.chat.id, 'Упс!', reply_markup=keyboard3)

        bot.send_message(call.message.chat.id, answer)

#
#
