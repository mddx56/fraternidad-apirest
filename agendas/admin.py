from django.contrib import admin

from .models import (
    Agenda,
    Deuda,
    Pago,
    EstadoDeuda,
    EstadoReserva,
    TipoEvento,
    DetalleDeuda,
    Qr,
)
 
admin.site.register(EstadoReserva)
admin.site.register(TipoEvento)
admin.site.register(EstadoDeuda)
admin.site.register(Agenda)
admin.site.register(Deuda)
admin.site.register(DetalleDeuda)
admin.site.register(Pago)
admin.site.register(Qr)