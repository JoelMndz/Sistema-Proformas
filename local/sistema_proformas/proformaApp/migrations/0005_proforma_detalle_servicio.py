# Generated by Django 3.1.7 on 2021-04-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proformaApp', '0004_proforma_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='proforma_detalle',
            name='servicio',
            field=models.ManyToManyField(to='proformaApp.Servicio'),
        ),
    ]
