from django.db import models
from django.db.models.fields.related import ForeignObject

MARCAS = (
    ("X","Xiaomi"),
    ("A","Apple"),
    ("S","Samsung"),
    ("M","Motorola"),
)
ESTADO_FISICO = (
    ("N","Nuevo"),
    ("U","Usado"),
)

class Producto(models.Model):
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
        ("SS","Sin Stock"),
    )
    TIPOS = (
        ("T","Telefono"),
        ("A","Articulo(s)"),
        ("S","Servicio"),
        ("TA","Telefono y Articulo"),
        ("TAS","Telefono, Articulo(s) y servicio"),
        ("TS","Telefono y servicio"),
        ("AS","Articulo y servicio"),
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
        """Propiedades adicionales del modelo"""
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
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
        ("F","Finalizado"),
        ("E","En espera")
    )
    promocion_Id = models.Foreignkey('Promocion', on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaExpiracion = models.DateField()
    estado = models.CharField(max_length=2)

    def __srt__(self):
        return self.fechaInicio

    class Meta:
        db_table = "Fecha"

class Articulo(models.Model):
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
        ("SS","Sin stock"),
    )
    TIPO = (
        ("A","Accesorio"),
        ("T","Telefono"),
    )
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    marca = models.CharField(max_length=1, choices=MARCAS)
    producto_Articulo = models.ManyToManyField('Producto')
    foto = models.ImageField(
        upload_to = 'images/articule/%y/%m/%d',
        default ='images/articule/default.jpg',
        max_length = 255
    )
    estado_fisico = models.CharField(max_field=1,choices=ESTADO_FISICO)
    tipo = models.CharField(max_field=1,choices=TIPO)
    estado = models.CharField(max_length=2, CHOICES=ESTADOS, default="A")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Articulo"

class Servicio(models.Model):
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
    )
    producto_Id = models.OneToOneField('Producto',on_delete=models.CASCADE)
    nombre = models.Charfield(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20,descimal_place=3)
    foto = models.ImageField(
        upload_to='images/services/%y/%m/%d',
        default='image/services/default.jpg',
        max_length=255
    )
    estado = models.CharField(max_length=1,choices=ESTADOS,default="A")

    def __str__(self):
        return self.nombre

    class Meta:
        """Propiedades adicionales del modelo"""
        db_table = "Servicio"

class Modelo(models.Model):
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
    )
    sku = models.CharField(primary_key=True, unique=True) #falta generar codigo
    Articulo_Id = models.ForeignKey('Articulo',on_delete=models.CASCADE)
    nombre = models.Charfield(max_length=255)
    precio = models.DecimalField(max_digits=20,descimal_place=3)
    stock = models.PositiveSmallIntegerField()
    foto = models.ImageField(
        upload_to = 'images/model/%y/%m/%d',
        default ='images/model/default.jpg',
        max_length = 255
    )
    estado = models.CharField(max_length=2, CHOICES=ESTADOS, default="A")
    
    def __str__(self):
        return self.nombre

    class Meta:
        """Propiedades adicionales del modelo"""
        db_table = "Modelo"

class Caracteristica (models.Model):
    ESTADOS = (
        ("A","Activo"),
        ("I","Inactivo"),
    )
    TIPO = (
        ("AP","Afecta el precio"),
        ("NP","No afecta el precio"),
    )
    #Si afecta el precio solo puede tener un valor
    #Si no afecta el precio puede tener varios valores
    modelo_Id = models.ForeignKey('Modelo',on_delete=models.CASCADE)
    variante_Id = models.ForeignKey('Variante',on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2, CHOICES=TIPO)
    estado = models.CharField(max_length=1, CHOICES=ESTADOS, default="A")
        
    def __str__(self):
        return self.modelo_Id

    class Meta:
        """Propiedades adicionales del modelo"""
        db_table = "Caracteristica"

class Valor (models.Model):
    caracteristica_id = models.ForeignKey('Caracteristica',on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)
            
    def __str__(self):
        return self.caracteristica_id

    class Meta:
        """Propiedades adicionales del modelo"""
        db_table = "Valor"

class Variante(models.Model):
    nombre = models.CharField(max_length=255)
                
    def __str__(self):
        return self.nombre

    class Meta:
        """Propiedades adicionales del modelo"""
        db_table = "Variante"