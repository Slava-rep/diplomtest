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
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(SiReference)
class SiReferenceAdmin(admin.ModelAdmin):
    list_display = ('standard_type', 'brand', 'serial_number')
    search_fields = ('standard_type', 'brand', 'serial_number')
    list_filter = ('standard_type', 'brand')

@admin.register(SiMeasurementtype)
class SiMeasurementtypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)