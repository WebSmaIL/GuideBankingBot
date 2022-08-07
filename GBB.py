from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db 


async def on_start(_):
    print('Bot is working')
    sqlite_db.sql_start()

from handlers import GBB_admin, GBB_client
GBB_client.client_handlers_register(dp)
GBB_admin.client_handlers_register(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)