# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-03 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0018_auto_20190503_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emchilgee_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='onoshdahi_emchilgee',
            name='code',
        ),
        migrations.RemoveField(
            model_name='onoshdahi_emchilgee',
            name='name',
        ),
        migrations.AlterField(
            model_name='onoshdahi_emchilgee',
            name='emchilgee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.Emchilgee'),
        ),
        migrations.AddField(
            model_name='onoshdahi_emchilgee',
            name='emchilgee_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Emchilgee_list'),
        ),
    ]
