from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Categoria, Cliente, Proveedor, Insumo, Producto, Pedido
from .forms import CategoriaForm, ClienteForm, ProveedorForm, InsumoForm, ProductoForm, PedidoForm

# Función de inicio
def inicio_mcdonalds(request):
    return render(request, 'inicio.html')

# ==========================
# CRUD para CATEGORIA
# ==========================
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/agregar_categoria.html', {'form': form})

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

def actualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('ver_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/actualizar_categoria.html', {'form': form})

def borrar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})

# ==========================
# CRUD para CLIENTE
# ==========================
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/agregar_cliente.html', {'form': form})

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/actualizar_cliente.html', {'form': form})

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==========================
# CRUD para PROVEEDOR
# ==========================
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/agregar_proveedor.html', {'form': form})

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('ver_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/actualizar_proveedor.html', {'form': form})

def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================
# CRUD para INSUMO
# ==========================
def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_insumos')
    else:
        form = InsumoForm()
    return render(request, 'insumo/agregar_insumo.html', {'form': form})

def ver_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumo/ver_insumos.html', {'insumos': insumos})

def actualizar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('ver_insumos')
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'insumo/actualizar_insumo.html', {'form': form})

def borrar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        insumo.delete()
        return redirect('ver_insumos')
    return render(request, 'insumo/borrar_insumo.html', {'insumo': insumo})

# ==========================
# CRUD para PRODUCTO
# ==========================
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto/agregar_producto.html', {'form': form})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/actualizar_producto.html', {'form': form})

def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ==========================
# CRUD para PEDIDO
# ==========================
def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedido/agregar_pedido.html', {'form': form})

def ver_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('ver_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido/actualizar_pedido.html', {'form': form})

def borrar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})