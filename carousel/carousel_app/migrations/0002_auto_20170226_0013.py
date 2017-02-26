# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='image_count',
        ),
        migrations.RemoveField(
            model_name='image',
            name='carousel_order_index',
        ),
        migrations.AddField(
            model_name='carousel',
            name='auto_advance_timer',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='image',
            name='carousel_position_index',
            field=models.IntegerField(default=-1),
        ),
    ]