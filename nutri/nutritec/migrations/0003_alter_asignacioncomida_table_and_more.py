# Generated by Django 5.0.6 on 2024-06-02 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutritec', '0002_comida_images_ejercicio_images'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='asignacioncomida',
            table='nut_asignacion_comida',
        ),
        migrations.AlterModelTable(
            name='asignacionejercicio',
            table='nut_asignacion_ejercicio',
        ),
        migrations.AlterModelTable(
            name='categoriacomida',
            table='nut_categoria_comida',
        ),
        migrations.AlterModelTable(
            name='comida',
            table='nut_comida',
        ),
        migrations.AlterModelTable(
            name='ejercicio',
            table='nut_ejercicio',
        ),
        migrations.AlterModelTable(
            name='registroimc',
            table='nut_registro_imc',
        ),
        migrations.AlterModelTable(
            name='tipoimc',
            table='nut_tipo_imc',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='nut_usuario',
        ),
    ]
