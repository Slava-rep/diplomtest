# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     pass  # Добавьте кастомные поля при необходимости
#     employee = models.OneToOneField(
#         'employees.Employee', 
#         on_delete=models.SET_NULL, 
#         null=True,
#         related_name='user_profile',  # Added explicit related_name
#         verbose_name="Сотрудник",
#         blank=True  # Added to make field optional
#     )
class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя, расширяющая AbstractUser
    """
    # Дополнительные поля можно добавить здесь
    
    class Meta:
        app_label = 'users'
        db_table = 'users_customuser'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        swappable = 'AUTH_USER_MODEL'
    def __str__(self):
        return self.username
    def get_full_name(self):
        """
        Возвращает полное имя пользователя
        """
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username