# Generated manually

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS journals_journalregistration (
                id SERIAL PRIMARY KEY,
                receipt_date DATE NOT NULL,
                receipt_signature VARCHAR(100) NOT NULL,
                issue_date DATE NULL,
                issue_signature VARCHAR(100) NULL,
                si_id INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS journals_journalverification (
                id SERIAL PRIMARY KEY,
                verification_result VARCHAR(100) NOT NULL,
                certificate_id INTEGER NOT NULL,
                si_id INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS journals_journalenvironment (
                id SERIAL PRIMARY KEY,
                measurement_date DATE NOT NULL,
                affecting_factors_id INTEGER NOT NULL
            );
            """,
            reverse_sql="""
            DROP TABLE IF EXISTS journals_journalregistration;
            DROP TABLE IF EXISTS journals_journalverification;
            DROP TABLE IF EXISTS journals_journalenvironment;
            """
        ),
    ] 