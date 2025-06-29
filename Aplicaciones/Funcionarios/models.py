from django.db import models

# Create your models here.
class Funcionario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)

    def _str_(self):
        fila="{0}: {1} {2} {3} "
        return fila.format(self.id, self.nombre, self.correo, self.cargo)