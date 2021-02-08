#Докрутить картинку города и информация о городе. Перенести функционал погоды в отдельный файл
# Оформить файл README.md под бота


from time import sleep

import config
import telebot
import requests


url = 'http://api.openweathermap.org/data/2.5/weather'
bot = telebot.TeleBot(config.token)
sleep(1)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}! \n' +
                     'Чтобы узнать погоду напишите в чат название города')


@bot.message_handler(commands=['help'])
def assist(message):
    bot.send_message(message.chat.id,
                     '/start запуск бота\n/help команды бота\nчтобы узнать погоду напишите в чат название города')


@bot.message_handler(content_types=['text'])
def city_weather(message):
    city_name = message.text

    try:
        params = {'APPID': config.api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
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

        bot.send_message(message.chat.id, f"Текущая температура в городе " + str(weather["name"]) + ': ' + str(
            float(weather["main"]['temp'])) + "°С. Ощущается как: " + str(float(weather['main']['feels_like'])) + "\n" +
                         "Максимальная температура: " + str(float(weather['main']['temp_max'])) + "°С\n" +
                         "Минимальная температура: " + str(float(weather['main']['temp_min'])) + "°С\n" +
                         "Скорость ветра: " + str(float(weather['wind']['speed'])) + ' м/с' + "\n" +
                         "Давление: " + str(int(weather['main']['pressure']*0.750062)) + ' мм. рт. ст.' + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "Видимость: " + str(weather['visibility']) + " м\n" +
                         "Описание: " + str(weather['weather'][0]["description"])
                         + "\n\n" + status)

    except:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")


if __name__ == '__main__':
    bot.polling(none_stop=True)
