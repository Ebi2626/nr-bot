import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from handlers import common, navigation

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(token=os.getenv("BOT_TOKEN"))

    # TODO: Replace with REDIS
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.include_router(common.router)
    dp.include_router(navigation.router)

    logger.info("Bot uruchomiony. Czekam na wiadomości…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())