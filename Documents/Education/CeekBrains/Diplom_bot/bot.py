import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import API_TOKEN
from handlers import register_handlers

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Setup middleware
dp.middleware.setup(LoggingMiddleware())

# Register handlers
register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
