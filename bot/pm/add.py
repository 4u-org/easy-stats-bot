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

add_bot_state = State("add_bot")
add_bot_state_filter = StateFilter(add_bot_state)

router = Router()

def create_add_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text=texts.CANCEL.value)
    result_kb = kb.as_markup()
    result_kb.resize_keyboard = True
    result_kb.input_field_placeholder = texts.ADD_BOT_HINT.value
    return result_kb

@router.message(Command(commands=["add"]))
@router.message(F.text == texts.HELLO_ADD_BOT_BUTTON.lazy)
async def command_start_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot,
    user: DbUser
) -> None:
    await state.set_state(add_bot_state)
    kb = create_add_keyboard()
    await message.answer(texts.ADD_BOT.value, reply_markup=kb)
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
    await message.answer(texts.CANCEL_ADD_TEXT.value, reply_markup=kb)
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
        await message.answer(texts.ADD_BOT.value, reply_markup=kb)
        return
    bot_token = message.text
    try:
        new_bot = Bot(bot_token, parse_mode="HTML")
        info = await new_bot.get_me()
    except Exception as e:
        kb = create_add_keyboard()
        await message.answer(texts.ADD_BOT_ERROR.value, reply_markup=kb)
        return
    app = info.username

    # Send request to add bot with aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get(
            config.API_HOST + "/add_bot",
            params={"app": app, "token": bot_token, "force_auth": True},
        ) as resp:
            if resp.status != 200:
                kb = create_add_keyboard()
                await message.answer(texts.ADD_BOT_ERROR.value, reply_markup=kb)
                return
            kb = create_default_keyboard()
            await message.answer(texts.ADD_BOT_SUCCESS.value, reply_markup=kb)
            await state.clear()
            return
            
    
