from django.db import models


class Fraternidad(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    color = models.CharField(max_length=7, default="", null=True)
    direccion = models.CharField(max_length=300, default="", null=True)
    mensualidad = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    monto_suspendido = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    monto_no_reserva = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    turno_semanal = models.CharField(max_length=50, default="", null=False)
    banco = models.CharField(max_length=150, default="", null=True)
    nro_cuenta = models.CharField(max_length=150, default="", null=True)

    def __str__(self) -> str:
        return f"Fraternidad : {self.nombre}"


class Medio(models.Model):
    MEDIA_TYPES = (
        ("image", "Image"),
        ("video", "Video"),
    )

    tipo = models.CharField(max_length=10, choices=MEDIA_TYPES)
    url = models.URLField()
    descripcion = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    fraternidad = models.ForeignKey(Fraternidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Medio : {self.descripcion},  Tipo:  {self.tipo} "
