from rest_framework.routers import DefaultRouter

from .views import UserViewset

routers = DefaultRouter()

routers.register(f'user', UserViewset, basename='user')

urlpatterns = routers.urls
