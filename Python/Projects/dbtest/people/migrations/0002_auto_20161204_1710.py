# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='person',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]