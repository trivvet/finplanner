# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from finance.models import Account

TYPE_OF_ACCOUNT = (
    ('cash', u"Готівка"),
    ('bank', u"Банк"),
)

def add_account(request):
    if request.method == "POST":
        form = AddAccount(request.POST)
        if form.is_valid():
            data = {}
            data['name'] = form.cleaned_data['name']
            data['kind'] = form.cleaned_data['kind']
            account = Account(**data)
            account.save()
            messages.success(request, u"Рахунок %s успішно доданий" % account.name)
    return HttpResponseRedirect(reverse("home"))

def delete_account(request, aid):
    if request.method == "POST":
        account = Account.objects.get(pk=aid)
        account.delete()
        messages.success(request, u"Рахунок %s (%s) успішно видалений" % 
            (account.name, account.kind))
    return HttpResponseRedirect(reverse("home"))

class AddAccount(forms.Form):
    name = forms.CharField(label=u"Назва рахунку", max_length=50)
    kind = forms.ChoiceField(label=u"Вид рахунку", choices=TYPE_OF_ACCOUNT)