# Generated by Django 4.0.5 on 2023-07-23 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0006_alter_vehiculopermission_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VehiculoPermission',
        ),
    ]
