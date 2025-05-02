from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0009_fill_additional_fields'),
        ('journals', '0005_update_journal_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Диапазон измерений для остальных СИ (на всякий случай)
            UPDATE si SET measurement_range = '0-10 бар' WHERE serial_number = 'P001';
            UPDATE si SET measurement_range = '0-100 кПа' WHERE serial_number = 'D001';

            -- Дата выдачи для строки с id=10 в журнале регистрации СИ
            UPDATE journals_journalregistration SET issue_date = '2025-05-05' WHERE id = 10;
            """,
            reverse_sql="""
            UPDATE si SET measurement_range = NULL WHERE serial_number IN ('P001', 'D001');
            UPDATE journals_journalregistration SET issue_date = NULL WHERE id = 10;
            """
        ),
    ] 