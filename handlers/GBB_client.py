from cgitb import text
from aiogram import types, Dispatcher
from create_bot import commandsDict, messagesDict, dp, bot, dataDict
from keyboards import client_keyboard, inline_client_keyboard_info
# from data_base.sqlite_db import sql_read


async def command_start(message : types.Message):
    if message.text in commandsDict.keys():
        await message.answer(commandsDict[message.text], reply_markup=client_keyboard)


async def messages_handler(message: types.Message):
    if message.text in messagesDict.keys():
        await message.reply(messagesDict[message.text], reply_markup=inline_client_keyboard_info)

# @dp.callback_query_handler(func=lambda c: c.data in dataDict.keys())
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, dataDict[callback_query.data])

def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(messages_handler)
    dp.register_callback_query_handler(process_callback, text=dataDict.keys())


    """ dp.register_message_handler(send_menu, commands=['Меню']) """
    
    """ async def send_menu(message : types.Message):
    await sql_read(message) """