from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio_mcdonalds, name='inicio_mcdonalds'),
    
    # CRUD para Categoria
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/ver/', views.ver_categorias, name='ver_categorias'),
    path('categoria/actualizar/<int:pk>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/borrar/<int:pk>/', views.borrar_categoria, name='borrar_categoria'),
    
    # CRUD para Cliente
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
    
    # CRUD para Proveedor
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),
    
    # CRUD para Insumo
    path('insumo/agregar/', views.agregar_insumo, name='agregar_insumo'),
    path('insumo/ver/', views.ver_insumos, name='ver_insumos'),
    path('insumo/actualizar/<int:pk>/', views.actualizar_insumo, name='actualizar_insumo'),
    path('insumo/borrar/<int:pk>/', views.borrar_insumo, name='borrar_insumo'),
    
    # CRUD para Producto
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_productos, name='ver_productos'),
    path('producto/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:pk>/', views.borrar_producto, name='borrar_producto'),
    
    # CRUD para Pedido
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/ver/', views.ver_pedidos, name='ver_pedidos'),
    path('pedido/actualizar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedido/borrar/<int:pk>/', views.borrar_pedido, name='borrar_pedido'),
]