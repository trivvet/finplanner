# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from finance.models import Account, Month, PlannedExpense

def add_transaction(request, mid):
    # if request.method == "POST":
    #     form = AddTransaction(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         month = Month.objects.get(pk=mid)
    #         data['month'] = month
    #         expense = PlannedExpense(**data)
    #         expense.save()
    #         month.expenses_plan += data['amount']
    #         month.save()
    #         messages.success(request, u"Запланована витрата на %s успішно додана!" % expense.title)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

# def delete_planned_expense(request, mid, pid):
#     planned_expense = PlannedExpense.objects.get(pk=pid)
#     planned_expense.delete()
#     month = Month.objects.get(pk=mid)
#     month.expenses_plan -= planned_expense.amount
#     month.save()
#     messages.success(request, u"Запланована витрата на %s успішно видалена!" % planned_expense.title)
#     return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddTransaction(forms.Form, mid):
    accounts = Account.objects.all()
    account_choices = []
    for account in accounts:
        choice = (account.id, account.name)
        account_choices.append(choice)
    month = Month.objects.get(pk=mid)
    expenses = PlannedExpense.objects.filter(month=month)
    expense_choices = []
    for expense in expenses:
        choice = (expense.id, expense.title)
        expense_choices.append(choice)
    source = forms.ChoiceField(label=u"Рахунок", choices=account_choices)
    goal = forms.ChoiceField(label=u"Рахунок", choices=account_choices)
    expense = forms.ChoiceField(label=u"Витрата", choices=expense_choices)
    amount = forms.IntegerField(label=u"Розмір транзакції")