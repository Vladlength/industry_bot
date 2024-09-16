import asyncio
from aiogram import Bot, Dispatcher, F

import config
from handlers import router


async def main():
    bot = Bot(token=config.TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot is off")
