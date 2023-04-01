from rest_framework.routers import DefaultRouter

from api.advertising.views.views import AdvertisingViewset

routers = DefaultRouter()

routers.register(f'advertising', AdvertisingViewset, basename='advertising')

urlpatterns = routers.urls
