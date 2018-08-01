# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from finance.models import Account, Month, Score

# Create your views here.

TYPE_OF_ACCOUNT = (
    ('cash', u"Готівка"),
    ('bank', u"Банк"),
)

def add_score(request, mid):
    if request.method == "POST":
        form = AddScore(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            month = Month.objects.get(pk=mid)
            account = Account.objects.get(pk=form.cleaned_data['account'])
            amount = form.cleaned_data['amount']
            data['account'] = account
            data['month'] = month
            data['amount'] = amount
            data['remainder'] = form.cleaned_data['amount']
            score = Score(**data)
            score.save()
            month.balance += amount
            month.save()
            if account.blocked:
                account.blocked += amount
            else:
                account.blocked = amount
            account.save()
            messages.success(request, u"Надходження на %s успішно додане!" % score.account.name)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

def delete_score(request, mid, sid):
    score = Score.objects.get(pk=sid)
    score.delete()
    month = Month.objects.get(pk=mid)
    month.balance -= score.amount
    month.save()
    account = score.account
    account.blocked -= score.amount
    account.save()
    messages.success(request, u"Надходження на %s успішно видалене!" % score.account.name)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddScore(forms.Form):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        account_choices = []
        for account in Account.objects.all():
            choice = (account.id, account.remainder())
            account_choices.append(choice)
        self.fields['account'].choices = account_choices

    account = forms.ChoiceField(label=u"Рахунок")
    amount = forms.IntegerField(label=u"Залишок")