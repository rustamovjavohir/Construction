from django.urls import path, include


urlpatterns = [
    path('advertsing/', include('apps.advertising.urls')),
    path('apartment/', include('apps.apartment')),
    path('send-email/', include('apps.sendEmail')),
]