# Generated by Django 4.0.6 on 2022-10-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecosas', '0012_alter_entrada_descripcion_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='descripcion_entrada',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]
