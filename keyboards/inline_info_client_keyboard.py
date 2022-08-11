from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton(
    'Что запрещено на площадке', callback_data='illegal'
    )
inline_btn_2 = InlineKeyboardButton(
    'Что можно', callback_data='legal'
    )

inline_client_keyboard_info = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)