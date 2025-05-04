from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import CertificateCreateFromExampleView
from .views import CertificateListView
from django.urls import path, include

# app_name = 'certificates'

# urlpatterns = [
#     path('', CertificateListView.as_view(), name='list'),  # Список свидетельств
#     path('new/', views.CertificateCreateView.as_view(), name='create'),
#     path('<int:pk>/', views.CertificateDetailView.as_view(), name='detail'),
#     path('<int:pk>/create_from_example/', CertificateCreateFromExampleView.as_view(), name='create_from_example'),
#     path('<int:pk>/print/', views.CertificatePrintView.as_view(), name='print'),
#     path('admin/', admin.site.urls),
#     # path('certificates/', include('certificates.urls')),  # Маршруты для certificates
#     path('si/', include('si.urls')),  # Маршруты для si

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# diplomtest/certificates/urls.py
from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.CertificateListView.as_view(), name='list'),
    path('create/', views.CertificateCreateView.as_view(), name='create'),
    path('print/<int:pk>/', views.print_certificate, name='print'),
    path('print/', views.print_certificate, name='print_empty'),
    path('create-from-example/<int:pk>/', views.CertificateCreateFromExampleView.as_view(), name='create_from_example'),
    path('detail/<int:pk>/', views.CertificateDetailView.as_view(), name='detail'),
    path('temperature/create/', views.TemperatureCertificateCreateView.as_view(), name='temperature_create'),
    path('delete/<int:pk>/', views.CertificateDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

