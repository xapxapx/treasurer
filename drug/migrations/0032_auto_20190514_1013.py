# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-14 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0031_staff_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_resource',
            name='staff',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Other_staff'),
        ),
    ]
