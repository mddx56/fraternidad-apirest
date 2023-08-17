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
    UserTurno,
    Mensualidad,
    Extraordinaria,
    DeudaExtraordinaria,
    
)

admin.site.site_header = "Sistema de Gestión para Fraternidad ⛺"
admin.site.site_title = "Fraternidad "
admin.site.index_title = "Bienvenidos al portal de administración"

admin.site.register(EstadoReserva)
admin.site.register(TipoEvento)
admin.site.register(EstadoDeuda)


class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "descripcion",
    )  # Ahora la interfaz mostrará nombre, apellido y email de cada autor.
    #search_fields = ("fecha")

admin.site.register(Agenda, AgendaAdmin)

admin.site.register(Deuda)
admin.site.register(DetalleDeuda)
admin.site.register(Pago)
admin.site.register(Qr)
admin.site.register(Turno)
admin.site.register(UserTurno)


