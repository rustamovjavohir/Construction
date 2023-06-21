from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Dispatcher, CallbackContext, CommandHandler, MessageHandler, Filters, filters
from apps.bot.handlers import start_handler, main_handler, wep_app_handler
bot = Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dispatcher: Dispatcher = Dispatcher(bot, update_queue=None)

# web_app_data_filter = Filters.web_app_data(key='identifier')
# web_app_data_handler = MessageHandler(web_app_data_filter, wep_app_handler)

dispatcher.add_handler(CommandHandler('start', start_handler))
# dispatcher.add_handler(MessageHandler(web_app_data_filter, wep_app_handler))
dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=main_handler))
