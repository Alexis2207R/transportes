# Generated by Django 3.1.2 on 2022-10-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecosas', '0014_auto_20221022_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradamaterial',
            name='cantidad_entrada',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='mermamaterial',
            name='cantidad_merma',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='pecosamaterial',
            name='cantidad',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
    ]