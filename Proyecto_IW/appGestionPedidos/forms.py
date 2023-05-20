from django import forms
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'CIF': forms.TextInput(attrs={'placeholder': 'Ej.: A12147193'}),
            'nombreEmpresa': forms.TextInput(attrs={'placeholder': 'Ej.: Forjas Alavesas'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ej.: Calle Postas 4'}),
            'datosContacto': forms.NumberInput(attrs={'placeholder': 'Ej.: 660862421'}),
        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
        widgets = {
            'codigoReferencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471R'}),
            'nombreModelo': forms.TextInput(attrs={'placeholder': 'Ej.: Procesador i5 '}),
            'marca': forms.TextInput(attrs={'placeholder': 'Ej.: Intel'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'referencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471R93-T'}),
            'precio': forms.TextInput(attrs={'placeholder': 'Ej.: 549.99'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej.: Travel Mate'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ej.: Ordenador portatil 14" '}),
            # 'categoria': forms.TextInput(attrs={'placeholder': 'Seleccionar categoria'}),
            # 'componente': forms.TextInput(attrs={'placeholder': 'Seleccionar 1 o más elem.'}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude= ['producto']
        widgets = {
            'referencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471342Q'}),
            'fecha': forms.DateInput(attrs={'placeholder': 'Ej.: 2023-01-25'}),
            # 'cliente': forms.ListInput(attrs={'placeholder': 'Ej.: Intel'}),
            'precioTotal': forms.NumberInput(attrs={'placeholder': 'Ej.: 549.99'}),
        }

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['idProducto', 'idPedido', 'cantidad']
