# Generated by Django 4.0.1 on 2022-01-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='asiento',
            table='asiento',
        ),
        migrations.AlterModelTable(
            name='bus',
            table='bus',
        ),
        migrations.AlterModelTable(
            name='chofer',
            table='chofer',
        ),
        migrations.AlterModelTable(
            name='pasajero',
            table='pasajero',
        ),
        migrations.AlterModelTable(
            name='trayecto',
            table='trayecto',
        ),
        migrations.AlterModelTable(
            name='viaje',
            table='viaje',
        ),
    ]
