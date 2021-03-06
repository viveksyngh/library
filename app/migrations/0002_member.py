# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-17 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
