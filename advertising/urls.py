from django.urls import path
from advertising.views import *
from advertising.routers import urlpatterns as router_urls

urlpatterns = [
    path('', AdvertisingListView.as_view(), name='advertising')
]

urlpatterns += router_urls
