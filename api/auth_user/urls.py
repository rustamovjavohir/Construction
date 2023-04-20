from django.urls import path

from api.auth_user.views.views import LoginView, GetRefreshTokenView, LogoutView, CustomUserView, CustomTemplateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', GetRefreshTokenView.as_view(), name='refresh_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', CustomUserView.as_view(), name='profile'),
    path('template/', CustomTemplateView.as_view(), name='template-view'),
]
