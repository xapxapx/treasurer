# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-24 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20190419_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='date',
        ),
    ]