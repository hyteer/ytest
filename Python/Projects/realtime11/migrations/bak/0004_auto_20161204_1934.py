# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtime', '0003_auto_20161204_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='rooms',
        ),
    ]