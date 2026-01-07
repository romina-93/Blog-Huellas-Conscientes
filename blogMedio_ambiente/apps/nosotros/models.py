
from django.db import models

class Nosotros(models.Model):
    titulo = models.CharField(max_length=200, default="Sobre nosotros")
    descripcion = models.TextField()
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    valores = models.TextField(blank=True, null=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    redes_sociales = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
