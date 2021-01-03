from django.db import models

class Producto(models.Model):
    ESTADOS = (
        ("A","Activo"
         "I","Inactivo"
         "SS","Sin Stock"),
    )
    TIPOS = (
        ("T","Telefono"),
        ("A","Accesorio(s)"),
        ("S","Servicio"),
        ("TA","Telefono y accesorio"),
        ("TAS","Telefono, accesorio(s) y servicio"),
        ("TS","Telefono y servicio"),
        ("AS","Accesorio y servicio"),
        ("V","Vacio"),
    )
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=20,decimal_places=3)
    descipcion = models.TextField()
    foto = models.imagefield(
        upload_to='images/products/%y/%m/%d',
        default='images/products/default.jpg',
        max_length=255
    )
    estado = models.CharField(max_length=1, choices=ESTADOS)
    tipo = models.CharField(max_length=3,choices=TIPOS ,default="V")

    def __str__(self):
        return self.nombre

    class Meta:
        """Propiedades adicionales del modelo Empleado"""
        db_table = "Producto"

class Promocion(models.Model):
    TIPOS = (
        ("D","Descuento"),
        ("EF","Evento o dia festivo"),
        ("CP","Cliente premium"),
    )
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
        ("E","En espera"),
        ("F","Finalizado"),
    )
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=2,choices=TIPOS)
    descuento = models.DecimalField(max_digits=5,decimal_place=2)
    estado = models.CharField(max_length=1, default="A")
    producto_promocion = models.ManyToManyField("Producto")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table="Promocion"

class Fecha(models.Model):
    promocion_Id = models.Foreignkey('Promocion', on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaExpiracion = models.DateField()
    estado = models.DateField()

class Accesorio(models.Model):
    nombre = models.CharField()
    descripcion = models.Charfield()
    estado = models.CharField(max_length=1)

class Telefono(models.Model):
    nombre = models.CharField()
    modelo = models.charfield()
    marca = models.CharField()
    