# Generated by Django 3.1.7 on 2021-04-03 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proformaApp', '0007_auto_20210403_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proforma',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='proforma_detalle',
            options={'ordering': ['proforma']},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['id']},
        ),
    ]
