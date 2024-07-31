from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from admin_interface.admin import Theme

admin.site.unregister(Group)
admin.site.unregister(Theme)

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
    DetallePagoEvento,
    DetallePagoExtraordianria,
    DetallePagoMensualidad,
    GrupoTurno,
    Extraord,
    Cuota,
    DetallePagoExtraord,
    FraterExtraord
)

admin.site.site_header = "Sistema de Gestión para Fraternidad ⛺"
admin.site.site_title = "Flojonazos"
admin.site.index_title = "Bienvenidos al portal de administración"

admin.site.register(Extraord)
admin.site.register(Cuota)
admin.site.register(DetallePagoExtraord)
admin.site.register(FraterExtraord)


class GestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "anio",
        "en_curso",
    )
    list_display_links = ("id", "anio")
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "anio")
    list_per_page = 25


admin.site.register(Gestion, GestionAdmin)


class QrAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "qr_valor",
        "url",
        "descripcion",
        "tipo_evento",
    )
    list_display_links = (
        "id",
        "qr_valor",
    )
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "descripcion")
    list_per_page = 25


admin.site.register(Qr, ImportExportModelAdmin)
# admin.site.register(Qr, QrAdmin)


class TurnoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "grupo_turno",
    )
    list_display_links = (
        "id",
        "fecha",
    )
    list_filter = (
        "grupo_turno",
        "fecha",
    )
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "fecha")
    list_per_page = 25


admin.site.register(Turno, TurnoAdmin)


class DetallePagoEventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        "evento",
    )
    list_display_links = (
        "id",
        "pago",
    )
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoEvento, DetallePagoEventoAdmin)


class DetallePagoExtraordianriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        # "deuda_extraordinaria",
    )
    list_display_links = (
        "id",
        "pago",
    )

    # list_editable = ("precio", "nombre")
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoExtraordianria, DetallePagoExtraordianriaAdmin)


class DetallePagoMensualidadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pago",
        "mensualidad",
    )
    list_display_links = (
        "id",
        "pago",
    )

    # list_editable = ("precio", "nombre")
    search_fields = ("id", "pago")
    list_per_page = 25


admin.site.register(DetallePagoMensualidad, DetallePagoMensualidadAdmin)


class TipoEventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "descripcion",
        "costo_entresemana",
        "costo_finsemana",
    )
    list_display_links = (
        "id",
        "nombre",
    )
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
    list_display_links = (
        "id",
        "user",
        "fecha",
    )
    list_filter = ("tipo_evento",)
    # list_editable = ("deuda_total", "estado_deuda")
    search_fields = ("id", "user", "fecha")
    list_per_page = 25


admin.site.register(Agenda, AgendaAdmin)


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
    list_display = ("id", "fecha", "costo", "gestion")
    list_display_links = ("id", "fecha")
    # list_filter = ( "gestion")
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
