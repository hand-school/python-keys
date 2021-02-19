#Докрутить картинку города и информация о городе. Перенести функционал погоды в отдельный файл
# Оформить файл README.md под бота


from time import sleep

import src.config

from src.weather import bot
from src.weather import WeatherFunc
from src.weather import CityInfo

import telebot
import requests


sleep(1)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}! \n' +
                     'Чтобы узнать погоду напишите в чат название города')


@bot.message_handler(commands=['help'])
def assist(message):
    bot.send_message(message.chat.id,
                     '/start запуск бота\n/help команды бота\nчтобы узнать погоду напишите в чат название города')

#При вводе города нужно вывести инфу по городу. Дальше необходимо по кнопке выбрать день, погоду котрого нужно узнать
CityInfo.city_description
WeatherFunc.city_weather



if __name__ == '__main__':
    bot.polling(none_stop=True)
