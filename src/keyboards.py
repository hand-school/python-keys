from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from src.massage import MsgWord

button_junk_food = KeyboardButton(MsgWord.alcohol)
button_smoking = KeyboardButton(MsgWord.smoking)
button_bear = KeyboardButton(MsgWord.junk_food)

starting_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_junk_food).add(button_bear).add(button_smoking)
