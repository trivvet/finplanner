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
            data['account'] = Account.objects.get(pk=form.cleaned_data['account'])
            data['month'] = month
            data['amount'] = form.cleaned_data['amount']
            data['remainder'] = form.cleaned_data['amount']
            score = Score(**data)
            score.save()
            month.balance += data['amount']
            month.save()
            messages.success(request, u"Надходження на %s успішно додане!" % score.account.name)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

def delete_score(request, mid, sid):
    score = Score.objects.get(pk=sid)
    score.delete()
    month = Month.objects.get(pk=mid)
    month.balance -= score.amount
    month.save()
    messages.success(request, u"Надходження на %s успішно видалене!" % score.account.name)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddScore(forms.Form):
    accounts = Account.objects.all()
    account_choices = []
    try:
        accounts
    except ProgrammingError:
        accounts = []
    else:
        for account in accounts:
            choice = (account.id, account.name)
            account_choices.append(choice)
    account = forms.ChoiceField(label=u"Рахунок", choices=account_choices)
    amount = forms.IntegerField(label=u"Залишок")