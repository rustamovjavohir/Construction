from rest_framework.routers import DefaultRouter

from api.user.views.views import UserViewSet

routers = DefaultRouter()

routers.register(f'user', UserViewSet, basename='user')

urlpatterns = routers.urls
