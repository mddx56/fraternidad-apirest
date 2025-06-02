from django.db import models
from django.core.validators import MinValueValidator
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


class QRRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    moneda = models.CharField(max_length=3, verbose_name="Moneda", default="BOB")
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Monto",
    )
    concepto = models.CharField(max_length=255, verbose_name="Concepto")
    unsolouso = models.BooleanField(default=True, verbose_name="Un solo uso")
    fecha_expiracion = models.DateField(verbose_name="Fecha de expiración")
    datos = models.TextField(blank=True, null=True, verbose_name="Datos adicionales")
    cuenta_destino = models.CharField(max_length=50, verbose_name="ID Cuenta destino")

    qr_id = models.CharField(
        max_length=50, verbose_name="ID del QR", blank=True, null=True
    )
    generado = models.BooleanField(default=False, verbose_name="Generación exitosa")
    api_message = models.TextField(
        blank=True, null=True, verbose_name="Mensaje de la API"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    user_craeted = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Creado por",
    )

    def __str__(self):
        return f"QR {self.id} - {self.montot} {self.moneda} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Registro de QR"
        verbose_name_plural = "Registros de QR"
        ordering = ["-created_at"]
