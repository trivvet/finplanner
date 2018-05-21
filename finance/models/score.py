# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ScorePrototype(models.Model):

    class Meta:
        abstract=True

    month = models.ForeignKey(
        'Month',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Month"
    )

    amount = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Money Amount"
    )


class Score(ScorePrototype):

    class Meta:
        verbose_name = "Belance"
        verbose_name_plural = "Belances"

    account = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Bank Account"
    )

    def __unicode__(self):
        return u"Залишок за %s по %s" % (self.month.name, self.account)


class PlannedExpense(ScorePrototype):

    class Meta:
        verbose_name = "Planned Expense"
        verbose_name_plural = "Planned Expenses"

    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name="Title"
    )

    def __unicode__(self):
        return u"Заплановані витрати на %s за %s" % (self.title, self.month.name)


class Expense(ScorePrototype):

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    account = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Bank Account"
    )

    plan = models.ForeignKey(
        'PlannedExpense',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Planned Expense"
    )

    detail = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Detail Info"
    )

    def __unicode__(self):
        if self.plan:
            return u"Витрати по %s за %s" % (self.plan, self.account)
        else:
            return u"Витрати за %s" % (self.month.name)