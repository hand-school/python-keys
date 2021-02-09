import telebot
import src.config
import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
bot = telebot.TeleBot(src.config.token)


@bot.message_handler(content_types=['text'])
def city_weather(message):
    city_name = message.text

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

    except Exception as e:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")