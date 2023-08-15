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
    Turno,
    UserTurno
)

admin.site.site_header = "Sistema de Gestión para Fraternidad ⛺"
admin.site.site_title = "Fraternidad "
admin.site.index_title = "Bienvenidos al portal de administración"

admin.site.register(EstadoReserva)
admin.site.register(TipoEvento)
admin.site.register(EstadoDeuda)
admin.site.register(Agenda)
admin.site.register(Deuda)
admin.site.register(DetalleDeuda)
admin.site.register(Pago)
admin.site.register(Qr)
admin.site.register(Turno)
admin.site.register(UserTurno)

