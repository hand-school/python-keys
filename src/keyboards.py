from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

button_junk_food = KeyboardButton('Джанкфудд')
button_smoking = KeyboardButton('Курение')
button_bear = KeyboardButton('Алкоголь')

starting_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_junk_food).add(button_bear).add(button_smoking)
