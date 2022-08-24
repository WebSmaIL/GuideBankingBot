import json
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


tests_client_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
with open('./json/testsDict.json', 'r', encoding="utf-8") as data:
    testsDict = json.load(data)

for key in testsDict:
    tests_client_keyboard.insert(KeyboardButton(key))

exit_btn = KeyboardButton("Назад")
tests_client_keyboard.add(exit_btn)

keyboard_for_test = ReplyKeyboardMarkup(
    resize_keyboard=True
).row(KeyboardButton("1"), 
      KeyboardButton("2"), 
      KeyboardButton("3"), 
      KeyboardButton("4")).add(KeyboardButton("Выйти"))