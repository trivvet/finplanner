"""finplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from finance import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    url(r'^month/add/$', views.add_month, name="add_month"),
    url(r'^month/(?P<mid>[0-9]+)/$', views.show_month, name="show_month"),
    url(r'^month/(?P<mid>[0-9]+)/score/add/$', views.add_score, name="add_score"),

    url(r'^account/add/$', views.add_account, name="add_account"),
]
