from django.contrib import admin
from .models import Employee, EmployeeMeasurementType

# employees/admin.py


class EmployeeMeasurementTypeInline(admin.TabularInline):
    model = EmployeeMeasurementType
    extra = 1
    fk_name = 'employee'

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     inlines = [EmployeeMeasurementTypeInline]



# class MeasurementTypeInline(admin.TabularInline):
#     model = EmployeeMeasurementType
#     extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_measurement_types')
    inlines = [EmployeeMeasurementTypeInline]
    
    def get_measurement_types(self, obj):
        if hasattr(obj, 'employeemeasurementtype_set'):
            return ", ".join([str(mt.measurement_type) for mt in obj.employeemeasurementtype_set.all()])
        return ""
    get_measurement_types.short_description = "Виды измерений"
    
    # def get_measurement_types(self, obj):
    #     return ", ".join([mt.name for mt in obj.employeemeasurementtype_set.all()])  #measurement_types
    # get_measurement_types.short_description = "Виды измерений"