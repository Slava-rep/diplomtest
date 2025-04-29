# from django.contrib import admin
# from .models import Employee, EmployeeMeasurementType

# # employees/admin.py
# class EmployeeMeasurementTypeInline(admin.TabularInline):
#     model = EmployeeMeasurementType
#     extra = 1
#     fk_name = 'employee'

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'get_measurement_types')
#     inlines = [EmployeeMeasurementTypeInline]
    
#     def get_measurement_types(self, obj):
#         if hasattr(obj, 'employeemeasurementtype_set'):
#             return ", ".join([str(mt.measurement_type) for mt in obj.employeemeasurementtype_set.all()])
#         return ""
#     get_measurement_types.short_description = "Виды измерений"



# diplomtest/employees/admin.py
from django.contrib import admin
from .models import EmployeesEmployee, EmployeesEmployeemeasurementtype

@admin.register(EmployeesEmployee)
class EmployeesEmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'snils', 'specialization', 'qualification')
    search_fields = ('user__username', 'snils', 'specialization')
    list_filter = ('specialization', 'qualification')

@admin.register(EmployeesEmployeemeasurementtype)
class EmployeesEmployeemeasurementtypeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'measurement_type_id')
    search_fields = ('employee__user__username',)
    list_filter = ('measurement_type_id',)