from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import CertificateCreateFromExampleView
from .views import CertificateListView
from django.urls import path, include

app_name = 'certificates'

urlpatterns = [
    path('', CertificateListView.as_view(), name='list'),  # Список свидетельств
    path('new/', views.CertificateCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CertificateDetailView.as_view(), name='detail'),
    path('<int:pk>/create_from_example/', CertificateCreateFromExampleView.as_view(), name='create_from_example'),
    path('<int:pk>/print/', views.CertificatePrintView.as_view(), name='print'),
    path('admin/', admin.site.urls),
    # path('certificates/', include('certificates.urls')),  # Маршруты для certificates
    path('si/', include('si.urls')),  # Маршруты для si

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


