from django.contrib import admin
from .models import Cliente, Pedido, Producto, Componente, ProductoPedido, Categoria

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(ProductoPedido)

