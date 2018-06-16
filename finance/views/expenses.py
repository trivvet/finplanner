# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from finance.models import Month, PlannedExpense

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
            messages.success(request, u"Запланована витрата на %s успішно додана!" % expense.title)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

def delete_planned_expense(request, mid, pid):
    planned_expense = PlannedExpense.objects.get(pk=pid)
    planned_expense.delete()
    month = Month.objects.get(pk=mid)
    month.expenses_plan -= planned_expense.amount
    month.save()
    messages.success(request, u"Запланована витрата на %s успішно видалена!" % planned_expense.title)
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddExpense(forms.Form):
    title = forms.CharField(label=u"Назва запланованої витрати", max_length=256)
    amount = forms.IntegerField(label=u"Розмір витрати", 
        widget=forms.NumberInput(attrs={'placeholder': u'Сума'}))