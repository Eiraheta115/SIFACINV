from .views import *
from django.urls import path
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('', inicio, name="inicio"),
    path('nueva_venta', nueva_venta, name="nueva_venta"),
    path('nueva_compra', nueva_compra, name="nueva_compra"),
    path('busqueda', prueba, name="busqueda"),
    path('crear_producto', new_product, name="new_product"),
    path('crear_bodega', new_bodega, name="new_bodega"),
    path('crear_categoria', new_categoria, name="new_categoria"),
    path('products', new_product, name="new_product"),
    path('listar_bodega', BodegasList.as_view(), name="list_bodega"),
    path('listar_categoria', CategoriasList.as_view(), name="list_categoria"),
    path('listar_producto', ProductosList.as_view(), name="list_producto"),
    path('lista_cliente', clientes_list, name='clientes_list'),
    path('lista_proveedores', proveedores_list, name='proveedores_list'),
    path('reporte_ventas', reporte_ventas, name='reporte_ventas'),
    url(r'^getVentas$', getVentas, name='getVentas'),
    url(r'^$', clientes_list, name='clientes_list'),
    url(r'^clientes_new$', clientes_create, name='clientes_new'),
    url(r'^clientes_edit/(?P<pk>\d+)$', clientes_update, name='clientes_edit'),
    url(r'^clientes_delete/(?P<pk>\d+)$', clientes_delete, name='clientes_delete'),
    path('clientes_edit/clientes_list', clientes_list, name='clientes_list'),
    path('clientes_delete/clientes_list.html', clientes_list, name='clientes_list'),
    path('clientes_list.html', clientes_list, name='clientes_list'),
    url(r'^$', proveedores_list, name='proveedores_list'),
    url(r'^proveedores_new$', proveedores_create, name='proveedores_new'),
    url(r'^proveedores_edit/(?P<pk>\d+)$', proveedores_update, name='proveedores_edit'),
    url(r'^proveedores_delete/(?P<pk>\d+)$', proveedores_delete, name='proveedores_delete'),
    path('proveedores_edit/proveedores_list', proveedores_list, name='proveedores_list'),
    path('proveedores_delete/proveedores_list.html', proveedores_list, name='proveedores_list'),
    path('proveedores_list.html', proveedores_list, name='proveedores_list'),

    path('reporte_facturas', reporte_facturas, name='reporte_facturas'),
    url(r'^getFacturas$', getFacturas, name='getFacturas'),

    path('mod_producto/<id>/', mod_productos, name='mod_producto'),
    path('mod_bodega/<id>/', mod_bodegas, name='mod_bodega'),
    path('mod_categoria/<id>/', mod_categorias, name="mod_categoria")

]
