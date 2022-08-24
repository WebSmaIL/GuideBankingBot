import json
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

tests_client_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
)
with open('./json/testsDict.json', 'r', encoding="utf-8") as data:
    testsDict = json.load(data)

for key in testsDict:
    tests_client_keyboard.insert(KeyboardButton(key))

exit_btn = KeyboardButton("Выйти")
tests_client_keyboard.add(exit_btn)