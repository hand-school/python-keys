import aiogram
import logging
from src.config import token
import src.sql_commands

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=token)

dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands="start")
async def message_welcome(message: aiogram.types.Message):
    await message.reply("Привет, {}! \nЯ бот для отслеживания ик вредных привычек.\nЯ помогу тебя урегулировать твои "
                        "вредные пркевычки, давай начнём!\nВыбери инетересующую тебя привычку."
                        .format(aiogram.types.User.first_name))


@dp.message_handler(commands="help")
async def message_help(message: aiogram.types.Message):
    await message.reply(
        "Напиши команду /start, узнать о боте.\nНапиши команду /clear, чтобы очить всю информацию о себе в памяти бота")


@dp.message_handler(commands="clear")
async def command_clear(message: aiogram.types.Message):
    await message.reply("Данная функция пока не реализованна")


@dp.message_handler(aiogram.types.Message())
async def message_bad_habit(massage:aiogram.types.Message):
    pass


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
