# # certificates/forms.py
# from django import forms
# from .models import Certificate
# from si.models import SI, AffectingFactors  # Явный импорт
# from si.models import VerificationType  # Явный импорт
# from si.models import VerificationMethod  # Явный импорт
# from django.forms import DateInput, RadioSelect
# from .models import AffectingFactors, Certificate
# from django.forms import ModelForm
# # certificates/forms.py
# class AffectingFactorsForm(forms.ModelForm):
#     class Meta:
#         model = AffectingFactors
#         fields = [
#             'temperature', 
#             'humidity', 
#             'pressure', 
#             'voltage', 
#             'frequency', 
#             'harmonic_coefficient', 
#             'liquid_temperature', 
#             'temperature_change', 
#             'pressure_change_rate',

#         ]
#         widgets = {
#             'temperature': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'humidity': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'pressure': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'voltage': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'frequency': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'harmonic_coefficient': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'liquid_temperature': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'temperature_change': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#             'pressure_change_rate': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
#         }

# class CertificateForm(forms.ModelForm):             
#     class Meta:
#         model = Certificate
#         fields = [
#             'verification_date',
#             'next_verification_date',
#             'si',
#             'verification_type',
#             'verification_method',
#             'verification_result',
#             'interval',
#             'previous_verification_mark',
#             'is_vn',
#             'mark_in_passport',
#             'mark_on_si',
#             'affecting_factors',
#             'comment',
#             'gov_reg_number',
#             'inventory_number',
#             'modification',
#             'status',
#             # 'created_at',
#             'number',
#             'organization_name',
#             'inn',
#             'department_head',
#             'verifier',
#             'composition',
#             'applied_standards',
#             'protocol',
#         ]
        
        
        
#         widgets = {                                 ##########
#             'verification_date': forms.DateInput(   ##########
#                 format='%d.%m.%Y',                  ##########
#                 attrs={                             ##########
#                     'type': 'date',                 ##########
#                     'class': 'form-control'         ##########
#                 }                                   ##########
#             ),                                       ##########
#             'next_verification_date': DateInput(attrs={
#                 'type': 'date',
#                 'class': 'form-control',
#                 'readonly': True
#             }),
#             'verification_type': RadioSelect(choices=Certificate.VERIFICATION_TYPE_CHOICES),
#             'si': forms.Select(attrs={
#                 'class': 'select2',
#                 'data-url': '/api/si-autocomplete/'
#             }),
            
#         }
#         help_texts = {
#             'gov_reg_number': "Номер в государственном реестре (пример: 88375-23)",
#             'inventory_number': "Инвентарный номер средства измерений",
#         }
    
        
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)  # Получаем пользователя
#         super().__init__(*args, **kwargs)
#         # Пример кастомизации queryset
#          # Фильтрация СИ для обычных пользователей
#         if self.user and not self.user.is_superuser:
#             employee = getattr(self.user, 'employee', None)
#             if employee:
#                 # Получаем разрешенные типы измерений
#                 measurement_types = employee.measurement_types.all()
#                 # Фильтруем СИ по связанным типам
#                 self.fields['si'].queryset = SI.objects.filter(
#                     si_type__measurement_types__in=measurement_types
#                 ).distinct()
        
#         # Настройка виджетов
#         self.fields['si'].queryset = SI.objects.all() #SI.objects.filter(is_active=True)
#         self.fields['verification_type'].queryset = VerificationType.objects.all()


# diplomtest/certificates/forms.py
from django import forms
from .models import CertificatesCertificate
from si.models import SiSi, SiAffectingfactors, SiVerificationtype, SiVerificationmethod
from django.forms import DateInput, RadioSelect
from django.forms import ModelForm

class AffectingFactorsForm(forms.ModelForm):
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

class CertificateForm(forms.ModelForm):             
    class Meta:
        model = CertificatesCertificate
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
            'number',
            'organization_name',
            'inn',
            'department_head',
            'verifier',
            'composition',
            'protocol',
        ]
        
        widgets = {
            'verification_date': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'next_verification_date': DateInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'verification_type': forms.Select(attrs={'class': 'form-control'}),
            'si': forms.Select(attrs={'class': 'form-control'}),
            'verification_method': forms.Select(attrs={'class': 'form-control'}),
            'affecting_factors': forms.Select(attrs={'class': 'form-control'}),
            'gov_reg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'inventory_number': forms.TextInput(attrs={'class': 'form-control'}),
            'modification': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_name': forms.TextInput(attrs={'class': 'form-control'}),
            'inn': forms.TextInput(attrs={'class': 'form-control'}),
            'department_head': forms.TextInput(attrs={'class': 'form-control'}),
            'verifier': forms.TextInput(attrs={'class': 'form-control'}),
            'composition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'protocol': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        help_texts = {
            'gov_reg_number': "Номер в государственном реестре (пример: 88375-23)",
            'inventory_number': "Инвентарный номер средства измерений",
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Настройка виджетов
        self.fields['si'].queryset = SiSi.objects.all().select_related('si_type_id')
        self.fields['verification_type'].queryset = SiVerificationtype.objects.all().order_by('name')
        self.fields['verification_method'].queryset = SiVerificationmethod.objects.all().order_by('name')
        
        # Добавляем подсказки для полей
        self.fields['si'].help_text = "Выберите средство измерений из списка"
        self.fields['verification_type'].help_text = "Выберите тип поверки"
        self.fields['verification_method'].help_text = "Выберите метод поверки"