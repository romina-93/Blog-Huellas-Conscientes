
from django.db import models
from apps.categorias.models import Categoria
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Articulo(models.Model):
    creado = models.DateTimeField(
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        auto_now=True
    )
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, null = True, on_delete = models.CASCADE)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    fecha = models.DateField(default=timezone.now)  
    slug = models.SlugField(unique=True, blank=True)
    destacado = models.BooleanField(default=False)  
    

    def __str__(self):
        return self.titulo
    
    def misComentarios(self):
	    return self.comentario_set.all()

class FraseInspiradora(models.Model):
    texto = models.TextField()
    autor = models.CharField(max_length=100, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.texto[:50]}..."

