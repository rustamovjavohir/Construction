from django.apps import apps

app_configs = apps.get_app_configs()

for app_config in app_configs:
    print(app_config.name)
