# Generated by Django 3.1.7 on 2021-04-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proformaApp', '0009_auto_20210403_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proforma_detalle',
            name='total_linea',
        ),
    ]
