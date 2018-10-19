# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
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
    for account in accounts:
        account.savings = savings.filter(account=account)
    return render(request, 'finance/savings.html', 
        {'savings': savings_total, 'accounts': accounts, 
        'savings_p': savings})

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
        saving_total_id = request.POST.get("saving_total", "")
        saving_total = SavingTotal.objects.get(pk=saving_total_id)
        data["saving_total"] = saving_total
        account = request.POST.get("account", "")
        data["account"] = Account.objects.get(pk=account)
        amount = request.POST.get("amount", 0)
        try:
            saving_exist = Saving.objects.get(
                saving_total=data['saving_total'], account=data['account'])
        except ObjectDoesNotExist:
            data['amount'] = amount
            new_saving = Saving(**data)
            new_saving.save()
        else:
            saving_exist.amount += int(amount)
            saving_exist.save()

        saving_total.total_amount += int(amount)
        saving_total.save()

        messages.success(request,
            u"Гроші у сумі {} на {} успішно додано".format(
                amount, saving_total.title
                ))
        return HttpResponseRedirect(reverse("savings_list"))

def saving_delete(request, sid):
    saving = Saving.objects.get(pk=sid)
    saving.delete()
    messages.warning(request, u"Збереження успішно видалене")
    return HttpResponseRedirect(reverse("savings_list"))