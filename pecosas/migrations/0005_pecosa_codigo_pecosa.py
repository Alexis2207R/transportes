# Generated by Django 4.0.6 on 2022-10-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecosas', '0004_pecosa_matpecosa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pecosa',
            name='codigo_pecosa',
            field=models.CharField(max_length=50, null=True, verbose_name='CTA contable'),
        ),
    ]
