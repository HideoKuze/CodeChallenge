# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convoapp', '0008_auto_20180217_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputinfo',
            name='conversation_id',
            field=models.CharField(max_length=4),
        ),
    ]
