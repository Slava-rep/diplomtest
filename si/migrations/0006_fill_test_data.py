from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0005_insert_si_types'),
        ('journals', '0005_update_journal_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Заполняем поля для всех СИ, которые участвуют в журналах
            UPDATE si SET 
                si_type_id = 23, 
                measurement_range = '0-1000 В', 
                year_of_manufacture = 2023,
                serial_number = 'V001'
            WHERE serial_number = 'V001' OR "id_SI" = 1;

            UPDATE si SET 
                si_type_id = 24, 
                measurement_range = '0-10 А', 
                year_of_manufacture = 2022,
                serial_number = 'A001'
            WHERE serial_number = 'A001' OR "id_SI" = 2;

            UPDATE si SET 
                si_type_id = 25, 
                measurement_range = '0-1000 Ом', 
                year_of_manufacture = 2021,
                serial_number = 'M001'
            WHERE serial_number = 'M001' OR "id_SI" = 3;

            -- Если есть другие serial_number или id_SI, добавьте их аналогично!
            """,
            reverse_sql="""
            -- Откатить только тестовые данные
            UPDATE si SET si_type_id = NULL, measurement_range = NULL, year_of_manufacture = NULL WHERE serial_number IN ('V001', 'A001', 'M001') OR "id_SI" IN (1,2,3);
            """
        ),
    ]