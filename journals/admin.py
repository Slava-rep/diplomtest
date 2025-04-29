# diplomtest/journals/admin.py
from django.contrib import admin
from .models import JournalsJournalregistration, JournalsJournalverification, JournalsJournalenvironment

@admin.register(JournalsJournalregistration)
class JournalsJournalregistrationAdmin(admin.ModelAdmin):
    list_display = ('si', 'receipt_date', 'receipt_signature', 'issue_date', 'issue_signature')
    list_filter = ('receipt_date', 'issue_date')
    search_fields = ('si__registration_number', 'si__type__name', 'receipt_signature', 'issue_signature')
    date_hierarchy = 'receipt_date'

@admin.register(JournalsJournalverification)
class JournalsJournalverificationAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'si', 'verification_result')
    list_filter = ('verification_result',)
    search_fields = ('certificate__number', 'si__registration_number', 'si__type__name')

@admin.register(JournalsJournalenvironment)
class JournalsJournalenvironmentAdmin(admin.ModelAdmin):
    list_display = ('affecting_factors', 'measurement_date')
    list_filter = ('measurement_date',)
    search_fields = ('affecting_factors__temperature', 'affecting_factors__humidity', 'affecting_factors__pressure')
    date_hierarchy = 'measurement_date'