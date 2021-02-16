import telebot
import config
import sticker

bot = telebot.TeleBot(config.token)
START = 'start'
HELP = 'help'
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('Привет', 'Фильм', 'Пока')


@bot.message_handler(commands=[START, HELP])
def send_welcome(message):
    bot.reply_to(message, f'Вас привествует КиноджоБот', reply_markup=keyboard, )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.from_user.id
    username = message.from_user.first_name
    user_text = message.text.lower
    if user_text() == 'привет':
        bot.send_message(chat_id, f'Привет, {username}')
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
        markup.add(telebot.types.InlineKeyboardButton(text='Мистика', callback_data='Мистика'))
        markup.add(telebot.types.InlineKeyboardButton(text='Научный', callback_data='Научный'))
        markup.add(telebot.types.InlineKeyboardButton(text='Криминал', callback_data='Криминал'))
        markup.add(telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='Ужасы'))
        markup.add(telebot.types.InlineKeyboardButton(text='Фэнтези', callback_data='Фэнтези'))
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
        answer = 'Вот список!'
    elif call.data == 'Комедия':
        answer = 'Вот список!'
    elif call.data == 'Боевик':
        answer = 'Вот список!'
    elif call.data == 'Детектив':
        answer = 'Вот список!'
    elif call.data == 'Мультфильм':
        answer = 'Вот список!'
    elif call.data == 'Драма':
        answer = 'Вот список!'
    elif call.data == 'Мелодрама':
        answer = 'Вот список!'
    elif call.data == 'Мистика':
        answer = 'Вот список!'
    elif call.data == 'Научный':
        answer = 'Вот список!'
    elif call.data == 'Криминал':
        answer = 'Вот список!'
    elif call.data == 'Ужасы':
        answer = 'Вот список!'
    elif call.data == 'Фэнтези':
        answer = 'Вот список!'
    elif call.data == 'Триллер':
        answer = 'Вот список!'
    elif call.data == 'Документальный':
        answer = 'Вот список!'
    else:
        answer = 'Очень жаль!'

    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True)

