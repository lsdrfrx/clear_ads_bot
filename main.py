import asyncio
import os
import sys

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

router = Router()


def message_contain_ads(message):
    return "лс" in message


@router.message(F.text)
async def handle_message(message: Message):
    if message_contain_ads(message.text):
        await message.delete()


async def main():
    TOKEN = os.getenv("TOKEN", "")
    if not TOKEN:
        print("Failed to read token")
        sys.exit()

    bot = Bot(token=TOKEN, parse_mode="html")
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
