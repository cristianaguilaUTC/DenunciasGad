from django.db import models
from Aplicaciones.Usuarios.models import Usuario

# Create your models here.
class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        fila="{0}: {1} {2} {3} {4} {5} {6} {7} {8}"
        return fila.format(self.id, self.usuario.nombre, self.titulo, self.descripcion, self.ubicacion, self.latitud, self.longitud, self.estado, self.fecha_creacion)