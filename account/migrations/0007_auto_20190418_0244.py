# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-18 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_worker_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
