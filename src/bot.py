import telebot
from telebot import apihelper
import config
import sticker
from kinopoisk import get_cinema

bot = telebot.TeleBot(config.token)
apihelper.proxy = {'http': config.proxy}
START = 'start'
HELP = 'help'
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Привет')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Фильм')
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('Пока')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, f'Напиши команду /start и мы начнем')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Вас приветствует КиноджоБот', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.from_user.id
    username = message.from_user.first_name
    user_text = message.text.lower
    if user_text() == 'привет':
        bot.send_message(chat_id, f'Привет, {username}', reply_markup=keyboard2)
        bot.send_sticker(chat_id, sticker.hello_sticker)
    elif user_text() == 'фильм':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Аниме', callback_data='Аниме'))
        markup.add(telebot.types.InlineKeyboardButton(text='Комедия', callback_data='Комедия'))
        markup.add(telebot.types.InlineKeyboardButton(text='Боевик', callback_data='Боевик'))
        markup.add(telebot.types.InlineKeyboardButton(text='Детектив', callback_data='Детектив'))
        markup.add(telebot.types.InlineKeyboardButton(text='Мультфильм', callback_data='Мультфильм'))
        markup.add(telebot.types.InlineKeyboardButton(text='Драма', callback_data='Драма'))
        markup.add(telebot.types.InlineKeyboardButton(text='Мелодрама', callback_data='Мелодрама'))
        markup.add(telebot.types.InlineKeyboardButton(text='Научный', callback_data='Научный'))
        markup.add(telebot.types.InlineKeyboardButton(text='Криминал', callback_data='Криминал'))
        markup.add(telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='Ужасы'))
        markup.add(telebot.types.InlineKeyboardButton(text='Фантастика', callback_data='Фантастика'))
        markup.add(telebot.types.InlineKeyboardButton(text='Триллер', callback_data='Триллер'))
        markup.add(telebot.types.InlineKeyboardButton(text='Документальный', callback_data='Документальный'))
        markup.add(telebot.types.InlineKeyboardButton(text='Ничего не подходит', callback_data='Ничего не подходит'))
        bot.send_message(message.chat.id, text="Какой жанр предпочитаете?", reply_markup=markup)
    elif user_text() == 'пока':
        bot.send_message(chat_id, f'Пока, {username}')
        bot.send_sticker(chat_id, sticker.bye_sticker)
    else:
        bot.send_sticker(chat_id, sticker.wtf_sticker)


cinema = {
    'Аниме': 'https://jut.su/jojo-bizarre-adventure/season-1/episode-1.html',
    'Комедия': 'https://www.kinopoisk.ru/film/535341',
    'Боевик': 'https://www.kinopoisk.ru/film/1009536/',
    'Детектив': 'https://www.kinopoisk.ru/film/467099/',
    'Мультфильм': 'https://www.kinopoisk.ru/film/81621/',
    'Драма': 'https://www.kinopoisk.ru/film/220541/',
    'Мелодрама': 'https://www.kinopoisk.ru/film/22803/',
    'Научный': 'https://www.kinopoisk.ru/film/652833/',
    'Криминал': 'https://www.kinopoisk.ru/film/278522/',
    'Ужасы': 'https://www.kinopoisk.ru/film/686898/',
    'Фантастика': 'https://www.kinopoisk.ru/film/538225',
    'Триллер': 'https://www.kinopoisk.ru/film/572461/',
    'Документальный': 'https://www.kinopoisk.ru/film/424378/',
}


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
    sad = 'Очень жаль'
    if call.data in cinema:
        answer = get_cinema(call.data)
        bot.send_message(call.message.chat.id, answer)

    else:
        bot.send_message(call.message.chat.id, sad, reply_markup=keyboard3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
