# Generated by Django 4.1.1 on 2022-09-22 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RotoARG', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='estado',
        ),
    ]
