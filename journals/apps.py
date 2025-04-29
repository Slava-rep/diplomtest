# from django.apps import AppConfig


# class JournalsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'journals'

#     def ready(self):
#         import journals.signals



# diplomtest/journals/apps.py
from django.apps import AppConfig

class JournalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journals'
    verbose_name = 'Журналы'