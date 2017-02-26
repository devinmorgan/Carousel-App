# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_count', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carousel_order_index', models.IntegerField()),
                ('image_url', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='carousel_app.Carousel')),
            ],
        ),
    ]