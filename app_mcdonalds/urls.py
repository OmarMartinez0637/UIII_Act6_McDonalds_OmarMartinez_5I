from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_mcdonalds, name='inicio_mcdonalds'),
    # Empleados
    path('empleados/agregar/', views.agregar_empleados, name='agregar_empleados'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleados, name='actualizar_empleados'),
    path('empleados/actualizar/<int:id>/realizar/', views.realizar_actualizacion_empleados, name='realizar_actualizacion_empleados'),
    path('empleados/borrar/<int:id>/', views.borrar_empleados, name='borrar_empleados'),
    # Clientes
    path('clientes/agregar/', views.agregar_clientes, name='agregar_clientes'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id>/', views.actualizar_clientes, name='actualizar_clientes'),
    path('clientes/actualizar/<int:id>/realizar/', views.realizar_actualizacion_clientes, name='realizar_actualizacion_clientes'),
    path('clientes/borrar/<int:id>/', views.borrar_clientes, name='borrar_clientes'),
    # Productos
    path('productos/agregar/', views.agregar_productos, name='agregar_productos'),
    path('productos/ver/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:id>/', views.actualizar_productos, name='actualizar_productos'),
    path('productos/actualizar/<int:id>/realizar/', views.realizar_actualizacion_productos, name='realizar_actualizacion_productos'),
    path('productos/borrar/<int:id>/', views.borrar_productos, name='borrar_productos'),
    # Pedidos
    path('pedidos/agregar/', views.agregar_pedidos, name='agregar_pedidos'),
    path('pedidos/ver/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/actualizar/<int:id>/', views.actualizar_pedidos, name='actualizar_pedidos'),
    path('pedidos/actualizar/<int:id>/realizar/', views.realizar_actualizacion_pedidos, name='realizar_actualizacion_pedidos'),
    path('pedidos/borrar/<int:id>/', views.borrar_pedidos, name='borrar_pedidos'),
    # Proveedores
    path('proveedores/agregar/', views.agregar_proveedores, name='agregar_proveedores'),
    path('proveedores/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedores, name='actualizar_proveedores'),
    path('proveedores/actualizar/<int:id>/realizar/', views.realizar_actualizacion_proveedores, name='realizar_actualizacion_proveedores'),
    path('proveedores/borrar/<int:id>/', views.borrar_proveedores, name='borrar_proveedores'),
    # Inventario
    path('inventario/agregar/', views.agregar_inventario, name='agregar_inventario'),
    path('inventario/ver/', views.ver_inventario, name='ver_inventario'),
    path('inventario/actualizar/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
    path('inventario/actualizar/<int:id>/realizar/', views.realizar_actualizacion_inventario, name='realizar_actualizacion_inventario'),
    path('inventario/borrar/<int:id>/', views.borrar_inventario, name='borrar_inventario'),
]