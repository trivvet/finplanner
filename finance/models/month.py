# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Month(models.Model):
    class Meta:
        verbose_name = "month"
        verbose_name_plural = "months"

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Month Name"
    )

    balance = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Money Amount"
    )

    expenses_plan = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Amount of Planned Expenses"
    )

    expenses_done = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Amount of Done Expenses"
    )

    approved = models.NullBooleanField(
        blank=True,
        null=True,
        verbose_name="State of Affirmation")

    def __unicode__(self):
        if (self.approved):
            month = u"%s (Затверджений)" % self.name
        else:
            month = self.name
        return u"Бюджет за %s" % (month)