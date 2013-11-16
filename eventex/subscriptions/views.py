# coding: utf-8

from django.shortcuts import render

def subscribe(resquest):
    return render(resquest, 'subscriptions/subscriptions_form.html')
