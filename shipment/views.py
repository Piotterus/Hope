from django.shortcuts import render

# Create your views here.
def listShipment(request):
    return render(request,'shipment/listShipment.html')
