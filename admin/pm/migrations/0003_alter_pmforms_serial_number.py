# Generated by Django 4.2.7 on 2023-11-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0002_pmforms_device_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmforms',
            name='serial_number',
            field=models.CharField(max_length=70),
        ),
    ]