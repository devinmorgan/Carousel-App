# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel_app', '0005_auto_20170226_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
