from rest_framework.routers import DefaultRouter

from api.apartment.views.views import ApartmentViewset

routers = DefaultRouter()

routers.register(f'apartment', ApartmentViewset, basename='apartment')

urlpatterns = routers.urls
