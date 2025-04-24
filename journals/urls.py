from django.urls import include, path
from .views import (
    JournalRegistrationListView,
    JournalVerificationListView,
    JournalEnvironmentListView,
    JournalHubView
)
from .views import registration_pdf_view
from .views import verification_pdf_view, environment_pdf_view

app_name = 'journals'
# urlpatterns = [
#     path('registration/', JournalRegistrationListView.as_view(), name='journal-registration'),
#     path('verification/', JournalVerificationListView.as_view(), name='journal-verification'),
#     path('environment/', JournalEnvironmentListView.as_view(), name='journal-environment'),
# ]

# urlpatterns = [
#     path('registration/', JournalRegistrationListView.as_view(), name='registration'),
#     path('verification/', JournalVerificationListView.as_view(), name='verification'),
#     path('environment/', JournalEnvironmentListView.as_view(), name='environment'),
# ]

# urlpatterns = [
#     path('registration/', JournalRegistrationListView.as_view(), name='registration'),
#     path('verification/', JournalVerificationListView.as_view(), name='verification'),
#     path('environment/', JournalEnvironmentListView.as_view(), name='environment'),
#     path('journals/', JournalHubView.as_view(), name='journals'),
#     path('journals/', include('journals.urls')),
# ]

urlpatterns = [
    path('', JournalHubView.as_view(), name='hub'),
    path('registration/', JournalRegistrationListView.as_view(), name='registration'),
    path('registration/pdf/', registration_pdf_view, name='registration_pdf'),
    path('verification/', JournalVerificationListView.as_view(), name='verification'),
    path('verification/pdf/', verification_pdf_view, name='verification_pdf'),
    path('environment/', JournalEnvironmentListView.as_view(), name='environment'),
    path('environment/pdf/', environment_pdf_view, name='environment_pdf'),
]