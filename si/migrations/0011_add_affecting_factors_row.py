from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0010_fix_issue_date_and_ranges'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            INSERT INTO affecting_factors (
                id_affecting_factors, temperature, humidity, pressure, employee_signature
            ) VALUES (
                1, '22 ± 2', '60 ± 5', '101.5 ± 0.5', 'Иванов И.И.'
            )
            ON CONFLICT (id_affecting_factors) DO NOTHING;
            """,
            reverse_sql="""
            DELETE FROM affecting_factors WHERE id_affecting_factors = 1;
            """
        ),
    ] 