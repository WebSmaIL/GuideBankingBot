import json
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

with open('./json/commandsDict.json', 'r', encoding="utf-8") as data:
    commandsDict = json.load(data)
with open('./json/messagesDict.json', 'r', encoding="utf-8") as data:
    messagesDict = json.load(data)
with open('./json/datadict.json', 'r', encoding="utf-8") as data:
    dataDict = json.load(data)