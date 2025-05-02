from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('si', '0006_fill_test_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='sisi',
            name='measurement_range',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ] 