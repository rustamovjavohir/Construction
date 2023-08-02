from config import settings
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot

bot = Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)


class Command(BaseCommand):
    help = 'Run webhook bot'

    def handle(self, *args, **kwargs):
        self.ready()

    def ready(self):
        hostname = f'{settings.HOST}/api/bot/'
        print(f'setting MASTER webhook at {hostname}')
        bot.set_webhook(hostname)
