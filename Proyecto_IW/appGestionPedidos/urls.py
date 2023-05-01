from django.contrib import admin
from django.urls import include, path
from . import views
from .views import cliente_modify, cliente_delete, componente_delete, producto_delete, pedido_delete

urlpatterns = [

    # URL INDEX (Defecto al iniciar)

    path('', views.ClienteListView.as_view(), name='index'), #Es provisional

    # URLs LISTAR
    
    path('cliente/list', views.ClienteListView.as_view(), name='cliente'),
    path('pedido/list', views.PedidoListView.as_view(), name='pedido'),
    path('producto/list', views.ProductoListView.as_view(), name='producto'),
    path('componente/list', views.ComponenteListView.as_view(), name='componente'),

    # URLs CREAR
    path('cliente/create', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('componente/create', views.ComponenteCreateView.as_view(), name='componente_create'),
    path('producto/create', views.ProductoCreateView.as_view(), name='producto_create'),
    path('pedido/create', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('productoPedido/create', views.ProductoPedidoCreateView.as_view(), name='productoPedido_create'),

    # URLs BORRAR
    path('eliminar-cliente/<id>', cliente_delete, name='cliente_delete'),
    path('eliminar-componente/<id>', componente_delete, name='componente_delete'),
    path('eliminar-producto/<id>', producto_delete, name='producto_delete'),
    path('eliminar-pedido/<id>', pedido_delete, name='pedido_delete'),

    # URLs MODIFICAR
    path('modificar-cliente/<id>/', cliente_modify, name='cliente_modify'),
    path('modificar-pedido/<id>/', cliente_modify, name='cliente_modify'),


    # URLs DETALLE

    path('detallesPedido/<int:pk>/', views.ProductoPedidoDetailView.as_view(), name='detalles_Pedido'),


]   

