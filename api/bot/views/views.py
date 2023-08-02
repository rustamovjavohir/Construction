import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from apps.bot.views import bot, dispatcher


# Create your views here.

@method_decorator(csrf_exempt, 'dispatch')
class BotView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            body = request.body
            data = json.loads(body)
            update: Update = Update.de_json(data, bot)
            dispatcher.process_update(update)
            # print(data)
        except Exception as e:
            print('\n Exception:\n')
            print(e)

        return HttpResponse('ok', status=200)


class HelloView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world', status=200)


class WebView(View):
    def get(self, request, *args, **kwargs):
        print('WebView')
        # return render(request, 'web_telegram/simple.html')
        return render(request, 'web_telegram/index.html')

    def post(self, request, *args, **kwargs):
        print('WebView')
        # return render(request, 'web_telegram/simple.html')
        return render(request, 'web_telegram/index.html')
