import asyncio
import logging
from aiogram import Bot,Dispatcher,Router
from config import TOKEN
from aiogram.types import Message,CallbackQuery
from hendlers import router


bot = Bot(token=TOKEN)

dp = Dispatcher()






async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)
    


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')