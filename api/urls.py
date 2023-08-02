from django.urls import path, include

urlpatterns = [
    path('advertsing/', include('api.advertising.urls')),
    path('apartment/', include('api.apartment.urls')),
    path('email/', include('api.sendEmail.urls')),
    path('selenium/', include('api.selenium.urls')),
    path('beautiful/', include('api.beautifulSoap.urls')),
    path('users/', include('api.user.urls')),
    path('auth/', include('api.auth_user.urls')),
    path('orders/', include('api.order.urls')),
    path('face_recognition/', include('api.face_recognition.urls')),
    path('bot/', include('api.bot.urls')),
    path('oauth2/', include('api.oauth2.urls'))
]

# go
