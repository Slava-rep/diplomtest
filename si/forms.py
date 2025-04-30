# diplomtest/si/forms.py
from django import forms
from .models import (
    SiVerificationtype, SiVerificationmethod, 
    SiAffectingfactors, SiReference
)

class SiVerificationtypeForm(forms.ModelForm):
    class Meta:
        model = SiVerificationtype
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SiVerificationmethodForm(forms.ModelForm):
    class Meta:
        model = SiVerificationmethod
        fields = ['name', 'method_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'method_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SiAffectingfactorsForm(forms.ModelForm):
    class Meta:
        model = SiAffectingfactors
        fields = [
            'temperature',
            'humidity',
            'pressure',
            'voltage',
            'frequency',
            'harmonic_coefficient',
            'liquid_temperature',
            'temperature_change',
            'pressure_change_rate'
        ]
        widgets = {
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'humidity': forms.TextInput(attrs={'class': 'form-control'}),
            'pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'harmonic_coefficient': forms.TextInput(attrs={'class': 'form-control'}),
            'liquid_temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature_change': forms.TextInput(attrs={'class': 'form-control'}),
            'pressure_change_rate': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'temperature': 'Температура',
            'humidity': 'Влажность',
            'pressure': 'Давление',
            'voltage': 'Напряжение',
            'frequency': 'Частота',
            'harmonic_coefficient': 'Коэффициент гармоник',
            'liquid_temperature': 'Температура жидкости',
            'temperature_change': 'Изменение температуры',
            'pressure_change_rate': 'Скорость изменения давления'
        }

class SiReferenceForm(forms.ModelForm):
    class Meta:
        model = SiReference
        fields = [
            'standard_type', 'brand', 'manufacturer_name', 'serial_number',
            'measurement_range', 'uncertainty', 'fif_registration_number',
            'country_of_manufacturer', 'manufacture_year', 'commissioning_year',
            'inventory_number', 'calibration_certificate_number',
            'calibration_certificate_date', 'calibration_certificate_validity',
            'ownership', 'installation_location', 'note'
        ]
        widgets = {
            'standard_type': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacturer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'measurement_range': forms.TextInput(attrs={'class': 'form-control'}),
            'uncertainty': forms.TextInput(attrs={'class': 'form-control'}),
            'fif_registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacture_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'commissioning_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'inventory_number': forms.TextInput(attrs={'class': 'form-control'}),
            'calibration_certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'calibration_certificate_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'calibration_certificate_validity': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ownership': forms.TextInput(attrs={'class': 'form-control'}),
            'installation_location': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }