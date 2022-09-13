from aiogram.utils import executor
from create_bot import databasesIsWorking, dp


async def on_start(_):
    # Вывод системных сообщений
    databasesIsWorking()
    print('Bot is working')

from handlers import GBB_client
GBB_client.client_handlers_register(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)