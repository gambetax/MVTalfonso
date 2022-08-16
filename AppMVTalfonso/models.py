from django.db import models

# Create your models here.
class Familia(models.Model):
    apellido = models.CharField(max_length=40)
    cantidad_integrantes = models.IntegerField()
    fecha_creacion = models.CharField(max_length=40)

class Integrantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
