# #sertificates/models.py
# from django.db import models
# # Create your models here.
# from django.utils import timezone
# from django.contrib.auth import get_user_model
# import datetime


# from si.models import SI, VerificationType, VerificationMethod, AffectingFactors, Reference

# User = get_user_model()

# def generate_cert_number():
#     # Генерация номера типа ВНИКТИ/дата/000000001
#     today = timezone.now().strftime('%d-%m-%Y')
#     last_cert = Certificate.objects.order_by('-id').first()
#     sequence = last_cert.id + 1 if last_cert else 1
#     return f"ВНИКТИ/{today}/{sequence:09d}"

# # class VerificationMethod(models.Model):
# #     name = models.CharField("Название методики", max_length=200)
# #     verification_type = models.ForeignKey(
# #         VerificationType,
# #         on_delete=models.CASCADE,
# #         verbose_name="Тип поверки"
# #     )
# class VerificationMethod(models.Model):
#     doc_number = models.CharField("Номер методики", max_length=50, default="МП 000-000-0000")  # Добавляем поле для номера методики
#     name = models.CharField("Название методики", max_length=200)  # Поле для названия методики
#     si = models.ForeignKey(
#         'si.SI',  # Укажите правильную модель, если связь должна быть
#         on_delete=models.CASCADE,
#         verbose_name="Средство измерений",
#         null=True,  # Если поле необязательно
#         blank=True
#     )
#     def __str__(self):
#         return f"{self.doc_number} - {self.name}"  # Удобное отображение в админке    

# class SIVerification(models.Model):
#     certificate = models.ForeignKey(
#         'Certificate', 
#         on_delete=models.CASCADE,
#         verbose_name="Свидетельство"
#     )
#     reference = models.ForeignKey(
#         'si.Reference', 
#         on_delete=models.CASCADE,
#         verbose_name="Эталон"
#     )
#     applied_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Дата применения"
#     )

#     class Meta:
#         verbose_name = "Применение эталона"
#         verbose_name_plural = "Применения эталонов"

# class Certificate(models.Model):
#         # Добавляем обязательные поля
    
#     VERIFICATION_TYPE_CHOICES = [
#         ('primary', 'Первичная'),
#         ('periodic', 'Периодическая'),
#         ('unscheduled', 'Внеплановая'),
#     ]
    
#     STATUS_CHOICES = [
#         ('draft', 'Черновик'),
#         ('published', 'Опубликовано'),
#     ]
    
#     protocol = models.FileField(
#         upload_to='protocols/',
#         blank=True,
#         null=True,
#         verbose_name="Протокол"
#     )
#     gov_reg_number = models.CharField("Гос. реестр", max_length=20, default='GOS-0000')
#     inventory_number = models.CharField("Инв. номер", max_length=50, default='INV-0000')
#     modification = models.CharField("Модификация", max_length=100, blank=True)

#     status = models.CharField(
#         "Статус", 
#         max_length=10, 
#         choices=STATUS_CHOICES, 
#         default='draft'
#     )
#     created_at = models.DateTimeField(
#         "Дата создания", 
#         auto_now_add=True
#     )
    
#     VERIFICATION_RESULT_CHOICES = [
#         ('full', 'В полном объеме'),
#         ('partial', 'В неполном объеме'),
#     ]

#     # Основная информация
#     number = models.CharField(
#         max_length=50, 
#         unique=True, 
#         default=generate_cert_number,
#         verbose_name="Номер свидетельства"
#     )
#     verification_date = models.DateField(
#         default=timezone.now,
#         verbose_name="Дата проведения поверки"
#     )
#     interval = models.PositiveIntegerField(
#         default=1,
#         verbose_name="Интервал поверки (лет)"
#     )
#     next_verification_date = models.DateField(
#         verbose_name="Срок действия поверки"
#     )
    
#     # Связь с СИ
#     si = models.ForeignKey(
#         'si.SI',
#         on_delete=models.PROTECT,
#         related_name='certificates',
#         verbose_name="Средство измерений"
#     )
    
#     # Информация о поверке
#     verification_type = models.ForeignKey(
#         'si.VerificationType',
#         on_delete=models.PROTECT,
#         verbose_name="Вид поверки"
#     )
#     verification_method = models.ForeignKey(
#         'si.VerificationMethod',
#         on_delete=models.PROTECT,
#         verbose_name="Методика поверки"
#     )
#     verification_result = models.CharField(
#         max_length=7,
#         choices=VERIFICATION_RESULT_CHOICES,
#         default='full',
#         verbose_name="Результат поверки"
#     )
#     affecting_factors = models.ForeignKey(
#         'si.AffectingFactors',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         verbose_name="Влияющие факторы",
#         related_name="certificates_affecting"  # Добавьте это
#     )
#     # Маркировка и идентификация
#     previous_verification_mark = models.CharField(
#         max_length=100,
#         blank=True,
#         verbose_name="Клеймо предыдущей поверки"
#     )
#     is_vn = models.BooleanField(
#         default=False,
#         verbose_name="СИ ВН"
#     )
#     mark_in_passport = models.BooleanField(
#         default=False,
#         verbose_name="Знак в паспорте"
#     )
#     mark_on_si = models.BooleanField(
#         default=False,
#         verbose_name="Знак на СИ"
#     )
    
