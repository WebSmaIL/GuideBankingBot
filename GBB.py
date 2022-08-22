from aiogram.utils import executor
from create_bot import databasesIsWorking, dp
from data_base import sqlite_db 
""" from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext """

# class test_1(StatesGroup):
#     question_1 = State()
#     question_2 = State()
#     question_3 = State()

async def on_start(_):
    # Вывод системных сообщений
    databasesIsWorking()
    print('Bot is working')
    # sqlite_db.sql_start()

from handlers import GBB_admin, GBB_client
GBB_client.client_handlers_register(dp)
# GBB_admin.client_handlers_register(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)