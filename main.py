from aiogram import executor
import logging
from bot.dispetcher import dp
from bot import handlers

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
