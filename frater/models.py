from django.db import models
from django.contrib.auth.models import User

class Fraternidad(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    direccion = models.CharField(max_length=300, default="", null=False)

    def __str__(self) -> str:
        return f"Fraternidad : {self.nombre}"


class Cumpleanio(models.Model):
    disponible = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cumpleanio : {self.user.username}"
