from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido
from .forms import ClienteFrom, ComponenteForm, ProductoFrom, PedidoFrom, ProductoPedidoFrom


#___________________ VISUALIZAR LISTA ____________________

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

#____________________ CREAR ____________________

class ClienteCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = ClienteFrom()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/cliente_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ClienteForm(request.POST) #NOS DA PROBLEMA, LO PILLA, NO SABEMOS PORQUE, REVISAR!!!
        if formulario.is_valid(): 
            formulario.save()
            return redirect('appGestionPedidos/cliente_create.html')
        return render(request, 'appGestionPedidos/cliente_create.html', {'formulario': formulario})








