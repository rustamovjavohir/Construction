from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.utils import IntegrityError
from telegram import Bot, Update
from telegram.error import InvalidToken
from telegram.ext import Dispatcher, CallbackContext, CommandHandler


class CustomBot:

    def __init__(self, token):
        self.token = token

    def get_bot(self):
        bot = Bot(token=self.token)
        return bot

    def get_dispatcher(self):
        dispatcher = Dispatcher(self.get_bot(), None, workers=0)
        return dispatcher

