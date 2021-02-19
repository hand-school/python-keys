import telebot
import config
import sticker

bot = telebot.TeleBot(config.token)
url = 'https://kinopoiskapiunofficial.tech/api/v2.1/films'
START = 'start'
HELP = 'help'
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Привет')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Фильм')
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('Пока')


@bot.message_handler(commands=[HELP])
def send_help(message):
    bot.reply_to(message, f'Напиши команду /start и мы начнем')


@bot.message_handler(commands=[START])
def send_welcome(message):
    bot.reply_to(message, f'Вас привествует КиноджоБот', reply_markup=keyboard1)


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


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
    answer = ''
    if call.data == 'Аниме':
        answer = 'https://jut.su/jojo-bizarre-adventure/season-1/episode-1.html'
    elif call.data == 'Комедия':
        answer = 'https://www.kinopoisk.ru/film/535341/'
    elif call.data == 'Боевик':
        answer = 'https://www.kinopoisk.ru/film/1009536/'
    elif call.data == 'Детектив':
        answer = 'https://www.kinopoisk.ru/film/467099/'
    elif call.data == 'Мультфильм':
        answer = 'https://www.kinopoisk.ru/film/81621/!'
    elif call.data == 'Драма':
        answer = 'https://www.kinopoisk.ru/film/220541/'
    elif call.data == 'Мелодрама':
        answer = 'https://www.kinopoisk.ru/film/22803/'
    elif call.data == 'Научный':
        answer = 'https://www.kinopoisk.ru/film/652833/'
    elif call.data == 'Криминал':
        answer = 'https://www.kinopoisk.ru/film/278522/'
    elif call.data == 'Ужасы':
        answer = 'https://www.kinopoisk.ru/film/686898/'
    elif call.data == 'Фантастика':
        answer = 'https://www.kinopoisk.ru/film/538225'
    elif call.data == 'Триллер':
        answer = 'https://www.kinopoisk.ru/film/572461/'
    elif call.data == 'Документальный':
        answer = 'https://www.kinopoisk.ru/film/424378/'
    else:
        bot.send_message(call.message.chat.id, 'Очень жаль!', reply_markup=keyboard3)

    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)

