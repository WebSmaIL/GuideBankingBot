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
    cdIsConnect = [True, "commandsDict"]
    
with open('./json/messagesDict.json', 'r', encoding="utf-8") as data:
    messagesDict = json.load(data)
    mdIsConnect = [True, "messagesDict"]
    
with open('./json/datadict.json', 'r', encoding="utf-8") as data:
    dataDict = json.load(data)
    ddIsConnect = [True, "dataDict"]

def databasesIsWorking():
    for i in [cdIsConnect, mdIsConnect, ddIsConnect]:
        if i[0]:
            print(f"{i[1]} is connect!")
