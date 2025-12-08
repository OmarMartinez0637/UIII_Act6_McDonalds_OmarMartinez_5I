from django.contrib import admin
from .models import Categoria, Cliente, Proveedor, Insumo, Producto, Pedido

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Insumo)
admin.site.register(Producto)
admin.site.register(Pedido)