from django.shortcuts import render, redirect
from .models import Order
from . import forms

# Create your views here.
def listOrders(request):
    orders = Order.objects.all().order_by('dateCreate')
    for order in orders:
        order.deadline = str(order.deadline)


    return render(request,'orders/listOrders.html', {'orders': orders})

def detailOrder(request, id):
    order = Order.objects.get(id=id)

    return render(request,'orders/detailOrder.html', {'order': order})


def createOrder(request):
    if request.method == "POST":
        form = forms.CreateOrderNew(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.account = request.user
            instance.save()
            return redirect('orders:list')
    else:
        form = forms.CreateOrderNew()
    return render(request,'orders/createOrder.html',{'form': form})
