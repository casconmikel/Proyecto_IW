from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Cliente, Pedido, Producto, Componente, ProductoPedido
from django.views import View
from django.views.generic import DetailView, ListView
# from appGestionPedidos.forms import DepartamentoForm, EmpleadoForm #Todavia no hemos llegado, parte del formulario


#___________________VISUALIZAR LISTA____________________

class ClienteListView(ListView):
    model = Cliente

class PedidoListView(ListView):
    model = Pedido

class ProductoListView(ListView):
    model = Producto

class ComponenteListView(ListView):
    model = Componente

class ProductoPedidoDetailView(DetailView):
    model = ProductoPedido



