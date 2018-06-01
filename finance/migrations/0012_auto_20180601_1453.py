# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_auto_20180528_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannedexpense',
            name='remainder',
            field=models.IntegerField(blank=True, null=True, verbose_name='Money Remainder'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='score_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Score', verbose_name='Transaction Source'),
        ),
    ]
