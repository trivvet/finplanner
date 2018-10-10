# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import locale
from datetime import datetime

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from finance.models import (
    Account, 
    Month, 
    Score, 
    PlannedExpense, 
    Transaction, 
    TransactionToAccount
    )
from accounts import AddAccount
from .scores import AddScore
from .expenses import AddExpense
from .transactions import AddTransaction

# Create your views here.

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
        url = reverse("home") + "?list=budgets"
        return HttpResponseRedirect(url)
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
        date = request.POST.get("month_date", '')
        month = {}
        month_date = datetime.strptime(date, "%Y-%m")
        locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')
        month_name = unicode(month_date.strftime('%B'), 'utf8').capitalize()
        year = month_date.year
        month['name'] = "{} {}".format(month_name, year)
        month['date'] = month_date
        month = Month(**month)
        month.save()
        messages.success(request, 
            u"Бюджет за {} успішно доданий!".format(month.name))
    return HttpResponseRedirect(reverse("home"))

def delete_month(request, mid):
    month = Month.objects.get(pk=mid)
    month.delete()
    messages.success(request, 
        u"Бюджет на %s успішно видалений!" % month.name)
    return HttpResponseRedirect(reverse("home"))