from django.urls import path
from apps.beautifulSoap.views import *

urlpatterns = [
    path("", beautifulSoap, name='beautiful'),
    path('katm/', katm, name='katm')
]
