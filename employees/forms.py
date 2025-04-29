# from django import forms
# from .models import Employee
# from django.contrib.auth import get_user_model

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['user', 'birth_date', 'snils', 'specialization', 'qualification']
#         widgets = {
#             'birth_date': forms.DateInput(attrs={'type': 'date'}),
#             'user': forms.Select(attrs={'class': 'select2'}),
#         }
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user'].queryset = get_user_model().objects.filter(employee__isnull=True)

# diplomtest/employees/forms.py
from django import forms
from .models import EmployeesEmployee
from django.contrib.auth import get_user_model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeesEmployee
        fields = ['user', 'birth_date', 'snils', 'specialization', 'qualification']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'user': forms.Select(attrs={'class': 'select2'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = get_user_model().objects.filter(employee__isnull=True)