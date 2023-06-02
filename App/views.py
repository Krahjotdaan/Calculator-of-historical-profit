from django.shortcuts import render
from App import models, forms

def exchange_rates(request):
    context = {}
    context['currencies_rates'] = models.CurrencyRate.get()
    context['precious_metals_rates'] = models.PreciousMetalRate.get()
    return render(request, "exchange_rates.html", context)


def converter(request):
    context = {}
    form = forms.ConverterForm()
    context['form'] = form
    return render(request, "converter.html", context)


def calculator(request):
    context = {}
    return render(request, "calculator.html", context)


def currency_reference(request):
    context = {}
    context['currencies'] = models.Currency.get()
    return render(request, "currency_reference.html", context)
