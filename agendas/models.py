from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)

    def __str__(self) -> str:
        return f"EstadoReserva : {self.nombre}"


class EstadoDeuda(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)

    def __str__(self) -> str:
        return f"EstadoDeuda : {self.nombre}"


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    descripcion = models.TextField(default="", null=True)

    def __str__(self) -> str:
        return f"TipoEvento : {self.nombre}, {self.descripcion}"


class Agenda(models.Model):
    fecha = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    descripcion = models.TextField(default="", null=True)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.DO_NOTHING)
    estado_reserva = models.ForeignKey(EstadoReserva, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Agenda : {self.fecha}, {self.descripcion}"


class Deuda(models.Model):
    mes = models.SmallIntegerField()
    estado_reserva = models.ForeignKey(EstadoDeuda, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Deuda : {self.user}, {self.mes}"


class DetalleDeuda(models.Model):
    monto_cargo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    monto_abono = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fecha_detalle = models.DateField(auto_now_add=True)
    concepto = models.CharField(max_length=300, default="", null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Deuda : {self.fecha_detalle}, {self.concepto}"


class Qr(models.Model):
    qr_valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"QR : {self.qr_valor}, {self.deuda.mes}"


class Pago(models.Model):
    fecha_pago = models.DateField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    evento = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Pago : {self.fecha_pago}, {self.monto_pagado} - user = {self.user.username}"
    
class Turno(models.Model):
    nro_semana = models.IntegerField(default=0)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dia_default = models.IntegerField(default=0)
    dias = models.JSONField()

    def __str__(self) -> str:
        return f"Turno : {self.nro_semana}, {self.hora_inicio} - {self.hora_fin}"

class UserTurno(models.Model):
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"UserTurno : {self.turno.id}, {self.user.username}"