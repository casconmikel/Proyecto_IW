from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='index'), #Es provisional
    path('cliente/<int:pk>', views.ClienteListView.as_view(), name='cliente'),
    path('pedido/<int:pk>', views.PedidoListView.as_view(), name='pedido'),
    path('producto/<int:pk>', views.ProductoListView.as_view(), name='producto'),
    path('componente/<int:pk>', views.ComponenteListView.as_view(), name='componente'),

    path('detallesPedido/<int:pk>', views.ProductoPedidoDetailView.as_view(), name='detallesPedido'),
]

