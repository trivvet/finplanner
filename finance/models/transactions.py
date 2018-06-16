# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Transaction(models.Model):
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
    
    month = models.ForeignKey(
        'Month',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Month"
    )

    score_source = models.ForeignKey(
        'Score',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Transaction Source"
    )

    score_goal = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Transaction Goal Id"
    )

    score_goal_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Transaction Goal Name"
    )

    planned_expense = models.ForeignKey(
        'PlannedExpense',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Planned Expense"
    )

    amount = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Transaction Amount"
    )

    date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True,
        verbose_name="Transaction Time")

    detail = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Detail Info"
    )

    def __unicode__(self):
        if self.planned_expense:
            return u"Витрати на %s" % (self.planned_expense.title)
        elif self.score_goal_name:
            return u"Переказ з рахунку %s на рахунок %s" % (self.score_source.account.name, self.score_goal_name)
        elif self.score_goal:
            return u"Переказ з рахунку %s на інший рахунок" % (self.score_source.account.name)