# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-28 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20181028_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='model_id',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Model Id'),
        ),
    ]
