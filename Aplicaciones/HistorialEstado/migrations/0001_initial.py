# Generated by Django 5.2 on 2025-06-30 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Denuncias', '0002_rename_ubicacion_denuncia_referencia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_anterior', models.CharField(max_length=50)),
                ('estado_nuevo', models.CharField(max_length=50)),
                ('fecha_cambio', models.DateTimeField(auto_now_add=True)),
                ('denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Denuncias.denuncia')),
            ],
        ),
    ]
