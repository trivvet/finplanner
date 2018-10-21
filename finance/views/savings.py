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
    total = 0
    for account in accounts:
        total += account.get_total_saving_amount()
    return render(request, 'finance/savings.html', 
        {'savings': savings_total, 'accounts': accounts, 
        'savings_p': savings, 'total_saving': total})

def saving_total_add(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        saving = SavingTotal(title=title)
        saving.save()
        accounts = Account.objects.all()
        for account in accounts:
            data = {}
            data["saving_total"] = saving
            data["account"] = account
            saving_account = Saving(**data)
            saving_account.save()
        messages.success(request, 
            u"Цільове збережння {} успішно додане".format(saving.title))       
    return HttpResponseRedirect(reverse("savings_list"))


def saving_add(request, sid):
    if request.method == "POST":
        saving = Saving.objects.get(pk=sid)
        amount = request.POST.get("amount", 0)
        saving.amount += int(amount)
        saving.save()

        messages.success(request,
            u"Гроші у сумі {} на {} успішно додано".format(
                amount, saving.saving_total.title
                ))
        return HttpResponseRedirect(reverse("savings_list"))

def saving_total_delete(request, tid):
    saving_total = SavingTotal.objects.get(pk=tid)
    saving_total.delete()
    messages.warning(request, u"Збереження успішно видалене")
    return HttpResponseRedirect(reverse("savings_list"))