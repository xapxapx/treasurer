# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-18 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20190418_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_nurse',
        ),
        migrations.AddField(
            model_name='user',
            name='is_worker',
            field=models.BooleanField(default=False, verbose_name='worker status'),
        ),
    ]
