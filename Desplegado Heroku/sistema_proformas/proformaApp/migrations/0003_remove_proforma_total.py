# Generated by Django 3.1.7 on 2021-04-03 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proformaApp', '0002_auto_20210328_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proforma',
            name='total',
        ),
    ]
