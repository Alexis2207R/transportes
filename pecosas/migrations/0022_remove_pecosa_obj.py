# Generated by Django 4.1.1 on 2022-11-07 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pecosas', '0021_pecosa_obj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pecosa',
            name='obj',
        ),
    ]
