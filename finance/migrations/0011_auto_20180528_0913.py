# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_auto_20180528_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='data',
            new_name='date',
        ),
    ]
