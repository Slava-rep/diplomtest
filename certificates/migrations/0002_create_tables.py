# Generated manually

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS certificates_certificate (
                id SERIAL PRIMARY KEY,
                gov_reg_number VARCHAR(20) NOT NULL,
                inventory_number VARCHAR(50) NOT NULL,
                modification VARCHAR(100) NOT NULL,
                status VARCHAR(10) NOT NULL,
                created_at TIMESTAMP NOT NULL,
                number VARCHAR(50) UNIQUE NOT NULL,
                verification_date DATE NOT NULL,
                interval INTEGER NOT NULL,
                next_verification_date DATE NOT NULL,
                verification_result VARCHAR(7) NOT NULL,
                previous_verification_mark VARCHAR(100) NOT NULL,
                is_vn BOOLEAN NOT NULL,
                mark_in_passport BOOLEAN NOT NULL,
                mark_on_si BOOLEAN NOT NULL,
                organization_name VARCHAR(100) NOT NULL,
                inn VARCHAR(12) NOT NULL,
                department_head VARCHAR(100) NOT NULL,
                composition TEXT NOT NULL,
                comment TEXT NOT NULL,
                protocol VARCHAR(100),
                affecting_factors_id INTEGER,
                si_id INTEGER NOT NULL,
                verification_method_id INTEGER NOT NULL,
                verification_type_id INTEGER NOT NULL,
                verifier_id INTEGER NOT NULL
            );
            """,
            reverse_sql="""
            DROP TABLE IF EXISTS certificates_certificate;
            """
        ),
    ] 