from aiogram import types, Dispatcher
from create_bot import messageDict, dp
# from aiogram.dispatcher import Dispatcher


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    if message.text in messageDict.keys():
        await message.answer(messageDict[message.text])
        
def client_handlers_regiser(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])