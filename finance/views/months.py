# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.http import HttpResponse

from finance.models import Account, Month, Score, PlannedExpense
from .scores import AddScore

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
    return render(request, 'finance/month.html', 
        {'month': month, 'scores': scores, 'form': form, 
         'form_planned_expense': form_planned_expense, 'planned_expenses': expenses})

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

def delete_month(request, mid):
    month = Month.objects.get(pk=mid)
    month.delete()
    return HttpResponseRedirect(reverse("home"))

def add_planned_expense(request, mid):
    if request.method == "POST":
        form = AddExpense(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            month = Month.objects.get(pk=mid)
            data['month'] = month
            expense = PlannedExpense(**data)
            expense.save()
            month.expenses_plan += data['amount']
            month.save()
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

def delete_planned_expense(request, mid, pid):
    planned_expense = PlannedExpense.objects.get(pk=pid)
    planned_expense.delete()
    month = Month.objects.get(pk=mid)
    month.expenses_plan -= planned_expense.amount
    month.save()
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddExpense(forms.Form):
    title = forms.CharField(label=u"Назва запланованої витрати", max_length=256)
    amount = forms.IntegerField(label=u"Розмір витрати")

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