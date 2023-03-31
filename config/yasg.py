import rest_framework
import rest_framework_simplejwt
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Apartment",
        default_version='v1',
        description="Test Api",
        license=openapi.License(name="BSD License"),
        contact=openapi.Contact(email='rustamovj366@gmail.com')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(
        rest_framework_simplejwt.authentication.JWTAuthentication,
    ),
)
urlpatterns = [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
