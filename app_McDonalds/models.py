from django.db import models

# ==========================
#   CATEGORÍAS
# ==========================
class Categoria(models.Model):
    id_categorias = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

# ==========================
#   CLIENTES
# ==========================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# ==========================
#   PROVEEDORES
# ==========================
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# ==========================
#   INSUMOS
# ==========================
class Insumo(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=50)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return self.nombre_insumo

# ==========================
#   PRODUCTOS
# ==========================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    insumos_usados = models.ManyToManyField(Insumo)

    def __str__(self):
        return self.nombre

# ==========================
#   PEDIDOS
# ==========================
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    metodo_pago = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.id_pedido}"