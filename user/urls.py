from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from user.routers import urlpatterns as r_urls

urlpatterns = [
]

urlpatterns += r_urls

