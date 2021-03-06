# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-14 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0029_auto_20190514_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_resource',
            name='drug',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Drug'),
        ),
        migrations.AlterField(
            model_name='drug_resource',
            name='qty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordered_drug',
            name='qty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordered_staff',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
