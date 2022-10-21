# Generated by Django 4.0.6 on 2022-10-18 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0007_material_nombre_material'),
        ('pecosas', '0008_alter_pecosa_codigo_pecosa_alter_pecosa_solicitante'),
    ]

    operations = [
        migrations.CreateModel(
            name='MermaMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_merma', models.IntegerField(default=1)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.material')),
                ('merma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecosas.merma')),
            ],
        ),
        migrations.CreateModel(
            name='EntradaMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_entrada', models.IntegerField(default=1)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecosas.entrada')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.material')),
            ],
        ),
    ]