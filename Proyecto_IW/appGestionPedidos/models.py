from django.db import models
 
class Cliente(models.Model):
    CIF = models.IntegerField()
    nombreEmpresa = models.CharField(max_length=16)
    direccion = models.CharField(max_length=60)
    datosContacto = models.CharField(max_length=60)

class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Falta relacionar con cliente ¿Esta bien?
    #Falta producto y cantidad ¿array o diccionario? OJO!!
    precioTotal = models.FloatField()

class Producto(models.Model):
    precio = models.FloatField()
    nombre = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=16)
    pedido = models.ManyToManyField(Pedido)     #Falta relacionar con componentes ¿Esta bien?

class Componentes(models.Model):
    codigoReferencia = models.IntegerField()
    nombreModelo = models.CharField(max_length=16)
    marca = models.CharField(max_length=16)
    producto = models.ManyToManyField(Producto) #¿Esta bien?
    

    
    
