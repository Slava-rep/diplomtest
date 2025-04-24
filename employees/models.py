from urllib import request
from django.db import models
from django.conf import settings
# employees/models.py

# В любом месте кода
# user = request.user
# employee = user.employee  # Получаем связанного сотрудника

from django.conf import settings

class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_profile'         #        related_name='employee_profile'
    )
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    birth_place = models.CharField("Место рождения", max_length=255, blank=True)
    snils = models.CharField("СНИЛС", max_length=14, unique=True)
    email = models.EmailField("Email", blank=True)
    specialization = models.CharField("Специализация", max_length=100, blank=True)
    qualification = models.CharField("Квалификация", max_length=100, blank=True)
    note = models.TextField("Примечание", blank=True)
    
    # Связь с видами измерений через таблицу employee_measurement_type
    measurement_types = models.ManyToManyField(
        'si.MeasurementType',  # Предполагая, что модель MeasurementType в приложении si
        through='EmployeeMeasurementType',
        related_name='employees',               #employee_measurements
        verbose_name="Виды измерений"
    )
    def __str__(self):
        return f"{self.user.username} (Employee)"
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

# class EmployeeMeasurementType(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     measurement_type = models.ForeignKey('measurements.MeasurementType', on_delete=models.CASCADE)

class EmployeeMeasurementType(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_measurement_types' )
    measurement_type = models.ForeignKey('si.MeasurementType', on_delete=models.CASCADE, related_name='employee_measurement_types')
    
    class Meta:
        verbose_name = "Вид измерений сотрудника"
        verbose_name_plural = "Виды измерений сотрудников"
        unique_together = ['employee', 'measurement_type']

    def __str__(self):
        return f"{self.employee} - {self.measurement_type}"

# class Employee(models.Model):
#     user = models.OneToOneField(
#         'users.CustomUser', 
#         on_delete=models.CASCADE,
#         related_name='employee_profile'
#     )

    

