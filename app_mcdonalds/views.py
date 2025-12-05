from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleados, Clientes, Productos, Pedidos, Proveedores, Inventario

def inicio_mcdonalds(request):
    return render(request, 'inicio.html')

# CRUD para Empleados
def agregar_empleados(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        puesto = request.POST['puesto']
        fecha_contratacion = request.POST['fecha_contratacion']
        salario = request.POST['salario']
        Empleados.objects.create(nombre=nombre, apellido=apellido, puesto=puesto, fecha_contratacion=fecha_contratacion, salario=salario)
        return redirect('ver_empleados')
    return render(request, 'empleados/agregar.html')

def ver_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados/ver.html', {'empleados': empleados})

def actualizar_empleados(request, id):
    empleado = get_object_or_404(Empleados, id_empleado=id)
    return render(request, 'empleados/actualizar.html', {'empleado': empleado})

def realizar_actualizacion_empleados(request, id):
    empleado = get_object_or_404(Empleados, id_empleado=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.puesto = request.POST['puesto']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.save()
        return redirect('ver_empleados')
    return redirect('ver_empleados')

def borrar_empleados(request, id):
    empleado = get_object_or_404(Empleados, id_empleado=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar.html', {'empleado': empleado})

# CRUD para Clientes
def agregar_clientes(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        genero = request.POST['genero']
        Clientes.objects.create(nombre=nombre, telefono=telefono, email=email, direccion=direccion, genero=genero)
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar.html')

def ver_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/ver.html', {'clientes': clientes})

def actualizar_clientes(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    return render(request, 'clientes/actualizar.html', {'cliente': cliente})

def realizar_actualizacion_clientes(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        cliente.genero = request.POST['genero']
        cliente.save()
        return redirect('ver_clientes')
    return redirect('ver_clientes')

def borrar_clientes(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar.html', {'cliente': cliente})

# CRUD para Productos
def agregar_productos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        precio = request.POST['precio']
        stock = request.POST['stock']
        descripcion = request.POST['descripcion']
        Productos.objects.create(nombre=nombre, categoria=categoria, precio=precio, stock=stock, descripcion=descripcion)
        return redirect('ver_productos')
    return render(request, 'productos/agregar.html')

def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/ver.html', {'productos': productos})

def actualizar_productos(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    return render(request, 'productos/actualizar.html', {'producto': producto})

def realizar_actualizacion_productos(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.descripcion = request.POST['descripcion']
        producto.save()
        return redirect('ver_productos')
    return redirect('ver_productos')

def borrar_productos(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'productos/borrar.html', {'producto': producto})

# CRUD para Pedidos
def agregar_pedidos(request):
    clientes = Clientes.objects.all()
    empleados = Empleados.objects.all()
    if request.method == 'POST':
        id_cliente = request.POST['id_cliente']
        id_empleado = request.POST['id_empleado']
        fecha = request.POST['fecha']
        metodo_pago = request.POST['metodo_pago']
        total = request.POST['total']
        cliente = get_object_or_404(Clientes, id_cliente=id_cliente)
        empleado = get_object_or_404(Empleados, id_empleado=id_empleado)
        Pedidos.objects.create(id_cliente=cliente, id_empleado=empleado, fecha=fecha, metodo_pago=metodo_pago, total=total)
        return redirect('ver_pedidos')
    return render(request, 'pedidos/agregar.html', {'clientes': clientes, 'empleados': empleados})

def ver_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/ver.html', {'pedidos': pedidos})

def actualizar_pedidos(request, id):
    pedido = get_object_or_404(Pedidos, id_pedido=id)
    clientes = Clientes.objects.all()
    empleados = Empleados.objects.all()
    return render(request, 'pedidos/actualizar.html', {'pedido': pedido, 'clientes': clientes, 'empleados': empleados})

def realizar_actualizacion_pedidos(request, id):
    pedido = get_object_or_404(Pedidos, id_pedido=id)
    if request.method == 'POST':
        id_cliente = request.POST['id_cliente']
        id_empleado = request.POST['id_empleado']
        pedido.fecha = request.POST['fecha']
        pedido.metodo_pago = request.POST['metodo_pago']
        pedido.total = request.POST['total']
        pedido.id_cliente = get_object_or_404(Clientes, id_cliente=id_cliente)
        pedido.id_empleado = get_object_or_404(Empleados, id_empleado=id_empleado)
        pedido.save()
        return redirect('ver_pedidos')
    return redirect('ver_pedidos')

def borrar_pedidos(request, id):
    pedido = get_object_or_404(Pedidos, id_pedido=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedidos/borrar.html', {'pedido': pedido})

# CRUD para Proveedores
def agregar_proveedores(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        producto_suministrado = request.POST['producto_suministrado']
        Proveedores.objects.create(nombre=nombre, telefono=telefono, email=email, direccion=direccion, producto_suministrado=producto_suministrado)
        return redirect('ver_proveedores')
    return render(request, 'proveedores/agregar.html')

def ver_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'proveedores/ver.html', {'proveedores': proveedores})

def actualizar_proveedores(request, id):
    proveedor = get_object_or_404(Proveedores, id_proveedor=id)
    return render(request, 'proveedores/actualizar.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedores(request, id):
    proveedor = get_object_or_404(Proveedores, id_proveedor=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.telefono = request.POST['telefono']
        proveedor.email = request.POST['email']
        proveedor.direccion = request.POST['direccion']
        proveedor.producto_suministrado = request.POST['producto_suministrado']
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('ver_proveedores')

def borrar_proveedores(request, id):
    proveedor = get_object_or_404(Proveedores, id_proveedor=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedores/borrar.html', {'proveedor': proveedor})

# CRUD para Inventario
def agregar_inventario(request):
    proveedores = Proveedores.objects.all()
    if request.method == 'POST':
        nombre_insumo = request.POST['nombre_insumo']
        cantidad = request.POST['cantidad']
        unidad = request.POST['unidad']
        id_proveedor = request.POST['id_proveedor']
        fecha_entrega = request.POST['fecha_entrega']
        proveedor = get_object_or_404(Proveedores, id_proveedor=id_proveedor)
        Inventario.objects.create(nombre_insumo=nombre_insumo, cantidad=cantidad, unidad=unidad, id_proveedor=proveedor, fecha_entrega=fecha_entrega)
        return redirect('ver_inventario')
    return render(request, 'inventario/agregar.html', {'proveedores': proveedores})

def ver_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario/ver.html', {'inventario': inventario})

def actualizar_inventario(request, id):
    insumo = get_object_or_404(Inventario, id_insumo=id)
    proveedores = Proveedores.objects.all()
    return render(request, 'inventario/actualizar.html', {'insumo': insumo, 'proveedores': proveedores})

def realizar_actualizacion_inventario(request, id):
    insumo = get_object_or_404(Inventario, id_insumo=id)
    if request.method == 'POST':
        insumo.nombre_insumo = request.POST['nombre_insumo']
        insumo.cantidad = request.POST['cantidad']
        insumo.unidad = request.POST['unidad']
        id_proveedor = request.POST['id_proveedor']
        insumo.fecha_entrega = request.POST['fecha_entrega']
        insumo.id_proveedor = get_object_or_404(Proveedores, id_proveedor=id_proveedor)
        insumo.save()
        return redirect('ver_inventario')
    return redirect('ver_inventario')

def borrar_inventario(request, id):
    insumo = get_object_or_404(Inventario, id_insumo=id)
    if request.method == 'POST':
        insumo.delete()
        return redirect('ver_inventario')
    return render(request, 'inventario/borrar.html', {'insumo': insumo})