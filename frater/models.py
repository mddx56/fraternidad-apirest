from django.db import models
from django.contrib.auth.models import User


class Fraternidad(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    color = models.CharField(max_length=7,default="")
    direccion = models.CharField(max_length=300, default="", null=False)
    mensualidad = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=False)
    monto_suspendido = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=False)
    monto_no_reserva = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)
    turno_semanal = models.CharField(max_length=50, default="", null=False)
    banco = models.CharField(max_length=150, default="", null=False)
    nro_cuenta = models.CharField(max_length=150, default="", null=False)

    def __str__(self) -> str:
        return f"Fraternidad : {self.nombre}"


class Cumpleanio(models.Model):
    disponible = models.BooleanField(default=False)
    fecha = models.DateTimeField(null=False)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cumpleanio : {self.user.username}"
