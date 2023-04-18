from django.shortcuts import render 
from django.http import HttpResponse

#___________________VISUALIZAR LISTA____________________

def indexPedidos(request):
    return HttpResponse("VISUALIZACIÓN PEDIDOS") #En "hola guapas" deberiamos poner el link a la pagina html

def indexCliente(request):
    return HttpResponse("VISUALIZACIÓN CLIENTES")

def indexProducto(request):
    return HttpResponse("VISUALIZACIÓN CLEINTES")

def indexComponente(request):
    return HttpResponse("VISUALIZACIÓN CLEINTES")



