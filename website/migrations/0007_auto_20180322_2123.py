# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-23 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180322_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell_phone',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='nro de celular'),
        ),
    ]
