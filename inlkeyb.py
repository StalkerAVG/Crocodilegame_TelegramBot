from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_word = InlineKeyboardButton(text = "Подивитися Слово", callback_data='check_word')
get_new_word = InlineKeyboardButton(text = "Змінити слово", callback_data='get_new_word')
keyboard1 = InlineKeyboardMarkup().add(check_word, get_new_word)

new_game = InlineKeyboardButton(text = "Хто хоче бути ведучим, хай нажме на кнопку", callback_data='new_game')
keyboard2 = InlineKeyboardMarkup().add(new_game)

