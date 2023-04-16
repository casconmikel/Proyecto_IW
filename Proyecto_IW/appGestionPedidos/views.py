from django.shortcuts import render 
from django.http import HttpResponse

def indexPedidos(request):
    return HttpResponse("Gestion Pedidos")

