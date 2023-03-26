from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from apps.apartment.views import *
from apps.apartment.routers import urlpatterns as r_urls

urlpatterns = [
    path("", ApartmentListView.as_view(), name='apartment-list'),
    path("floorList/", FloorListView.as_view(), name='floor-list'),
    path("detail/<int:pk>/", CustomAdminView.as_view(), name='detail'),
]

urlpatterns += r_urls

