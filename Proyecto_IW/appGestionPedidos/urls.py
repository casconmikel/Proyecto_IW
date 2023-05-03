from django.contrib import admin
from django.urls import include, path
from . import views
from .views import cliente_modify, cliente_delete, productoPedido_delete, componente_delete, producto_delete, pedido_delete, componente_modify, producto_modify, pedido_modify, productoPedido_modify 

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
    path('eliminar-productoPedido/<id>', productoPedido_delete, name='productoPedido_delete'),


    # URLs MODIFICAR
    path('modificar-cliente/<id>/', cliente_modify, name='cliente_modify'),
    path('modificar-componente/<id>/', componente_modify, name='componente_modify'),
    path('modificar-producto/<id>/', producto_modify, name='producto_modify'),
    path('modificar-pedido/<id>/', pedido_modify, name='pedido_modify'),
    path('modificar-productoPedido/<id>/', productoPedido_modify, name='productoPedido_modify'),

    # URLs DETALLES

    path('detallesPedido/<int:pk>/', views.ProductoPedidoDetailView.as_view(), name='detalles_Pedido'),
    path('detallesProducto/<int:pk>/', views.ProductoDetailView.as_view(), name='detalles_Producto'),


]   

