# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from finance.models import Month, Account, Score

def new_home(request):
    content = {}
    if request.GET.get('list', '') == 'budgets':
        content['months'] = Month.objects.exclude(approved=True)
        content['add_form'] = 'budgets'
    elif request.GET.get('list', '') == 'accounts':
        content['accounts'] = Account.objects.all()
    elif request.GET.get('list', '') == 'remnants':
        content['remnants'] = Score.objects.all()
    else:
        content['months'] = Month.objects.filter(approved=True)
    return render(request, 'finance/new_home.html', {'content': content})