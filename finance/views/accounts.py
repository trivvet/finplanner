# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from finance.models import (
    Account, 
    AccountTransaction, 
    Score, 
    SavingTotal,
    Saving
    )

def account_detail(request, aid):
    account = Account.objects.get(pk=aid)
    transactions = AccountTransaction.objects.filter(account=account)
    remnants = Score.objects.filter(account=account)
    return render(request, "finance/account_detail.html", 
        {"account": account, "transactions": transactions,
            "remnants": remnants})

def add_account(request):
    if request.method == "POST":
        form = AddAccount(request.POST)
        if form.is_valid():
            data = {}
            data['name'] = form.cleaned_data['name']
            data['kind'] = form.cleaned_data['kind']
            account = Account(**data)
            account.save()
            savings = SavingTotal.objects.all()
            for saving in savings:
                data = {}
                data['saving_total'] = saving
                data['account'] = account
                new_saving = Saving(**data)
                new_saving.save()
            messages.success(request, 
                u"Рахунок %s успішно доданий" % account.name)
    url = reverse("home") + "?list=accounts"
    return HttpResponseRedirect(url)

def delete_account(request, aid):
    if request.method == "POST":
        account = Account.objects.get(pk=aid)
        account.delete()
        messages.success(request, u"Рахунок %s (%s) успішно видалений" % 
            (account.name, account.kind))
    url = reverse("home") + "?list=accounts"
    return HttpResponseRedirect(url)

class AddAccount(forms.Form):
    name = forms.CharField(label=u"Назва рахунку", max_length=50)
    kind = forms.ChoiceField(label=u"Вид рахунку", 
        choices=Account.TYPE_OF_ACCOUNT)