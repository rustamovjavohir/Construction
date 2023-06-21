from telegram import Update
from telegram.ext import CallbackContext

from apps.bot.buttons import main_button, start_inline_button


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!', reply_markup=start_inline_button())


def main_handler(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(msg, reply_markup=main_button())


def wep_app_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!', reply_markup=start_inline_button())
