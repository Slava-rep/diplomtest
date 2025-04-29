# diplomtest/users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from employees.models import EmployeesEmployee

@receiver(post_save, sender=CustomUser)
def create_employee(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'employee_profile'):
        EmployeesEmployee.objects.create(user=instance)