# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tls', '0003_auto_20161201_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Time'),
        ),
    ]