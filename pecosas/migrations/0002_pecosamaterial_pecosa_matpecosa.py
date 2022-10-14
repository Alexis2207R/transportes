# Generated by Django 4.1.1 on 2022-10-12 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0003_remove_categoria_descripcion_categoria_and_more'),
        ('pecosas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PecosaMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.material')),
                ('pecosa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pecosas.pecosa')),
            ],
        ),
        migrations.AddField(
            model_name='pecosa',
            name='matpecosa',
            field=models.ManyToManyField(through='pecosas.PecosaMaterial', to='materiales.material'),
        ),
    ]