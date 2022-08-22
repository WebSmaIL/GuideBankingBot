from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура с информацией
info_inline_btn_1 = InlineKeyboardButton(
    'Что запрещено на площадке', callback_data='illegal'
    )
info_inline_btn_2 = InlineKeyboardButton(
    'Перечень знаний, умений, навыков', callback_data='listOfKnowledge'
    )
info_inline_btn_3 = InlineKeyboardButton(
    'Обобщенная оценочная ведомость', callback_data='SumEvalState'
    )
info_inline_btn_4 = InlineKeyboardButton(
    'Модули с описанием работ', callback_data='modules'
    )

inline_client_keyboard_info = InlineKeyboardMarkup().add(info_inline_btn_1).add(info_inline_btn_2).add(info_inline_btn_3).add(info_inline_btn_4)

# Клавиатура разделов
chapter_inline_btn_1 = InlineKeyboardButton(
    'Организация работы ',
    callback_data='OrganizationOfWork'
    )
chapter_inline_btn_2 = InlineKeyboardButton(
    'Работа с залогами',
    callback_data='WorkingWithCollateral'
    )
chapter_inline_btn_3 = InlineKeyboardButton(
    'Ипотечное кредитование',
    callback_data='MortgageLending'
    )
chapter_inline_btn_4 = InlineKeyboardButton(
    'Потребительское кредитование',
    callback_data='ConsumerLending'
    )
chapter_inline_btn_5 = InlineKeyboardButton(
    'Работа с просроченной задолженностью',
    callback_data='DealingWithOverdueDebts'
    )

inline_client_keyboard_chapter = InlineKeyboardMarkup().add(
        chapter_inline_btn_1
    ).add(
        chapter_inline_btn_2
    ).add(
        chapter_inline_btn_3
    ).add(
        chapter_inline_btn_4
    ).add(
        chapter_inline_btn_5
    )