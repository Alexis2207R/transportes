# Generated by Django 4.1.1 on 2022-11-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecosas', '0020_remove_pecosa_codigo_pecosa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pecosa',
            name='obj',
            field=models.TextField(blank=True, null=True),
        ),
    ]
