from cgitb import text
from aiogram import types, Dispatcher
from create_bot import commandsDict, messagesDict, dp, bot, dataDict
from keyboards import client_keyboard, inline_client_keyboard_info, inline_client_keyboard_chapter
# from data_base.sqlite_db import sql_read
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

kb_dict = {
    'info' : inline_client_keyboard_info,
    'chapter' : inline_client_keyboard_chapter,
}

async def command_start(message : types.Message):
    if message.text in commandsDict.keys():
        await message.answer(message.from_user.full_name + ", " + commandsDict[message.text], reply_markup=client_keyboard)

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

class test_1(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()

@dp.message_handler(commands=['starttest'])
async def test_1_start(message: types.Message):
    await message.answer("1)Активы коммерческого банка по степени риска разделены на ______ групп")
    await test_1.question_1.set()

@dp.message_handler(state=test_1.question_1)
async def test_1_answer_1(message: types.Message, state: FSMContext):
    await state.update_data(answer_1=message.text)
    await message.answer("2)Банк аккумулирует необходимые ресурсы с помощью ________ операций.")
    await test_1.next()

@dp.message_handler(state=test_1.question_2)
async def test_1_answer_1(message: types.Message, state: FSMContext):
    await state.update_data(answer_2=message.text)
    await message.answer("3)Банк размещает собственные и привлеченные средства для получения прибыли с помощью _________ операций.")
    await test_1.next()

@dp.message_handler(state=test_1.question_3)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(answer_3=message.text)
    data = await state.get_data()
    await message.answer(f"1) {data['answer_1']}\n"
                         f"2) {data['answer_2']}\n"
                         f"3) {data['answer_3']}")
    await state.finish()


def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(messages_handler)
    dp.register_callback_query_handler(process_callback, text=dataDict.keys())