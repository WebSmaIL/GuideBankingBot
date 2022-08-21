from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

commandsDict = {
    '/start' : 'Привет, вы пользуетесь ботом GuideBanking_bot, который предназначен для того чтобы в помочь вам разобраться в том, как устроен демонстрационный экзамен по банковскому делу!!!',
    '/help' : 'Информация о помощи по боту'
}

messagesDict = {
    'Информация про экзамен' : [
        'info', 'Выберите один из пунктов, чтобы узнать подробную информацию по теме.'
        ],
    'Задания' : [
        'tasks', 'Задания с прошлых экзаменов'
        ]
}

dataDict = {
    'illegal' : [False, 'Запрещается использование мобильных телефонов, личных ноутбуков, планшетов, иных электронных устройств.'],
    'listOfKnowledge': [
                        'chapter',
                        '<b>Важность разделов:</b><br><b>1)</b> Организация работы. <i>Важность - 24%</i><br><b>2)</b> Работа с залогами. <i>Важность - 8%</i><br><b>3)</b> Ипотечное кредитование. <i>Важность - 6%</i><br><b>4)</b> Потребительское кредитование. <i>Важность - 14%</i><br><b>5)</b> Работа с просроченной задолженностью. <i>Важность - 6%</i><br><b>Выберите нужный вам раздел:</b>'
                        ],
    'OrganizationOfWork' : [False, 'Организация работы'],
    'WorkingWithCollateral' : [False, 'Работа с залогами'],
    'MortgageLending' : [False, 'Ипотечное кредитование'],
    'ConsumerLending' : [False, 'Потребительское кредитование'],
    'DealingWithOverdueDebts' : [False, 'Работа с просроченной задолженностью'],
}