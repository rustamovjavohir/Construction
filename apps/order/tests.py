from django.conf import settings
from django.test import TestCase
from telegram import Bot


# Create your tests here.
class CustomBot:
    def __init__(self):
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        self.chat_id = settings.TELEGRAM_CHAT_ID

    def send_message(self, text):
        return self.bot.send_message(chat_id=self.chat_id, text=text)
