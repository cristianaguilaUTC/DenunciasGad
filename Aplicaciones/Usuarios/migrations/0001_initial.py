# Generated by Django 5.2 on 2025-06-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
                ('tipo_usuario', models.CharField(max_length=50)),
                ('anonimo', models.BooleanField(default=False)),
            ],
        ),
    ]
