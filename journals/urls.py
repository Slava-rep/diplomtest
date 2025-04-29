from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'journals'

urlpatterns = [
    path('', login_required(views.hub), name='hub'),
    path('verification/', login_required(views.JournalVerificationListView.as_view()), name='verification'),
    path('registration/', login_required(views.JournalRegistrationListView.as_view()), name='registration'),
    path('environment/', login_required(views.JournalEnvironmentListView.as_view()), name='environment'),
    
    # PDF экспорт
    path('verification/pdf/', login_required(views.verification_pdf_view), name='verification_pdf'),
    path('registration/pdf/', login_required(views.registration_pdf_view), name='registration_pdf'),
    path('environment/pdf/', login_required(views.environment_pdf_view), name='environment_pdf'),
]