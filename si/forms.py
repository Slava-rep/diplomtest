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
            'pressure_change_rate': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SiReferenceForm(forms.ModelForm):
    class Meta:
        model = SiReference
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }