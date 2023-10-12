from typing import Awaitable
from aiogram import Router, Bot, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import TranslationTexts as texts
from tgtypes.db_user import DbUser

router = Router()

def create_default_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text=texts.HELLO_ADD_BOT_BUTTON.value)
    result_kb = kb.as_markup()
    result_kb.resize_keyboard = True
    result_kb.input_field_placeholder = texts.HELLO_HINT.value
    return result_kb

@router.message(Command(commands=["start"]))
async def command_start_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot,
    user: DbUser
) -> None:
    if not user.db.pm_referer and message.text and message.text.startswith("/start"):
        user.db.pm_referer = message.text[7:]
    kb = create_default_keyboard()
    await message.answer(texts.HELLO.value, reply_markup=kb)
    return
