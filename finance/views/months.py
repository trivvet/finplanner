# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
# from django.http import HttpResponse

from finance.models import Account, Month, Score, PlannedExpense, Transaction
from accounts import AddAccount
from .scores import AddScore
from .expenses import AddExpense
from .transactions import AddTransaction

# Create your views here.

def home(request):
    content = {}
    content['months'] = Month.objects.all()
    content['accounts'] = Account.objects.all()
    content['scores'] = Score.objects.all()
    content['months_approved'] = content['months'].filter(approved=True)
    content['months_disapproved'] = content['months'].exclude(approved=True)
    form = AddMonth()
    form_account = AddAccount()
    return render(request, 'finance/home.html', 
        {'content': content, 'form': form, 'form_account': form_account})

def show_month(request, mid):
    month = Month.objects.get(pk=mid)
    scores = Score.objects.filter(month=month)
    planned_expenses = PlannedExpense.objects.filter(month=month)
    form = AddScore()
    form_planned_expense = AddExpense()
    form_transaction = AddTransaction()
    if request.method == "POST":
        month.approved = True
        month.save()
        messages.success(request, 
            u"Бюджет на %s затверджено!" % month.name)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, 'finance/month.html', 
            {'month': month, 'scores': scores, 'form': form, 
             'form_planned_expense': form_planned_expense, 
             'planned_expenses': planned_expenses})

def show_balance(request, mid):
    month = Month.objects.get(pk=mid)
    scores = Score.objects.filter(month=month)
    planned_expenses = PlannedExpense.objects.filter(month=month)
    transactions = Transaction.objects.filter(month=month).order_by('date')
    form_transaction = AddTransaction()
    for planned_expense in planned_expenses:
        expenses = Transaction.objects.filter(planned_expense=planned_expense)
        planned_expense.expenses = expenses
    return render(request, 'finance/month_balance.html', 
        {'month': month, 'scores': scores,  
         'planned_expenses': planned_expenses,
         'form_transaction': form_transaction, 
         'transactions': transactions})

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