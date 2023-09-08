from django.contrib import admin

from .models import (
    Agenda,
    Pago,
    TipoEvento,
    Gestion,
    Qr,
    Turno,
    UserTurno,
    Mensualidad,
    Extraordinaria,
    DeudaExtraordinaria,
    DetallePagoEvento,
    DetallePagoExtraordianria,
    DetallePagoMensualidad,
    GrupoTurno,
)

admin.site.site_header = "Sistema de Gestión para Fraternidad ⛺"
admin.site.site_title = "Flojonazos"
admin.site.index_title = "Bienvenidos al portal de administración"


class TipoEventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "descripcion",
        "costo_entresemana",
        "costo_finsemana",
    )
    list_display_links = ("id",)
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "nombre")
    list_per_page = 25


admin.site.register(TipoEvento, TipoEventoAdmin)


class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "hora_inicio",
        "hora_fin",
        # "descripcion",
        "tipo_evento",
        "user",
    )
    list_display_links = ("id", "user")
    list_filter = ("tipo_evento",)
    # list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user", "fecha")
    list_per_page = 25


admin.site.register(Agenda, AgendaAdmin)


"""
class DeudaAdmin(admin.ModelAdmin):
    list_display = ("id", "deuda_total", "estado_deuda", "user", "created_date")
    list_display_links = ("id", "user")
    list_filter = ("estado_deuda",)
    list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user")
    list_per_page = 25


admin.site.register(Deuda, DeudaAdmin)
"""


class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_pago", "monto_pagado", "user", "created_date")
    list_display_links = ("id", "user")
    list_filter = ("fecha_pago",)
    search_fields = ("id", "user")
    list_per_page = 25


admin.site.register(Pago, PagoAdmin)


class GrupoTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "dia")
    list_display_links = ("id", "nombre")
    list_filter = ("nombre",)
    list_per_page = 25


admin.site.register(GrupoTurno, GrupoTurnoAdmin)


class UserTurnoAdmin(admin.ModelAdmin):
    list_display = ("id", "grupo_turno", "user")
    list_display_links = ("id", "grupo_turno", "user")
    list_per_page = 25


admin.site.register(UserTurno, UserTurnoAdmin)


class MensualidadAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "costo", "pagado", "gestion")
    list_display_links = ("id", "fecha")
    list_filter = ("pagado", "gestion")
    search_fields = ("fecha",)
    list_per_page = 25


admin.site.register(Mensualidad, MensualidadAdmin)


class ExtraordinariaAdmin(admin.ModelAdmin):
    list_display = (
        "monto",
        "concepto",
        "created_date",
    )


admin.site.register(Extraordinaria, ExtraordinariaAdmin)


class DeudaExtraordinariaAdmin(admin.ModelAdmin):
    list_display = (
        "extraordinaria",
        "pagado",
        "detalle",
        "created_date",
    )


admin.site.register(DeudaExtraordinaria, DeudaExtraordinariaAdmin)
