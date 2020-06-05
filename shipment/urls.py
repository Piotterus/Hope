from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "shipment"

urlpatterns = [
    path('list/', views.listShipment, name="list"),
    path('list/', views.listShipment, name="create"),
]
