# Generated by Django 4.2.4 on 2023-08-21 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_calendariomensal_jornada_diaria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargos',
            options={'ordering': ['id']},
        ),
    ]
