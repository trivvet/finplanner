# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from finance.models import Month, Account, Score

def home(request):
    content = {}
    if request.GET.get('list', '') == 'budgets':
        content['months'] = Month.objects.exclude(approved=True)
        content['add_form'] = 'budgets'
    elif request.GET.get('list', '') == 'accounts':
        content['accounts'] = Account.objects.all()
        content['add_form'] = 'accounts'
    elif request.GET.get('list', '') == 'remnants':
        content['remnants'] = Score.objects.all()
    else:
        content['months'] = Month.objects.filter(approved=True)
    return render(request, 'finance/home.html', 
        {'content': content})