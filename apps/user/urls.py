from django.urls import path

from apps.user.routers import urlpatterns as r_urls
from apps.user.views import LoginView, GetRefreshTokenView, LogoutView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView, TokenBlacklistView)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', GetRefreshTokenView.as_view(), name='refresh-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += r_urls
