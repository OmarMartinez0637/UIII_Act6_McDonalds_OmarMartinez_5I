from django.db import models

class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateTimeField()
    salario = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True, unique=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    metodo_pago = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id_pedido}"

class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()
    producto_suministrado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    id_insumo = models.AutoField(primary_key=True, unique=True)
    nombre_insumo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=50)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return self.nombre_insumo