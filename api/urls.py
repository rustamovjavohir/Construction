from django.urls import path, include

urlpatterns = [
    path('advertsing/', include('api.advertising.urls')),
    path('apartment/', include('api.apartment.urls')),
    path('email/', include('api.sendEmail.urls')),
    path('selenium/', include('api.selenium.urls')),
    path('beautiful/', include('api.beautifulSoap.urls')),
    path('users/', include('api.user.urls')),
]