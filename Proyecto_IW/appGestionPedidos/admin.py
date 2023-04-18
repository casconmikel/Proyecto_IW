from django.contrib import admin
from .models import Cliente, Pedido, Producto, Componente, ProductoPedido

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(ProductoPedido)

