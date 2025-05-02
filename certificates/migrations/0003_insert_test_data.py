# Generated manually

from django.db import migrations
from django.utils import timezone
from datetime import datetime, timedelta

class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_create_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            INSERT INTO certificates_certificate (
                gov_reg_number, inventory_number, modification, status,
                created_at, number, verification_date, interval,
                next_verification_date, verification_result, previous_verification_mark,
                is_vn, mark_in_passport, mark_on_si, organization_name,
                inn, department_head, composition, comment, protocol,
                affecting_factors_id, si_id, verification_method_id,
                verification_type_id, verifier_id
            ) VALUES 
            (
                '88375-23', 'INV-001', 'Стандартная', 'active',
                NOW(), 'ВНИКТИ/02-05-2025/000000001', '2025-05-02', 12,
                '2026-05-01', 'full', 'КЛ-001',
                false, true, true, 'ВНИКТИ',
                '5022067103', 'Крюков С.А.', 'В комплекте', 'Поверка выполнена успешно', 'П-001',
                1, 1, 1, 1, 1
            ),
            (
                '88376-23', 'INV-002', 'Модифицированная', 'active',
                NOW(), 'ВНИКТИ/02-05-2025/000000002', '2025-05-02', 12,
                '2026-05-01', 'full', 'КЛ-002',
                false, true, true, 'ВНИКТИ',
                '5022067103', 'Крюков С.А.', 'В комплекте с датчиком', 'Поверка выполнена в полном объеме', 'П-002',
                1, 2, 1, 1, 1
            ),
            (
                '88377-23', 'INV-003', 'Базовая', 'active',
                NOW(), 'ВНИКТИ/02-05-2025/000000003', '2025-05-02', 12,
                '2026-05-01', 'full', 'КЛ-003',
                false, true, true, 'ВНИКТИ',
                '5022067103', 'Крюков С.А.', 'Стандартная комплектация', 'Замечаний нет', 'П-003',
                1, 3, 1, 1, 1
            );
            """,
            reverse_sql="""
            DELETE FROM certificates_certificate 
            WHERE number IN (
                'ВНИКТИ/02-05-2025/000000001',
                'ВНИКТИ/02-05-2025/000000002',
                'ВНИКТИ/02-05-2025/000000003'
            );
            """
        ),
    ] 