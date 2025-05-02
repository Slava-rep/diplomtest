# Generated manually

from django.db import migrations
from django.utils import timezone
from datetime import datetime, timedelta

class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_create_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Добавление записей в журнал регистрации
            INSERT INTO journals_journalregistration (
                receipt_date, receipt_signature, issue_date, issue_signature, si_id
            ) VALUES 
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 1),
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 2),
            ('2025-05-02', 'Крюков С.А.', '2025-05-03', 'Иванов И.И.', 3),
            ('2025-05-01', 'Петров П.П.', '2025-05-02', 'Сидоров С.С.', 1),
            ('2025-05-01', 'Петров П.П.', NULL, NULL, 2);

            -- Добавление записей в журнал поверки
            INSERT INTO journals_journalverification (
                verification_result, certificate_id, si_id
            ) VALUES 
            ('Пригодно', 1, 1),
            ('Пригодно', 2, 2),
            ('Пригодно', 3, 3),
            ('Непригодно', 1, 2),
            ('На калибровку', 2, 1);

            -- Добавление записей в журнал условий среды
            INSERT INTO journals_journalenvironment (
                measurement_date, affecting_factors_id
            ) VALUES 
            ('2025-05-02', 1),
            ('2025-05-01', 1),
            ('2025-05-01', 1),
            ('2025-04-30', 1),
            ('2025-04-30', 1);
            """,
            reverse_sql="""
            DELETE FROM journals_journalregistration;
            DELETE FROM journals_journalverification;
            DELETE FROM journals_journalenvironment;
            """
        ),
    ] 