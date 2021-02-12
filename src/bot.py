import telebot
import config
import sticker

bot = telebot.TeleBot(config.token)
START = 'start'
HELP = 'help'


@bot.message_handler(commands=[START, HELP])
def send_welcome(message):
    bot.reply_to(message, f'Вас привествует КиноджоБот', reply_markup=keyboard, )


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('Привет', 'Фильм', 'Пока')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.from_user.id
    username = message.from_user.first_name
    if message.text.lower() == 'привет':
        bot.send_message(chat_id, f'Привет, {username}')
        bot.send_sticker(chat_id, sticker.hello_sticker)
    elif message.text.lower() == 'фильм':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Ужастик', callback_data='Ужастик'))
        markup.add(telebot.types.InlineKeyboardButton(text='Комедия', callback_data='Комедия'))
        markup.add(telebot.types.InlineKeyboardButton(text='Боевик', callback_data='Боевик'))
        bot.send_message(message.chat.id, text="Какой жанр предпочитаете?", reply_markup=markup)
    elif message.text.lower() == 'пока':
        bot.send_message(chat_id, f'Пока, {username}')
        bot.send_sticker(chat_id, sticker.bye_sticker)
    else:
        bot.send_sticker(chat_id, sticker.wtf_sticker)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
    answer = ''
    if call.data == 'Ужастик':
        answer = 'Вот список!'
    elif call.data == 'Комедия':
        answer = 'Вот список!'
    elif call.data == 'Боевик':
        answer = 'Вот список!'

    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True)

