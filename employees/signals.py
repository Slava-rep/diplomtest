# diplomtest/employees/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import EmployeesEmployee

User = get_user_model()

@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'employee_profile'):
        EmployeesEmployee.objects.create(user=instance)