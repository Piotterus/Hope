from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "orders"

urlpatterns = [
    path('list/', views.listOrders, name="list"),
    path('list/<int:id>/', views.detailOrder, name="detail"),
    path('create/', views.createOrder, name="create")
]
