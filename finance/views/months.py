# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.http import HttpResponse

from finance.models import Account, Month, Score, PlannedExpense
from .scores import AddScore
from .expenses import AddExpense
from .transactions import AddTransaction

# Create your views here.

TYPE_OF_ACCOUNT = (
    ('cash', u"Готівка"),
    ('bank', u"Банк"),
)

def home(request):
    content = {}
    content['months'] = Month.objects.all()
    content['accounts'] = Account.objects.all()
    content['scores'] = Score.objects.all()
    form = AddMonth()
    form_account = AddAccount()
    return render(request, 'finance/home.html', 
        {'content': content, 'form': form, 'form_account': form_account})

def show_month(request, mid):
    month = Month.objects.get(pk=mid)
    scores = Score.objects.filter(month=month)
    expenses = PlannedExpense.objects.filter(month=month)
    form = AddScore()
    form_planned_expense = AddExpense()
    form_transaction = AddTransaction(mid)
    if request.method == "POST":
        month.approved = True
        month.save()
        messages.success(request, u"Бюджет на %s затверджено!" % month.name)
    return render(request, 'finance/month.html', 
        {'month': month, 'scores': scores, 'form': form, 
         'form_planned_expense': form_planned_expense, 'planned_expenses': expenses,
         'form_transaction': form_transaction})

def add_month(request):
    if request.method == "POST":
        form = AddMonth(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            month = Month(name=name)
            month.save()
            messages.success(request, u"Бюджет на %s успішно доданий!" % month.name)
    return HttpResponseRedirect(reverse("home"))

class AddMonth(forms.Form):
    name = forms.CharField(label="", max_length=50)

def delete_month(request, mid):
    month = Month.objects.get(pk=mid)
    month.delete()
    messages.success(request, u"Бюджет на %s успішно видалений!" % month.name)
    return HttpResponseRedirect(reverse("home"))

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

class AddAccount(forms.Form):
    name = forms.CharField(label=u"Назва рахунку", max_length=50)
    kind = forms.ChoiceField(label=u"Вид рахунку", choices=TYPE_OF_ACCOUNT)