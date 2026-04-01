import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("🇵🇱 Witaj w Wielkiej Polsce 🇵🇱")

    await dp.start_polling(bot)  # Long Polling – brak SSL/portów

if __name__ == "__main__":
    asyncio.run(main())