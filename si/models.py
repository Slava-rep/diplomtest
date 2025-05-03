from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class SiSitype(models.Model):
    id_SI_type = models.AutoField(primary_key=True, db_column='id_SI_type')
    gov_registry_number = models.CharField(max_length=255, null=True, blank=True)
    si_name = models.CharField(max_length=255, null=True, blank=True)
    type_designation = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    record_number = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    description_document = models.TextField(null=True, blank=True)
    calibration_method_document = models.TextField(null=True, blank=True)
    procedure = models.CharField(max_length=255, default='Standard')
    certificate_term = models.DateField(null=True, blank=True)
    periodic_calibration = models.BooleanField(default=False)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, default='active')
    verification_method = models.ForeignKey('SiVerificationmethod', on_delete=models.CASCADE, db_column='verification_method_id')
    
    def __str__(self):
        return f"{self.si_name} ({self.gov_registry_number})"
    
    class Meta:
        db_table = 'si_types'
        verbose_name = 'Тип СИ'
        verbose_name_plural = 'Типы СИ'

class SiSi(models.Model):
    id_SI = models.AutoField(primary_key=True, db_column='id_SI')
    registration_number = models.CharField(max_length=255, db_column='registration_number')
    year_of_manufacture = models.IntegerField(db_column='year_of_manufacture')
    modification = models.CharField(max_length=255, blank=True, null=True, db_column='modification')
    serial_number = models.CharField(max_length=255, db_column='serial_number')
    si_type_id = models.ForeignKey(SiSitype, on_delete=models.CASCADE, db_column='si_type_id')
    
    def __str__(self):
        return f"{self.registration_number} - {self.si_type_id.si_name}"
    
    class Meta:
        db_table = 'si'
        verbose_name = 'Средство измерений'
        verbose_name_plural = 'Средства измерений'

class SiVerificationtype(models.Model):
    id_verification_type = models.AutoField(primary_key=True, db_column='id_verification_type')
    name = models.CharField(max_length=255, db_column='name')
    description = models.TextField(blank=True, null=True, db_column='description')

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'verification_types'
        verbose_name = 'Вид поверки'
        verbose_name_plural = 'Виды поверки'

class SiVerificationmethod(models.Model):
    id_verification_method = models.AutoField(primary_key=True, db_column='id_verification_method')
    name = models.CharField(max_length=255, db_column='name')
    method_number = models.CharField(max_length=255, blank=True, null=True, db_column='method_number')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'verification_methods'
        verbose_name = 'Методика поверки'
        verbose_name_plural = 'Методики поверки'

class SiAffectingfactors(models.Model):
    id_affecting_factors = models.AutoField(primary_key=True, db_column='id_affecting_factors')
    temperature = models.CharField(max_length=255, null=True, blank=True)
    humidity = models.CharField(max_length=255, null=True, blank=True)
    pressure = models.CharField(max_length=255, null=True, blank=True)
    voltage = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.CharField(max_length=255, null=True, blank=True)
    harmonic_coefficient = models.CharField(max_length=255, null=True, blank=True)
    liquid_temperature = models.CharField(max_length=255, null=True, blank=True)
    temperature_change = models.CharField(max_length=255, null=True, blank=True)
    pressure_change_rate = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"Фактор #{self.id_affecting_factors}"
    
    class Meta:
        db_table = 'affecting_factors'
        verbose_name = 'Влияющий фактор'
        verbose_name_plural = 'Влияющие факторы'

class SiMeasurementtype(models.Model):
    id_measurement_type = models.AutoField(primary_key=True, db_column='id_measurement_type')
    name = models.CharField(max_length=255, db_column='name')
    description = models.TextField(blank=True, null=True, db_column='description')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'measurement_types'
        verbose_name = 'Вид измерений'
        verbose_name_plural = 'Виды измерений'

class SiReference(models.Model):
    id_reference = models.AutoField(primary_key=True, db_column='id_reference')
    range = models.CharField(max_length=255, null=True, blank=True)
    standard_type = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    fif_registration_number = models.CharField(max_length=255, null=True, blank=True)
    country_of_manufacturer = models.CharField(max_length=255, null=True, blank=True)
    manufacturer_name = models.CharField(max_length=255, null=True, blank=True)
    manufacture_year = models.IntegerField(null=True, blank=True)
    commissioning_year = models.IntegerField(null=True, blank=True)
    inventory_number = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    measurement_range = models.CharField(max_length=255, null=True, blank=True)
    uncertainty = models.CharField(max_length=255, null=True, blank=True)
    calibration_results_link = models.CharField(max_length=255, null=True, blank=True)
    calibration_certificate_date = models.DateField(null=True, blank=True)
    calibration_certificate_validity = models.DateField(null=True, blank=True)
    calibration_certificate_number = models.CharField(max_length=255, null=True, blank=True)
    ownership = models.CharField(max_length=255, null=True, blank=True)
    installation_location = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.brand} - {self.serial_number}"
    
    class Meta:
        db_table = 'references'
        verbose_name = 'Эталон'
        verbose_name_plural = 'Эталоны' 