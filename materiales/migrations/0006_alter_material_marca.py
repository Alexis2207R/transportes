# Generated by Django 4.0.6 on 2022-10-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0005_remove_material_nombre_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='marca',
            field=models.CharField(default='Sin marca', max_length=200, verbose_name='Marca'),
        ),
    ]