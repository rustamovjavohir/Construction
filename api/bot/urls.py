from django.urls import path

from api.bot.views.views import BotView, HelloView

urlpatterns = [
    path("", BotView.as_view(), name="bot"),
    path("hello/", HelloView.as_view(), name="hello"),
]
