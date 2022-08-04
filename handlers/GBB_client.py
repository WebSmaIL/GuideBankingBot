from aiogram import types, Dispatcher
from create_bot import messageDict, dp
from keyboards import client_keyboard


async def command_start(message : types.Message):
    if message.text in messageDict.keys():
        await message.answer(messageDict[message.text], reply_markup=client_keyboard)
        
async def veronika_love(message : types.Message):
    await message.answer('Привет Вероника я тебя безумно люблю💖💖💖')
        
def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(veronika_love)