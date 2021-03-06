# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-26 14:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Account Name')),
                ('money', models.IntegerField(blank=True, null=True, verbose_name='Amount of Money')),
                ('blocked', models.IntegerField(blank=True, null=True, verbose_name='Blocked Money')),
                ('kind', models.CharField(choices=[('cash', '\u0413\u043e\u0442\u0456\u0432\u043a\u0430'), ('bank', '\u0411\u0430\u043d\u043a')], max_length=100, verbose_name='Type of Account')),
            ],
            options={
                'verbose_name': ('Bank Account',),
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Month Name')),
                ('balance', models.IntegerField(default=0, verbose_name='Money Amount')),
                ('expenses_plan', models.IntegerField(default=0, verbose_name='Amount of Planned Expenses')),
                ('expenses_done', models.IntegerField(default=0, verbose_name='Amount of Done Expenses')),
                ('approved', models.NullBooleanField(verbose_name='State of Affirmation')),
            ],
            options={
                'verbose_name': 'month',
                'verbose_name_plural': 'months',
            },
        ),
        migrations.CreateModel(
            name='PlannedExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Money Amount')),
                ('remainder', models.IntegerField(blank=True, null=True, verbose_name='Money Remainder')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Month', verbose_name='Month')),
            ],
            options={
                'verbose_name': 'Planned Expense',
                'verbose_name_plural': 'Planned Expenses',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Money Amount')),
                ('remainder', models.IntegerField(blank=True, null=True, verbose_name='Money Remainder')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Account', verbose_name='Bank Account')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Month', verbose_name='Month')),
            ],
            options={
                'verbose_name': 'Belance',
                'verbose_name_plural': 'Belances',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_goal', models.CharField(blank=True, max_length=256, null=True, verbose_name='Transaction Goal Id')),
                ('score_goal_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Transaction Goal Name')),
                ('amount', models.IntegerField(verbose_name='Transaction Amount')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Transaction Time')),
                ('detail', models.CharField(blank=True, max_length=256, null=True, verbose_name='Detail Info')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Month', verbose_name='Month')),
                ('planned_expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='finance.PlannedExpense', verbose_name='Planned Expense')),
                ('score_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Score', verbose_name='Transaction Source')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
