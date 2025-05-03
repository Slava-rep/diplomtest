#si/urls.py
from django.urls import path
from . import views
# from .views import SIListView, si_autocomplete
# from .views import CertificateListView
from certificates.views import CertificateListView

# urlpatterns = [
#     # Пример:
#     # path('', views.SIListView.as_view(), name='si_list'),
#     # path('', SIListView.as_view(), name='si-list'),
#     # path('', CertificateListView.as_view(), name='home'),  # Главная страница для /si/
#     path('', SIListView.as_view(), name='home'),  # Отображение списка СИ (если нужно)
#     path('autocomplete/', si_autocomplete, name='si-autocomplete'),
#     path('certificates/', CertificateListView.as_view(), name='certificate_list'),
# ]

# diplomtest/si/urls.py
from django.urls import path
from . import views

app_name = 'si'

urlpatterns = [
    # Home page
    path('', views.SiHomeView.as_view(), name='home'),
    
    # Verification Types
    path('verification-types/', views.SiVerificationtypeListView.as_view(), name='verificationtype_list'),
    path('verification-types/add/', views.SiVerificationtypeCreateView.as_view(), name='verificationtype_create'),
    path('verification-types/delete/<int:pk>/', views.SiVerificationtypeDeleteView.as_view(), name='verificationtype_delete'),
    path('verification-types/<int:pk>/update/', views.SiVerificationtypeUpdateView.as_view(), name='verificationtype_update'),
    
    # Verification Methods
    path('verification-methods/', views.SiVerificationmethodListView.as_view(), name='verificationmethod_list'),
    path('verification-methods/create/', views.SiVerificationmethodCreateView.as_view(), name='verificationmethod_create'),
    path('verification-methods/<int:pk>/update/', views.SiVerificationmethodUpdateView.as_view(), name='verificationmethod_update'),
    path('verification-methods/<int:pk>/delete/', views.SiVerificationmethodDeleteView.as_view(), name='verificationmethod_delete'),
    path('api/verification-methods/', views.get_verification_methods, name='get_verification_methods'),
    
    # Affecting Factors
    path('affecting-factors/', views.SiAffectingfactorsListView.as_view(), name='affectingfactors_list'),
    path('affecting-factors/create/', views.SiAffectingfactorsCreateView.as_view(), name='affectingfactors_create'),
    path('affecting-factors/<int:pk>/update/', views.SiAffectingfactorsUpdateView.as_view(), name='affectingfactors_update'),
    path('affecting-factors/<int:pk>/delete/', views.SiAffectingfactorsDeleteView.as_view(), name='affectingfactors_delete'),
    
    # References
    path('references/', views.SiReferenceListView.as_view(), name='reference_list'),
    path('references/create/', views.SiReferenceCreateView.as_view(), name='reference_create'),
    path('references/<int:pk>/update/', views.SiReferenceUpdateView.as_view(), name='reference_update'),
    path('references/<int:pk>/delete/', views.SiReferenceDeleteView.as_view(), name='reference_delete'),
]