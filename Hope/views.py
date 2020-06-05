from django.http import HttpResponse
from django.shortcuts import render
from clients.models import Client
from orders.models import Order
from prizes.models import Prize

def homepage(request):
    prizeCount = Prize.objects.all().count()
    orderCount = Order.objects.all().count()
    clientCount = Client.objects.all().count()

    return render(request,'homepage.html', {'prizeCount': prizeCount, 'orderCount': orderCount, 'clientCount': clientCount})
    #return HttpResponse('homepage')

def about(request):
    return render(request,'about.html')
    #return HttpResponse('about')
