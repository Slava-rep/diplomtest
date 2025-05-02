# Generated manually

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_insert_test_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Очищаем существующие данные
            DELETE FROM journals_journalregistration;
            DELETE FROM journals_journalverification;
            DELETE FROM journals_journalenvironment;
            
            -- Добавляем новые записи в журнал регистрации
            INSERT INTO journals_journalregistration (
                receipt_date, receipt_signature, issue_date, issue_signature, si_id
            ) VALUES 
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 1),
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 2),
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 3),
            ('2025-05-01', 'Петров П.П.', '2025-05-02', 'Сидоров С.С.', 1),
            ('2025-05-01', 'Петров П.П.', NULL, NULL, 2);

            -- Добавляем новые записи в журнал поверки
            INSERT INTO journals_journalverification (
                verification_result, certificate_id, si_id
            ) VALUES 
            ('Пригодно к применению', 1, 1),
            ('Пригодно к применению', 2, 2),
            ('Пригодно к применению', 3, 3),
            ('Не соответствует требованиям', 1, 2),
            ('Направлено на калибровку', 2, 1);

            -- Добавляем новые записи в журнал условий среды с разными значениями
            INSERT INTO journals_journalenvironment (
                measurement_date, affecting_factors_id
            ) VALUES 
            ('2025-05-02', 1),  -- Температура: 20 ± 2, Влажность: 65 ± 5, Давление: 101.3 ± 0.5
            ('2025-05-01', 2),  -- Температура: 22 ± 2, Влажность: 60 ± 5, Давление: 101.5 ± 0.5
            ('2025-05-01', 3),  -- Температура: 21 ± 2, Влажность: 55 ± 5, Давление: 101.4 ± 0.5
            ('2025-04-30', 4),  -- Температура: 19 ± 2, Влажность: 70 ± 5, Давление: 101.2 ± 0.5
            ('2025-04-30', 1);  -- Температура: 20 ± 2, Влажность: 65 ± 5, Давление: 101.3 ± 0.5
            """,
            reverse_sql="""
            DELETE FROM journals_journalregistration;
            DELETE FROM journals_journalverification;
            DELETE FROM journals_journalenvironment;
            """
        ),
    ] 