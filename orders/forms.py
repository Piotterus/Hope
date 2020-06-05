from django import forms
from . import models
from clients.models import Client
from prizes.models import Prize
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateOrder(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ['onPlace', 'account']
        widgets = {
            'deadline': DateInput(),
        }

class CreateOrderNew(forms.Form):
    STAY = 'stay'
    SEND = 'send'
    WHAT_TO_DO_NEXT = [
        (STAY, 'Towar zostaje na magazynie'),
        (SEND, 'Wysyłka dalej'),
    ]
    id_client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label="Nowy", required=False, label="Wybierz klienta")
    new_client = forms.CharField(required=False, label="Nowy klient")
    id_prize = forms.ModelChoiceField(queryset=Prize.objects.all(), empty_label="Nowy", required=False, label="Wybierz nagrodę")
    new_prize = forms.CharField(required=False, label="Nowa nagroda")
    amount = forms.IntegerField(label="Ilość")
    comment = forms.CharField(label="Komentarz")
    plannedValue = forms.DecimalField(max_digits = 10, decimal_places = 2, label="Planowana wartość")
    deadline = forms.DateField(widget = DateInput(), label="DeadLine")
    doNext = forms.ChoiceField(choices = WHAT_TO_DO_NEXT, label="Co dalej z nagrodą")
