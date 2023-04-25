from django import forms
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido

class ClienteFrom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

class ProductoFrom(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoFrom(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProductoPedidoFrom(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = '__all__'
