from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0003_insert_test_data'),
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
                '88378-23', 'INV-004', 'Расширенная', 'active',
                NOW(), 'ВНИКТИ/03-05-2025/000000004', '2025-05-03', 12,
                '2026-05-02', 'full', 'КЛ-004',
                false, true, true, 'ВНИКТИ',
                '5022067103', 'Петров П.П.', 'С датчиком', 'Поверка выполнена успешно', 'П-004',
                2, 4, 1, 1, 1
            ),
            (
                '88379-23', 'INV-005', 'Базовая', 'active',
                NOW(), 'ВНИКТИ/03-05-2025/000000005', '2025-05-03', 12,
                '2026-05-02', 'full', 'КЛ-005',
                false, true, true, 'ВНИКТИ',
                '5022067103', 'Сидоров С.С.', 'Комплект', 'Без замечаний', 'П-005',
                3, 5, 1, 1, 1
            );
            """,
            reverse_sql="""
            DELETE FROM certificates_certificate 
            WHERE number IN (
                'ВНИКТИ/03-05-2025/000000004',
                'ВНИКТИ/03-05-2025/000000005'
            );
            """
        ),
    ] 