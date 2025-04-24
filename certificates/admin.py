# certificates/admin.py
from django.contrib import admin

from si.models import MeasurementType, SIType, VerificationMethod, VerificationType
from .models import Certificate, SIVerification,Certificate, VerificationType, VerificationMethod, AffectingFactors, Reference
class SIVerificationInline(admin.TabularInline):
    model = SIVerification
    extra = 1

# certificates/admin.py
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'number', 
        'si', 
        'verification_date', 
        'status',  # Теперь это поле существует в модели
        'created_at'  # И это тоже
    )
    list_editable = ('status',)
    list_filter = ('status', 'verification_date')
    readonly_fields = ('created_at',)
    search_fields = ('number', 'si__registration_number')
    date_hierarchy = 'verification_date'
    raw_id_fields = ('si',)
    list_display = (
        'number', 
        'si',
        'verification_date',
        'next_verification_date',
        'status'
    )
    list_filter = ('status', 'verification_type')
    search_fields = ('number', 'si__registration_number')
    inlines = [SIVerificationInline]
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основные данные', {
            'fields': (
                'number',
                'si',
                'verification_date',
                'next_verification_date',
                'interval'
            )
        }),
        ('Результаты поверки', {
            'fields': (
                'verification_type',
                'verification_method',
                'verification_result',
                'affecting_factors'
            )
        }),
        ('Дополнительно', {
            'fields': (
                'status',
                'created_at',
                'verifier'
            )
        })
    )
    



@admin.register(VerificationMethod)
class VerificationMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'verification_type')
    list_filter = ('verification_type',)
    search_fields = ('name',)


# # Пример регистрации модели из si
# @admin.register(SIType)
# class SITypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'reg_number', 'slug')

# @admin.register(MeasurementType)
# class MeasurementTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# @admin.register(Reference)
# class ReferenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'registration_number')




    def get_queryset(self, request):
        return super().get_queryset(request).select_related('si')    
    
    def verification_date_formatted(self, obj):
        return obj.verification_date.strftime("%d-%m-%Y")
    verification_date_formatted.admin_order_field = 'verification_date'