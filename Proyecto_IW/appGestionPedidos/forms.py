from django import forms
from .models import Cliente, Componente, Producto, Pedido, ProductoPedido
from django.core.mail import send_mail

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'CIF': forms.TextInput(attrs={'placeholder': 'Ej.: A12147193', 'id': 'cif'}),
            'nombreEmpresa': forms.TextInput(attrs={'placeholder': 'Ej.: Forjas Alavesas'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ej.: Calle Postas 4'}),
            'datosContacto': forms.NumberInput(attrs={'placeholder': 'Ej.: 660862421', 'id': 'tel'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ej.: elnano33@gmail.com'}),
        }
    
    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.save()

        # Enviar el correo electrónico nuevo cliente registrado
        subject = 'Alta en Deustronic Componentes'
        message = f'Hola {cliente.nombreEmpresa}, le confirmamos que ha sido registrado en nuestra base de datos.'
        from_email = 'mcm.lab.mercadona@gmail.com'  
        recipient_list = [cliente.email]

        send_mail(subject, message, from_email, recipient_list)

        return cliente

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
        widgets = {
            'codigoReferencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471'}),
            'nombreModelo': forms.TextInput(attrs={'placeholder': 'Ej.: Procesador i5 '}),
            'marca': forms.TextInput(attrs={'placeholder': 'Ej.: Intel'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'referencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471793'}),
            'precio': forms.TextInput(attrs={'placeholder': 'Ej.: 549.99'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej.: Travel Mate'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ej.: Ordenador portatil 14" '}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude= ['producto']
        widgets = {
            'referencia': forms.TextInput(attrs={'placeholder': 'Ej.: 471342'}),
            'fecha': forms.DateInput(attrs={'placeholder': 'Ej.: 2023-01-25'}),
            'precioTotal': forms.NumberInput(attrs={'placeholder': 'Ej.: 549.99'}),
        }
    
    def save(self, commit=True):
        pedido = super().save(commit=False)
        pedido.save()

        # Enviar el correo electrónico, confirmación nuevo pedido 
        subject = 'Nuevo pedido en Deustronic Componentes'
        message = f'Hola {pedido.cliente.nombreEmpresa}, le confirmamos que acaba de registrarse su pedido con referencia {pedido.referencia}.'
        from_email = 'mcm.lab.mercadona@gmail.com'  
        recipient_list = [pedido.cliente.email]

        send_mail(subject, message, from_email, recipient_list)

        return pedido

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['idProducto', 'idPedido', 'cantidad']
