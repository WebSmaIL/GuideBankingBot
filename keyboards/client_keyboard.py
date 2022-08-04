from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

btn_1 = KeyboardButton('/Меню')
btn_2 = KeyboardButton('/Помощь')

client_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)

client_keyboard.row(btn_1, btn_2)