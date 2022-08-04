from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
messageDict = {
    '/start' : 'Привет, вы пользуетесь ботом GuideBanking_bot, который предназначен для того чтобы в помочь вам разобраться в том, как устроен демонстрационный экзамен по банковскому делу!!!',
    '/help' : 'Готов помогать'
}

async def on_start(_):
    print('Bot is working')

""" ************************* Клиентская часть бота ************************* """

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    if message.text in messageDict.keys():
        await message.answer(messageDict[message.text])
    
""" ************************* Админская часть бота ************************** """

executor.start_polling(dp, skip_updates=True, on_startup=on_start)