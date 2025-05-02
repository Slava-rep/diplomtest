# Generated manually

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0004_update_journal_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Обновляем записи в журнале условий среды
            UPDATE journals_journalenvironment SET
                affecting_factors_id = 1  -- Температура: 20 ± 2, Влажность: 65 ± 5, Давление: 101.3 ± 0.5
            WHERE measurement_date = '2025-05-02';

            UPDATE journals_journalenvironment SET
                affecting_factors_id = 2  -- Температура: 22 ± 2, Влажность: 60 ± 5, Давление: 101.5 ± 0.5
            WHERE measurement_date = '2025-05-01';

            UPDATE journals_journalenvironment SET
                affecting_factors_id = 3  -- Температура: 21 ± 2, Влажность: 55 ± 5, Давление: 101.4 ± 0.5
            WHERE measurement_date = '2025-05-01' AND id > (
                SELECT MIN(id) FROM journals_journalenvironment 
                WHERE measurement_date = '2025-05-01'
            );

            UPDATE journals_journalenvironment SET
                affecting_factors_id = 4  -- Температура: 19 ± 2, Влажность: 70 ± 5, Давление: 101.2 ± 0.5
            WHERE measurement_date = '2025-04-30';

            -- Обновляем записи в журнале поверки
            UPDATE journals_journalverification SET
                verification_result = 'Пригодно к применению'
            WHERE certificate_id = 1;

            UPDATE journals_journalverification SET
                verification_result = 'Пригодно к применению'
            WHERE certificate_id = 2;

            UPDATE journals_journalverification SET
                verification_result = 'Пригодно к применению'
            WHERE certificate_id = 3;

            -- Обновляем записи в журнале регистрации
            UPDATE journals_journalregistration SET
                receipt_signature = 'Крюков С.А.',
                issue_signature = 'Иванов И.И.'
            WHERE receipt_date = '2025-05-02';

            UPDATE journals_journalregistration SET
                receipt_signature = 'Петров П.П.',
                issue_signature = 'Сидоров С.С.'
            WHERE receipt_date = '2025-05-01';
            """,
            reverse_sql="SELECT 1;"  # No need to reverse these updates
        ),
    ] 