from django.urls import path
from api.apartment.views.views import *
from api.apartment.routers.routers import urlpatterns as r_urls

urlpatterns = [
    path("", ApartmentListView.as_view(), name='apartment-list'),
    path("floorList/", FloorListView.as_view(), name='floor-list'),
    path("detail/<int:pk>/", CustomAdminView.as_view(), name='detail'),
    path("meta/", get_meta, name='get_meta'),
]

urlpatterns += r_urls

