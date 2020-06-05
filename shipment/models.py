from django.db import models
from orders.models import Order

# Create your models here.
class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    dateCreate = models.DateTimeField(auto_now_add = True)
    firstname = models.TextField(null = True)
    lastname = models.TextField(null = True)
    name = models.TextField(null = True)
    street = models.TextField()
    postal = models.TextField()
    city = models.TextField()
