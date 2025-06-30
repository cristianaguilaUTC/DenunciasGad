from django.db import models
from Aplicaciones.Usuarios.models import Usuario

class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_denuncia = models.CharField(max_length=200)
    descripcion = models.TextField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    referencia = models.CharField(max_length=255)
    evidencia = models.FileField(upload_to='evidencias', null=True, blank=True)
    estado = models.CharField(max_length=50, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fila = "{0}: {1} {2} {3} {4} {5} {6} {7} {8}"
        return fila.format(
            self.id,
            self.usuario.nombre,
            self.tipo_denuncia,
            self.descripcion,
            self.latitud,
            self.longitud,
            self.referencia,
            self.estado,
            self.fecha_creacion
        )
    
