from django.conf import settings
from telegram import Bot


class TelegramErrorMiddleware:
    def __init__(self, get_response: callable):
        self.get_response = get_response
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        self.chat_id = settings.TELEGRAM_CHAT_ID

    def __call__(self, request, *args, **kwargs):
        # do something before the view is called
        print('before view')
        response = self.get_response(request, *args, **kwargs)
        print('after view')
        return response

    def process_exception(self, request, exception):
        print('exception')
        message = f"{request.path}: {str(exception)}"
        self.bot.send_message(chat_id=self.chat_id, text=message)
        return None
