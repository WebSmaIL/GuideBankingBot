from cgitb import text
from aiogram import types, Dispatcher
from create_bot import commandsDict, messagesDict, dp, bot, dataDict
from keyboards import client_keyboard, inline_client_keyboard_info, inline_client_keyboard_chapter
# from data_base.sqlite_db import sql_read

kb_dict = {
    'info' : inline_client_keyboard_info,
    'chapter' : inline_client_keyboard_chapter
}

async def command_start(message : types.Message):
    if message.text in commandsDict.keys():
        await message.answer(commandsDict[message.text], reply_markup=client_keyboard)


async def messages_handler(message: types.Message):
    if message.text in messagesDict.keys():
        await message.reply(messagesDict[message.text][1],
                            reply_markup=kb_dict[messagesDict[message.text][0]],
                            parse_mode=types.ParseMode.HTML
                            )

async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if dataDict[callback_query.data][0]:
        await bot.send_message(
            callback_query.from_user.id,
            dataDict[callback_query.data][1],
            reply_markup=kb_dict[dataDict[callback_query.data][0]],
            parse_mode=types.ParseMode.HTML
        )
    else:
        await bot.send_message(
            callback_query.from_user.id,
            dataDict[callback_query.data][1],
            parse_mode=types.ParseMode.HTML
        )

def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(messages_handler)
    dp.register_callback_query_handler(process_callback, text=dataDict.keys())