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

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

 

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('about', views.about),
#     path('contact', views.contact),
# ]

# urlpatterns = [
#     path('', views.index),
#     re_path(r'^about', views.about),        #регулярные выражения
#     re_path(r'^contact', views.contact),
# ]
# urlpatterns = [
#     re_path(r'^about/contact/', views.contact),   
#     re_path(r'^about', views.about),
#     path('', views.index),                #общие в конце
# ]

# urlpatterns = [
#     path('', views.index),
#     path("index", views.index),
#     path('about', views.about, kwargs={"name":"Tom", "age": 38}),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
#     path("user/<str:name>/<int:age>", views.user),
# ]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Добавьте этот импорт
from journals.views import JournalHubView  # Добавьте этот импорт
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Аутентификация
    path('login/', auth_views.LoginView.as_view(
            template_name='user/login.html'
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(
            next_page='login'
        ),
        name='logout'
    ),
    # path('password_change/', auth_views.PasswordChangeView.as_view(               потом потом идеи
    #         template_name='users/password_change.html',
    #         success_url='/'
    #     ),
    #     name='password_change'
    # ),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
    #         template_name='users/password_change_done.html'
    #     ),
    #     name='password_change_done'
    # ),
    path('si/', include('si.urls')),
    path('certificates/', include('certificates.urls')),
    path('users/', include('users.urls')),
    path('journals/', include('journals.urls')),
    # Добавьте один из вариантов ниже:
    #path('journals/', JournalHubView.as_view(), name='journals'),
    # Вариант 1: Редирект на существующий URL (например, на список СИ)
    path('', RedirectView.as_view(url='/si/')),
    
    
    # ИЛИ 
    
    # Вариант 2: Собственное представление для главной страницы
    # path('', include('certificates.urls')),  # Если есть главная страница в certificates
]