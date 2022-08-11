from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

commandsDict = {
    '/start' : 'Привет, вы пользуетесь ботом GuideBanking_bot, который предназначен для того чтобы в помочь вам разобраться в том, как устроен демонстрационный экзамен по банковскому делу!!!',
    '/help' : 'Информация о помощи по боту'
}

messagesDict = {
    'Информация про экзамен' : 'Выберите один из пунктов, чтобы узнать подробную информацию по теме.',
    'Задания' : 'Задания с прошлых экзаменов'
}

dataDict = {
    'illegal' : 'Запрещается использование мобильных телефонов, личных ноутбуков,планшетов, иных электронных устройств.',
    'legal': 'можно все'
}