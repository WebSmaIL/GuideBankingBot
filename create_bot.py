from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

commandsDict = {
    '/start' : 'Привет, вы пользуетесь ботом GuideBanking_bot, который предназначен для того чтобы в помочь вам разобраться в том, как устроен демонстрационный экзамен по банковскому делу!!!',
    '/help' : 'Готов помогать'
}