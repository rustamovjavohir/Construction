from django.urls import path
from apps.seleniumApp.views import *

urlpatterns = [
    path("", scrape_info, name='scrape_info')
]
