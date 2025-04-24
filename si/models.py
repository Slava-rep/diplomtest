#si/models.py
# Create your models here.
from django.db import models
from django.utils.text import slugify
class SIType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    reg_number = models.CharField(max_length=50, verbose_name="Рег. номер")
    #slug = models.SlugField("Slug", max_length=255, unique=True)                                       # Добавляем поле      
    description = models.TextField("Описание", blank=True)                                             # Добавляем поле
    slug = models.SlugField(blank=True)  # Временно убрали unique=True
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            counter = 1
            while SIType.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

# class SI(models.Model):
#     type = models.ForeignKey(SIType, on_delete=models.PROTECT, verbose_name="Тип СИ")
#     serial = models.CharField(max_length=100, verbose_name="Серийный номер")
#     manufacture_year = models.PositiveIntegerField(verbose_name="Год выпуска")

#     def __str__(self):
#         return f"{self.type} - {self.serial}"
class SI(models.Model):
    type = models.ForeignKey(
        SIType, 
        on_delete=models.PROTECT, 
        verbose_name="Тип СИ"
    )
    serial = models.CharField(
        max_length=100, 
        verbose_name="Серийный номер"
    )
    manufacture_year = models.PositiveIntegerField(
        verbose_name="Год выпуска"
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name='Активно'
    )
    registration_number = models.CharField(
    max_length=50, 
    unique=True, 
    verbose_name="Регистрационный номер"
    )

    def __str__(self):
        return f"{self.type} - {self.serial} ({self.manufacture_year})"
        
    


class VerificationType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип поверки")

    def __str__(self):
        return self.name

class VerificationMethod(models.Model):
    name = models.CharField(max_length=200, verbose_name="Методика")
    doc_number = models.CharField(max_length=50, verbose_name="Номер документа")

    def __str__(self):
        return f"{self.name} ({self.doc_number})"

class AffectingFactors(models.Model):
    temperature = models.FloatField(
        verbose_name="Температура воздуха (°C)", 
        default=20.0  # Значение по умолчанию
    )
    humidity = models.FloatField(
        verbose_name="Относительная влажность (%)", 
        default=50.0  # Значение по умолчанию
    )
    pressure = models.FloatField(
        verbose_name="Атмосферное давление (мм рт. ст.)", 
        default=760.0  # Значение по умолчанию
    )
    voltage = models.FloatField(
        verbose_name="Напряжение сети (В)", 
        blank=True, 
        null=True
    )
    frequency = models.FloatField(
        verbose_name="Частота сети (Гц)", 
        blank=True, 
        null=True
    )
    harmonic_coefficient = models.FloatField(
        verbose_name="Коэффициент гармоник (%)", 
        blank=True, 
        null=True
    )
    liquid_temperature = models.FloatField(
        verbose_name="Температура жидкости (°C)", 
        blank=True, 
        null=True
    )
    temperature_change = models.FloatField(
        verbose_name="Изменение температуры (°C)", 
        blank=True, 
        null=True
    )
    pressure_change_rate = models.FloatField(
        verbose_name="Скорость изменения давления (гПа/мин)", 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"Влияющие факторы от {self.created_at.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = "Влияющие факторы"
        verbose_name_plural = "Влияющие факторы"

# si/models.py
class Reference(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название эталона")
    registration_number = models.CharField(max_length=50, verbose_name="Рег. номер")
    
    def __str__(self):
        return f"{self.name} ({self.registration_number})"

class MeasurementType(models.Model):
    id_measurement_type = models.AutoField(primary_key=True)
    # id_measurement_type = models.CharField(max_length=20, unique=True, verbose_name="Код типа измерений")
    name = models.CharField(max_length=100, verbose_name='Наименование')
    measurement_range = models.CharField(max_length=100, verbose_name='Диапазон измерений')
    error_uncertainty = models.CharField(null=True, max_length=100, verbose_name='Погрешность/неопределенность')
    code = models.CharField(max_length=20, unique=True, verbose_name='Код')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = "Вид измерений"
        verbose_name_plural = "Виды измерений"
        
    def __str__(self):
        return self.name