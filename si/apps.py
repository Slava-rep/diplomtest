# from django.apps import AppConfig


# class SiConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'si'
# diplomtest/si/apps.py
from django.apps import AppConfig

class SiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'si'
    verbose_name = 'Средства измерений'