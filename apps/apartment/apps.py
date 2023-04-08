from django.apps import AppConfig


class ApartmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.apartment'


# class CustomAdminConfig(AdminConfig):  # 1.
#     default_site = 'myproject.admin.CustomAdminSite'  # 2.
#     name = 'Salom'
#     label = 'salom'
