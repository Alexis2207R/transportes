# Generated by Django 4.1.1 on 2022-10-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_solicitante', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion_solicitante', models.TextField(verbose_name='Descripcion')),
                ('creacion_solicitante', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificacion_solicitante', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'solicitante',
                'verbose_name_plural': 'solicitantes',
            },
        ),
    ]
