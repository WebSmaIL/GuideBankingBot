from aiogram.utils import executor
from create_bot import dp



async def on_start(_):
    print('Bot is working')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)