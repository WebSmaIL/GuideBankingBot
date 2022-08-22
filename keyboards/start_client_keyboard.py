from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

btn_1 = KeyboardButton('Информация про экзамен')

client_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)

client_keyboard.row(btn_1)