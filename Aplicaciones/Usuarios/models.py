from django.db import models

# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    tipo_usuario = models.CharField(max_length=50)
    anonimo = models.BooleanField(default=False)

    def _str_(self):
        fila="{0}: {1} {2} {3} {4} "
        return fila.format(self.id, self.nombre, self.correo, self.contrasena, self.tipo_usuario, self.anonimo)
