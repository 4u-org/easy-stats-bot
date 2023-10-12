from typing import Awaitable
from aiogram import Router, Bot, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import aiohttp

from utils.texts import TranslationTexts as texts
from tgtypes.db_user import DbUser
import config

router = Router()
@router.message()
async def command_start_handler(
    message: types.Message,
    state: FSMContext,
    bot: Bot,
    user: DbUser
) -> None:
    from bot.pm.start import create_default_keyboard
    kb = create_default_keyboard()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            config.ID_API_HOST + "/get_info",
            params={"query": message.text, "access_token": config.ID_API_TOKEN},
        ) as resp:
            # print(resp.status, await resp.json())
            if resp.status != 200:
                await message.answer(texts.BOT_NOT_FOUND.value, reply_markup=kb)
                return
            answer = await resp.json()
            if answer["info"]["type"] != "ChatType.BOT":
                await message.answer(texts.IS_NOT_BOT.value, reply_markup=kb)
                return
            bot_info = answer["info"] 

    async with aiohttp.ClientSession() as session:
        async with session.get(
            config.API_HOST + "/get_bot",
            params={"bot_id": bot_info["id"]},
        ) as resp:
            if resp.status != 200:
                await message.answer(texts.BOT_NOT_ADDED.value, reply_markup=kb)
                return
            answer = await resp.json()
            app = answer["app"]

    link = texts.BOT_STATS_LINK.value.format(app_name=app, bot_id=bot_info["id"])
    await message.answer(texts.BOT_STATS.value.format(link=link), reply_markup=kb)
    return
