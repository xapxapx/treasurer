# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-13 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0027_auto_20190514_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='partner',
        ),
    ]
