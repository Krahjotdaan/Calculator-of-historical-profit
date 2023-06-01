from django import forms


class ConverterForm(forms.Form):
    currency_a = forms.Select(label='Обменять', required=True)
    amount_a = forms.FloatField(required=True, widget=forms.NumberInput())
    currency_a = forms.Select(label='Получить', required=True)
    amount_b = forms.FloatField(disabled=True)


class ProfitCalculatorForm(forms.Form):
    pass
