import aiogram
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import src.keyboards as kb
from src.config import token, MsgReply
from src.sql_commands import SQLiter

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=token)

storage = MemoryStorage()

dp = aiogram.Dispatcher(bot, storage=storage)

db = SQLiter('habits.db')


@dp.message_handler(commands="start")
async def message_welcome(message: aiogram.types.Message):
    print(message.from_user.id)
    db.add_user(message.from_user.id)
    await message.reply(MsgReply.greeting.format(message.from_user.first_name), reply_markup=kb.starting_kb)


@dp.message_handler(commands="help")
async def message_help(message: aiogram.types.Message):
    await message.reply(MsgReply.helping)


@dp.message_handler(commands="clear")
async def command_clear(message: aiogram.types.Message):
    if db.user_exists(message.from_user.id):
        db.delete_user(message.from_user.id)
        await message.reply(MsgReply.clearing_apply)
    else:
        await message.reply(MsgReply.clearing_cancel)


# @dp.message_handler(aiogram.types.Message())
# async def message_bad_habit(massage: aiogram.types.Message):
#     pass


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
