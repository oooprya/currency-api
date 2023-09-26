from django.shortcuts import render
from django.http import Http404
from .models import Currency



def index(request):
    currency_all = Currency.objects.all()
    return render(request, 'currency/currency.html', {'currency_all': currency_all} )

def single_exchanger(request, exchanger_id):
    try:
        exchanger = Currency.objects.get(pk=exchanger_id)
        return render(request, 'currency/single_exchanger.html', {'exchanger': exchanger})
    except Currency.DoesNotExist:
        return render(request, 'currency/http404.html')