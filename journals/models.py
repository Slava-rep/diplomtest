from django.db import models

from django.db import models
from si.models import SI, AffectingFactors
from certificates.models import Certificate

class JournalRegistration(models.Model):
    si = models.ForeignKey(
        SI,
        on_delete=models.PROTECT,
        verbose_name="Средство измерений"
    )
    receipt_date = models.DateField(
        verbose_name="Дата поступления"
    )
    receipt_signature = models.CharField(
        max_length=100,
        verbose_name="Подпись принявшего"
    )
    issue_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата выдачи"
    )
    issue_signature = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Подпись выдавшего"
    )

    class Meta:
        verbose_name = "Запись журнала регистрации"
        verbose_name_plural = "Журнал регистрации СИ"
        ordering = ['-receipt_date']

class JournalVerification(models.Model):
    certificate = models.ForeignKey(
        Certificate,
        on_delete=models.CASCADE,
        verbose_name="Свидетельство"
    )
    si = models.ForeignKey(
        SI,
        on_delete=models.PROTECT,
        verbose_name="Средство измерений"
    )
    verification_result = models.CharField(
        max_length=100,
        verbose_name="Результат поверки"
    )

    class Meta:
        verbose_name = "Запись журнала поверки"
        verbose_name_plural = "Журнал поверки"
        ordering = ['-certificate__verification_date']

class JournalEnvironment(models.Model):
    affecting_factors = models.ForeignKey(
        AffectingFactors,
        on_delete=models.CASCADE,
        verbose_name="Факторы влияния"
    )
    measurement_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата измерения"
    )

    class Meta:
        verbose_name = "Запись условий среды"
        verbose_name_plural = "Журнал условий среды"
        ordering = ['-measurement_date']