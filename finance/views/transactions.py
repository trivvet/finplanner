# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import sys  

# reload(sys)  
# sys.setdefaultencoding('utf8')

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from finance.models import Account, Month, PlannedExpense, Transaction, Score, TransactionToAccount

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
            score_goal_id = post_data.get('score_goal', '')
            if score_goal_id:
                score_goal = Score.objects.get(pk=score_goal_id)
                data['score_goal'] = str(score_goal.id)
                data['score_goal_name'] = score_goal.account.name
                transaction = Transaction(**data)
                transaction.save()
                score_source.remainder -= data['amount']
                score_source.save()
                score_goal.remainder += data['amount']
                score_goal.save()
                messages.success(request, u"Переказ успішно доданий!")
            elif post_data.get('planned_expense', ''):
                planned_expense = PlannedExpense.objects.get(pk=post_data.get('planned_expense', ''))
                data['planned_expense'] = planned_expense
                transaction = Transaction(**data)
                transaction.save()
                change_accounts(transaction, planned_expense, month, 
                    score_source, True)
                messages.success(request, u"Витрата успішно додана!")
    return HttpResponseRedirect(reverse("show_balance", kwargs={'mid': mid}))

def delete_transaction(request, mid, tid):
    transaction = Transaction.objects.get(pk=tid)
    transaction.delete()
    month = Month.objects.get(pk=mid)
    score_source = Score.objects.get(pk=transaction.score_source.id)
    if transaction.planned_expense:
        planned_expense = PlannedExpense.objects.get(pk=transaction.planned_expense.id)
        change_accounts(transaction, planned_expense, month, score_source, False)
    elif transaction.score_goal:
        score_goal = Score.objects.get(pk=transaction.score_goal)
        score_source.remainder += transaction.amount
        score_goal.remainder -= transaction.amount
        score_goal.save()
        score_source.save()
    messages.success(request, u"Транзакція успішно видалена!")
    return HttpResponseRedirect(reverse("show_balance", kwargs={'mid': mid}))

def add_plus_transaction(request):
    if request.method == "POST":
        data = {}
        account_id = request.POST.get('score_source')
        data['account_goal'] = Account.objects.get(pk=account_id)
        data['date'] = request.POST.get('date')
        data['amount'] = request.POST.get('money')
        transaction = TransactionToAccount(**data)
        transaction.save()
        account = data['account_goal']
        if account.money:
            account.money += transaction.amount
        else:
            account.money = transaction.amount
        account.save()
    messages.success(request, u"Гроші на рахунок успішно зараховано!")
    return HttpResponseRedirect(reverse("home"))

class AddTransaction(forms.Form):
    date = forms.DateField(label=u"Дата", initial=timezone.now().strftime("%Y-%m-%d"))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': u"Сума"}))
    detail = forms.CharField(label=u"Деталі", required=False,
      widget=forms.TextInput(attrs={'placeholder': u"Деталі"}))

def change_accounts(transaction, expense, month, score, add):
    if add:
        if not expense.remainder:
            expense.remainder = expense.amount
        expense.remainder -= transaction.amount
        month.balance -= transaction.amount
        score.remainder -= transaction.amount
    else:
        expense.remainder += transaction.amount
        month.balance += transaction.amount
        score.remainder += transaction.amount
    expense.save()
    month.save()
    score.save()
