from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)

    def __str__(self) -> str:
        return f"EstadoReserva : {self.nombre}"


# class EstadoDeuda(models.Model):
#    nombre = models.CharField(max_length=100, default="", null=False)

#    def __str__(self) -> str:
#        return f"EstadoDeuda : {self.nombre}"


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    descripcion = models.TextField(default="", null=True)
    costo_entresemana = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    costo_finsemana = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def __str__(self) -> str:
        return f"TipoEvento : {self.nombre}"


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
    PENDIENTE = "pendiente"
    PAGADA = "pagada"
    ESTADOS = [(PENDIENTE, "Pendiente"), (PAGADA, "Pagada")]
    deuda_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_deuda = models.CharField(max_length=15, choices=ESTADOS, default=PENDIENTE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"Deuda : {self.user}, {self.estado_deuda}"


class Mensualidad(models.Model):
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    pagado = models.BooleanField(default=False)
    fecha = models.DateField(null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"Deuda : {self.costo}, {self.fecha}"


class Extraordinaria(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    concepto = models.TextField(default="")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Deuda : {self.monto}, {self.concepto}"


class DeudaExtraordinaria(models.Model):
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    extraordinaria = models.ForeignKey(Extraordinaria, on_delete=models.CASCADE)
    pagado = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


"""
class DetalleDeuda(models.Model):
    monto_cargo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    monto_abono = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fecha_detalle = models.DateField(auto_now_add=True)
    concepto = models.CharField(max_length=300, default="", null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Deuda : {self.fecha_detalle}, {self.concepto}"
"""


class Qr(models.Model):
    qr_valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    url = models.URLField(max_length=700, null=False, default="")
    descripcion = models.TextField(blank=True, null=True)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"QR : {self.qr_valor}, {self.deuda.mes}"


class Pago(models.Model):
    fecha_pago = models.DateField(null=True, blank=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    evento = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"Pago : {self.fecha_pago}, {self.monto_pagado} - user = {self.user.username}"


class Turno(models.Model):
    dia = models.IntegerField(default=0, blank=True)
    semana = models.IntegerField(default=0, blank=True)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Turno : {self.nro_semana}, {self.fecha}"


class UserTurno(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"UserTurno : {self.turno.nro_semana}, {self.turno.dia_default}- {self.user.username} "
