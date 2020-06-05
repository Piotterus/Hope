from django.shortcuts import render, redirect
from .models import Client
from . import forms

# Create your views here.
def listClients(request):
    clients = Client.objects.all()

    return render(request,'clients/listClients.html', {'clients': clients})

def detailClient(request, id):
    client = Client.objects.get(id=id)

    return render(request,'clients/detailClient.html', {'client': client})


def createClient(request):
    if request.method == "POST":
        form = forms.CreateClient(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save()
            return redirect('clients:list')
    else:
        form = forms.CreateClient()
    return render(request,'clients/createClient.html',{'form': form})
