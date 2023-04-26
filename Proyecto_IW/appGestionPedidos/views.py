from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido
from .forms import ClienteForm, ComponenteForm, ProductoForm, PedidoForm, ProductoPedidoForm


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

#___________________ ELIMINAR ___________________

# class ClienteDeleteView(View):
#     def cliente_delete(request, id):
#         cliente = get_object_or_404(Cliente, id=id)
#         if request.method.lower() == 'post':
#             cliente.delete()
#             return HttpResponse('Delete success')
#         context = {'object': cliente}
#         return render(request, 'index', context)
    
# OTRO METODO
def cliente_delete(request, id):
      cliente = get_object_or_404(Cliente, id=id)
      cliente.delete()
      return redirect('index')
     

#___________________ Modificar ___________________

# class   ClienteModifyView(View):
def cliente_modify(request, id): 

    cliente = get_object_or_404(Cliente, id=id)

    data = {
            'form': ClienteForm(instance=cliente)
        } 
        
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("index")
        data["form"] = formulario 

    return render(request, 'appGestionPedidos/cliente_modify.html', data)


