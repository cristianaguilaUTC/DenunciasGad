from django.db import models
from Aplicaciones.Denuncias.models import Denuncia
from Aplicaciones.Funcionarios.models import Funcionario
# Create your models here.

class Respuesta(models.Model):
    id=models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta a {self.denuncia.tipo_denuncia}"