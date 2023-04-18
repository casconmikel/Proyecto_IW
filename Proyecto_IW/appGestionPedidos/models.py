from django.db import models
 
class Cliente(models.Model):
    CIF = models.IntegerField()
    nombreEmpresa = models.CharField(max_length=16)
    direccion = models.CharField(max_length=60)
    datosContacto = models.CharField(max_length=60)

    def __str__(self):
       return f"{self.id} - {self.CIF} - {self.nombreEmpresa} - {self.direccion} - {self.datosContacto}" 

class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    precioTotal = models.FloatField()

    def __str__(self):
       return f"{self.id} - {self.fecha} - {self.cliente} - {self.precioTotal}" 

class Producto(models.Model):
    precio = models.FloatField()
    nombre = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=16)
    pedido = models.ManyToManyField(Pedido)    

    def __str__(self):
       return f"{self.id} - {self.precio} - {self.nombre} - {self.descripcion} - {self.categoria} - {self.pedido}" 

class Componente(models.Model): 
    codigoReferencia = models.IntegerField()
    nombreModelo = models.CharField(max_length=16)
    marca = models.CharField(max_length=16)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
       return f"{self.id} - {self.codigoReferencia} - {self.nombreModelo} - {self.marca} - {self.producto}" 

class ProductoPedido(models.Model):
    idProducto = models.ManyToManyField(Producto)
    idPedido = models.ManyToManyField(Pedido)
    cantidad = models.IntegerField()

    def __str__(self):
       return f"{self.id} - {self.idProducto} - {self.idPedido} - {self.cantidad}" 
    

    
    
