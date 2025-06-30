from django.db import models

# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cedula = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=128)
    
    def _str_(self):
        fila="{0}: {1} {2} {3} {4} "
        return fila.format(self.id, self.nombre, self.correo, self.cedula, self.anonimo)
