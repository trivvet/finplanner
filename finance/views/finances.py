# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def new_home(request):
    return render(request, 'finance/new_home.html', {})