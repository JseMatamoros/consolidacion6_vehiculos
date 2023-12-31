# Generated by Django 4.0.5 on 2023-07-23 07:05

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vehiculo', '0002_vehiculo_condicion_precio_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoPermission',
            fields=[
            ],
            options={
                'verbose_name': 'Puede visualizar Catálogo de Vehículos',
                'verbose_name_plural': 'Permisos para visualizar Catálogo de Vehículos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='condicion_precio',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
