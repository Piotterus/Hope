from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "prizes"

urlpatterns = [
    path('list/', views.listPrizes, name="list"),
    path('list/<int:id>/', views.detailPrize, name="detail"),
    path('create/', views.createPrize, name="create")
]
