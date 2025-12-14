from django.db import models

from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
