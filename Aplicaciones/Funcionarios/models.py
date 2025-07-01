from django.db import models

# Create your models here.
class Funcionario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)

    
    def __str__(self):
        fila="{0}: {1} {2} {3} "
        return fila.format(self.id, self.nombre, self.correo)