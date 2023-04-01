from django.urls import path
from api.selenium.views.views import *

urlpatterns = [
    path("", scrape_info, name='scrape_info')
]
