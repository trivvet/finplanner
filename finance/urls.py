from django.conf.urls import url
from django.contrib import admin

from finance import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    
    # Month URLS
    url(r'^month/(?P<mid>[0-9]+)/$', views.show_month, 
        name="show_month"),
    url(r'^month/(?P<mid>[0-9]+)/balance/$', views.show_balance, 
        name="show_balance"),
    url(r'^month/add/$', views.add_month, name="add_month"),
    url(r'^month/(?P<mid>[0-9]+)/delete/$', views.delete_month, 
        name="delete_month"),

    # Accoun URLS
    url(r'^account/add/$', views.add_account, name="add_account"),
    url(r'^account/(?P<aid>[0-9]+)/delete/$', 
        views.delete_account, name="delete_account"),
    url(r'^account/(?P<aid>[0-9]+)/detail/$',
        views.account_detail, name="account_detail"),

    # Saving URLS
    url(r'^saving/$', views.savings_list, name="savings_list"),
    url(r'^saving/total/add/$', views.saving_total_add, 
        name="saving_total_add"),
    url(r'^saving/add/$', views.saving_add, 
        name="saving_add"),
    url(r'^saving/(?P<sid>[0-9]+)/delete/$', views.saving_delete,
        name="saving_delete"),
    url(r'^saving/total/(?P<tid>[0-9]+)/delete/$', views.saving_total_delete,
        name="saving_total_delete"),

    # Score URLS
    url(r'^month/(?P<mid>[0-9]+)/score/add/$', views.add_score, 
        name="add_score"),
    url(r'^month/(?P<mid>[0-9]+)/score/(?P<sid>[0-9]+)/delete/$', 
        views.delete_score, name="delete_score"),

    # Expense URLS
    url(r'^month/(?P<mid>[0-9]+)/expense/add/$', 
        views.add_planned_expense, name="add_planned_expense"),
    url(r'^month/(?P<mid>[0-9]+)/expense/(?P<pid>[0-9]+)/delete/$', 
        views.delete_planned_expense, name="delete_planned_expense"),

    #Transaction URLS
    url(r'^transaction/month/(?P<mid>[0-9]+)/add/$', 
        views.add_transaction, name="add_transaction"),
    url(r'^transaction/(?P<tid>[0-9]+)/month/(?P<mid>[0-9]+)/delete/$', 
        views.delete_transaction, name="delete_transaction"),
    url(r'^transation/add/$', views.add_plus_transaction, 
        name="add_plus_transaction"),
    url(r'^transation/(?P<tid>[0-9]+)/delete/$', 
        views.delete_plus_transaction, 
        name="delete_plus_transaction")
]