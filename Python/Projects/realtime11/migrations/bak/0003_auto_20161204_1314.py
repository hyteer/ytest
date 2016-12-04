# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtime', '0002_room_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ManyToManyField(to='realtime.Room'),
        ),
    ]
