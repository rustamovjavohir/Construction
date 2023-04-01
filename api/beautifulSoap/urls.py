from django.urls import path
from api.beautifulSoap.views.views import *

urlpatterns = [
    path("", beautifulSoap, name='beautiful'),
    path('katm/', katm, name='katm')
]
