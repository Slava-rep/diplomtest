# from django.contrib import admin
# from .models import MeasurementType, Reference, SIType, SI

# # Класс для встроенного редактирования SI
# class SIInline(admin.TabularInline):
#     model = SI
#     extra = 1

# # Административный класс для SIType
# @admin.register(SIType)
# class SITypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug', 'description')
#     prepopulated_fields = {'slug': ('name',)}
#     inlines = [SIInline]  # Добавляем встроенное отображение SI

# # Административный класс для SI
# @admin.register(SI)
# class SIAdmin(admin.ModelAdmin):
#     list_display = ('registration_number', 'serial', 'type', 'is_active')
#     search_fields = ('registration_number', 'serial')
#     list_filter = ('type', 'is_active')
#     ordering = ('-manufacture_year',)
    
#     actions = ['deactivate_si']
    
#     def deactivate_si(self, request, queryset):
#         queryset.update(is_active=False)
#     deactivate_si.short_description = "Деактивировать выбранные СИ"



# @admin.register(MeasurementType)
# class MeasurementTypeAdmin(admin.ModelAdmin):
#     list_display = ('id_measurement_type', 'name', 'measurement_range', 'error_uncertainty')

# @admin.register(Reference)
# class ReferenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'registration_number')


# diplomtest/si/admin.py
from django.contrib import admin
from .models import (
    SiSi, SiSitype, SiVerificationtype, SiVerificationmethod,
    SiAffectingfactors, SiReference, SiMeasurementtype
)

@admin.register(SiSi)
class SiSiAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'si_type_id', 'serial_number', 'year_of_manufacture')
    search_fields = ('registration_number', 'serial_number')
    list_filter = ('si_type_id', 'year_of_manufacture')

@admin.register(SiSitype)
class SiSitypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SiVerificationtype)
class SiVerificationtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SiVerificationmethod)
class SiVerificationmethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'method_number')
    search_fields = ('name', 'method_number')

@admin.register(SiAffectingfactors)
class SiAffectingfactorsAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'pressure', 'voltage', 'frequency', 'harmonic_coefficient')
    search_fields = ('temperature', 'humidity', 'pressure', 'voltage', 'frequency')

@admin.register(SiReference)
class SiReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(SiMeasurementtype)
class SiMeasurementtypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)