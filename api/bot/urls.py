from django.urls import path

from api.bot.views.views import BotView, HelloView, WebView

urlpatterns = [
    path("", BotView.as_view(), name="bot"),
    path("hello/", HelloView.as_view(), name="hello"),
    path("web/", WebView.as_view(), name="web"),
]
