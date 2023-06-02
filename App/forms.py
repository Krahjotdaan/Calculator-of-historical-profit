from django import forms


class ConverterForm(forms.Form):
    currency_a = forms.ChoiceField(label='Обменять', required=True)
    amount_a = forms.FloatField(required=True, widget=forms.NumberInput())
    currency_b = forms.ChoiceField(label='Получить', required=True)
    amount_b = forms.FloatField(required=True, widget=forms.NumberInput())


class ProfitCalculatorForm(forms.Form):
    pass
