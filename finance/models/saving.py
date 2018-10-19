# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SavingTotal(models.Model):

    class Meta:
        verbose_name = "Total Saving"
        verbose_name_plural = "Total Savings"

    title = models.CharField(
        max_length = 256,
        blank=False,
        null=False,
        verbose_name="Title"
    )

    def __unicode__(self):
        return u"Загальні збереження по позиції {}".format(self.title)

    def get_total_amount(self):
        savings = Saving.objects.filter(saving_total=self)
        total = 0
        for saving in savings:
            total += saving.amount
        return total

class Saving(models.Model):
    class Meta:
        verbose_name = "Saving"
        verbose_name_plural = "Savings"

    saving_total = models.ForeignKey(
        'SavingTotal',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Total Saving"
    )

    account = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Account"
    )

    amount = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Money Amount"
    )

    def __unicode__(self):
        return u"Збереження по позиції {} на рахунку {}".format(
            self.saving_total.title, self.account.name)

