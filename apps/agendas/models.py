import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TipoEvento(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre", max_length=100, default="", null=False
    )
    descripcion = models.TextField(verbose_name="Descripcion", default="", null=True)
    costo_entresemana = models.DecimalField(
        verbose_name="Costo entre semana",
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )
    costo_finsemana = models.DecimalField(
        verbose_name="Costo fin semana",
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0,
    )

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Evento"

    def __str__(self) -> str:
        return (
            f"{self.nombre} ({self.costo_entresemana} Bs. ,{self.costo_finsemana} Bs.)"
        )


class Agenda(models.Model):
    ACTIVA = "activa"
    PENDIENTE = "pendiente"
    RECHAZADA = "rechazada"
    ESTADOS = [(PENDIENTE, "Pendiente"), (ACTIVA, "Activa"), (RECHAZADA, "Rechazada")]
    fecha = models.DateField(verbose_name="Fecha", null=False)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    descripcion = models.TextField(
        verbose_name="Descripcion", default="", null=True, blank=True
    )
    tipo_evento = models.ForeignKey(
        TipoEvento,
        verbose_name="Tipo de evento",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    es_entresemana = models.BooleanField(verbose_name="Entre semana", default=False)
    estado_reserva = models.CharField(
        verbose_name="Estado", max_length=15, choices=ESTADOS, default=PENDIENTE
    )
    user = models.ForeignKey(User, verbose_name="Fraterno", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self) -> str:
        return f"{self.fecha}, {self.tipo_evento.nombre}"


class Gestion(models.Model):
    anio = models.IntegerField(verbose_name="Año", null=False, default=-1)
    en_curso = models.BooleanField(verbose_name="En curso?")

    class Meta:
        verbose_name = "Gestion"
        verbose_name_plural = "Gestiones"

    def __str__(self):
        return f"{self.anio}"

    def to_json(self):
        return {"anio": self.anio, "en_curso": self.en_curso}


class Cupon(models.Model):
    fecha = models.DateField(verbose_name="Fecha", null=False)
    estado = models.BooleanField(verbose_name="Estado", default=True)
    user = models.ForeignKey(User, verbose_name="Fraterno", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cupon"
        verbose_name_plural = "Cupones"

    def __str__(self):
        return f"{self.fecha}, {self.user.full_name}"

    def to_json(self):
        return {"fecha": self.fecha, "estado": self.estado}


class Mensualidad(models.Model):
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fecha = models.DateField(null=False)
    mes = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(default=False, verbose_name="Estado")
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Mensualidad"
        verbose_name_plural = "Mensualidades"

    def __str__(self) -> str:
        return f"mes: {self.mes}-{self.gestion.anio}, costo: {self.costo}"

    def to_json(self):
        return {
            "costo": self.costo,
            "fecha": self.fecha,
            "mes": self.mes,
            "gestion": self.gestion.anio,
        }


class Extraordinaria(models.Model):
    monto = models.DecimalField(
        verbose_name="Monto", max_digits=10, decimal_places=2, null=False
    )
    concepto = models.TextField(verbose_name="Concepto", default="")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Extraordinaria"
        verbose_name_plural = "Extraordinarias"

    def __str__(self) -> str:
        return f"Concepto: {self.concepto}, monto: {self.monto}, "

    def to_json(self):
        return {
            "id": self.pk,
            "monto": self.monto,
            "concepto": self.concepto,
            "create_date": self.created_date,
        }


class Qr(models.Model):
    qr_valor = models.DecimalField(
        verbose_name="Monto de QR", max_digits=10, decimal_places=2, null=False
    )
    url = models.URLField(
        verbose_name="Url de QR", max_length=700, null=False, default=""
    )
    descripcion = models.TextField(verbose_name="Descripcion", blank=True, null=True)
    tipo_evento = models.ForeignKey(
        TipoEvento, verbose_name="Tipo de Evento", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"QR : {self.qr_valor}, {self.descripcion}"


class Pago(models.Model):
    fecha_pago = models.DateField(null=True, blank=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"Pago: {self.monto_pagado} Bs, User {self.user.full_name}"

    def to_json(self):
        return {
            "fecha_pago": self.fecha_pago,
            "monto_pagado": self.monto_pagado,
            # "user": self.user.to_json(),
            "created_date": self.created_date,
        }


class GrupoTurno(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    dia = models.IntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.dia}"


class Turno(models.Model):
    fecha = models.DateField(null=True, blank=True)
    grupo_turno = models.ForeignKey(GrupoTurno, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.fecha}, {self.grupo_turno}"


class UserTurno(models.Model):
    grupo_turno = models.ForeignKey(GrupoTurno, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.grupo_turno}- {self.user.full_name}"


class DetallePagoMensualidad(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    mensualidad = models.ForeignKey(Mensualidad, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Detalle Pago Mensualidad"
        verbose_name_plural = "Detalles Pago Mensualidad"

    def __str__(self):
        return f"{self.pago.id} ,Mes: {self.mensualidad.mes}, Gestion: {self.mensualidad.gestion.anio}"

    def to_json(self):
        return {
            "pago": self.pago.to_json(),
            "mensualidad": self.mensualidad.to_json(),
            "created_date": self.created_date,
        }


class DetallePagoExtraordianria(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    extraordinaria = models.ForeignKey(Extraordinaria, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Detalle Pago Extraordianria"
        verbose_name_plural = "Detalles Pago Extraordianria"

    def __str__(self):
        return f"{self.pago.id} ,{self.extraordinaria.concepto}"

    def to_json(self):
        return {
            "pago": self.pago.to_json(),
            "extraordinaria": self.extraordinaria.to_json(),
            "created_date": self.created_date,
        }


class DetallePagoEvento(models.Model):
    pago = models.ForeignKey(Pago, verbose_name="Pago", on_delete=models.CASCADE)
    evento = models.ForeignKey(Agenda, verbose_name="Evento", on_delete=models.CASCADE)
    canselado = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Detalle Pago Evento"
        verbose_name_plural = "Detalles Pago Evento"

    def __str__(self):
        return f"{self.pago.id} ,{self.evento}"


class TimeStampedBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Extraord(TimeStampedBaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    concepto = models.TextField(default="")

    def __str__(self) -> str:
        return f"{self.concepto}, monto: {self.total}, "


class FraterExtraord(TimeStampedBaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    extraord = models.ForeignKey(Extraord, on_delete=models.DO_NOTHING)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self) -> str:
        return f"{self.user.pk}, {self.extraord.pk}, "


class Cuota(TimeStampedBaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    mes = models.SmallIntegerField(null=True)
    pagado = models.BooleanField(default=False)
    frater_extraord = models.ForeignKey(FraterExtraord, on_delete=models.DO_NOTHING)
    gestion = models.ForeignKey(Gestion, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"costo: {self.costo}, cuota: {self.mes}-{self.gestion.anio}"


class DetallePagoExtraord(TimeStampedBaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    cuota = models.ForeignKey(Cuota, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.id}, "
