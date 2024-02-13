from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from connections.database.models import User
from aiogram.utils.keyboard import InlineKeyboardBuilder

back_button = InlineKeyboardButton(text='🔙 В главное меню', callback_data='back')

def main_keyboard(user: User):
    keyboard = InlineKeyboardBuilder()

    if user.language == 0:
        language = '🇷🇺 Русский'
    else:
        language = '🇺🇸 English'

    keyboard.row(InlineKeyboardButton(text='💡 Индексация', callback_data='new_order'))
    keyboard.row(
                InlineKeyboardButton(text='🏦 Мой баланс', callback_data='calc_order'),
                InlineKeyboardButton(text='🚀 Реферальная система', callback_data='my_orders')
                 )
    keyboard.row(
                InlineKeyboardButton(text='🏙️ Наш канал', url='https://t.me/romariosneakers'),
    )
    keyboard.row(
                InlineKeyboardButton(text=language, callback_data='change_language'),
                InlineKeyboardButton(text='☎️ Менеджер', url='https://t.me/playerrn')
    )
    return keyboard.as_markup()