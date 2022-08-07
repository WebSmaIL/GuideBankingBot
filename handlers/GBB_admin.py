from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import sql_add_command

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Начало диалога загрузки нового пункта
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')

# Ловим первый ответ
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введи название")

# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введи описание")

# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Введи цену")

# Ловим четвертый ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await sql_add_command(state)
    await message.reply("Товар успешно добавлен!!!\n") 
    await state.finish()

# Отмена
# @dp.message_handler(commands='отмена', state="*")
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message : types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()

def client_handlers_register(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, commands='отмена', state="*")
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")