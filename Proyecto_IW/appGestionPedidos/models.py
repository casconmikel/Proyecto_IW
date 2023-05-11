from enum import unique
from django.db import models
 
class Cliente(models.Model):
    CIF = models.CharField(max_length=9, unique=True)
    nombreEmpresa = models.CharField(max_length=16)
    direccion = models.CharField(max_length=60)
    datosContacto = models.CharField(max_length=60)

    def __str__(self):
       return f"{self.CIF} - {self.nombreEmpresa}" 


class Componente(models.Model): 
    codigoReferencia = models.IntegerField(unique=True)
    nombreModelo = models.CharField(max_length=16)
    marca = models.CharField(max_length=16)

    def __str__(self):
       return f"{self.id} - {self.codigoReferencia} - {self.nombreModelo}"
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=16)

    def __str__(self):
       return f"{self.nombre}" 
    

class Producto(models.Model):
    referencia = models.IntegerField(unique=True)
    precio = models.FloatField()
    nombre = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    componente = models.ManyToManyField(Componente) 

    def __str__(self):
       return f"{self.id} - {self.precio} - {self.nombre} - {self.categoria}" 


class Pedido(models.Model):
    referencia = models.IntegerField(unique=True)
    producto = models.ManyToManyField(Producto, through="ProductoPedido")
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    precioTotal = models.FloatField(blank=True, null=True)

    def __str__(self):
       return f"{self.id} - {self.fecha} - {self.cliente}" 
    def obtener_cantidad(self):
        cantidad = []
        productoPedido = ProductoPedido.objects.filter(pedido_solicitado=self)
        for i in productoPedido:
            cantidad.append(i.cantidad)
        return cantidad


class ProductoPedido(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
       return f"{self.id} - {self.idProducto} - {self.idPedido} - {self.cantidad}" 
    





    
