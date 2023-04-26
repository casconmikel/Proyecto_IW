from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    # URL INDEX (Defecto al iniciar)

    path('', views.ClienteListView.as_view(), name='index'), #Es provisional

    # URLs LISTAR
    
    path('cliente/list', views.ClienteListView.as_view(), name='cliente'),
    path('pedido/list', views.PedidoListView.as_view(), name='pedido'),
    path('producto/list', views.ProductoListView.as_view(), name='producto'),
    path('componente/list', views.ComponenteListView.as_view(), name='componente'),

    path('detallesPedido/<int:pk>', views.ProductoPedidoDetailView.as_view(), name='detallesPedido'),

    # URLs CREAR
    path('cliente/create', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('componente/create', views.ComponenteCreateView.as_view(), name='componente_create'),
    path('producto/create', views.ProductoCreateView.as_view(), name='producto_create'),
    # URLs BORRAR

    # URLs MODIFICAR
]

