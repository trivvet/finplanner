# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import sys  

# reload(sys)  
# sys.setdefaultencoding('utf8')

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from finance.models import Account, Month, PlannedExpense, Transaction, Score

def add_transaction(request, mid):
    if request.method == "POST":
        post_data = request.POST
        form = AddTransaction(post_data)
        month = Month.objects.get(pk=mid)
        if form.is_valid():
            data = form.cleaned_data
            score_source = Score.objects.get(pk=post_data.get('score_source', ''))
            data['score_source'] = score_source
            data['month'] = month
            if post_data.get('score_goal', ''):
                score_goal = Score.objects.get(pk=post_data.get('score_goal', ''))
                data['score_goal'] = str(score_goal.id)
                transaction = Transaction(**data)
                transaction.save()
                score_source.amount -= data['amount']
                score_source.save()
                score_goal.amount += data['amount']
                score_goal.save()
                messages.success(request, u"Переказ успішно доданий!")
            elif post_data.get('planned_expense', ''):
                planned_expense = PlannedExpense.objects.get(pk=post_data.get('planned_expense', ''))
                data['planned_expense'] = planned_expense
                transaction = Transaction(**data)
                transaction.save()
                messages.success(request, u"Витрата успішно додана!")
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

def delete_transaction(request, mid, tid):
    transaction = Transaction.objects.get(pk=tid)
    transaction.delete()
    messages.success(request, u"Транзакція успішно видалена!")
    return HttpResponseRedirect(reverse("show_month", kwargs={'mid': mid}))

class AddTransaction(forms.Form):
    amount = forms.IntegerField(label=u"Розмір транзакції")
    detail = forms.CharField(label=u"Деталі", required=False)