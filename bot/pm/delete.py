from typing import Awaitable
import aiohttp
import config
from aiogram import Router, Bot, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import TranslationTexts as texts
from tgtypes.db_user import DbUser

add_bot_state = State("delete_bot")
add_bot_state_filter = StateFilter(add_bot_state)

router = Router()

def create_add_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text=texts.CANCEL.value)
    result_kb = kb.as_markup()
    result_kb.resize_keyboard = True
    result_kb.input_field_placeholder = texts.ADD_BOT_HINT.value
    return result_kb

@router.message(Command(commands=["delete"]))
async def command_start_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot,
    user: DbUser
) -> None:
    await state.set_state(add_bot_state)
    kb = create_add_keyboard()
    await message.answer(texts.DELETE_BOT.value, reply_markup=kb)
    return

@router.message(add_bot_state_filter, F.text == texts.CANCEL.lazy)
async def cancel_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot
) -> None:
    from bot.pm.start import create_default_keyboard
    await state.clear()
    kb = create_default_keyboard()
    await message.answer(texts.CANCEL_DELETE_TEXT.value, reply_markup=kb)
    return

@router.message(add_bot_state_filter)
async def add_bot_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot,
    user: DbUser
) -> None:
    from bot.pm.start import create_default_keyboard
    if not message.text:
        kb = create_add_keyboard()
        await message.answer(texts.DELETE_BOT.value, reply_markup=kb)
        return
    await message.answer("Произошла ошибка при удалении бота. Попробуйте еще раз")
            
    
