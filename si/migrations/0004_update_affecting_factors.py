# Generated manually

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Обновляем существующие записи в таблице affecting_factors
            UPDATE affecting_factors 
            SET 
                temperature = '20 ± 2',
                humidity = '65 ± 5',
                pressure = '101.3 ± 0.5',
                voltage = '220 ± 10',
                frequency = '50 ± 1'
            WHERE id_affecting_factors = 1;
            
            -- Добавляем новые записи с разными значениями
            INSERT INTO affecting_factors (
                id_affecting_factors, temperature, humidity, pressure, voltage, frequency
            ) VALUES 
            (2, '22 ± 2', '60 ± 5', '101.5 ± 0.5', '220 ± 10', '50 ± 1'),
            (3, '21 ± 2', '55 ± 5', '101.4 ± 0.5', '220 ± 10', '50 ± 1'),
            (4, '19 ± 2', '70 ± 5', '101.2 ± 0.5', '220 ± 10', '50 ± 1');
            """,
            reverse_sql="""
            DELETE FROM affecting_factors WHERE id_affecting_factors > 1;
            UPDATE affecting_factors 
            SET 
                temperature = NULL,
                humidity = NULL,
                pressure = NULL,
                voltage = NULL,
                frequency = NULL
            WHERE id_affecting_factors = 1;
            """
        ),
    ] 