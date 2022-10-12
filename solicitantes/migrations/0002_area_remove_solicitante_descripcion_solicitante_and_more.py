# Generated by Django 4.1.1 on 2022-10-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=200, verbose_name='Nombre')),
                ('creacion_area', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificacion_area', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.RemoveField(
            model_name='solicitante',
            name='descripcion_solicitante',
        ),
        migrations.AddField(
            model_name='solicitante',
            name='sexo_solicitante',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1, verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='solicitante',
            name='telefono_solicitante',
            field=models.CharField(max_length=13, null=True, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='solicitante',
            name='nombre_solicitante',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]
