# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel_app', '0002_auto_20170226_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='date_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='auto_advance_timer',
            new_name='image_time_interval',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='date_created',
            new_name='created',
        ),
    ]