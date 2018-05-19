# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.http import HttpResponse

from finance.models import Account, Month, Score

# Create your views here.

TYPE_OF_ACCOUNT = (
    ('cash', u"Готівка"),
    ('bank', u"Банк"),
)

def home(request):
    content = {}
    content['months'] = Month.objects.all()
    content['accounts'] = Account.objects.all()
    form = AddMonth()
    form_account = AddAccount()
    return render(request, 'finance/home.html', 
        {'content': content, 'form': form, 'form_account': form_account})

def add_month(request):
    if request.method == "POST":
        form = AddMonth(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            month = Month(name=name)
            month.save()
    return HttpResponseRedirect(reverse("home"))

class AddMonth(forms.Form):
    name = forms.CharField(label="", max_length=50)

def show_month(request, mid):
    month = Month.objects.get(pk=mid)
    scores = Score.objects.all()
    form = AddScore()
    return render(request, 'finance/month.html', {'month': month, 'scores': scores, 'form': form})

def add_score(request, mid):
    if request.method == "POST":
        form = AddScore(request.POST)
        if form.is_valid():
            data = {}
            data['account'] = Account.objects.get(pk=form.cleaned_data['account'])
            data['month'] = Month.objects.get(pk=mid)
            data['amount'] = form.cleaned_data['amount']
            score = Score(**data)
            score.save()
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddScore(forms.Form):
    accounts = Account.objects.all()
    account_choices = []
    for account in accounts:
        choice = (account.id, account.name)
        account_choices.append(choice)
    account = forms.ChoiceField(label=u"Рахунок", choices=account_choices)
    amount = forms.IntegerField(label=u"Залишок")

def add_account(request):
    if request.method == "POST":
        form = AddAccount(request.POST)
        if form.is_valid():
            data = {}
            data['name'] = form.cleaned_data['name']
            data['kind'] = form.cleaned_data['kind']
            month = Account(**data)
            month.save()
    return HttpResponseRedirect(reverse("home"))

class AddAccount(forms.Form):
    name = forms.CharField(label=u"Назва рахунку", max_length=50)
    kind = forms.ChoiceField(label=u"Вид рахунку", choices=TYPE_OF_ACCOUNT)