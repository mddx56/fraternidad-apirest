from django.db import models
from django.utils.html import mark_safe

from django.contrib.auth import get_user_model

User = get_user_model()

"""
class Notificacion(models.Model):
    titulo = models.CharField(max_length=300, default="", null=False)
    descripcion = models.TextField(default="", null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user_destino = models.IntegerField(default=-1)
    user_remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    leido = models.BooleanField(default=False)


class Token(models.Model):
    token = models.TextField(default="", null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
"""


class Cumpleanio(models.Model):
    disponible = models.BooleanField(default=False)
    fecha = models.DateTimeField(null=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"Cumpleanio : {self.fecha}, {self.disponible}"


class Fraternidad(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    color = models.CharField(max_length=7, default="", null=True, blank=True)
    telefono = models.CharField(max_length=15, default="", null=True, blank=True)
    direccion = models.CharField(max_length=300, default="", null=True, blank=True)
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
    url = models.URLField(max_length=700, default="")
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    banco = models.CharField(max_length=150, default="", null=True, blank=True)
    nro_cuenta = models.CharField(max_length=150, default="", null=True, blank=True)

    def __str__(self) -> str:
        return f"Fraternidad : {self.nombre}"


class MediaImage(models.Model):
    url = models.URLField(max_length=700)
    descripcion = models.TextField(blank=True, null=True)
    secuencia = models.IntegerField(default=0, blank=True)
    mostrar = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    fraternidad = models.ForeignKey(Fraternidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Media Imagen : {self.descripcion},  Fecha subido:  {self.upload_date} "

    def image_tag(self):
        return mark_safe(
            f"<div style='width: 200px; height: 200px; display: flex; justify-content: center; align-items: center; overflow: hidden;'><img src='{self.url}' alt='Mi imagen' style='width: 100%; height: auto;'></div>"
        )


class MediaVideo(models.Model):
    url = models.URLField(max_length=700)
    video_id = models.CharField(max_length=15, default="", null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    mostrar = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    fraternidad = models.ForeignKey(Fraternidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"MediaVideo : {self.descripcion}"

    def video_tag(self):
        return mark_safe(
            f"<iframe width='200' height='200' src='{self.url}' ></iframe>"
        )


class Articulo(models.Model):
    titulo = models.CharField(max_length=256, default="")
    descripcion = models.TextField(blank=True, null=True)
    mostrar = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    fraternidad = models.ForeignKey(Fraternidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Articulo : {self.titulo}"


class Cronograma(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Cronograma : {self.nombre}"


class DiaSemana(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self):
        return f"Dia Semana : {self.nombre}"


class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin}"


class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Actividad {self.nombre}"
