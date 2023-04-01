from django.urls import path
from api.advertising.views.views import *
from api.advertising.routers.routers import urlpatterns as router_urls

urlpatterns = [
    path('', AdvertisingListView.as_view(), name='advertising'),
    path('template/', TemplateView.as_view(), name='template')
]

urlpatterns += router_urls
