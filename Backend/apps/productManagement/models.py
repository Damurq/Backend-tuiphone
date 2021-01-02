from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField()
    precio = models.()
    foto = models.imagefield()
    estado = models-CharField()

    def __str__(self):
        return self.nombre


    class Meta:
        """Propiedades adicionales del modelo Empleado"""
        db_table = "Producto"
        

foto = models.ImageField(
        upload_to='pictures/%y/%m/%d',
        default='pictures/default.jpg',
        max_length=255
    )





class Promocion(models.Model):

class Fecha   
class Accesorio(models.Model):
    nombre = models.CharField()
    descripcion = models.Charfield()
    estado = models.CharField(max_length=1)

class Telefono(models.Model):
    nombre = models.CharField()
    modelo = models.charfield()
    marca = models.CharField()
    