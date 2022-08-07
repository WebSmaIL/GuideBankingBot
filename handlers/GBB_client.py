from aiogram import types, Dispatcher
from create_bot import commandsDict, dp
from keyboards import client_keyboard
from data_base.sqlite_db import sql_read


async def command_start(message : types.Message):
    if message.text in commandsDict.keys():
        await message.answer(commandsDict[message.text], reply_markup=client_keyboard)
    
async def send_menu(message : types.Message):
    await sql_read(message)

        
def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(send_menu, commands=['Меню'])