from aiogram import Router
from bot.pm import start, add, delete, info

router = Router()

router.include_router(start.router)
router.include_router(add.router)
router.include_router(delete.router)
router.include_router(info.router)