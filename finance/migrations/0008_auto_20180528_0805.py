# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_month_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_goal', models.CharField(blank=True, max_length=256, null=True, verbose_name='Transaction Goal')),
                ('amount', models.IntegerField(verbose_name='Transaction Amount')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Transaction Time')),
                ('detail', models.CharField(blank=True, max_length=256, null=True, verbose_name='Detail Info')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Month', verbose_name='Month')),
                ('planned_expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='finance.PlannedExpense', verbose_name='Planned Expense')),
                ('score_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Account', verbose_name='Transaction Source')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.RemoveField(
            model_name='expense',
            name='account',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='month',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='plan',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]