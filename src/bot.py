import telebot
import config
import sticker

bot = telebot.TeleBot(config.token)

START = 'start'
HELP = 'help'


@bot.message_handler(commands=[START, HELP])
def send_welcome(message):
    bot.reply_to(message, f'Вас привествует КиноджоБот', reply_markup=keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.from_user.id
    username = message.from_user.first_name
    if message.text.lower() == 'привет':
        bot.send_message(chat_id, f'Привет, {username}')
        bot.send_sticker(chat_id, sticker.hello_sticker)
    elif message.text.lower() == 'пока':
        bot.send_message(chat_id, f'Пока, {username}')
        bot.send_sticker(chat_id, sticker.bye_sticker)
    else:
        bot.send_sticker(chat_id, sticker.wtf_sticker)


bot.polling(none_stop=True)
