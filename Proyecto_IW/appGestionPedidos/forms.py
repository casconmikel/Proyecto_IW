from django import forms
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude= ['producto']

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['idProducto', 'idPedido', 'cantidad']
