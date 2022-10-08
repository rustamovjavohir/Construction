from rest_framework.routers import DefaultRouter

from advertising.views import AdvertisingViewset

routers = DefaultRouter()

routers.register(f'advertising', AdvertisingViewset, basename='advertising')

urlpatterns = routers.urls
