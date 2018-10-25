# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from .account import Account
from .saving import Saving

class TransactionPrototype(models.Model):

    class Meta:
        abstract=True

    amount = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Transaction Amount"
    )

    date = models.DateTimeField(
        default=datetime.now,
        blank=False,
        null=False,
        verbose_name="Transaction Time")

    detail = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Detail Info"
    )


class AccountTransaction(TransactionPrototype):
    class Meta:
        verbose_name = "Account Transaction"
        verbose_name_plural = "Account Transactions"

    account = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Account"
    )

class TransactionToAccount(TransactionPrototype):
    class Meta:
        verbose_name = u"Plus-Transaction"
        verbose_name_plural = u"Plus-Transactions"

    account_goal = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Transaction Source"
    )

    transaction = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Transaction"
    )

    def __unicode__(self):
        return u"Додавання коштів на рахунок {}".format(self.account_goal.name)

class SavingTransaction(TransactionPrototype):
    class Meta:
        verbose_name = u"Saving Transaction"
        verbose_name_plural = u"Saving Transactions"

    saving = models.ForeignKey(
        'Saving',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Saving"
    )

    transaction = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Transaction"
    )

class Transaction(TransactionPrototype):
    class Meta:
        verbose_name = u"Transaction"
        verbose_name_plural = u"Transactions"

    model = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name="Model"
    )

    date = models.DateTimeField(
        default=datetime.now,
        blank=False,
        null=False,
        verbose_name="Transaction Time"
    )

    def __unicode__(self):
        if model == "Account":
            return u"Транзакція по рахунках від {}".format(self.date.date())
        elif model == "Saving":
            return u"Транзакція по збереженнях від {}".format(self.date.date())

    def get_elements(self):
        if model == "Account":
            return AccountTransaction.objects.filter(transaction=self)
        elif model == "Saving":
            return SavingTransaction.objects.filter(transaction=self)





