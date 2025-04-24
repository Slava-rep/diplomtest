# certificates/forms.py
from django import forms
from .models import Certificate
from si.models import SI, AffectingFactors  # Явный импорт
from si.models import VerificationType  # Явный импорт
from si.models import VerificationMethod  # Явный импорт
from django.forms import DateInput, RadioSelect
from .models import AffectingFactors, Certificate
from django.forms import ModelForm
# certificates/forms.py
class AffectingFactorsForm(forms.ModelForm):
    class Meta:
        model = AffectingFactors
        fields = [
            'temperature', 
            'humidity', 
            'pressure', 
            'voltage', 
            'frequency', 
            'harmonic_coefficient', 
            'liquid_temperature', 
            'temperature_change', 
            'pressure_change_rate',

        ]
        widgets = {
            'temperature': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'humidity': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'pressure': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'voltage': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'frequency': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'harmonic_coefficient': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'liquid_temperature': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'temperature_change': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'pressure_change_rate': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
        }

class CertificateForm(forms.ModelForm):             
    class Meta:
        model = Certificate
        fields = [
            'verification_date',
            'next_verification_date',
            'si',
            'verification_type',
            'verification_method',
            'verification_result',
            'interval',
            'previous_verification_mark',
            'is_vn',
            'mark_in_passport',
            'mark_on_si',
            'affecting_factors',
            'comment',
            'gov_reg_number',
            'inventory_number',
            'modification',
            'status',
            # 'created_at',
            'number',
            'organization_name',
            'inn',
            'department_head',
            'verifier',
            'composition',
            'applied_standards',
            'protocol',
        ]
        
        
        
        widgets = {                                 ##########
            'verification_date': forms.DateInput(   ##########
                format='%d.%m.%Y',                  ##########
                attrs={                             ##########
                    'type': 'date',                 ##########
                    'class': 'form-control'         ##########
                }                                   ##########
            ),                                       ##########
            'next_verification_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'readonly': True
            }),
            'verification_type': RadioSelect(choices=Certificate.VERIFICATION_TYPE_CHOICES),
            'si': forms.Select(attrs={
                'class': 'select2',
                'data-url': '/api/si-autocomplete/'
            }),
            
        }
        help_texts = {
            'gov_reg_number': "Номер в государственном реестре (пример: 88375-23)",
            'inventory_number': "Инвентарный номер средства измерений",
        }
    
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Получаем пользователя
        super().__init__(*args, **kwargs)
        # Пример кастомизации queryset
         # Фильтрация СИ для обычных пользователей
        if self.user and not self.user.is_superuser:
            employee = getattr(self.user, 'employee', None)
            if employee:
                # Получаем разрешенные типы измерений
                measurement_types = employee.measurement_types.all()
                # Фильтруем СИ по связанным типам
                self.fields['si'].queryset = SI.objects.filter(
                    si_type__measurement_types__in=measurement_types
                ).distinct()
        
        # Настройка виджетов
        self.fields['si'].queryset = SI.objects.all() #SI.objects.filter(is_active=True)
        self.fields['verification_type'].queryset = VerificationType.objects.all()


        