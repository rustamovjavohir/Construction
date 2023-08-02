from django.core.management import BaseCommand
from telegram import Bot
from django.conf import settings

bot = Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)


class Command(BaseCommand):
    help = 'Delete webhook bot'

    def handle(self, *args, **kwargs):
        self.ready()

    def ready(self):
        hostname = f'{settings.HOST}/bot/'
        print(f'deleted MASTER webhook at {hostname}')
        bot.delete_webhook()
