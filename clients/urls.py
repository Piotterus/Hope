from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "clients"

urlpatterns = [
    path('list/', views.listClients, name="list"),
    path('list/<int:id>/', views.detailClient, name="detail"),
    path('create/', views.createClient, name="create")
]
