# Generated by Django 3.1.7 on 2021-04-03 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proformaApp', '0010_remove_proforma_detalle_total_linea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proforma',
            name='iva',
        ),
        migrations.RemoveField(
            model_name='proforma',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='proforma',
            name='total',
        ),
    ]
