from django.shortcuts import render, redirect
from .models import Prize
from . import forms

# Create your views here.
def listPrizes(request):
    prizes = Prize.objects.all()
    return render(request,'prizes/listPrizes.html', {'prizes': prizes})

def detailPrize(request, id):
    prize = Prize.objects.get(id=id)

    return render(request,'prizes/detailPrizes.html', {'prize': prize})


def createPrize(request):
    if request.method == "POST":
        form = forms.CreatePrize(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save()
            return redirect('prizes:list')
    else:
        form = forms.CreatePrize()
    return render(request,'prizes/createPrizes.html',{'form': form})
