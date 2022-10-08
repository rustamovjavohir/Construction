from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import *
from .routers import urlpatterns as r_urls

urlpatterns = [
    path("apartmentList/", ApartmentListView.as_view(), name='apartment-list'),
    path("floorList/", FloorListView.as_view(), name='floor-list')
]

urlpatterns += r_urls

