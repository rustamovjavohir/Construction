from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Dispatcher, CallbackContext, CommandHandler, MessageHandler, Filters
from apps.bot.handlers import start_handler, main_handler

bot = Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dispatcher: Dispatcher = Dispatcher(bot, update_queue=None)

dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=main_handler))
