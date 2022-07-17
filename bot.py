from aiogram import Bot, types, Dispatcher, executor
import asyncio
import config
import getword
from getword import get_new_word
from inlkeyb import keyboard1, keyboard2

bot = Bot(token=config.token)
dp = Dispatcher(bot)

async def start(ch, player):
    await bot.send_message(ch, text=f"Ведучий - {player}", reply_markup=keyboard1)

@dp.message_handler(commands=['start'])
async def game_start(message: types.Message):
    await bot.send_message(message.chat.id, text="Хто хоче бути ведучим?",
                                                 reply_markup=keyboard2)

@dp.message_handler()
async def right_word(message: types.Message):
    if message.text.lower() == config.server[message.chat.id][1].lower():
        await bot.send_message(message.chat.id, text = "Вітаю ви вгадали слово", reply_markup=keyboard2)
    else:
        pass

@dp.callback_query_handler(text = ["check_word", "get_new_word", "new_game"])
async def words(call: types.CallbackQuery):
    chat_id = call.message.chat.id

    if call.data == 'check_word' and call.from_user.id == config.server[chat_id][0]:
        await call.answer(text = f'Твоє слово: {config.server[chat_id][1]}', show_alert = True)

    elif call.data == "get_new_word" and call.from_user.id == config.server[chat_id][0]:
        config.word = get_new_word(chat_id)
        await call.answer(text = f'Нове слово: {config.server[chat_id][1]}', show_alert = True)

    if call.data == "new_game":
        config.server[chat_id] = [call.from_user.id, None]
        getword.get_new_word(chat_id)
        await asyncio.gather(start(chat_id, call.from_user.full_name))

    else:
        await call.answer(text='Заборонено', show_alert=True)

    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp)


