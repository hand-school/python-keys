import telebot
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Вас привествует КиноджоБот', reply_markup=keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}')
        bot.send_sticker(message.from_user.id,'CAACAgIAAxkBAALKQGAek25AlerPVL4DwkAYqCbZUcnvAAKpCQACeVziCRbryzP9_dc6HgQ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, f'Пока, {message.from_user.first_name}')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALKQ2Aek_Q1xznJSFFKT15RdS0HBLLtAAIKAAMkcWIa1JSZpG-I8EYeBA')
    else:
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAALKNGAejF3p09-9xwnqqjVHg2Vx-GALAAJkAAM0IuoFKnXdXBIl-cUeBA')


bot.polling(none_stop=True)