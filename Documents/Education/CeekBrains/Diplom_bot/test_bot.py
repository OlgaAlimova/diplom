import unittest
from aiogram import Bot, Dispatcher, types
from config import API_TOKEN  # Убедитесь, что API_TOKEN импортирован корректно
from handlers import send_welcome, send_advisor_info, send_university_info, send_crypto_info, send_otc_info, \
    handle_callback
import asyncio
from unittest.mock import MagicMock
import datetime


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = Bot(token=API_TOKEN)
        Bot.set_current(self.bot)  # Установить текущий экземпляр бота
        self.dp = Dispatcher(self.bot)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    async def _test_message(self, command, handler):
        message = types.Message(
            message_id=1,
            from_user=types.User(id=1, is_bot=False, first_name="Test", last_name="User", username="testuser"),
            chat=types.Chat(id=1, type="private"),
            date=int(datetime.datetime.now().timestamp()),
            text=command
        )
        await handler(message)

    async def _test_callback(self, data, handler):
        callback_query = types.CallbackQuery(
            id='1',
            from_user=types.User(id=1, is_bot=False, first_name="Test", last_name="User", username="testuser"),
            message=types.Message(
                message_id=1,
                from_user=types.User(id=1, is_bot=False, first_name="Test", last_name="User", username="testuser"),
                chat=types.Chat(id=1, type="private"),
                date=int(datetime.datetime.now().timestamp()),
                text=""
            ),
            data=data
        )
        await handler(callback_query)

    def test_send_welcome(self):
        self.loop.run_until_complete(self._test_message('/start', send_welcome))

    def test_send_advisor_info(self):
        self.loop.run_until_complete(self._test_message('Финансовый советник', send_advisor_info))

    def test_send_university_info(self):
        self.loop.run_until_complete(self._test_message('Университет', send_university_info))

    def test_send_crypto_info(self):
        self.loop.run_until_complete(self._test_message('Криптоакадемия', send_crypto_info))

    def test_send_otc_info(self):
        self.loop.run_until_complete(self._test_message('Внебиржевые акции', send_otc_info))

    def test_handle_callback(self):
        self.loop.run_until_complete(self._test_callback('back_to_menu', handle_callback))
        self.loop.run_until_complete(self._test_callback('advisor_signup', handle_callback))
        self.loop.run_until_complete(self._test_callback('university_more_info', handle_callback))
        self.loop.run_until_complete(self._test_callback('crypto_more_info', handle_callback))
        self.loop.run_until_complete(self._test_callback('otc_more_info', handle_callback))

    def tearDown(self):
        self.loop.close()


if __name__ == '__main__':
    unittest.main()



