#si/urls.py
from django.urls import path
from . import views
from .views import SIListView, si_autocomplete
# from .views import CertificateListView
from certificates.views import CertificateListView
app_name = 'si'

urlpatterns = [
    # Пример:
    # path('', views.SIListView.as_view(), name='si_list'),
    # path('', SIListView.as_view(), name='si-list'),
    # path('', CertificateListView.as_view(), name='home'),  # Главная страница для /si/
    path('', SIListView.as_view(), name='home'),  # Отображение списка СИ (если нужно)
    path('autocomplete/', si_autocomplete, name='si-autocomplete'),
    path('certificates/', CertificateListView.as_view(), name='certificate_list'),
]