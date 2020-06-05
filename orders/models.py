from django.db import models
from clients.models import Client
from prizes.models import Prize
from django.contrib.auth.models import User


# Create your models here
class Order(models.Model):
    STAY = 'stay'
    SEND = 'send'
    WHAT_TO_DO_NEXT = [
        (STAY, 'Towar zostaje na magazynie'),
        (SEND, 'Wysyłka dalej'),
    ]
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    prize = models.ForeignKey(Prize, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dateCreate = models.DateTimeField(auto_now_add = True)
    amount = models.IntegerField()
    comment = models.TextField()
    plannedValue = models.DecimalField(max_digits = 10, decimal_places = 2)
    deadline = models.DateField()
    doNext = models.TextField(choices = WHAT_TO_DO_NEXT)
    onPlace = models.IntegerField(default = 0, null = True)

    def __str__(self):
        return "Klient:" + self.client.name + " Nagroda:" + self.prize.name + " Deadline:" + str(self.deadline)