#     # Организация и ответственные
#     organization_name = models.CharField(
#         max_length=100,
#         default="ВНИКТИ",
#         verbose_name="Организация"
#     )
#     inn = models.CharField(
#         max_length=12,
#         default="5022067103",
#         verbose_name="ИНН"
#     )
#     department_head = models.CharField(
#         max_length=100,
#         default="Крюков Сергей Александрович",
#         verbose_name="Начальник отдела"
#     )
#     verifier = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name='certificates',
#         verbose_name="Поверитель"
#     )
    
#     # Дополнительная информация
#     composition = models.TextField(
#         blank=True,
#         verbose_name="В составе"
#     )
#     comment = models.TextField(
#         blank=True,
#         verbose_name="Комментарий"
#     )
    
#     # Связи
#     applied_standards = models.ManyToManyField(
#         'si.Reference',
#         through='SIVerification',
#         verbose_name="Примененные эталоны"
#     )
#     # factors = models.OneToOneField(
#     #     'si.AffectingFactors',
#     #     on_delete=models.SET_NULL,
#     #     null=True,
#     #     blank=True,
#     #     verbose_name="Основные факторы",
#     #     related_name="certificates_factors"  # Добавьте это
#     # )




    
#     # Методы
#     # def save(self, *args, **kwargs):
#     #     # Автоматический расчет даты следующей поверки
#     #     if not self.next_verification_date:
#     #         next_date = self.verification_date + datetime.timedelta(days=self.interval*365-1)
#     #         self.next_verification_date = next_date
#     #     super().save(*args, **kwargs)
#     def save(self, *args, **kwargs):
#         if not self.number:
#             today = timezone.now().strftime('%d-%m-%Y')
#             last_cert = Certificate.objects.order_by('-id').first()
#             sequence = last_cert.id + 1 if last_cert else 1
#             self.number = f"ВНИКТИ/{today}/{sequence:09d}"
            
#         if not self.next_verification_date:
#             next_date = self.verification_date + datetime.timedelta(days=self.interval*365-1)
#             self.next_verification_date = next_date
            
#         super().save(*args, **kwargs)    
#     # Метаданные
#     class Meta:
#         verbose_name = "Свидетельство о поверке"
#         verbose_name_plural = "Свидетельства о поверке"
#         ordering = ['-verification_date']
    
#     def __str__(self):
#         return f"Свидетельство {self.number} ({self.si})"
    

# diplomtest/certificates/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

def generate_cert_number():
    # Генерация номера типа ВНИКТИ/дата/000000001
    today = timezone.now().strftime('%d-%m-%Y')
    last_cert = CertificatesCertificate.objects.order_by('-id').first()
    sequence = last_cert.id + 1 if last_cert else 1
    return f"ВНИКТИ/{today}/{sequence:09d}"

class CertificatesCertificate(models.Model):
    id = models.BigAutoField(primary_key=True)
    gov_reg_number = models.CharField(max_length=20)
    inventory_number = models.CharField(max_length=50)
    modification = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    number = models.CharField(unique=True, max_length=50)
    verification_date = models.DateField()
    interval = models.IntegerField()
    next_verification_date = models.DateField()
    verification_result = models.CharField(max_length=7)
    previous_verification_mark = models.CharField(max_length=100)
    is_vn = models.BooleanField()
    mark_in_passport = models.BooleanField()
    mark_on_si = models.BooleanField()
    organization_name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    department_head = models.CharField(max_length=100)
    composition = models.TextField()
    comment = models.TextField()
    affecting_factors = models.ForeignKey('si.SiAffectingfactors', models.DO_NOTHING, blank=True, null=True)
    si = models.ForeignKey('si.SiSi', models.DO_NOTHING)
    verification_method = models.ForeignKey('si.SiVerificationmethod', models.DO_NOTHING)
    verification_type = models.ForeignKey('si.SiVerificationtype', models.DO_NOTHING)
    verifier = models.ForeignKey(User, models.DO_NOTHING)
    protocol = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'certificates_certificate'
        verbose_name = "Свидетельство о поверке"
        verbose_name_plural = "Свидетельства о поверке"
        ordering = ['-verification_date']
    
    def save(self, *args, **kwargs):
        if not self.number:
            today = timezone.now().strftime('%d-%m-%Y')
            last_cert = CertificatesCertificate.objects.order_by('-id').first()
            sequence = last_cert.id + 1 if last_cert else 1
            self.number = f"ВНИКТИ/{today}/{sequence:09d}"
            
        if not self.next_verification_date:
            next_date = self.verification_date + datetime.timedelta(days=self.interval*365-1)
            self.next_verification_date = next_date
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Свидетельство {self.number} ({self.si})"

class CertificatesSiverification(models.Model):
    id = models.BigAutoField(primary_key=True)
    applied_at = models.DateTimeField()
    certificate = models.ForeignKey(CertificatesCertificate, models.DO_NOTHING)
    reference = models.ForeignKey('si.SiReference', models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'certificates_siverification'
        verbose_name = "Применение эталона"
        verbose_name_plural = "Применения эталонов"
    
    def __str__(self):
        return f"{self.certificate} - {self.reference}"

class CertificatesVerificationmethod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    doc_number = models.CharField(max_length=50)
    si = models.ForeignKey('si.SiSi', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'certificates_verificationmethod'
        verbose_name = "Методика поверки"
        verbose_name_plural = "Методики поверки"
    
    def __str__(self):
        return f"{self.doc_number} - {self.name}"





