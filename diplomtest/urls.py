"""
URL configuration for diplomtest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Добавьте этот импорт
# from journals.views import JournalHubView  # Добавьте этот импорт
from django.contrib.auth import views as auth_views

# diplomtest/diplomtest/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('si.urls')),
    path('certificates/', include('certificates.urls')),
    path('journals/', include('journals.urls')),
    path('employees/', include('employees.urls')),
    path('users/', include('users.urls')),
    
    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    
    # Редирект с корневого URL
    path('', RedirectView.as_view(url='/si/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Аутентификация
#     path('login/', auth_views.LoginView.as_view(
#             template_name='user/login.html'
#         ),
#         name='login'
#     ),
#     path('logout/', auth_views.LogoutView.as_view(
#             next_page='login'
#         ),
#         name='logout'
#     ),
#     # path('password_change/', auth_views.PasswordChangeView.as_view(               потом потом идеи
#     #         template_name='users/password_change.html',
#     #         success_url='/'
#     #     ),
#     #     name='password_change'
#     # ),
#     # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
#     #         template_name='users/password_change_done.html'
#     #     ),
#     #     name='password_change_done'
#     # ),
#     path('si/', include('si.urls')),
#     path('certificates/', include('certificates.urls')),
#     path('users/', include('users.urls')),
#     path('journals/', include('journals.urls')),
#     # Добавьте один из вариантов ниже:
#     #path('journals/', JournalHubView.as_view(), name='journals'),
#     # Вариант 1: Редирект на существующий URL (например, на список СИ)
#     path('', RedirectView.as_view(url='/si/')),
    
    
#     # ИЛИ 
    
#     # Вариант 2: Собственное представление для главной страницы
#     # path('', include('certificates.urls')),  # Если есть главная страница в certificates
# ]