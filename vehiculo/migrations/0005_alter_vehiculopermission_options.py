# Generated by Django 4.0.5 on 2023-07-23 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculopermission_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculopermission',
            options={'verbose_name': 'Puede visualizar Catálogo de Vehículos', 'verbose_name_plural': 'Permisos para visualizar Catálogo de Vehículos'},
        ),
    ]
