from rest_framework.routers import DefaultRouter

from apps.advertising.views import AdvertisingViewset

routers = DefaultRouter()

routers.register(f'advertising', AdvertisingViewset, basename='advertising')

urlpatterns = routers.urls
