# Generated by Django 3.2 on 2021-05-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_alter_filter_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='oil_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name="Quantita' Olio"),
        ),
    ]