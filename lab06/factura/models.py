from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    ruc = models.CharField(max_length=11, unique=True) 
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Empleado(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    contraseña = models.CharField(max_length=128) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=45, unique=True)
    fecha = models.DateField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    igv = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Factura {self.numero_factura}'


class DetallesProducto(models.Model): 
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} unidades'