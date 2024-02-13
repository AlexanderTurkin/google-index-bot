from typing import Dict
import requests
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery, InputMediaPhoto

from connections.database.requests import user_exists, add_user, get_user
from connections.database.models import User
from tgbot.keyboards.inline import main_keyboard

main_router = Router()


@main_router.message()
async def main(message: Message, state: FSMContext):
    await state.clear()

    try:
        if message.text != '/start':
            await message.delete()
    except:
        pass

    await message.answer_photo(photo=FSInputFile('media/main.png'),
                               caption='👋 <b>Привет!</b> Это бот <b>Google Indexing</b> 🗺️\n ➥ Помогу быстро <b>происндексировать твои </b> <code>ссылки</code> 👇',
                               reply_markup=main_keyboard())
