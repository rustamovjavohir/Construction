from telegram import Update
from telegram.ext import CallbackContext


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!')


def main_handler(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(msg)
