from django.db import models
from Aplicaciones.Denuncias.models import Denuncia
# Create your models here.
class HistorialEstado(models.Model):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=50)
    estado_nuevo = models.CharField(max_length=50)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estado_anterior} → {self.estado_nuevo}"