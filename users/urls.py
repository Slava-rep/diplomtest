from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Пример:
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

