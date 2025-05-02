from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0007_add_measurement_range'),
        ('journals', '0005_update_journal_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Заполняем поля для СИ, которые участвуют в журналах
            UPDATE si SET 
                si_type_id = 23, 
                measurement_range = '0-1000 В', 
                year_of_manufacture = 2023
            WHERE serial_number = 'V001';

            UPDATE si SET 
                si_type_id = 24, 
                measurement_range = '0-10 А', 
                year_of_manufacture = 2022
            WHERE serial_number = 'A001';

            UPDATE si SET 
                si_type_id = 25, 
                measurement_range = '0-1000 Ом', 
                year_of_manufacture = 2021
            WHERE serial_number = 'M001';
            """,
            reverse_sql="""
            -- Откатить только тестовые данные
            UPDATE si SET si_type_id = NULL, measurement_range = NULL, year_of_manufacture = NULL WHERE serial_number IN ('V001', 'A001', 'M001');
            """
        ),
    ] 