from django.urls import path

from api.user.routers.routers import urlpatterns as r_urls
from api.user.views.views import LoginView, GetRefreshTokenView, LogoutView, CustomUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', GetRefreshTokenView.as_view(), name='refresh_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', CustomUserView.as_view(), name='profile'),
]

urlpatterns += r_urls
