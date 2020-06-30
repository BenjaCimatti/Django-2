from django.db import models

# Hay que ver como relacionar Cliente y Proveedor con direccion
# Revisar la lógica del monto_final
# Ver como hacer la relacion Producto, Venta

class Detalle(models.Model):
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.cantidad)

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Venta(models.Model, Producto, Detalle):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField()
    descuento = models.FloatField()
    monto_final = models.FloatField()
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def MontoFinal(self, Producto.precio, Detalle.cantidad):
        precio = Producto.precio
        cantidad = Detalle.cantidad
        monto_final = precio * cantidad

    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length=25)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=45)

    def __str__(self):
        return str(self.calle)

class Cliente(models.Model):
    RUT = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    RUT = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    WEB = models.CharField(max_length=75)
    telefono = models.IntegerField()
    direccion = Direccion()

    def __str__(self):
        return str(self.nombre)
