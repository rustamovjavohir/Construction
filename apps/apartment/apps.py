from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ApartmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.apartment'


class CustomAdminConfig(AdminConfig):  # 1.
    default_site = 'myproject.admin.CustomAdminSite'  # 2.
    name = 'Salom'
    label = 'salom'
