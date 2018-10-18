# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from finance.models import (
    SavingTotal, 
    Saving,
    Account
    )

def savings_list(request):
    savings_total = SavingTotal.objects.all()
    accounts = Account.objects.all()
    savings = Saving.objects.all()
    print savings
    for account in accounts:
        account.savings = savings.filter(account=account)
    return render(request, 'finance/savings.html', 
        {'savings': savings_total, 'accounts': accounts})

def saving_total_add(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        saving = SavingTotal(title=title, total_amount=0)
        saving.save()
        messages.success(request, 
            u"Цільове збережння {} успішно додане").format(saving.title)       
    return HttpResponseRedirect(reverse("savings_list"))


def saving_add(request):
    if request.method == "POST":
        data = {}
        saving_total = request.POST.get("saving_total", "")
        data["saving_total"] = SavingTotal.objects.get(pk=saving_total)
        account = request.POST.get("account", "")
        data["account"] = Account.objects.get(pk=account)
        data['amount'] = request.POST.get("amount", 0)
        new_saving = Saving(**data)
        new_saving.save()
        messages.success(request,
            u"Гроші у сумі {} на {} успішно додано".format(
                new_saving.amount, new_saving.saving_total.title
                ))
        return HttpResponseRedirect(reverse("savings_list"))

def saving_delete(request, sid):
    return HttpResponseRedirect(reverse("savings_list"))