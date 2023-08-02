from django.urls import path, include
from api.oauth2.views.views import IndexView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='oauth3-index'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
