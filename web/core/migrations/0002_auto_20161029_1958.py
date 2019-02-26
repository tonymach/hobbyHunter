# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 23:58
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_interests',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_reviews',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_classKeys',
            field=jsonfield.fields.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_previouslyTaken',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=200), blank=True, null=True, size=None),
        ),
    ]
