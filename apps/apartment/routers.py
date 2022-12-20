from rest_framework.routers import DefaultRouter

from .views import ApartmentViewset

routers = DefaultRouter()

routers.register(f'apartment', ApartmentViewset, basename='apartment')

urlpatterns = routers.urls
