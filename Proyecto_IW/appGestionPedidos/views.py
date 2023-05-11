from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido, Categoria
from .forms import ClienteForm, ComponenteForm, ProductoForm, PedidoForm, ProductoPedidoForm
from django.core.paginator import Paginator
from django.shortcuts import render



#___________________ VISUALIZAR LISTA ____________________

class ClienteListView(ListView):
    model = Cliente
    paginate_by = 1

class PedidoListView(ListView):
    model = Pedido
    paginate_by = 1

class CategoriaListView(ListView):
    model = Categoria
    
class ProductoListView(ListView):
    model = Producto
    paginate_by = 1

class ComponenteListView(ListView):
    model = Componente
    paginate_by = 1

class ProductoPedidoDetailView(DetailView):
    model = Pedido

#____________________ CREAR ____________________

class ClienteCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = ClienteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/cliente_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ClienteForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('index')
        return render(request, 'appGestionPedidos/cliente_create.html', {'formulario': formulario})
    




class ComponenteCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = ComponenteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/componente_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ComponenteForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('componente')
        return render(request, 'appGestionPedidos/componente_create.html', {'formulario': formulario})

class ProductoCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = ProductoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/producto_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ProductoForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('producto')
        return render(request, 'appGestionPedidos/producto_create.html', {'formulario': formulario})


class PedidoCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = PedidoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/pedido_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = PedidoForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('pedido')
        return render(request, 'appGestionPedidos/pedido_create.html', {'formulario': formulario})
    
class ProductoPedidoCreateView(View):

    def get(self, request, *args, **kwargs):
        formulario = ProductoPedidoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appGestionPedidos/productoPedido_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ProductoPedidoForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('pedido')
        return render(request, 'appGestionPedidos/productoPedido_create.html', {'formulario': formulario})

#___________________ ELIMINAR ___________________

def cliente_delete(request, id):
      cliente = get_object_or_404(Cliente, id=id)
      cliente.delete()
      return redirect('index')

def componente_delete(request, id):
      componente = get_object_or_404(Componente, id=id)
      componente.delete()
      return redirect('componente')

def producto_delete(request, id):
      producto = get_object_or_404(Producto, id=id)
      producto.delete()
      return redirect('producto')

def pedido_delete(request, id):
      pedido = get_object_or_404(Pedido, id=id)
      pedido.delete()
      return redirect('pedido')
def productoPedido_delete(request, id):
      productoPedido = get_object_or_404(ProductoPedido, id=id)
      productoPedido.delete()
      return redirect('pedido')
     

#___________________ MODIFICAR ___________________


def cliente_modify(request, id): 

    cliente = get_object_or_404(Cliente, id=id)

    data = {
            'formulario': ClienteForm(instance=cliente)
        } 
        
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("index")
        data["formulario"] = formulario 

    return render(request, 'appGestionPedidos/cliente_modify.html', data)

def componente_modify(request, id): 

    componente = get_object_or_404(Componente, id=id)

    data = {
            'formulario': ComponenteForm(instance=componente)
        } 
        
    if request.method == 'POST':
        formulario = ComponenteForm(data=request.POST, instance=componente, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("componente")
        data["formulario"] = formulario 

    return render(request, 'appGestionPedidos/componente_modify.html', data)

def producto_modify(request, id): 

    producto = get_object_or_404(Producto, id=id)

    data = {
            'formulario': ProductoForm(instance=producto)
        } 
        
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("producto")
        data["formulario"] = formulario 

    return render(request, 'appGestionPedidos/producto_modify.html', data)

def pedido_modify(request, id): 

    pedido = get_object_or_404(Pedido, id=id)

    data = {
            'formulario': PedidoForm(instance=pedido)
        } 
        
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("pedido")
        data["formulario"] = formulario 

    return render(request, 'appGestionPedidos/pedido_modify.html', data)

def productoPedido_modify(request, id): 

    productoPedido = get_object_or_404(ProductoPedido, id=id)

    data = {
            'formulario': ProductoPedidoForm(instance=productoPedido)
        } 
        
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=productoPedido, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("pedido")
        data["formulario"] = formulario 

    return render(request, 'appGestionPedidos/productoPedido_modify.html', data)


