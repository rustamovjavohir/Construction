from telegram import ReplyMarkup, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, \
    WebAppInfo


def main_button():
    button = [
        [KeyboardButton('📝Открытый сайт', web_app=WebAppInfo('https://radius.uz/'))],
    ]

    return ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)


def start_inline_button():
    button = [
        [InlineKeyboardButton('📝Открытый сайт', web_app=WebAppInfo('https://rustamovjavohir.jprq.live/bot/web/'))],
    ]

    return InlineKeyboardMarkup(button)
