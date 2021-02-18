import aiogram
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import src.keyboards as kb
from src.config import token, States
from src.massage import MsgReply, MsgWord
from src.sql_commands import SQLiter

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=token)

dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

db = SQLiter('habits.db')


@dp.message_handler(commands="start")
async def message_welcome(message: aiogram.types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(*States.STATE_START)
    if db.user_exists(message.from_user.id):
        await message.reply(MsgReply.greeting_cancel.format(message.from_user.first_name))
    else:
        db.add_user(message.from_user.id)
        await message.reply(MsgReply.greeting_apply.format(message.from_user.first_name), reply_markup=kb.starting_kb)


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


@dp.message_handler(aiogram.dispatcher.filters.Text(equals=MsgWord.junk_food), state="*")
async def message_habit_junk(message: aiogram.types.Message):
    db.add_habit(message.from_user.id, MsgWord.junk_food)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(*States.STATE_JUNK)
    await message.reply("Жрёшь", reply=False)


@dp.message_handler(aiogram.dispatcher.filters.Text(equals=MsgWord.smoking), state="*")
async def message_habit_smoke(message: aiogram.types.Message):
    db.add_habit(message.from_user.id, MsgWord.smoking)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(*States.STATE_SMOKE)
    await message.reply("Куришь", reply=False)


@dp.message_handler(aiogram.dispatcher.filters.Text(equals=MsgWord.alcohol), state="*")
async def message_habit_alcohol(message: aiogram.types.Message):
    db.add_habit(message.from_user.id, MsgWord.alcohol)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(*States.STATE_DRINK)
    await message.reply("Бухаешь", reply=False)


@dp.message_handler(state=States.STATE_JUNK)
async def message_junk(message: aiogram.types.Message):
    await message.reply("Знаю, что")


@dp.message_handler(state=States.STATE_DRINK | States.STATE_SMOKE)
async def message_drink(message: aiogram.types.Message):
    await message.reply("Знаю, что")


@dp.message_handler(state=States.STATE_SMOKE)
async def message_smoke(message: aiogram.types.Message):
    await message.reply("Знаю, что")


@dp.message_handler(state=States.all())
async def some_test_state_case_met(message: aiogram.types.Message):
    state = dp.current_state(user=message.from_user.id)
    text = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'.format(
            current_state=await state.get_state(),
            states=States.all()
    )
    await message.reply(text, reply=False)


@dp.message_handler()
async def message_other(message: aiogram.types.Message):
    await message.reply("Шо пишешь")


async def shutdown(dispatcher: aiogram.Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_shutdown=shutdown)
