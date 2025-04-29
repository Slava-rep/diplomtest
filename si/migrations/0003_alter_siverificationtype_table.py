from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0002_alter_sisi_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='siverificationtype',
            table='si_verification',
        ),
    ] 