from django.urls import path, include

urlpatterns = [
    path('advertsing/', include('apps.advertising.urls')),
    path('apartment/', include('apps.apartment.urls')),
    path('send-email/', include('apps.sendEmail.urls')),
    path('selenium/', include('apps.seleniumApp.urls')),
    path('beautiful/', include('apps.beautifulSoap.urls')),
]
