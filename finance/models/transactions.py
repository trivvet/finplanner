# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Transaction Source"
    )

    score_goal = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Transaction Goal"
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

    detail = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Detail Info"
    )

    def __unicode__(self):
        if self.planned_expense:
            return u"Витрати на %s за %s" % (self.planned_expense, self.month.name)
        elif self.score_goal:
            return u"Переказ з рахунку %s на рахунок %s за %s" % (self.score_source, self.score_goal, self.month.name)