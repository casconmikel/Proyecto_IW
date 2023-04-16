from django.contrib import admin
from .models import Cliente, Pedido, Producto, Componentes

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componentes)

