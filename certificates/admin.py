# # certificates/admin.py
# from django.contrib import admin

# from si.models import MeasurementType, SIType, VerificationMethod, VerificationType
# from .models import Certificate, SIVerification,Certificate, VerificationType, VerificationMethod, AffectingFactors, Reference
# class SIVerificationInline(admin.TabularInline):
#     model = SIVerification
#     extra = 1

# # certificates/admin.py
# @admin.register(Certificate)
# class CertificateAdmin(admin.ModelAdmin):
#     list_display = (
#         'number', 
#         'si', 
#         'verification_date', 
#         'status',  # Теперь это поле существует в модели
#         'created_at'  # И это тоже
#     )
#     list_editable = ('status',)
#     list_filter = ('status', 'verification_date')
#     readonly_fields = ('created_at',)
#     search_fields = ('number', 'si__registration_number')
#     date_hierarchy = 'verification_date'
#     raw_id_fields = ('si',)
#     list_display = (
#         'number', 
#         'si',
#         'verification_date',
#         'next_verification_date',
#         'status'
#     )
#     list_filter = ('status', 'verification_type')
#     search_fields = ('number', 'si__registration_number')
#     inlines = [SIVerificationInline]
#     readonly_fields = ('created_at',)
#     fieldsets = (
#         ('Основные данные', {
#             'fields': (
#                 'number',
#                 'si',
#                 'verification_date',
#                 'next_verification_date',
#                 'interval'
#             )
#         }),
#         ('Результаты поверки', {
#             'fields': (
#                 'verification_type',
#                 'verification_method',
#                 'verification_result',
#                 'affecting_factors'
#             )
#         }),
#         ('Дополнительно', {
#             'fields': (
#                 'status',
#                 'created_at',
#                 'verifier'
#             )
#         })
#     )
    

# @admin.register(VerificationMethod)
# class VerificationMethodAdmin(admin.ModelAdmin):
#     list_display = ('doc_number', 'name')  # Отображаем только номер и название методики
#     search_fields = ('doc_number', 'name')  # Добавляем возможность поиска
#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('si')    
    
#     def verification_date_formatted(self, obj):
#         return obj.verification_date.strftime("%d-%m-%Y")
#     verification_date_formatted.admin_order_field = 'verification_date'



# diplomtest/certificates/admin.py
from django.contrib import admin
from .models import CertificatesCertificate, CertificatesSiverification, CertificatesVerificationmethod

@admin.register(CertificatesCertificate)
class CertificatesCertificateAdmin(admin.ModelAdmin):
    list_display = ('number', 'si', 'verification_date', 'next_verification_date', 'verification_result', 'status')
    list_filter = ('verification_result', 'status', 'verification_date', 'next_verification_date')
    search_fields = ('number', 'si__registration_number', 'si__type__name')
    date_hierarchy = 'verification_date'

@admin.register(CertificatesSiverification)
class CertificatesSiverificationAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'reference', 'applied_at')
    list_filter = ('applied_at',)
    search_fields = ('certificate__number', 'reference__name')

@admin.register(CertificatesVerificationmethod)
class CertificatesVerificationmethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'doc_number', 'si')
    search_fields = ('name', 'doc_number', 'si__registration_number')