# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .saving import Saving

# Create your models here.

class Account(models.Model):
    TYPE_OF_ACCOUNT = (
        ('cash', u"Готівка"),
        ('bank', u"Банк"),
    )

    class Meta:
        verbose_name = "Bank Account",
        verbose_name_plural = "Bank Accounts"

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Account Name"
    )

    money = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Amount of Money"
    )

    blocked = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Blocked Money"
    )

    kind = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=TYPE_OF_ACCOUNT,
        verbose_name="Type of Account"
    )

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.kind)

    def remainder(self):
        if self.blocked:
            answer = "{} ({})".format(self.name, self.money - self.blocked)
        else:
            answer = "{} ({})".format(self.name, self.money)
        return answer

    def get_savings(self):
        return Saving.objects.filter(account=self)

    def get_total_saving_amount(self):
        savings = self.get_savings()
        total = 0
        for saving in savings:
            total += saving.amount
        return total

    def get_saving_remainder(self):
        return self.money - self.get_total_saving_amount()


