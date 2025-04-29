from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeDetailView,
    EmployeeMeasurementUpdateView
)

# app_name = 'employees'

# urlpatterns = [
#     path('', EmployeeListView.as_view(), name='list'),
#     path('create/', EmployeeCreateView.as_view(), name='create'),
#     path('<int:pk>/', EmployeeDetailView.as_view(), name='detail'),
#     path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='update'),
#     path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='delete'),
#     path('measurement/<int:pk>/update/', 
#          EmployeeMeasurementUpdateView.as_view(), 
#          name='measurement-update'),
# ]


# diplomtest/employees/urls.py
from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('measurement/<int:pk>/', views.EmployeeMeasurementUpdateView.as_view(), name='measurement_update'),
]