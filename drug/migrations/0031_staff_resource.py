# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-14 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0030_auto_20190514_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('last_transaction', models.DateField(default=django.utils.timezone.now)),
                ('staff', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Drug')),
            ],
        ),
    ]
