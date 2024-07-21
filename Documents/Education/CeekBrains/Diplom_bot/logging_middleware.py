# logging_middleware.py

import logging
from aiogram import types, Dispatcher

async def log_user_activity(user_id, command):
    logging.info(f"User: {user_id} - Command: {command}")

async def log_message(message: types.Message, data: dict):
    await log_user_activity(message.from_user.id, message.text)

def setup_logging(dp: Dispatcher):
    dp.middleware.setup(log_message)
