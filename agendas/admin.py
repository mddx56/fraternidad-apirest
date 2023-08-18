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


class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "precio")
    list_display_links = ("id",)
    list_editable = ("precio", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(TipoEvento, TipoEventoAdmin)


class EstadoDeudaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    list_display_links = ("id", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(EstadoDeuda, EstadoDeudaAdmin)


class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "hora_inicio",
        "hora_fin",
        "descripcion",
        "tipo_evento",
        "user",
    )
    list_display_links = ("id", "user")
    list_filter = ("tipo_evento",)
    # list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user", "fecha")
    list_per_page = 25


admin.site.register(Agenda, AgendaAdmin)


class DeudaAdmin(admin.ModelAdmin):
    list_display = ("id", "deuda_total", "estado_deuda", "user", "created_date")
    list_display_links = ("id", "user")
    list_filter = ("estado_deuda",)
    list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user")
    list_per_page = 25


admin.site.register(Deuda, DeudaAdmin)
# admin.site.register(DetalleDeuda)


class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_pago", "monto_pagado", "deuda", "evento", "user")
    list_display_links = ("id","deuda", "evento","user")
    list_filter = ("evento",)
    search_fields = ("id", "user")
    list_per_page = 25


admin.site.register(Pago, PagoAdmin)
# admin.site.register(Qr)


class UserTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "deuda_total", "estado_deuda", "user", "created_date")
    list_display_links = ("id", "user")
    list_filter = ("estado_deuda",)
    list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user")
    list_per_page = 25


admin.site.register(Turno)


class UserTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "turno", "user")
    list_display_links = ("id", "turno", "user")
    list_filter = ("turno",)
    search_fields = ("turno", "user")
    list_per_page = 25


admin.site.register(UserTurno)


class MensualidadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "monto_fijo",
        "pagado",
        "deuda",
    )
    list_display_links = ("id", "deuda")
    list_filter = ("pagado",)
    search_fields = ("fecha", "deuda")
    list_per_page = 25


admin.site.register(Mensualidad, MensualidadAdmin)


class ExtraordinariaAdmin(admin.ModelAdmin):
    list_display = (
        "monto",
        "concepto",
        "created_date",
    )  # Ahora la interfaz mostrará nombre, apellido y email de cada autor.
    # search_fields = ("monto")


admin.site.register(Extraordinaria, ExtraordinariaAdmin)


class DeudaExtraordinariaAdmin(admin.ModelAdmin):
    list_display = (
        "deuda",
        "extraordinaria",
        "pagado",
        "created_date",
    )  # Ahora la interfaz mostrará nombre, apellido y email de cada autor.
    # search_fields = "deuda"


admin.site.register(DeudaExtraordinaria, DeudaExtraordinariaAdmin)
