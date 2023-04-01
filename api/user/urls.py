from django.urls import path

from api.user.routers.routers import urlpatterns as r_urls
from api.user.views.views import LoginView, GetRefreshTokenView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', GetRefreshTokenView.as_view(), name='refresh-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += r_urls
