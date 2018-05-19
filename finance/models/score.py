# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Score(models.Model):

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

    month = models.ForeignKey(
        'Month',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Month")

    amount = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Money Amount"
    )

    def __unicode__(self):
        return u"Залишок за %s по %s" % (self.month.name, self.account)