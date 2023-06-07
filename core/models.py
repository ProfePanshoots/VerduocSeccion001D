from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    vencimiento = models.DateField()
    imagen = models.ImageField(null=True,blank=True)
    vigente = models.BooleanField()

    def __str__(self):
        return self.nombre



