import json
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

""" STATE CLASS FOR TESTS """
class test_1(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()
    

""" FUNCTIONS FOR TESTS """
# @dp.message_handler(commands=['starttest'])
async def test_1_start(message: types.Message):
    with open('./json/testsDict.json', 'r', encoding="utf-8") as data:
        global currentTest
        currentTest = json.load(data)[message.text]
    await message.answer(currentTest["question_1"])
    await test_1.question_1.set()

# @dp.message_handler(state=test_1.question_1)
async def test_1_answer_1(message: types.Message, state: FSMContext):
    await state.update_data(answer_0=message.text)
    await message.answer(currentTest["question_2"])
    await test_1.next()

# @dp.message_handler(state=test_1.question_2)
async def test_1_answer_2(message: types.Message, state: FSMContext):
    await state.update_data(answer_1=message.text)
    await message.answer(currentTest["question_3"])
    await test_1.next()

# @dp.message_handler(state=test_1.question_3)
async def test_1_answer_3(message: types.Message, state: FSMContext):
    await state.update_data(answer_2=message.text)
    data = await state.get_data()
    counter = 0
    strr=""
    for i in range(len(currentTest["answers"])):
        strr+=f"Вопрос {str(i+1)} \nВаш ответ: {data[f'answer_{str(i)}']}\nПравильный ответ: {currentTest['answers'][i]}\n\n"
        if currentTest['answers'][i] == data[f'answer_{str(i)}']:
            counter+=1
    strr+=f"Всего правильных ответов {str(counter)} из {str(len(currentTest['answers']))}"
    await message.answer(strr)
    
    await state.finish()


def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(
        command_start, 
        commands=['start', 'help']
    )
    dp.register_message_handler(
        test_1_start, 
        commands=['starttest1', 'starttest2'], 
        state=None
    )
    dp.register_message_handler(test_1_answer_1, state=test_1.question_1)
    dp.register_message_handler(test_1_answer_2, state=test_1.question_2)
    dp.register_message_handler(test_1_answer_3, state=test_1.question_3)
    dp.register_message_handler(messages_handler)
    dp.register_callback_query_handler(process_callback, text=dataDict.keys())
    