# Generated manually

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0004_update_affecting_factors'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Добавляем типы СИ
            INSERT INTO si_types (
                "id_SI_type", gov_registry_number, si_name, manufacturer, 
                type_designation, verification_method_id, status
            ) VALUES 
            (23, '34001-23', 'Вольтметр цифровой', 'ООО "Измерительная техника"', 
                'В7-78/1', 1, 'active'),
            (24, '34002-23', 'Амперметр цифровой', 'АО "Метрология"', 
                'А7-55/2', 1, 'active'),
            (25, '34003-23', 'Мультиметр', 'НПО "Измеритель"', 
                'М7-99/3', 1, 'active');

            -- Обновляем данные СИ
            UPDATE si SET
                registration_number = '23001',
                year_of_manufacture = 2023,
                serial_number = '001',
                si_type_id = 23
            WHERE "id_SI" = 1;

            UPDATE si SET
                registration_number = '23002',
                year_of_manufacture = 2023,
                serial_number = '002',
                si_type_id = 24
            WHERE "id_SI" = 2;

            UPDATE si SET
                registration_number = '23003',
                year_of_manufacture = 2023,
                serial_number = '003',
                si_type_id = 25
            WHERE "id_SI" = 3;
            """,
            reverse_sql="""
            DELETE FROM si_types WHERE "id_SI_type" IN (23, 24, 25);
            """
        ),
    ] 